import re

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)