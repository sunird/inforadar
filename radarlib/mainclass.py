#coding=utf-8
#Time : 2019-08-28
author = 'dynamic program security team'
version = '1.0.1'

from .publicfunc import *
import threading


green_s = '\033[32m'
red___s = '\033[31m'
red___b = '\033[41m'
color_e = '\033[0m'

greenning = '[' + green_s + '-' + color_e + ']'
redddiing = '[' + red___s + '+' + color_e + ']'


# Mainclass
# Created by Nerium at 2019/08/28
# Modify by Nerium at 2019/08/28
class Mainclass :
    number = 0
    mainurl = ''
    domainip = ''
    webtype = ''
    cdnflag = ''
    pathfile = ''
    server = ''
    container = ''
    language = ''
    cms = ''
    vitimpath = []
    wkuser = []
    wkpwd = []
    secdomain = []



# Scan&attack thread
# Created by Nerium at 2019/08/28
# Modify by Nerium at 2019/08/28
class sathread(threading.Thread) :
    def __init__(self, domain, number) :
        threading.Thread.__init__(self)

        thread_class = Mainclass()
        thread_class.mainurl = domain
        thread_class.number = number

        self.target = thread_class

    def scan(self) :
        print(greenning + 'Scanning {}...'.format(self.target.mainurl), end='\r')
        
        #Use Scan Tools 2 Scan Website
        mid_res = Public_Response(self.target.mainurl)

        mid_header = Public_HeaderInfo(self.target.mainurl)
        self.target.domainip = mid_header[0]
        self.target.server = mid_header[1]
        self.target.cdnflag = mid_header[2]

        self.target.secdomain = Public_SecDomainIn(self.target.mainurl, mid_res, True)

        print(redddiing + 'Detected {} Founded {} Weak Points & Pass {} Points.'.format(self.target.mainurl, '?', '?'))

    def attack(self) :
        print(greenning + 'Attacking {}...'.format(self.target.mainurl), end='\r')

        #Use Attack Tools 2 Attack Website

        print(redddiing + 'Attacked {} Total {} Weak Points & Pass {} Points.'.format(self.target.mainurl, '?', '?'))

    def run(self) :
        self.scan()
        self.attack()

        with open('results.txt', 'a')as f :
            for name, value in vars(self.target).items() :
                f.write('[{}] ==> {} --> {}\n'.format(self.target.number, name, value))
            f.write('\n')
        f.close()
