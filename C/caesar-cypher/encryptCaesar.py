#!/usr/bin/env python
import sys

story = sys.argv[1]
shift = sys.argv[2]
ceasar = lambda s,n:''.join([(lambda c,u:c.upper() if u else c)(("abcdefghijklmnopqrstuvwxyz"*2)[ord(c.lower())-97+n%26],c.isupper())if c.isalpha() else c for c in s])
print(ceasar(story, shift))
