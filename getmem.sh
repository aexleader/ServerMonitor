#! /bin/bash
# This function not list all valid process IDs, so be sure to use right
# process name to unique the object process.
function GetMem
{
    MEMUsage=`ps -o vsz -p $1|grep -v VSZ` 
    (( MEMUsage /= 1000 )) 
    echo $MEMUsage 
}

PID=`./getpid.sh $1 $2`

# branch in case process not exist
if [ $PID -lt 0 ];then
    echo "-1"
else
    GetMem $PID
fi
