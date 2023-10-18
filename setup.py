from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in emd_management/__init__.py
from emd_management import __version__ as version

setup(
	name="emd_management",
	version=version,
	description="Emd Management App",
	author="FinByz",
	author_email="info@finbyz.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
