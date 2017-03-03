#!/usr/bin/env python

import sys
from setuptools import setup

install_requires = [
    "h5py",
    "keras"
]

if sys.version_info[0] == 2:
    install_requires.append('unicodecsv')

setup(name="keras_cli",
      version="0.0.1",
      author="Paul Fitzpatrick",
      author_email="paulfitz@alum.mit.edu",
      description="Keras command line client",
      packages=['keras_cli'],
      entry_points={
          "console_scripts": [
              "keras=keras_cli.__main__:main"
          ]
      },
      install_requires=install_requires,
      url="https://github.com/paulfitz/keras_cli"
)
