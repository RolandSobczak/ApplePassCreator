"""This is sample for using this package to bundle .pkpass from sample `Generic.pass` provided, by Apple in examples.
Here is the link to samples:
https://developer.apple.com/services-account/download?path=/iOS/Wallet_Support_Materials/WalletCompanionFiles.zip

Here is example how to render pass.jso using jinja2
Everywhere in pass.json where You need to inject some data use standard jinja2 syntax: {{ variable_name }}
In this example I inject passTypeIdentifier and teamIdentifier from this python code,
but You can render any info you want.

Edit You pass.json using this lines:

  "passTypeIdentifier" : "{{ pass_type_identifier }}",
  "teamIdentifier" : "{{ team_identifier }}",

Remember to install this package before run:
pip install git+https://github.com/RolandSobczak/ApplePassCreator.git
"""

import os
from pathlib import Path

from apple_pass_creator import (
    bundle_files,
    create_manifest,
    generate_signification,
    render_pass_json,
)

PASS_TYPE_IDENTIFIER = "pass.com.reversed.domain"
TEAM_IDENTIFIER = "YOUR-TEAM-IDENTIFIER"
PASS_TEMPLATE_DIR_PATH = "BoardingPass.pass/"
WWDR_CERT_PATH = Path("./certs/wwdr.pem")
APPLE_CERT_PATH = Path("./certs/pass_cert.pem")
PRIVATE_KEY_PATH = Path("./certs/pass_key.pem")
PASSWORD_TO_PRIVATE_KEY = "YOUR-PRIVATE-KEY-PASSWORD"
OUTPUT_FILE_PATH = "Generic.pkpass"


def get_all_files_in_directory(directory):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(os.path.join(root, file))
            all_files.append(file_path)
    return all_files


def main():
    pass_json = render_pass_json(
        Path(PASS_TEMPLATE_DIR_PATH + "pass.json"),
        pass_type_identifier=PASS_TYPE_IDENTIFIER,
        team_identifier=TEAM_IDENTIFIER,
    )
    paths_to_template_files = [
        Path(PASS_TEMPLATE_DIR_PATH + "icon.png"),
        Path(PASS_TEMPLATE_DIR_PATH + "icon@2x.png"),
        Path(PASS_TEMPLATE_DIR_PATH + "logo.png"),
        Path(PASS_TEMPLATE_DIR_PATH + "logo@2x.png"),
    ]
    manifest_json = create_manifest(
        paths_to_template_files,
        other_files={"pass.json": pass_json.encode()},
    )
    signature = generate_signification(
        intermediate_cert=WWDR_CERT_PATH,
        signer_cert=APPLE_CERT_PATH,
        private_key=PRIVATE_KEY_PATH,
        password=PASSWORD_TO_PRIVATE_KEY,
        payload=manifest_json.encode(),
    )
    pkpass = bundle_files(
        paths_to_template_files,
        other_files={
            "manifest.json": manifest_json.encode(),
            "signature": signature,
            "pass.json": pass_json.encode(),
        },
    )

    with open(OUTPUT_FILE_PATH, mode="wb") as output:
        output.write(pkpass)


if __name__ == "__main__":
    main()
