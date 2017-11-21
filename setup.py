# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='tomobank',
    author='Francesco De Carlo',
    packages=find_packages(),
    version=open('VERSION').read().strip(),
    description = 'Tomography Data Archive.',
    license='BSD-3',
    platforms='Any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: BSD-3',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
