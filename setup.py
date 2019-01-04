from setuptools import setup, find_packages

__author__ = 'Jason Koh'
__version__ = '0.0.1'

install_reqs = parse_requirements(open('requirements.txt'))
reqs = [ir.name for ir in install_reqs]

setup(
    name = 'timeseries_interface',
    version = __version__,
    packages = find_packages(),
    description = 'A wrapper of Timeseries DBs',
    install_requires = reqs,
)

