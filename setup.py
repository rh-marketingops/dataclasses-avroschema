#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for dataclasses-avroschema."""

from setuptools import find_packages, setup

__version__ = "0.20.3"


with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="dataclasses-avroschema",
    version=__version__,
    description="Generate Avro Schemas from a Python class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marcos Schroh",
    install_requires=["inflect==5.3.0", "fastavro==1.4.0", "pytz", "dacite==1.6.0", "faker==8.1.1",],
    author_email="schrohm@gmail.com",
    url="https://github.com/marcosschroh/dataclasses-avroschema",
    download_url="",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
    ],
    keywords=(
        """
        Python, Data Classes, Avro Schema, Avro, Apache, Data Streaming
        """
    ),
)
