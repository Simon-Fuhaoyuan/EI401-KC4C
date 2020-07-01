#!/bin/bash

# stop present_server
i=$(ps -ef | grep presenter | grep video_analysis_person | grep -o '[0-9]\{1,\}' | head -n1)
if test -z "$i"
then
	echo "presenter server not in process!"
else
	kill -9 $i
	echo "presenter server stop success!"
fi

# delete analysis results
result_addr=$(tail -n1 present_server_config.txt)
# echo "do you want to delete the analysis results? (in ${result_addr}) [y/n]:"
# read a
#a=y
#if test "$a" = "y"
#then
#	rm -rf ${result_addr}/*
#	echo "delete files in ${result_addr} success!"
#else
#	echo "files in ${result_addr} remained!"
#fi
