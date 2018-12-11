import os
from distutils.core import setup, Extension

module_device = Extension('device',
                          sources=['device.cpp'],
                          library_dirs=["C:\Program Files (x86)\Windows Kits\8.1\bin\x86"]
                          )

setup(name='WindowsDevices',
      version='1.0',
      description='Get device list with DirectShow',
      ext_modules=[module_device])
