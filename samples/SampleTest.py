import sys
import os
sys.path.append('../')
import monitor

def queryPID():
    '''
    Get the process ID by username & process description
    '''
    pid = 0
    mon = monitor.Monitor()
    pid = mon.getPID("washington", "python SampleTest")
    print "The process ID of this one is", str(pid)

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
    Query the size of responding directory, As this function use accumulate solution, it's not fit for frequent usage.  
    '''
    mon = monitor.Monitor()
    rtn = mon.getDirSize("../")
    print "This library takes", str(rtn)+"K"

def checkDiskCapacity():
    '''
    Query the usage capacity of disk which the directory is mounted.
    '''
    mon = monitor.Monitor()
    rtn = mon.getDiskUtilization("/")
    print "The disk mounted to / is used", str(rtn)+"%"
    
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
    checkDiskCapacity()
    checkStreamHandles()
    queryPID()
    
if __name__ == "__main__":
    main()

