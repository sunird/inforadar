#coding=utf-8
#Time : 2019-01-21
__auther__ = 'n00b\'*'
__version__ = '1.0.2'

#from socket import *

import os
import re
import sys
import time
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



# HeaderInfo to get domain Header's info
# Created by Nerium at 2019/01/21
# Modify by Nerium at 2019/03/05
def Public_HeaderInfo(domain) :
    
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
            return ''

    get_ip = Public_GetIP(domain)
    get_header = get_response.headers
    print(redddiing + 'Created 5ocket & Got IP & Got Header Info Yet.')
    use_cdn = 'NO'

    # Check response header to confirm CDN and use proxy to check it...
    print(greenning + 'Detecting CDN...', end='\r')
    try :
        cmd_nsl_res = os.popen("nslookup {}".format(domain))
        nsl_res_str = cmd_nsl_res.read()
    except :
        print(red___b + '[!]Please Use Linux PC To Run This Program.' + color_e)

    if 'canonical' in nsl_res_str :
        use_cdn = 'YES'
    print(redddiing + 'Detected CDN State : {}.'.format(use_cdn))

    # Log website server info
    print(greenning + 'Detecting Server...', end='\r')
    try :
        get_server = get_header['Server']
    except :
        get_server = 'HIDDEN'
    print(redddiing + 'Detected Server State : {}.'.format(get_server))

    return get_response;



# Get second domain by recompile and create thread pool to scan all web
# Created by Nerium at 2019/02/04
# Modify by Nerium at 2019/03/05
def Public_SecDomainIn(domain, response) :

    if domain == '' or response == '' :
        return ''
    
    print(greenning + 'Searching Second Domains', end='\r')
    
    split_domain_str = domain.split('.');
    domain_str = '\w[-\w.+]*'
    for i in range(1,len(split_domain_str)) :
        domain_str = domain_str + '\.' + split_domain_str[i]
    regx = re.compile(domain_str);

    regx_res = regx.findall(response.text)
    regx_res.append(domain)
    
    fin_res = list(set(regx_res))
    print(redddiing + 'Found ' + str(len(fin_res)) + ' Domains Totally Include Original Domain.')

    return fin_res
