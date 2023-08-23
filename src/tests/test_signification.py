import subprocess
from pathlib import Path
from unittest.mock import patch

from src.apple_pass_creator.signification import generate_signification


@patch("subprocess.Popen")
def test_your_function(mock_popen):
    mock_communicate = mock_popen.return_value.communicate
    test_cert_path = Path("/test/test_cert.pem")
    test_private_key_path = Path("/test/test_private_key.pem")
    test_intermediate_cert = Path("/test/test_wwdr.pem")
    test_payload = b"manifest.json"
    test_password = "test_password"
    test_return_value = b"test_return_value"
    mock_communicate.return_value = (test_return_value, b"")
    valid_openssl_command = [
        "openssl",
        "smime",
        "-binary",
        "-sign",
        "-certfile",
        str(test_intermediate_cert),
        "-signer",
        str(test_cert_path),
        "-inkey",
        str(test_private_key_path),
        "-outform",
        "DER",
        "-passin",
        f"pass:{test_password}",
        "in",
        "-",
    ]

    signification = generate_signification(
        test_intermediate_cert,
        test_cert_path,
        test_private_key_path,
        test_password,
        test_payload,
    )

    mock_popen.assert_called_once_with(
        valid_openssl_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False,
    )
    mock_communicate.assert_called_once_with(input=test_payload)
    assert signification == test_return_value
