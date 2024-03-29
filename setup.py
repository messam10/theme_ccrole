from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in theme_ccrole/__init__.py
from theme_ccrole import __version__ as version

setup(
	name="theme_ccrole",
	version=version,
	description="New Theme design for Ccrole Company",
	author="Mohammed Al-Qershi",
	author_email="malqershi98@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
