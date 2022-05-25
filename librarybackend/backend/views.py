from multiprocessing import context
import re
from urllib import response
from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .forms import UploadForm
from . import models
from .models import Upload

def index(request):
    context = {
        'welcome': 'Backend for the Application!'
    }
    return render(request, 'index.html', context=context)
#POST-/GET-Request--------------------------------------------------------------------
@csrf_exempt  
def upload_image(request):
    context = {} 
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print('Is valid!')
            img = form.cleaned_data.get("img")
            description = form.cleaned_data.get("description")
        
            print(img)

            obj = Upload.objects.create(                
                description = description,
                img = img
            )

            obj.save()
            print('Description: ' , obj.description ,' img_file: ',obj.img)
            return HttpResponse(obj.description)
        else:
            res = form.errors.as_json()
            print(res)
            return HttpResponse(res)    
        
    else: 
        form = UploadForm()
        context['form']= form

    return render(request, 'upload.html', context=context)

@csrf_exempt
def grid(request):
    
    img_object = Upload.objects.all()
    
    files = {
          'img_object': img_object,
        }

    return render(request, 'grid.html', context=files)
#----------------------------------------------------------------------
#Error/Success Routes
@csrf_exempt
def success(request):
    print("Succeed")
    return render(request, 'success.html', {'msg': 'It Worked! 200 :D'})

@csrf_exempt
def error(request):
    print("Error 404")
    return render(request, 'error.html', {'msg': 'Ups, something went wrong! 404 :('})