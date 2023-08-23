from abc import ABC, abstractmethod
from hashlib import sha1
from json import dumps
from pathlib import Path
from typing import Dict, List, Optional


class Hash(ABC):
    """Template for all hashers"""

    def __init__(self):
        self._hash = None

    @abstractmethod
    def update(self, part: bytes):
        """This method updates current hash with new part

        :param part: part to add
        :type part: bytes
        """
        pass

    @abstractmethod
    def __hex__(self):
        pass


class SHA1Hasher(Hash):
    def __init__(self):
        self._hash = sha1()

    def update(self, part: bytes):
        self._hash.update(part)

    def __hex__(self) -> str:
        return self._hash.hexdigest()


def calculate_sha1(payload: bytes) -> str:
    """Calculates sha1 hash and return it in hex format

    :param payload: function which return value to hash
    :type payload: bytes
    :return: sha1 hash in hex format
    :rtype: str
    """
    hash = SHA1Hasher()
    hash.update(payload)

    return hash.__hex__()


def calculate_file_sha1(
    file_path: Path,
    chunk_size: int = 2096,
) -> str:
    """This function returns hash of file from given path. By default, this function use sha1 algorithm
    to hash files. To change this behavior overwrite callback kwarg with function which takes callback.
    Callback function should return hash of their callback.

    :param file_path: path to file to hash
    :type file_path: Path
    :param callback: function for hashing given callback return value
    :type callback: callable
    :param chunk_size: Function hash files part by part. It's size of single part.
    :type chunk_size: int
    :return: file hash
    :rtype: str
    """
    hash = SHA1Hasher()
    with open(file_path, mode="rb") as f:
        while chunk := f.read(chunk_size):
            hash.update(chunk)
    return hash.__hex__()


def create_manifest(
    paths: Optional[List[Path]] = None,
    other_files: Optional[Dict[str, bytes]] = None,
    **kwargs,
) -> str:
    """This function returns manifest.json file. This file is json contains dict: file_name: file_hash.
    It's required by .pkpass format.


    :param paths: list of file paths to hash
    :type paths: list[Path]
    :param other_files: Files in bytes to include in manifest.json.
    This dict should contain file_name: file_content pairs.
    :type other_files: dict
    :param kwargs: kwargs will be given to calculate_file_hash function
    :type kwargs: dict
    :return: json file contains files hashes
    :rtype: str
    """
    manifest = {}

    if paths:
        for file_path in paths:
            filename = file_path.name
            file_hash = calculate_file_sha1(file_path, **kwargs)
            manifest.update({filename: file_hash})
    if other_files:
        for filename, content in other_files.items():
            file_hash = calculate_sha1(content)
            manifest.update({filename: file_hash})

    return dumps(manifest)
