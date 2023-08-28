from django.shortcuts import render, redirect
from .forms import PictureForm
from .models import Picture
from django.conf import settings
import os
# Create your views here.

def main(request):
    return render(request, "app_hm10/index.html", context={"title": "Homework 10"})


def upload(request):
    form = PictureForm(instance=Picture())
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            form.save()
            return redirect(to="app_hm10:main")
    return render(request, "app_hm10/upload.html", context={"title": "Homework 10", "form": form})

def pictures(request):
    pictures = Picture.objects.all()
    return render(request, "app_hm10/pictures.html", context={"title": "Homework 10", "pictures": pictures})


def remove_picture(request, pic_id):
    try:
        picture = Picture.objects.get(pk=pic_id)
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(picture.path)))
        picture.delete()
    except Picture.DoesNotExist:
        print("Picture does not exist")
    except OSError as e:
        print(e)
    return redirect(to="app_hm10:pictures")


def edit_picture(request, pic_id):
    picture = Picture.objects.get(pk=pic_id)

    if request.method == "POST":
        description = request.POST["description"]
        picture.description=description
        picture.save()
        return redirect(to="app_hm10:pictures")
    
    context = {"title": "Homework 10", "picture": picture}
    return render(request, "app_hm10/edit.html", context=context)