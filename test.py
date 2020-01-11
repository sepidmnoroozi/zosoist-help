code = "L10: _rating=4;L11: a=7;L12: b=6;"
token_list = code.split(':')
print(token_list[0])
print(token_list[-2])

token_list = token_list[-2].split(";")
print(token_list[-1])

num = int(token_list[-1].replace("L", ""))
print(num)
num = num + 1
print(num)