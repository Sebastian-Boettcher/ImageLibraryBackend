from multiprocessing import context
from urllib import response
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


@csrf_exempt  
def upload_image(request):
    context = {} 
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print('Is valid!')
            description = form.cleaned_data.get("description")
            img = form.cleaned_data.get("img")

            obj = Upload.objects.create(                
                descript = description,
                uploadedFile = img
            )
            obj.save()
            print(obj)
            return HttpResponse('Form is valid and it worked!')
        else:
            res = 'The form is not Valid!'
            return HttpResponse(res)    
        
    else: 
        form = UploadForm()
        context['form']= form

    #return HttpResponse('Ended')    
    return render(request, 'upload.html', context=context)


@csrf_exempt
def grid(request):
    
    files = Upload.objects.all()
    #print(all_images[0].title)
    file_size = len(files)
    images = {}

    for i in range(0, file_size):
        image = {
            'description': files[i].description,
            #'image_file': files[i].uploadedFile
        }
        images[i] = image
    print("Send!")

    return JsonResponse(images, safe=False)

@csrf_exempt
def success(request):
    print("Succeed")
    return render(request, 'success.html', {'msg': 'It Worked! 200 :D'})

@csrf_exempt
def error(request):
    print("Error 404")
    return render(request, 'error.html', {'msg': 'Ups, something went wrong! 404 :('})