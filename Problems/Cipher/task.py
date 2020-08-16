string = "no clouds here to spy on pets"
string = string[0::5]
new_string = ''
for char in string:
    new_string = char + new_string
print(new_string)
