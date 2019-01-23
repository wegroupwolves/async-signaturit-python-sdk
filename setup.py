from __future__ import absolute_import
from distutils.core import setup

setup(
    author="Signaturit",
    author_email="api@signaturit.com",
    description="Signaturit Python SDK",
    install_requires=["requests", "httpretty", "asyncio"],
    keywords="signaturit e-signature python sdk",
    license="MIT",
    name="signaturit_sdk",
    packages=["signaturit_sdk", "signaturit_sdk.tests", "signaturit_sdk.resources"],
    url="https://github.com/signaturit/python-sdk",
    version="1.1.0",
)
