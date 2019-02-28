from django import forms
from .models import FileType, MyFiles
from django.urls import reverse_lazy
from .Helper import handle_uploaded_file


class UploadForm(forms.Form):
    filename = forms.CharField(max_length=100, min_length=2)
    file = forms.FileField()


class FileTypeForm(forms.ModelForm):
    class Meta:
        model = FileType
        fields = '__all__'


class FileForm(forms.ModelForm):
    file = forms.FileField(label='文件')
    success_url = reverse_lazy('files_list')

    class Meta:
        model = MyFiles
        fields = '__all__'
        exclude = ['file_name', 'file_exist_child_folder']

    def save(self, commit=True):
        if self.is_valid():
            print('valid')
            in_memory_uploaded_file = self.files['file']
            print(self.instance.file_type)
            file_type = FileType.objects.get(file_type_id=self.instance.file_type.file_type_id)
            handle_uploaded_file(in_memory_uploaded_file, file_type.file_folder_name)
            self.instance.file_name = in_memory_uploaded_file.name
            self.instance.file_exist_child_folder = file_type.file_folder_name
            self.instance.save()
        else:
            print('unvalid')
        return self.instance
