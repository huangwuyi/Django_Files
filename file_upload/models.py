from django.db import models


# Create your models here.
class FileType(models.Model):
    file_type_id = models.CharField(max_length=50, primary_key=True, verbose_name='文件类别编码')
    file_type_name = models.CharField(max_length=500, verbose_name='文件类别名称')
    file_type_describe = models.CharField(max_length=2000, verbose_name='文件类别描述')
    file_folder_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.file_type_id + ':' + self.file_type_name


class MyFiles(models.Model):
    file_type = models.ForeignKey(to=FileType, on_delete=models.CASCADE,verbose_name='文件类型')
    file_name = models.CharField(max_length=500)
    file_exist_child_folder = models.CharField(max_length=500)


class Author(models.Model):
    name = models.CharField(max_length=50)
    describe = models.CharField(max_length=2000)


class System(models.Model):
    name = models.CharField(max_length=50)
    primary_word = models.CharField(max_length=200)
    describe = models.CharField(max_length=2000)
