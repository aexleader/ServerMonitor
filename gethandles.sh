#! /bin/bash

function GetHandles
{
    DES=`ls /proc/$1/fd | wc -l` 
    echo $DES 
}

PID=`./getpid.sh $1 $2`

GetHandles $PID
