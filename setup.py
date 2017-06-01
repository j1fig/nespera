from setuptools import setup
from setuptools import find_packages

_version = '0.1.0'
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])


setup(
    name='nespera',
    version=_version,
    description='a small and juicy fruit',
    author='Joao Figueiredo',
    author_email='joaonvfigueiredo@gmail.com',
    url='http://nespera.org',
    install_requires=[],
    packages=_packages,
    include_package_data=True,
)
