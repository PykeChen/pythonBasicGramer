# strspn(str1,str2)
str1 = '12345678'
str2 = '456'
# str1 and chars both in str1 and str2
print(str1 and str2)

str1 = 'cekjgdklab'
str2 = 'gka'
nPos = -1
for c in str1:
    if c in str2:
        nPos = str1.index(c)
        break
print(nPos)
