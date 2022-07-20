from multiprocessing import context
from urllib import response
from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
import base64
from .forms import UploadForm
from . import models
from .models import Upload
from rest_framework import serializers

class File(object):
    def __init__(self,image):
        self.image = image

class FileSerializer(serializers.Serializer):
    image = serializers.ImageField()


@csrf_exempt  
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
        form = UploadForm(request.POST, request.FILES)  #Get Multiple Images and only one Descriptions
        if form.is_valid():
            img = form.cleaned_data.get("img")
            description = form.cleaned_data.get("description")
            obj = Upload.objects.create(                
                description = description,
                img = img
            )
            obj.save()
            return HttpResponse('It Worked!')
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
    img_object = list(Upload.objects.all())
    files = {
        'data'  : [],
        'length': 0,
    }
    files['length'] = len(img_object) #Länge der 

    for x in range(0, len(img_object)):
        img = File(img_object[x].img)
        serialized_img = FileSerializer(img)
        uploads = {}
        #with open(img,"rb") as img_file:
        #    b64_string = base64.b64encode(img_file.read())
        #    print(b64_string)
        uploads['Img'] = serialized_img.data
        uploads['Description'] = img_object[x].description
        files['data'].append(uploads)

    return JsonResponse(files)
#
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