import setuptools 
from pathlib import Path
from setuptools import setup, find_packages

setuptools.setup(
    name="src",
    version="0.0.1",
    author="Bhikipallai",
    author_email="vicky.pallai900@gmail.com",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)



