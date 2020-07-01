# EI401 工程实践与科技创新 IV-C

由于我们的项目是基于django框架开发的，因此保留了django框架的代码格式。我将会在这个readme中阐述我们的代码结构及其作用。

## 单个文件
单个文件是指本repo路径下所有未被文件夹包含的文件。只有一部分文件被描述了，未被描述的文件均对于项目的意义不大。

* run.sh：运行我们的整个项目
* run_vap.sh：启动Mind Studio项目。
* stop_present_server.sh：项目运行结束后，停止掉虚拟机及Atlas开发板的运行，减轻负载。

## EI401-KC4C 文件夹
这里的文件主要属于配置文件，由django框架自行生成主体结构，我们需要改动settings.py中的相关设置来完成项目。此外，urls.py文件主要用于调用templates文件夹中的html，从而实现web的布局。

## AIFace 文件夹
我们的主要工作集中于这个文件夹中。
* models.py：定义了IMG类
* run_vap.py：实现了Mind Studio的工作类，调用run_vap.sh脚本实现运行，并给出接口告知是否已解析完成视频。
* search.py：主要用于视频文件的上传，以及让用户等待视频解析的功能。
* views.py：实现了解析完成后的图片以及其他预测信息的上传和展示。

## templates 文件夹

templates文件夹保存了三个html文件，用于布局web。