# -*- coding: utf-8 -*-
"""Permutations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lVGYzjRqf81TI6FKlE6YL9DHcPAvR4NL
"""

n = int(input())
if n == 1:
  print("1")
elif n < 4:
  print("NO SOLUTION")
else:
  for i in range(2, n + 1, 2):
    print(i, end = " ")
  for i in range(1, n + 1, 2):
    print(i, end = " ")
