from django.db import models
import os
from uuid import uuid4


def generate_filename(filename):
    # filename: 上传文件的名称
    ext = os.path.splitext(filename)[-1]
    name = uuid4().hex
    return f'files/{name}.{ext}'


def generate_imgname(filename):
    # filename: 上传文件的名称
    ext = os.path.splitext(filename)[-1]
    name = uuid4().hex
    return f'imgs/{name}.{ext}'


# Create your models here.
class UploadFile(models.Model):
    file = models.FileField(upload_to=generate_filename, null=True, blank=True)
    img = models.ImageField(upload_to=generate_imgname, null=True, blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.file.name}=={self.img.name}=={self.desc}'

    class Meta:
        db_table = 't_upload_file'
        verbose_name = '上传文件'
