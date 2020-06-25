# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
# from Contr4C import models
import time
import os
from django.shortcuts import redirect
import threading
from django.http import HttpResponse
from run_vap import vap

worker = vap()

ctx ={}

#工作的函数
def work(Thread=None):
    pass

#检测工作的函数
def isworking():
    return True



def search_post(request):
    if request.POST:
        tip = request.FILES['video']
        print(type(tip))
        ticks = int(time.time())
        #这里是在数据库中新加数据
        # models.UpMovie.objects.create(id = ticks, name="person", movie = tip)
        #ctx['rlt'] = './static/images/%d.mp4'%(ticks)
        ctx['rlt'] = './static/images/person.mp4'
        #将读到的文件不经过数据库，直接写成文件，文件地址替换成虚拟机上的地址
        #fout = open('./static/images/%d.mp4'%(ticks), 'wb+')
        fout = open('./static/images/person.mp4', 'wb+')
        for chunk in tip.chunks():
            fout.write(chunk)
        fout.close()
        os.system('bash /home/atlas/kc401-Group3/helloworld1/scripts/transfer.sh')

        #新开线程跑后面的代码
        # _thread.start_new_thread(work,("Thread = working",) )
        t = threading.Thread(target=worker.work, args=('/home/atlas/kc401-Group3/helloworld1/media',))
        t.start()

        return redirect('/result')
    return render(request, "post.html",ctx)



def result(request):
    print("in result")
    if request.POST:
        if not worker.is_working():
            return redirect('/show')
        else:
            ctx['name'] = "Wait Please!!!"

    return render(request, "result.html",ctx)
    #return HttpResponse("Hello world ! ")






# #over
