#!/bin/bash

# delete previous analysis results
result_addr=$(tail -n1 present_server_config.txt)
rm -rf ${result_addr}/*

# run run_present_server.sh
bash /home/atlas/kc401-Group3/sample-videoanalysisperson/run_present_server.sh < /home/atlas/kc401-Group3/present_server_config.txt
echo "present server has started up!"

# run sample-videoanalysisperson
hiai_ip='172.168.225.2:22118'
proj_name='sample-videoanalysisperson'
proj_path='/home/atlas/kc401-Group3/sample-videoanalysisperson/run'
ddk_path='/home/atlas/.mindstudio/huawei/ddk/1.32.0.B080/ddk'
python /home/atlas/MindStudio-ubuntu/tools/run.py -i ${hiai_ip} -n ${proj_name} -j ${proj_path} -k ${ddk_path} -T RUN -M HIAI

