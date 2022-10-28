from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


def index(request):
    return HttpResponse('OK')
# def grocery_list(request):
#     grocery_items = get_object_or_404()
# Create your views here.
