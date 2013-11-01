#! /bin/bash
# This function not list all valid process IDs, so be sure to use right
# process name to unique the object process.
function GetCpu
{
    CpuValue=`ps -p $1 -o pcpu |grep -v CPU | awk '{print $1}'`
    echo $CpuValue
}

PID=`./getpid.sh $1 $2`

# branch in case process not exist
if [ $PID -lt 0 ];then
    echo "-1"
else
    GetCpu $PID
fi
