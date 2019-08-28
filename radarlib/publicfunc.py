#coding=utf-8
#Time : 2019-01-21
__author__ = 'dynamic program security team'
__version__ = '1.0.2'

#from socket import *

import os
import re
import sys
import socket
import requests
import subprocess



green_s = '\033[32m'
red___s = '\033[31m'
red___b = '\033[41m'
color_e = '\033[0m'

greenning = '[' + green_s + '-' + color_e + ']'
redddiing = '[' + red___s + '+' + color_e + ']'



# Get ip from socket packet
# Created by Nerium at 2019/01/21
# Modify by Nerium at 2019/01/21
def Public_GetIP(domain) :

    if domain == '' :
        return ''

    try :
        mid_ip = socket.getaddrinfo(domain, None)
        mid_ip = mid_ip[0][4][0]
    except :
        mid_ip = '127.0.0.1'

    return mid_ip



# Response to get response
# Created by Nerium at 2019/08/28
# Modify by Nerium at 2019/08/28
def Public_Response(domain) :
    
    if domain == '' :
        return ''
    
    # Try and except to solve https and http or other wrong problems
    print(greenning + 'Create 5ocket & Get IP & Get Header Info...', end='\r')
    try :
        url = 'http://' + domain
        get_response = requests.get(url, timeout=2)
    except :
        try :
            url = 'https://' + domain
            get_response = requests.get(url, timeout=2)
        except :
            print(red___b + '[!]Can\'t Create 5ocket With This Domain. Please Check It.' + color_e)
            get_response = ''
    
    return get_response



# HeaderInfo to get domain Header's info
# Created by Nerium at 2019/01/21
# Modify by Nerium at 2019/08/28
def Public_HeaderInfo(domain) :

    get_response = Public_Response(domain)

    get_ip = Public_GetIP(domain)
    
    try :
        get_header = get_response.headers
    except :
        return [get_ip, 'HIDDEN', 'HIDDEN']
    
    print(redddiing + 'Created 5ocket & Got IP & Got Header Info Yet.')
    use_cdn = 'HIDDEN'

    # Check response header to confirm CDN and use proxy to check it...
    print(greenning + 'Detecting CDN...', end='\r')
    try :
        cmd_nsl_res = os.popen("nslookup {}".format(domain))
        nsl_res_str = cmd_nsl_res.read()
    except :
        print(red___b + '[!]Please Use Linux PC To Run This Program.' + color_e)

    if 'canonical' in nsl_res_str :
        use_cdn = 'YES'
    else :
        use_cdn = 'NO'
    print(redddiing + 'Detected CDN State : {}.'.format(use_cdn))

    # Log website server info
    print(greenning + 'Detecting Server...', end='\r')
    try :
        get_server = get_header['Server']
    except :
        get_server = 'HIDDEN'
    print(redddiing + 'Detected Server State : {}.'.format(get_server))

    res = []
    res.append(get_ip)
    res.append(get_server)
    res.append(use_cdn)

    return res



# Get second domain by recompile
# Created by Nerium at 2019/02/04
# Modify by Nerium at 2019/08/28
def Public_SecDomainIn(domain, response, flag = False) :

    if domain == '' or response == '' :
        return ''
    
    print(greenning + 'Searching Second Domains', end='\r')
    
    split_domain_str = domain.split('.')
    domain_str = '\w[-\w.+]*'
    for i in range(1,len(split_domain_str)) :
        domain_str = domain_str + '\.' + split_domain_str[i]
    regx = re.compile(domain_str)

    regx_res = regx.findall(response.text)
    regx_res.append(domain)
    
    fin_res = set(regx_res)
    if flag :
        fin_res.remove(domain)
    fin_res = list(fin_res)

    if flag :
        print(redddiing + 'Found ' + str(len(fin_res)) + ' Domains Totally Don\'t Include Original Domain.')
    else :
        print(redddiing + 'Found ' + str(len(fin_res)) + ' Domains Totally Include Original Domain.')
    return fin_res
