import subprocess
from pathlib import Path


def generate_signification(
    intermediate_cert: Path,
    signer_cert: Path,
    private_key: Path,
    password: str,
    payload: bytes,
) -> bytes:
    """Generates pkpass signification using openssl command. Require openssl version 1.1.
     PCKS7 not working in latest openssl version.

    :param intermediate_cert: path to WWDR G4 Apple cert in .pem format
    :type intermediate_cert: Path
    :param signer_cert: Your Apple Wallet Pass cert in .pem format
    :type signer_cert: Path
    :param private_key: Private key for Your Apple Wallet Pass cert in .pem format
    :type private_key: Path
    :param password: Password to private_key.pem
    :type password: str
    :param payload: manifest.json file
    :type payload: bytes
    :return: Generated signification
    :rtype: bytes
    """
    openssl_command = [
        "openssl",
        "smime",
        "-binary",
        "-sign",
        "-certfile",
        str(intermediate_cert),
        "-signer",
        str(signer_cert),
        "-inkey",
        str(private_key),
        "-outform",
        "DER",
        "-passin",
        f"pass:{password}",
        "in",
        "-",
    ]
    process = subprocess.Popen(
        openssl_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False,
    )
    stdout, stderr = process.communicate(input=payload)
    if error_msg := stderr:
        raise RuntimeError(error_msg)

    signification = stdout
    return signification
