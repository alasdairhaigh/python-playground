import re

# Your code goes here
functionList = dir(re)
alphaFindList = []

for function in functionList:
    if function.startswith('find'):
        alphaFindList.append(function)

alphaFindList.sort()
print(alphaFindList)
