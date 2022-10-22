from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('ok')

# this needs to be updated..
def list(request):
    # context = {<name-value pairs>}
    return render(request, 'grocery_list/list.html', context)

    