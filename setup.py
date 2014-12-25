#!/usr/bin/env python

""" modem-cmd installation script """

VERSION = '0.0.1'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    requires = f.readlines()

setup(name='modem-cmd',
      version='{0}'.format(VERSION),
      description='Send arbitrary AT commands to your modem',
      license='MIT',
      author='YuLun Shih',
      author_email='shih@yulun.me',
      url='https://github.com/imZack/modem-cmd',
      download_url=
      'https://github.com/imZack/modem-cmd/archive/{0}.tar.gz'.format(VERSION),
      keywords=['modem', 'at commands', 'serial'],
      modules=['modem_cmd'],
      scripts=['modem_cmd.py'],
      install_requires=requires
      )
