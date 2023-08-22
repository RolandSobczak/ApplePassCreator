from setuptools import find_packages, setup

setup(
    name="apple-wallet-pass-creator",
    version="1.0",
    description="Simple helper module for creating apple wallet passes",
    author="Roland Sobczak",
    author_email="rolandsobczak@icloud.com",
    url="https://github.com/RolandSobczak/ApplePassCreator",
    packages=["src.apple_pass_creator"],
    install_requires=[
        "Jinja2==3.1.2",
    ],
)
