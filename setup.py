from __future__ import absolute_import, division, print_function

import os
import sys

from setuptools import find_packages, setup

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


setup(
    name='wabbit',
    version='0.0.0',
    description='The Wabbit Programming Language',
    packages=find_packages(include=['wabbit', 'wabbit.*']),
    author='pspenano',
    install_requires=[
        'sly',
    ]
)
