import re

line = 'hyccpq'
regex_str = '^hyq'
print(re.match(regex_str, line))
if re.match(regex_str, line):
    print('牛逼')
else:
    print('没有啦')
