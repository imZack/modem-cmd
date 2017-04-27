#!/usr/bin/env python

""" modem-cmd installation script """

VERSION = '1.0.0'

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
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Telephony',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Hardware',
        'Topic :: Terminals :: Serial',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
    ]
)
