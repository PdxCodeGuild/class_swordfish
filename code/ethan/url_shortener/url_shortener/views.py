from django.shortcuts import render
from django.http import HttpResponse
from .models import Shortener
from .forms import ShortenerForm

def index(request):
    urls = Shortener.objects.all()
    form = ShortenerForm()
    if request.method == 'POST':
        form = ShortenerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"urls": urls, 'form': form}
    return render(request, 'index.html', context)
