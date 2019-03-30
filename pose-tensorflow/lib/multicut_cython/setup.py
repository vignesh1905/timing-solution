from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from sys import platform as _platform
import os
import numpy as np

#openmp_arg = '-fopenmp'
#if _platform == "win32":
#    openmp_arg = '-openmp'

extensions = [
  Extension(
    'multicut', ['multicut.pyx', 'src/nl-lmp.cxx'],
    language="c++",
    include_dirs=[np.get_include(), '.', 'include', 'src'],
    extra_compile_args=['-std=c++11','-O3','-stdlib=libc++', '-mmacosx-version-min=10.9', '-DHAVE_CPP11_INITIALIZER_LISTS','-v'],
    extra_link_args=['-std=c++11', '-L./','-stdlib=libc++', '-mmacosx-version-min=10.9']
  )
]

setup(
    name = 'multicut',
    ext_modules = cythonize(extensions)
)
