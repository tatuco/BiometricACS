from setuptools import setup, find_packages
from BiometricACS import version
import os

VERSION = version.__version__

os.system(r'pip freeze > '+os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requirements.txt'))

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