#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="mpl_extras",
    version="0.0.1",
    description="Format for matplotlib",
    url="https://github.com/anthony-vo/mpl_extras.git",
    packages=find_packages(),
    python_requires=">=3.7,<4",
    install_requires=["matplotlib"],
    extras_require={},
    entry_points={},
    scripts=[],
)
