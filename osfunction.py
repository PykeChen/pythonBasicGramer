import os
import shutil
import glob
import sys


print('argv', sys.argv)
dir(os)
pwd = os.getcwd()
print(pwd)

sepIndex = pwd.rindex('/') + 1
dir = pwd[sepIndex:]
print(sepIndex, ' dir = ', dir)

shutil.copyfile(f'{pwd}/BasicGrammar/osfunction.py',
                f'{pwd}/BasicGrammar/osfun_copy.py')

print('cwd', os.getcwd())

os.system('mkdir totayTmp.py')

os.chdir('./PassGAN')
print('cwd', os.getcwd())

# 搜索文件
paths = glob.glob('*.py')
print(paths)
