# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:34:04 2019
http://batc.bao.ac.cn/BASS/doku.php?id=datarelease:home
@author: dingxu
"""

import os
lenlist = 4
listroute = [0 for i in range(lenlist)]
listroute[0] = 'http://das101.china-vo.org/bass/rawdata/20190105/index.html'
listroute[1] = 'http://das101.china-vo.org/bass/rawdata/20190104/index.html'
listroute[2] = 'http://das101.china-vo.org/bass/rawdata/20190103/index.html'
listroute[3] = 'http://das101.china-vo.org/bass/rawdata/20190102/index.html'

keeppath = [0 for i in range(lenlist)]
keeppath[0] = 'I:/BASS/20190105/'
keeppath[1] = 'I:/BASS/20190104/'
keeppath[2] = 'I:/BASS/20190103/'
keeppath[3] = 'I:/BASS/20190102/'

for i in range(lenlist):    
    cmd = 'python downdata.py'+' '+listroute[i]+' '+keeppath[i]
    os.system(cmd)
