from pathlib import Path
from json import dumps

from src.apple_pass_creator.manifest_hash import calculate_sha1, calculate_file_hash, create_manifest


TEST_FILE_PATH = Path("src/tests/test.txt")
TEST_FILE1_PATH = Path("src/tests/test1.txt")
TEST_FILE_VALID_SHA1_HASH = "3bb40f3ef694600497aa8588a21663444387bd39"


def test_calculate_sha1():
    with open(TEST_FILE_PATH, "rb") as f:
        hash_to_check = calculate_sha1(f.read)

    assert hash_to_check == TEST_FILE_VALID_SHA1_HASH


def test_calculate_file_hash():
    hash_to_check = calculate_file_hash(TEST_FILE_PATH)

    assert hash_to_check == TEST_FILE_VALID_SHA1_HASH


def test_create_manifest():
    test_files_paths = [TEST_FILE_PATH, TEST_FILE1_PATH]

    result_json = create_manifest(paths=test_files_paths)
    valid_result = dumps({
        TEST_FILE_PATH.name: TEST_FILE_VALID_SHA1_HASH,
        TEST_FILE1_PATH.name: TEST_FILE_VALID_SHA1_HASH,
    })

    assert result_json == valid_result

