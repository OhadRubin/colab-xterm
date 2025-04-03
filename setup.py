#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages  # type: ignore
import os

def _get_version():
    version_file = os.path.normpath(os.path.join(os.path.dirname(__file__), 'colabxterm', 'VERSION'))
    with open(version_file) as fh:
        version = fh.read().strip()
        return version

# Try to read README.md, but provide a fallback if it's not available
try:
    with open('README.md', 'r') as readme_file:
        long_description = readme_file.read()
except (IOError, FileNotFoundError):
    long_description = "Open a terminal in Google Colab, including the free tier."

setup(name='colab-xterm',
      version=_get_version(),
      description='Open a terminal in colab, including the free tier.',
      long_description_content_type="text/markdown",
      long_description=long_description,
      url='https://github.com/InfuseAI/colab-xterm',
      project_urls={
          "Bug Tracker": "https://github.com/InfuseAI/colab-xterm/issues",
      },
      python_requires=">=3.6",
      packages=["colabxterm"],
      package_data={
          'colabxterm': ['client/dist/*', 'VERSION']
      },
      include_package_data=False,
      install_requires=['ptyprocess~=0.7.0', 'tornado>5.1'],
      extras_require={
          'dev': [
              'jupyter',
              'twine'
          ],
      }
      )
