import io
import zipfile
from pathlib import Path


class Bundle:
    def __init__(self):
        self._zip_bytes = io.BytesIO()
        self._zipf = zipfile.ZipFile(self._zip_bytes, "w")

    def add_file(self, filename: str, content: bytes) -> None:
        self._zipf.writestr(filename, content)

    @property
    def zip(self) -> bytes:
        self._zip_bytes.seek(0)
        return self._zip_bytes.read()


def bundle_files(paths: list[Path], other_files: dict[str, bytes]) -> bytes:
    """This function helps with bundling files into zip files.
    Accept both paths to files and files as bytes.

    :param paths: List of paths to files which should be bundled
    :type paths: list[Path]
    :param other_files: Dict which contain filename: file_content_bytes pairs
    :type other_files: dict[str, bytes]
    :return: bundled zip file
    :rtype: bytes
    """
    bundle = Bundle()
    for file_path in paths:
        with open(file_path, mode="rb") as f:
            bundle.add_file(file_path.name, f.read())
    for filename, content in other_files.items():
        bundle.add_file(filename, content)

    return bundle.zip
