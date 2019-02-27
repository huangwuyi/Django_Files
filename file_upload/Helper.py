import os
from django.conf import settings


def handle_uploaded_file(f, folder):
    print(settings.UPLOAD_FILE_ROOT_DICTIONARY)
    father_folder = os.path.join(settings.UPLOAD_FILE_ROOT_DICTIONARY, folder)
    if os.path.exists(father_folder):
        pass
    else:
        os.mkdir(father_folder)
    with open(os.path.join(father_folder, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
