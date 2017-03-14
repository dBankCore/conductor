# coding=utf-8
import sys
from setuptools import find_packages
from setuptools import setup

assert sys.version_info[0] == 3 and sys.version_info[1] >= 5, "steem requires Python 3.5 or newer"

# yapf: disable
setup(
    name='conductor',
    version='0.1',
    description='Steem Witness Toolkit',
    long_description=open('README.md').read(),
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest',
                   'pep8',
                   'pytest-pylint',
                   'sphinx',
                   'recommonmark',
                   'sphinxcontrib-restbuilder',
                   'sphinxcontrib-programoutput',
                   'pytest-console-scripts'],
    install_requires=[
        'Click',
        'steem',
        'grequests',
        # 'maya',
        # 'toolz',
        # 'funcy',
    ],
    entry_points={
        'console_scripts': [
            'conductor=conductor.cli:witness',
        ]
    })
