#! /bin/bash

function GetDiskSpc 
{
    if [ $# -ne 1 ] 
    then 
        return 1 
    fi 

    Folder="$1$"
    DiskSpace=`df -k |grep $Folder | sed -n 1q | awk '{print $5}' | awk -F% '{print $1}'`
    echo $DiskSpace 
}

GetDiskSpc $1

