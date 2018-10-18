#from distutils.core import setup
from setuptools import setup, find_packages
from Cython.Build import cythonize

name='test_compile_py2so'

setup(
  packages=find_packages(),
  ext_modules=cythonize(['%s/mod_a/*.py' % name], annotate=False)
)
