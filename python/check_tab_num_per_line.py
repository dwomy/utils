#!/usr/bin/python
# coding: utf-8

import sys

num_kinds = []
f = open(sys.argv[1])
for num,line in enumerate(f):
    num_kinds.append(line.count('\t'))
    num_kinds = list(set(num_kinds))
    if len(num_kinds) > 1:
        print num
        break
f.close()

print num_kinds

""" later version >=2.5
from __future__ import with_statement
num_kinds = []
with open(sys.argv[1]) as f:
    for line in f:
        num_kinds.append(line.count('\t'))
        num_kinds = list(set(num_kinds))

print num_kinds
"""
