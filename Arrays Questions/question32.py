# Reverse an array without affecting special characters
import string

# "a,b$c"
str = "Ab,c,de!$"
size = len(str)
alphabets = string.ascii_letters
specials, chars = {}, []
for i in range(size):
    if str[i] in alphabets:
        chars.append(str[i])
    else:
        specials[i] = str[i]

reverse_chars = [chars[chx] for chx in range(len(chars)-1, -1, -1)]
temp = [item for item in str]

rvxid = 0
for idx in range(size):
    if (temp[idx] in reverse_chars) and (rvxid < len(reverse_chars)):
        temp[idx] = reverse_chars[rvxid]
        rvxid += 1

output = "".join(temp)

print(f"""
Input: {str}
Output: {output}
""")