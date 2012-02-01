#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='impermium',
    version='3.1.i',
    author='Connie Chen',
    author_email='connie@livefyre.com',
    url='http://github.com/conniec/impermium-python',
    description = 'Impermium API bindings for Python',
    packages=find_packages(),
    zip_safe=False,
    license='Apache License 2.0',
    install_requires=[
        'simplejson',
    ],
    tests_require=[
        'mock',
        'unittest2',
    ],
    test_suite='unittest2.collector',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)