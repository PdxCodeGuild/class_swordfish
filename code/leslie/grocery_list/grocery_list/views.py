#where we create the functions that will run when user visits url

from django.http import HttpResponse

def my_list(request):
    return HttpResponse('This is my list!')