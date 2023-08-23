"""
This is sample for using this package to bundle .pkpass from sample `Generic.pass` provided, by Apple in examples.
Here is the link to samples:
https://developer.apple.com/services-account/download?path=/iOS/Wallet_Support_Materials/WalletCompanionFiles.zip

Before You start playing with it, change passTypeIdentifier and teamIdentifier in pass.json file.
The next example shows how to render this data dynamic.

Remember to install this package before run:
pip install git+https://github.com/RolandSobczak/ApplePassCreator.git
"""

import os
from pathlib import Path

from apple_pass_creator import (
    bundle_files,
    create_manifest,
    generate_signification,
)

PASS_TEMPLATE_DIR_PATH = Path("BoardingPass.pass/")
WWDR_CERT_PATH = Path("./certs/wwdr.pem")
APPLE_CERT_PATH = Path("./certs/pass_cert.pem")
PRIVATE_KEY_PATH = Path("./certs/pass_key.pem")
PASSWORD_TO_PRIVATE_KEY = "YOUR_PRIVATE_KEY_PASSWORD"
OUTPUT_FILE_PATH = "Generic.pkpass"


def get_all_files_in_directory(directory):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(os.path.join(root, file))
            all_files.append(file_path)
    return all_files


def main():
    paths_to_template_files = get_all_files_in_directory(PASS_TEMPLATE_DIR_PATH)
    manifest_json = create_manifest(paths_to_template_files)
    signature = generate_signification(
        intermediate_cert=WWDR_CERT_PATH,
        signer_cert=APPLE_CERT_PATH,
        private_key=PRIVATE_KEY_PATH,
        password=PASSWORD_TO_PRIVATE_KEY,
        payload=manifest_json.encode(),
    )
    pkpass = bundle_files(
        paths_to_template_files,
        other_files={"manifest.json": manifest_json.encode(), "signature": signature},
    )

    with open(OUTPUT_FILE_PATH, mode="wb") as output:
        output.write(pkpass)


if __name__ == "__main__":
    main()
