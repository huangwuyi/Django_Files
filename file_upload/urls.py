from django.urls import path, re_path, include
from .views import upload, index, hello, FileTypeListView, FileTypeCreateView, FileTypeUpdateView, FileTypeDetailView, \
    FileTypeDeleteView, MyFilesListView, MyFilesCreateView, MyFilesUpdateView, MyFilesDetailView, DownLoadFile, \
    MyFilesDeleteView, CanGoHere,MyLogin,MyLogout
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('index/', index, name='index'),
    path('hello/', hello, name='hello'),
    path('filetype/list/', FileTypeListView.as_view(), name='filetype_list'),
    path('filetype/create/', FileTypeCreateView.as_view(), name='filetype_create'),
    path('filetype/update/<str:file_type_id>/', FileTypeUpdateView.as_view(), ),
    path('filetype/detail/<str:file_type_id_kkk>/', FileTypeDetailView.as_view(), ),
    path('filetype/delete/<str:file_type_id_kkk>/', FileTypeDeleteView.as_view(), ),
    path('files/list/', MyFilesListView.as_view(), name='files_list'),
    path('files/create/', MyFilesCreateView.as_view(), name='files_create'),
    path('files/update/<int:id>/', MyFilesUpdateView.as_view(), ),
    path('files/detail/<int:pk>/', MyFilesDetailView.as_view(), ),
    path('files/delete/<int:pk>/', MyFilesDeleteView.as_view(), ),
    path('download/<int:id>/', DownLoadFile, name='download'),

    path('login/', MyLogin.as_view(), name='self-login'),
    path('logout/', MyLogout.as_view(), name='self-logout'),
    path('cangohere/', CanGoHere.as_view(), name='cangohere'),
]
