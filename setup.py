#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='txStomper',
      version='1.0.2',
      description='STOMP client library for Twisted Python',
      author='Twingly AB',
      author_email='oskar@osd.se',
      url='http://github.com/twingly/txStomper',
      packages=find_packages(),
      install_requires=['setuptools', 'stomper'],
     )