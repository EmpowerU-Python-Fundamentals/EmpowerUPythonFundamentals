import re


# text = "Softserve Academy"
# pattern = "Sof"
# result = re.match(pattern, text)
# print(result)
# pattern = "Ac"
# result = re.match(pattern, text)
# print(result)

# result = re.search(pattern, text)
# print(result)

# pattern = "e"
# result = re.findall(pattern, text)
# print(result)

# pat = re.compile(pattern)

# result = pat.findall(text)
# print(result)

text = """Regular expressions originated in 1951, when mathematician Stephen Cole Kleene described regular languages using his mathematical notation called regular events.[6][7] These arose in theoretical computer science, in the subfields of automata theory (models of computation) and the description and classification of formal languages, motivated by Kleene's attempt to describe early artificial neural networks. (Kleene introduced it as an alternative to McCulloch & Pitts's "prehensible", but admitted "We would welcome any suggestions as to a more descriptive term."[8]) Other early implementations of pattern matching include the SNOBOL language, which did not use regular expressions, but instead its own pattern matching constructs.
aaa aabcs"""


# pattern = "[it5Mr]"
# result = re.findall(pattern, text)
# print(result)
# # pattern = "\d"
# pattern = "\w"
# result = re.findall(pattern, text)
# print(result)
# pattern = "[a-zA-C]"
# result = re.findall(pattern, text)
# print(result)
# pattern = "\d"
pattern = "m..e"
result = re.findall(pattern, text)
print(result)
pattern = "[a]{2,3}"
result = re.findall(pattern, text)
print(result)

# result = re.search(pattern, text)
# print(result)

import os
print(os.getenv("Path"))

[a-mA-Z]