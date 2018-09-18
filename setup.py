from setuptools import setup, find_packages
from BiometricACS import version

VERSION = version.__version__

with open("README.md", 'r') as f:
    long_description = f.read()

with open("requirements.txt", 'r') as f:
    install_requires = f.read().splitlines()

setup(
    version=VERSION,
    name='BiometricACS',
    license='MIT',
    url='https://github.com/kolpakovd/BiometricACS',
    packages=find_packages(),
    author='Kolpakov Denis',
    author_email='Denis050900@outlook.com',
    long_description=long_description,
    install_requires=install_requires
)