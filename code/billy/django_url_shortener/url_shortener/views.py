from django.shortcuts import render, redirect
import uuid
from .models import OriginalURL
from django.http import HttpResponse

def index(request):
    return render(request, 'url_shortener/index.html')

def add_url(request):
    if request.method == 'POST':
        url_link = request.POST['link']
        url_link_id = str(uuid.uuid4())[:7]
        shortened_link = OriginalURL(link=url_link, link_id = url_link_id)
        shortened_link.save()
        return HttpResponse(url_link_id)

def url_shortener(request, pk):
    url_link = OriginalURL.objects.get(url_link_id = pk)
    return redirect(url_link.link)