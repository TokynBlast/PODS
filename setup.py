"""
Setup script for the PODS package.
Handles package configuration and extension building.
"""

from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension, build_ext

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS',
    'License :: Other/Proprietary License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.13',
    'Programming Language :: Python :: 3.13.2',
]

setup(
    name='Python Oriented Data Storage',
    version='0.1.0',
    description='JSON, but built for Python!',
    long_description=(open('README.md', encoding='utf-8').read() + '\n\n' +
                      open('CHANGELOG.md', encoding='utf-8').read() + '\n\n' +
    long_description_content_type='text/markdown',
    url='https://github.com/TokynBlast/PODS',
    author='Tokyn Blast',
    author_email='tokynblast@gmail.com',
    license='Bspace',
    classifiers=classifiers,
    keywords='variant, pods, data, storage, json, pod',
    packages=find_packages(),
    install_requires=[],
    python_requires="=3.13.2",
    platforms=["Windows", "Linux", "MacOS"],
)
