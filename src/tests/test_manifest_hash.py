from hashlib import sha1
from json import dumps
from pathlib import Path
from unittest.mock import call, mock_open, patch

from src.apple_pass_creator.manifest_hash import (
    calculate_file_hash,
    calculate_sha1,
    create_manifest,
)


def test_calculate_sha1(encoded_content: bytes):
    valid_hash = sha1(encoded_content).hexdigest()

    def file_reader():
        has_returned = False
        while not has_returned:
            yield encoded_content
            has_returned = True
        yield None

    file = file_reader()
    hash_to_check = calculate_sha1(lambda: next(file))

    assert hash_to_check == valid_hash


def test_calculate_file_hash(encoded_content: bytes):
    test_file_path = Path("/test/test.txt")
    valid_hash = sha1(encoded_content).hexdigest()

    with patch("builtins.open", mock_open(read_data=encoded_content)) as mock_file:
        hash_to_check = calculate_file_hash(test_file_path)

    mock_file.assert_called_once_with(test_file_path, mode="rb")
    assert hash_to_check == valid_hash


def test_create_manifest(encoded_content: bytes):
    test_files_paths = [Path("/test/test1.txt"), Path("/test/test2.txt")]
    valid_hash = sha1(encoded_content).hexdigest()
    valid_result = dumps(
        {
            test_files_paths[0].name: valid_hash,
            test_files_paths[1].name: valid_hash,
        },
    )
    expected_calls = [
        call(test_files_paths[0], mode="rb"),
        call(test_files_paths[1], mode="rb"),
    ]

    with patch("builtins.open", mock_open(read_data=encoded_content)) as mock_file:
        result_json = create_manifest(paths=test_files_paths)

    assert mock_file.call_count == 2
    assert mock_file.call_args_list == expected_calls
    assert result_json == valid_result
