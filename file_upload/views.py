from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django import views
from .forms import UploadForm, FileForm
from django.http import HttpResponse, FileResponse
from .models import MyFiles, FileType
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
import os
from django.conf import settings


# Create your views here.
def upload(request):
    if request.method == 'POST':
        uploadform = UploadForm(request.POST, request.FILES)
        if uploadform.is_valid():
            print(True)
            print(request.POST)
            print(request.FILES['file'])
            handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
            return redirect(to='hello')
        else:
            print(False)
    else:
        uploadform = UploadForm()
    # uploadform = UploadForm
    return render(request, template_name='upload.html', context={'form': uploadform, })


def handle_uploaded_file(f, name):
    with open('E:/上传文件夹/' + name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index(request):
    return render(request, template_name='index.html')


def hello(request):
    http_response = HttpResponse('hello!')
    return http_response


class FileTypeListView(views.generic.ListView):
    model = FileType
    template_name = 'filetype/listview.html'
    context_object_name = 'filetypes'


class FileTypeCreateView(views.generic.CreateView):
    model = FileType
    fields = '__all__'
    context_object_name = 'filetype'
    template_name = 'filetype/createview.html'
    success_url = reverse_lazy('filetype_list')


class FileTypeUpdateView(views.generic.UpdateView):
    model = FileType
    fields = '__all__'
    # context_object_name = 'filetype'
    template_name = 'filetype/updateview.html'
    success_url = reverse_lazy('filetype_list')
    slug_field = 'file_type_id'
    slug_url_kwarg = 'file_type_id'

    # def get_object(self, queryset=None):
    #     print(self.kwargs)
    #     print(self.kwargs.get('file_type_id'))
    #     return FileType.objects.filter(file_type_id= self.kwargs.get('file_type_id')).first()


class FileTypeDetailView(DetailView):
    model = FileType
    template_name = 'filetype/detailview.html'
    field = '__all__'
    context_object_name = 'form'
    slug_field = 'file_type_id'
    # 用于表明主键是哪一列
    slug_url_kwarg = 'file_type_id_kkk'
    # 用于表明主键在url中的名称

    # def get_object(self, queryset=None):
    #     print(self.kwargs)
    #     print(self.kwargs.get('file_type_id'))
    #     return FileType.objects.filter(file_type_id= self.kwargs.get('file_type_id')).first()


class FileTypeDeleteView(DeleteView):
    model = FileType
    template_name = 'filetype/deleteview.html'
    success_url = reverse_lazy('filetype_list')
    slug_field = 'file_type_id'
    # 用于表明主键是哪一列
    slug_url_kwarg = 'file_type_id_kkk'
    # 用于表明主键在url中的名称
    context_object_name = 'form'


class MyFilesListView(ListView):
    model = MyFiles
    template_name = 'myfiles/listview.html'
    context_object_name = 'MyFileses'


class MyFilesCreateView(CreateView):
    model = MyFiles
    # fields = '__all__'
    success_url = reverse_lazy('files_list')
    template_name = 'myfiles/createview.html'
    form_class = FileForm


class MyFilesUpdateView(UpdateView):
    model = MyFiles
    form_class = FileForm
    success_url = reverse_lazy('files_list')
    template_name = 'myfiles/updateview.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'


class MyFilesDetailView(DetailView):
    model = MyFiles
    template_name = 'myfiles/detailview.html'
    context_object_name = 'model'


def DownLoadFile(request, id):
    file = MyFiles.objects.get(id=id)
    filepath = os.path.join(settings.UPLOAD_FILE_ROOT_DICTIONARY, file.file_exist_child_folder, file.file_name)
    response = FileResponse(open(filepath, 'rb+'), as_attachment=True, filename=file.file_name)
    return response
