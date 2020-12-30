from django.shortcuts import render
from django.http import HttpResponse
from . import util
from django import forms
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
import io
# Create your views here.

def index(request):
    return render(request, 'app1/index.html', {
        "content": FileInputForm()
    })

def result(request):
    msg = "Upload Error"
    if request.method == 'POST':
        upload_file = request.FILES['file']
        choice = request.POST['choice']
        key = request.POST['key']
        with default_storage.open('tmp/'+upload_file.name, 'wb+') as destination:
            for chunk in upload_file.chunks():
                destination.write(chunk)
        f = FileSystemStorage()
        name = 0
        if choice == 'encrypt':
            done_file = util.Encrypt(key, f'media/tmp/{upload_file.name}')
            dfile = io.BytesIO(done_file)
            name = f.save("encrypted_file.enc", dfile)
        elif choice == 'decrypt':
            done_file = util.Decrypt(key, f'media/tmp/{upload_file.name}')
            dfile = io.BytesIO(done_file)
            name = f.save("output.jpg", dfile)
        # name = f.save(upload_file.name, upload_file)
        url = f.url(name)

        print("Uploaded")
        msg = "Upload Success"
    return render(request, 'app1/result.html', {
        "msg": msg,
        "url": url
    })
