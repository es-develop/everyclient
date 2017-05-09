# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='everyclient',
    version='0.1.0',
    description='Everysense client package for Rest API',
    long_description=readme,
    author='Everysense Inc',
    author_email='support@every-sense.com',
    url='https://github.com/every-sense',
    license=license,
    packages=find_packages(exclude=('tests', 'example', 'docs'))
)
