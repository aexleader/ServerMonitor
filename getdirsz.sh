#! /bin/bash

# use KB as unity.
function GetDirSz
{
    size=`du -d 0 $1 | sed -n 1p | awk '{print $1}'`
    echo $size
}

GetDirSz $1
