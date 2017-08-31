#!/usr/bin/env python
import os
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(__file__)
for _ in open(os.path.join(BASEDIR, 'lds_org.py')).readlines():
    if _.startswith('__version__'):
        exec(_.strip(), None)
        break

requirements = [
    'requests',
    'certifi'
]

setup(
    name='LDS-org',
    author='Clinton James',
    author_email='clinton.james@anuit.com',
    url='https://www.github.com/jidn/lds-org/',
    download_url='https://github.com/jidn/lds-org/tarball/' + __version__,
    description='Access LDS.org json information',
    long_description=open('README.md').read(),
    version=__version__,
    keywords=['lds'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules=['lds_org'],
    # packages=find_packages(exclude=['tests']),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
    # Install these with "pip install -e '.[paging]'" or '.[docs]'
    # extras_require={
    #     'docs': 'sphinx',
    # }
)
