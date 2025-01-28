from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.

def base(requests):
    if requests.method == "POST":
        form = ImageForm(requests.POST, requests.FILES)
        if form.is_valid():
            form.save() 
    form = ImageForm()
    imgs = Image.objects.all()
    return render(requests, "base.html", {"imgs": imgs,'form': form})