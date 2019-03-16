#coding=utf-8
#Time : 2019-01-21
__auther__ = 'n00b\'*'
__version__ = '1.0.0'

from radarlib.publicfunc import *

import os
import re
import sys
import time
import socket
import requests
import subprocess



# Main function
# Created by Nerium at 2019/01/21
# Modify by Nerium at 2019/03/04
if __name__ == '__main__' :

    # get domain by split terminal command
    param = sys.argv[1:]
    param_domain = param[-1]

    # get Header info and return response to recompile all domain
    res = Public_HeaderInfo(param_domain)

    # get all second domain and create thread pool to scan them all
    Public_SecDomainIn(param_domain, res)
