# problem 10 - finding the frequency of words from a file
import re

doc = open('test_file.txt', 'r')
textz = doc.read().lower()
match = re.findall(r'\b[a-z]{3, 15}\b', textz)