import io
import zipfile
from pathlib import Path


def bundle_files(paths: list[Path]) -> bytes:
    with io.BytesIO() as in_memory_zip:
        with zipfile.ZipFile(in_memory_zip, "w") as zipf:
            for file_path in paths:
                with open(file_path, mode="rb") as f:
                    zipf.writestr(file_path.name, f.read())

        in_memory_zip.seek(0)
        in_memory_zip_bytes = in_memory_zip.read()
        return in_memory_zip_bytes
