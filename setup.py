import os
import re
import sys
import subprocess
from setuptools import setup, find_packages, Command

class CleanCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(['rm', '-vrf', './build', './dist', './*.pyc', './*.pyo', './*.pyd', './*.tgz', './*.egg-info'], check=True)
        subprocess.run(['find', '-type', 'd', '-name', '__pycache__', '-exec', 'rm', '-rf', '{}', '+'], check=True)

def get_init_content():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evillimiter', '__init__.py'), 'r') as f:
        return f.read()

def get_version():
    version_match = re.search(r'^__version__ = [\'"](\d\.\d\.\d)[\'"]', get_init_content(), re.M)
    if version_match:
        return version_match.group(1)
    
    print(f"Unable to locate version string in {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evillimiter', '__init__.py')}")
    sys.exit(1)

def get_description():
    desc_match = re.search(r'^__description__ = [\'"]((.)*)[\'"]', get_init_content(), re.M)
    if desc_match:
        return desc_match.group(1)
    
    print(f"Unable to locate description string in {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evillimiter', '__init__.py')}")
    sys.exit(1)


NAME = 'evillimiter'
AUTHOR = 'bitbrute'
AUTHOR_EMAIL = 'bitbrute@gmail.com'
LICENSE = 'MIT'
VERSION = get_version()
URL = 'https://github.com/bitbrute/evillimiter'
DESCRIPTION = get_description()
KEYWORDS = ["evillimiter", "limit", "bandwidth", "network"]
PACKAGES = find_packages()
INCLUDE_PACKAGE_DATA = True

CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Environment :: Console',
               'Intended Audience :: End Users/Desktop',
               'Intended Audience :: System Administrators',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: Unix',
               'Programming Language :: Python :: 3.9',
               'Programming Language :: Python :: 3 :: Only',
               'Topic :: System :: Networking',
               ]

PYTHON_REQUIRES = '>= 3.9'
ENTRY_POINTS = { 'console_scripts': ['evillimiter = evillimiter.evillimiter:run'] }

INSTALL_REQUIRES = ['colorama',
                    'netaddr',
                    'netifaces',
                    'tqdm',
                    'scapy',
                    'terminaltables'
                    ]

CMDCLASS = { 'clean': CleanCommand }


setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    keywords=KEYWORDS,
    packages=PACKAGES,
    include_package_data=INCLUDE_PACKAGE_DATA,
    version=VERSION,
    python_requires=PYTHON_REQUIRES,
    entry_points=ENTRY_POINTS,
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    url=URL,
    cmdclass=CMDCLASS,
)
