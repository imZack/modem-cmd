#!/usr/bin/env python

""" modem-cmd installation script """

VERSION = '1.0.1'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    requires = f.readlines()

setup(
    name='modem-cmd',
    version='{0}'.format(VERSION),
    description='Send arbitrary AT commands to your modem',
    license='MIT',
    author='YuLun Shih',
    author_email='shih@yulun.me',
    url='https://github.com/imZack/modem-cmd',
    download_url=(
        'https://github.com/imZack/modem-cmd/archive/{0}.tar.gz'
            .format(VERSION),
    ),
    keywords=['modem', 'at commands', 'serial'],
    packages=['modemcmd'],
    scripts=['bin/modem-cmd'],
    install_requires=requires,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Communications :: Telephony',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Hardware',
        'Topic :: Terminals :: Serial',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
    ]
)
