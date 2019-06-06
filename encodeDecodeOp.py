
print('北'.encode('unicode_escape').decode())

emojStr = '😂️'
transform = emojStr.encode('unicode_escape')
print(transform)
print(type(transform))
print(transform.decode('unicode_escape'))

tmpS = '\ud83d\ude02'
print('字符=', tmpS.decode('unicode_escape'), end='')

# tmpS = b'\ufe0f'
# tmpS = b'\uD83D\uDE02'
# print('字符=', tmpS.decode('unicode_escape'), end='')