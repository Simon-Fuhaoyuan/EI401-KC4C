This file is readme for run_vap.sh, present_server_config.txt, and stop_present_server.sh.

present_server_config.txt:
Contain parameters for run_present_server, which are the remote ip and the path of analysis results. The address is used when starting presenter server and stop it in stop_present_server.sh.

run_vap.sh:
To run this file, use 'bash run_vap.sh' in terminal, same as the other .sh file
This file start the presenter server (using run_present_server.sh in ./sample-videoanalysisperson) and run the project. 
Note that if the presenter server has been running, it will be killed and then restart, and files in the analysis results folder are deleted before restart.

stop_present_server.sh:
This file kill the presenter server and delete files in the analysis results folder.
Note that the path of analysis results comes from present_server_config.txt, so do not change it when the presenter server is running.

Default show address: 172.168.225.102:7011
Path of video resource: fixed in MindStudio. Change it through MindStudio and then rebuild the project
Path of analysis result: in present_server_config.txt

