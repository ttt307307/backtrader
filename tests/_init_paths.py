#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################


import os.path as osp
import sys

def add_path(path):
  if path not in sys.path:
    sys.path.insert(0, path)

this_dir = osp.dirname(__file__)

# lib_path = osp.join(this_dir, '..', 'backtrader')
lib_path = osp.join(this_dir, '..')
add_path(lib_path)

print('---------- %s' % (sys.path))

import backtrader