
import re

line = 'hyccpq'
regex_str = '^h.*'
if re.match(regex_str, line):
    print('牛逼')

