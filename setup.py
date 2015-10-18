from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bdr_replication',
    version='0.1',
    description='A wrapper around BDR Replications',
    long_description=long_description,

    url='https://github.com/sebinjohn/cloudera_bdr',
    author='Sebin John',
    author_email='sebin.john.sebin@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='cloudera bdr replication manager',
    py_modules=['replications'],
    install_requires=[
        'cm-api>=3',
        'requests'
    ]
)
