#!/usr/bin/env python

from setuptools import setup, find_packages

name = "dictionary"

setup(
    name = name,
    version = "0.1",
    url = "http://silpa.org.in/Spellchecker",
    license = "LGPL-3.0",
    description = "Dictionary for Indian Languages",
    author = "Santhosh Thottingal",
    author_email = "santhosh.thottingal@gmail.com",
    long_description = "This library provides dictionary for Indian Languages",
    packages = find_packages('.'),
    package_data = {'.':['dictionary/dictionaries']},
    include_package_data = True,
    setup_requires = ['setuptools-git'],
    install_requires = ['setuptools'],
    zip_safe = False,
    )
