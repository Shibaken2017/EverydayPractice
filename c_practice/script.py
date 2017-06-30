#just  practice in ussing c code from python

import ctypes

import os
lib = ctypes.cdll.LoadLibrary("./test.so")
print lib.hello()
print lib.hi()
