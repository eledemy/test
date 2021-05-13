import re

result = re.findall(r'\b[A-Z][a-z]+', 'author.txt')
print(result)
