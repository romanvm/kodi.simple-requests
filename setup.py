# coding: utf-8
# (c) 2020, Roman Miroshnychenko
# License: MIT

from pathlib import Path
from xml.dom.minidom import parse

from setuptools import setup

THIS_DIR = Path(__file__).resolve().parent


def get_version():
    doc = parse(str(THIS_DIR / 'script.module.simple-requests' / 'addon.xml'))
    return doc.firstChild.getAttribute('version')


setup(
    name='simple-requests',
    author='Roman Miroshnychenko',
    version=get_version(),
    package_dir = {'': 'script.module.simple-requests/libs'},
    py_modules=['simple_requests'],
    zip_safe=False
)
