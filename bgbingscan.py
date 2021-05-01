import os
import sys
import argparse

parser = argparse.ArgumentParser(description='bgbingscan help')
parser.add_argument('-v','--vuln', help='Please Input a vuln number!',default='')
args=parser.parse_args()
if args.vuln!="":
    number=args.vuln
    number=int(number)
    if number==13579:
        langling='"蓝凌OA custom.jsp 任意文件读取漏洞.py"'
        os.system("cd payload &&"+langling)
    elif number==135791:
        langling='"蓝凌OA custom.jsp 任意文件读取漏洞批量扫描.py"'
        os.system("cd payload &&"+langling)
else:
    print("""
\033[1;36m __               __                               \033[0m
\033[1;36m[  ]             [  ]                              \033[0m
\033[1;36m|  |             |  |     \     _ .--.  ------     \033[0m
\033[1;36m|  |.--..------  |  |.--.----- [ `.-. | /     \    \033[0m
\033[1;36m|      \/      \ |      \    / | |  | | |           \033[0m 
\033[1;36m|      ||        |      |   /  | |  | |  \__ _ _| scan \033[0m
\033[1;36m|.__ _/  \__ _ _||.__ _/   /__[___| [__]        |   \033[0m
\033[1;36m                |                               |    \033[0m
\033[1;36m                |                         \__ _ /      \033[0m    
\033[1;36m          \__ _ /           """)
    print("\n")
    print('\033[1;36m   使用方法\033[0m')
    print('\033[1;36m           python3 bgbingscan.py -v xxxx\033[0m')
    print('\033[1;36m            or\033[0m')
    print('\033[1;36m           python3 bgbingscan.py --vuln xxxx\033[0m')
    print("\n")
    print('\033[1;36m目前更新漏洞\033[0m')
    print(' \033[1;36m          2021/5/1 蓝凌OA custom.jsp 任意文件读取漏洞 (13579)\033[0m ')
    print(' \033[1;36m          2021/5/1 蓝凌OA custom.jsp 任意文件读取漏洞 (135791)\033[0m ')
    sys.exit()

