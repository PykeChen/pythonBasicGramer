
for line in open("BasicGrammar/dict.py"):
    # print line,  #python2 用法
    print(line)

with open('BasicGrammar/dict.py', 'r') as f:
    # read_data = f.read()
    # print(read_data)
    for line in f:
        print(line)

# 写入文件
with open('BasicGrammar/wirte_test.py', 'w+') as f:
    f.write('This is a line by my code')
