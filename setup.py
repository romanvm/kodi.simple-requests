# coding: utf-8
# (c) 2020, Roman Miroshnychenko
# License: MIT

import os
from xml.dom.minidom import parse

from setuptools import setup

this_dir = os.path.dirname(os.path.abspath(__file__))


def get_version():
    doc = parse(os.path.join(this_dir, 'script.module.simple-requests', 'addon.xml'))
    return doc.firstChild.getAttribute('version')


setup(
    name='simple-requests',
    author='Roman Miroshnychenko',
    version=get_version(),
    package_dir = {'': 'script.module.simple-requests/libs'},
    py_modules=['simple_requests'],
    zip_safe=False
)
