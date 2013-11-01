#! /bin/bash

function Listening 
{ 
    TCPListeningnum=`netstat -an | grep "$1 " | awk '$1 == "tcp" && $NF == "LISTEN" {print $0}' | wc -l` 
    UDPListeningnum=`netstat -an | grep "$1 " | awk '$1 == "udp" && $NF == "0.0.0.0:*" {print $0}' | wc -l` 
    (( Listeningnum = TCPListeningnum + UDPListeningnum )) 
    if [ $Listeningnum == 0 ] 
    then 
	{ 
            echo "0"
	} 
    else 
	{ 
	    echo $Listeningnum
	} 
    fi 
}

Listening $1
