# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13WezOqXqfnZKqGar0azIYO3zfkvgOdcc
"""

i = 0
while i < len(cast_list_a):
    actor = cast_list_a[i].get('alt').strip()
    cast.append(actor)
    i += 1