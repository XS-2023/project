import os
from uuid import uuid4

from django.shortcuts import render

from .models import UploadFile


# Create your views here.
def upload_file(request):
    global upload
    if request.method == 'GET':
        return render(request, 'upload.html')
    # 上传文件
    elif request.method == 'POST':
        # 获取上传的文件，如果没有文件，则默认为None
        file = request.FILES.get('file')
        img = request.FILES.get('img')
        desc = request.POST.get('desc')
        # 重新给文件命名
        # if file:
        #     file.name = generate_filename(file.name)
        # if img:
        #     img.name = generate_filename(img.name)
        # 实例化一个Upload对象
        upload = UploadFile()
        # 给Upload对象的file属性赋值
        upload.file = file
        upload.img = img
        upload.desc = desc
        # 保存
        upload.save()
    return render(request, 'show.html', {'upload': upload})


def get_file(request, pk):
    # 获取文件
    upload = UploadFile.objects.get(pk=pk)
    return render(request, 'show.html', {'upload': upload})


def generate_filename(filename):
    # filename: 上传文件的名称
    ext = os.path.splitext(filename)[-1]
    name = uuid4().hex
    return f'{name}.{ext}'
