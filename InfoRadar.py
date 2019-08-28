#coding=utf-8
#Time : 2019-01-21
__author__ = 'dynamic program security team'
__version__ = '1.0.2'

from radarlib.publicfunc import *
from radarlib.mainclass import *

import os
import sys
import socket
import threading



# Main function
# Created by Nerium at 2019/01/21
# Modify by Nerium at 2019/03/04
if __name__ == '__main__' :

    # get domain by split terminal command
    param = sys.argv[1:]
    param_domain = param[-1]

    mainc = Mainclass()
    # get Header info and return response to recompile all domain
    res = Public_Response(param_domain)

    mid_header = Public_HeaderInfo(param_domain)
    mainc.domainip = mid_header[0]
    mainc.server = mid_header[1]
    mainc.cdnflag = mid_header[2]

    # get all second domain and create thread pool to scan them all
    mainc.secdomain = Public_SecDomainIn(param_domain, res, False)

    #print(mainc.secdomain)
    for i in range(len(mainc.secdomain)) :
        t = sathread(mainc.secdomain[i], i)
        t.start()
