# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import os
from uploadpic.models import IMG
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse
import json

def upload(request):
    return render(request, 'uploadpic/templates/upload.html')

def show(request):
    img_root = os.path.join('video', 'channel1', 'stack_0')
    img_folder_list = os.listdir(os.path.join('media', img_root))
    img_folder_list = [int(i) for i in img_folder_list]
    img_folder_list.sort()
    img_folder_list = img_folder_list[1:]
    img_folder_list = [str(i) for i in img_folder_list]
    paginator = Paginator(img_folder_list, 1)

    if request.method == 'GET':
        page = request.GET.get('page')
        try:
            img_folder = paginator.page(page)
        except PageNotAnInteger:
            img_folder = paginator.page(1)
        except InvalidPage:
            return HttpResponse('Cannot find the content of this page')
        except EmptyPage:
            img_folder = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        page = request.POST['q']
        page = int(page)
        try:
            img_folder = paginator.page(page)
        except PageNotAnInteger:
            img_folder = paginator.page(1)
        except InvalidPage:
            return HttpResponse('Cannot find the content of this page')
        except EmptyPage:
            img_folder = paginator.page(paginator.num_pages)

    real_img_folder = img_folder_list[img_folder.number - 1]
    real_img_folder = os.path.join(img_root, real_img_folder)
    raw_img = IMG(img=os.path.join(real_img_folder, 'image.jpg'))
    print(os.path.join(real_img_folder, 'image.jpg'))
    has_face = 0
    face_img = None
    infer = None
    if 'face_1' in os.listdir(os.path.join('media', real_img_folder)):
        has_face = 1
        face_img = IMG(img=os.path.join(real_img_folder, 'face_1', 'image.jpg'))
        json_file = open(os.path.join('media', real_img_folder, 'face_1', 'inference.json'))
        json_str = json_file.readlines()[0]
        infer = json.loads(json_str)
    content = {
        'img_folder': img_folder,
        'raw_img': raw_img, 
        'has_face': has_face,
        'face_img': face_img,
        'infer': infer,
    }

    return render(request, 'uploadpic/templates/show.html', content)
