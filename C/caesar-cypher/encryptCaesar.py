#!/usr/bin/env python

story = "Teste"
shift = 12
ceasar = lambda s,n:''.join([(lambda c,u:c.upper() if u else c)(("abcdefghijklmnopqrstuvwxyz"*2)[ord(c.lower())-97+n%26],c.isupper())if c.isalpha() else c for c in s])
print(ceasar(story, shift))
