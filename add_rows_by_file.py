#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: edoardottt
https://edoardoottavianelli.it
"""

import sys

def add_func():
    word = sys.argv[1]
    new_file = 'README.md'
    with open(word) as f:
        text = f.read().split()
    with open(new_file) as f:
        t = f.read()
    ls = []
    for elem in text:
        if elem in t: ls.append(elem)
    if len(ls)!=0: return 'To check: '+str(ls)
    with open(new_file,'a+') as f:
        for i in range(len(text)):
            elem = text[i]
            stri = stringed(elem)
            f.write(stri)
    return 'OK'

def stringed(elem):
	if elem[-1]!='_': stri = '| '+elem+' | '+'https://instagram.com/'+elem+' |\n'
	else:
		stri = '| '+elem+' | '+'['+'https://instagram.com/'+elem+'](https://instagram.com/'+elem+') |\n'
	return stri

print(add_func())