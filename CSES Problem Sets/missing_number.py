# -*- coding: utf-8 -*-
"""Missing Number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lVGYzjRqf81TI6FKlE6YL9DHcPAvR4NL
"""

n = int(input())
nums = sorted(list(map(int, input().split())))
print((n * (n+1)) // 2 - sum(nums))

