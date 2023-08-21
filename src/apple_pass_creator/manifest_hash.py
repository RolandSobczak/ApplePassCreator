from hashlib import sha1
from json import dumps
from pathlib import Path


def calculate_sha1(callback) -> str:
    """This function calculates sha1 algorithm hash of value returned by callback

    :param callback: function which return value to hash
    :type callback: callable
    :return: sha1 hash
    :rtype: str
    """
    sha1_hash = sha1()

    while chunk := callback():
        sha1_hash.update(chunk)

    return sha1_hash.hexdigest()


def calculate_file_hash(
    file_path: Path,
    callback=calculate_sha1,
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
    with open(file_path, mode="rb") as f:
        file_hash = callback(callback=lambda: f.read(chunk_size))
        return file_hash


def create_manifest(paths: list[Path], **kwargs) -> str:
    """This function returns manifest.json file. This file is json contains dict: file_name: file_hash.
    It's required by .pkpass format.


    :param paths: list of file paths to hash
    :type paths: list[Path]
    :param kwargs: kwargs will be given to calculate_file_hash function
    :type kwargs: dict
    :return: json file contains files hashes
    :rtype: str
    """
    manifest = {}

    for file_path in paths:
        filename = file_path.name
        file_hash = calculate_file_hash(file_path, **kwargs)
        manifest.update({filename: file_hash})

    return dumps(manifest)
