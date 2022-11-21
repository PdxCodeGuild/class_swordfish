from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Shortener
import string, random
from django.urls import reverse

def index(request):
    urls = Shortener.objects.all()
    context = {'urls': urls}
    return render(request, 'index.html', context)

def addurl(request):
    long_url = request.POST.get('url', False)
    code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    new_url = Shortener(url = long_url, code = code)
    new_url.save()
    return HttpResponseRedirect(reverse('url_shortener:index'))

def redirect(request, url_code):
    print(url_code)
    object = get_object_or_404(Shortener, code = url_code)
    return HttpResponseRedirect(object.url)


