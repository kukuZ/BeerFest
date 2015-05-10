#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='BeerFest',
    version='0.1',
    description='blank',
    author='motoki-Z',
    author_email='',
    url='',
#    include_package_data = True,
    install_requires =
    [
        'Django==1.8'
        'django-bootstrap-form==3.2'
    ],
    packages=find_packages(),
    test_suite = "BeerFest",
    dependency_links = ['',]
    )
