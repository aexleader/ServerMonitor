#! /bin/bash

# Giving PID by analysis owner and process name.
function GetPID
{
    PsUser=$1
    PsName=$2
    pid=`ps -u $PsUser|grep $PsName|grep -v grep|grep -v grep|grep -v vi|grep -v dbx|grep -v tail|grep -v start|grep -v stop|sed -n 1p|awk '{print $1}'`
    echo $pid
}

PID=`GetPID $1 $2`

if [ "-$PID" == "-" ]
then
    {
	echo -1
    }
else
    {
	echo $PID
    }
fi
