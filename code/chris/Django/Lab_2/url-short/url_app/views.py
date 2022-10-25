import random
import string
import re
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from.models import CodeStorage

#CRUDL Time

def index(request):
    # url_create = CodeStorage.objects.create(long_url=request.POST['url'])
    #i need to take in long url and save it to database
    return render(request, 'url_app/index.html')

# def url_final(request, pk):
#     all_characters = string.printable
#     short_url = get_object_or_404(CodeStorage, pk=pk)
    
    #i need a way to cut off long url and add with all_characters - regex?
    #i need a way to take in seven random characters and limit to seven
    #i need to join seven random characters 

# def redirect(request):
#     #i need to then redirect User to new site with short url aka url_final
#     return HttpResponse(f"You're at your new site")