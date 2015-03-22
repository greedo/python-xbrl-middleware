try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
import os

long_description = 'various python-xbrl middlewares for python-xbrl-based API wrappers'
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name='python-xbrl-middleware',
    version='0.0.2',
    description='various python-xbrl middlewares',
    author='Joe Cabrera',
    author_email='jcabrera@eminorlabs.com',
    url='https://github.com/greedo/python-xbrl-middleware/',
    license='Apache License',
    keywords='xbrl, Financial, Accounting, file formats',
    packages=['xbrl_middleware'],
    install_requires=['pytest', 'pep8', 'python-xbrl',
    'xlsxwriter'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial',
    ],
    long_description=long_description
)
