#!/usr/bin/env python
#
# setup.py -- Installation for djblets
#
# Copyright (C) 2008 Christian Hammond
# Copyright (C) 2007-2008 David Trowbridge
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from setuptools import setup, find_packages

VERSION='custom'

setup(name="Djblets",
      version=VERSION,
      license="MIT",
      description="A collection of useful classes and functions for Django",
      packages=find_packages(),
      install_requires=['Django>=1.0.2', 'Pillow>=3.0'],
      include_package_data=True,
      zip_safe=False,
      maintainer="Christian Hammond",
      maintainer_email="chipx86@chipx86.com",
      url="http://www.review-board.org/wiki/Djblets",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Framework :: Django",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ]
)
