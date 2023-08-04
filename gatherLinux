#!/bin/bash
#basic Linux gather to build upon
gatherLinux(){
        echo "Gathering Linux info";
        echo " "
        echo "---------- Info------------" > LinuxInfo.txt
        cat /proc/cpuinfo >> LinuxInfo.txt
        echo "---------- Memory----------" >> LinuxInfo.txt
        cat /proc/meminfo >> LinuxInfo.txt
        echo "---------- DNS-------------" >> LinuxInfo.txt
        cat /etc/resolv.conf >> LinuxInfo.txt
        echo "---------- Network---------" >> LinuxInfo.txt
        cat /etc/network/interfaces >> LinuxInfo.txt
        ifconfig >> LinuxInfo.txt
        echo "---------- User---------" >> LinuxInfo.txt
        id >> LinuxInfo.txt
        w >> LinuxInfo.txt
        last -a >> LinuxInfo.txt
        echo "---------- Processes---------" >> LinuxInfo.txt
        ps -ef >> LinuxInfo.txt
        top >> LinuxInfo.txt
        
}
gatherLinux


#Allow the program to run for about 10 seconds + [allow top to gather intelliegence of data] then do CTRL+C and check LinuxInfo.txt for captured data
