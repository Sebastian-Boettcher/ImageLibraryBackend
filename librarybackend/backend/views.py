from multiprocessing import context
from django.shortcuts import render
from . import models

def index(request):
    
    context = {
        'welcome': 'Backend for the Application!'
    }
    return render(request, 'index.html', context=context)

def upload(request):
    
    if request.method == "POST":
    # Fetching the form data
        fileTitle = request.POST["title"]
        description = request.POST["description"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        image = models.Image(
            title = fileTitle,
            description = description,
            uploadedFile = uploadedFile
        )
        image.save()

    images = models.Image.objects.all()
    context = {
        'title': 'Upload new images!',
        "files": images

    }
    return render(request, 'upload.html', context=context)

def grid(request):
    
    files = models.Image.objects.all()
    #print(all_images[0].title)
    file_size = len(files)
    images = {}

    for i in range(0, files):
        image = {
            'title': files[0].title,
            'description': files[0].description,
            'image_file': files[0].uploadedFile
        }

    return render(request, 'grid.html', context=images)