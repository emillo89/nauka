from collections import Counter
import re

text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""

words = re.findall("\w+",text); """zliczanie slow"""
word = re.findall("\w",text); """zliczanie liter"""
# 10 z najwieksza liczba powtorzen
print(Counter(words).most_common(10))