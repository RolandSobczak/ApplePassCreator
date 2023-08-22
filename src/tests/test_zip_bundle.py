from pathlib import Path
from unittest.mock import call, mock_open, patch

from src.apple_pass_creator.zip_bundle import bundle_files


def test_bundle_file(encoded_content: bytes):
    test_file_paths = [Path("/test/test1.txt"), Path("/test/test2.txt")]
    expected_calls = [
        call(test_file_paths[0], mode="rb"),
        call(test_file_paths[1], mode="rb"),
    ]

    with patch("builtins.open", mock_open(read_data=encoded_content)) as mock_file:
        zip_bytes = bundle_files(test_file_paths)

    assert mock_file.call_count == 2
    assert mock_file.call_args_list == expected_calls
    assert type(zip_bytes) == bytes
