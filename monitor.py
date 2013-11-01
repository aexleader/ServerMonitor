'''
Monitor wrap the bash scripts for python user.
Error Code:
-1	Not get the value correctly

Contributor:
Zhongkai Mi	<zhongkai.mi@gmail.com>
'''

# -*- coding:gbk -*-

from subprocess import PIPE
from subprocess import call
from subprocess import Popen

import os

class Monitor(object):

    ENVIRONMENT = os.environ
    WORK_DIR = ''
    
    def __init__(self):
        self.WORK_DIR = os.path.dirname(__file__)
        self.ENVIRONMENT['PATH'] = ':'.join([self.ENVIRONMENT['PATH'], self.WORK_DIR])
        
    def getCPUUtilization(self, userName, procName):
        '''
        Utilization return percentage without % signal.
        E.x utilization = 0.2 means 0.2%
        '''
        try:
            proc = Popen('./getcpu.sh ' + userName + ' ' + procName,
                         shell=True,
                         env = self.ENVIRONMENT,
                         cwd=self.WORK_DIR,
                         stdout = PIPE,)
            utilization = proc.communicate()[0]
            
            return float(utilization.strip())
        except OSError:
            return -1.0

    def getMemUsage(self, userName, procName):
        '''
        Utilization return memory with megabyte.
        '''
        try:
            proc = Popen('./getmem.sh ' + userName + ' ' + procName,
                         shell=True,
                         env = self.ENVIRONMENT,
                         cwd=self.WORK_DIR,
                         stdout = PIPE,)
            utilization = proc.communicate()[0]
            return float(utilization.strip())
        except OSError:
            return -1.0

    def getDiskUtilization(self, dirName):
        '''
        Return the utilization of disk the responding directory is in.
        '''
        try:
            proc = Popen('./getdiskc.sh ' + dirName,
                         shell=True,
                         env = self.ENVIRONMENT,
                         cwd=self.WORK_DIR,
                         stdout = PIPE,)
            utilization = proc.communicate()[0]
            return float(utilization.strip())
        except OSError:
            return -1.0
        
    def getDirSize(self, dirName):
        '''
        Return the size of directory in megabyte.
        This function need to keep the current working directory of the caller environment
        '''
        try:
            proc = Popen('getdirsz.sh ' + dirName,
                         shell=True,
                         env = self.ENVIRONMENT,                                               stdout = PIPE,)
            utilization = proc.communicate()[0]
            return float(utilization.strip())
        except OSError:
            return -1.0
        
    def getHandles(self, userName, procName):
        '''
        Return the number of handles opened by responding process.
        '''
        try:
            proc = Popen('./gethandles.sh ' + userName + ' ' + procName,
                         shell=True,
                         env = self.ENVIRONMENT,
                         cwd=self.WORK_DIR,
                         stdout = PIPE,)
            utilization = proc.communicate()[0]
            return int(utilization.strip())
        except OSError:
            return -1
        
if __name__ == "__main__":
    monitor = Monitor()
    ans = monitor.getCPUUtilization("washington", "emacs")
    ans2 = monitor.getCPUUtilization("root", "emacs")
    print ans, ans2
    
    ans3 = monitor.getMemUsage("washington", "emacs")
    ans4 = monitor.getMemUsage("root", "emacs")
    print ans3, ans4

    ans5 = monitor.getDiskUtilization("/")
    ans6 = monitor.getDirSize("~/monitors")
    print ans5, ans6
        
    ans7 = monitor.getHandles("washington", "emacs")
    print ans7
    
