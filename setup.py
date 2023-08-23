from setuptools import setup

setup(
    name="apple_wallet_pass_creator",
    version="1.0",
    description="Simple helper module for creating apple wallet passes",
    author="Roland Sobczak",
    author_email="rolandsobczak@icloud.com",
    url="https://github.com/RolandSobczak/ApplePassCreator",
    package_dir={
        "apple_pass_creator": "src/apple_pass_creator",
    },
    packages=["apple_pass_creator"],
    install_requires=[
        "Jinja2==3.1.2",
    ],
)
