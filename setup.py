import sys

from setuptools import setup

setup(
      name             =   'med2image',
      version          =   '1.1.1',
      description      =   '(Python) utility to convert medical images to jpg and png',
      long_description =   readme(),
      author           =   'FNNDSC',
      author_email     =   'dev@babymri.org',
      url              =   'https://github.com/FNNDSC/med2image',
      packages         =   ['med2image'],
      install_requires =   ['nibabel', 'pydicom', 'numpy', 'matplotlib', 'pillow'],
      #test_suite       =   'nose.collector',
      #tests_require    =   ['nose'],
      license          =   'MIT',
)
