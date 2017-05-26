"""
pyflit 

Pyflit is a simple Python HTTP downloader.
"""

from setuptools import setup, find_packages
import pyflit

setup(
    name="pyflit",
    author="Galeo Tian",
    description="Pyflit is a simple Python HTTP downloader.",
    license="GNU General Public License",
    url="https://github.com/galeo/pyflit",
    packages=pyflit,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    install_requires=[
        ],
)
