import sys
import os
sys.path.append('../')
import monitor

def checkAverageCPU():
    '''
    Checking the CPU usage by getting mutiple values and return the mean.
    '''
    utilization = 0.0
    mon = monitor.Monitor()
    for i in range(0, 100):
        rtn = mon.getCPUUtilization("washington", "python SampleTest")
        utilization += rtn

    utilization /= 100.0
    print "This case used", str(utilization)+"% CPU capcity."

def checkMemUsage():
    '''
    Checking the Mem Cost 
    '''
    mon = monitor.Monitor()
    rtn = mon.getMemUsage("washington", "python SampleTest")
    print "This case take", str(rtn) + "M of memory"

def checkDirSize():
    '''
    Query the size of responding directory    
    '''
    mon = monitor.Monitor()
    rtn = mon.getDirSize("../")
    print "This library takes", str(rtn)+"K"

def checkStreamHandles():
    '''
    Query the opened stream handler
    '''
    mon = monitor.Monitor()
    rtn = mon.getHandles("washington", "python SampleTest")
    print str(rtn), "handles opened for this case"

def main():    
    checkAverageCPU()
    checkMemUsage()
    checkDirSize()
    checkStreamHandles()
    
if __name__ == "__main__":
    main()

