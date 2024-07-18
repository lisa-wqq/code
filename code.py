import re

def string_practice(s):
    match = re.search(r'\d+(\.\d+)?', s)
    number_str = match.group()
    if '.' in number_str:
        number_str1,number_str2 = number_str.split(".")
        if len(number_str2) > 2:
            number_str2 = number_str2[0:2]
            return f'{number_str1}.{number_str2}'
        else:
            return number_str
    if '.' not in number_str:
        if len(number_str) > 0:
           number_str += '.00'
        else:
            number_str = ""
    return number_str
