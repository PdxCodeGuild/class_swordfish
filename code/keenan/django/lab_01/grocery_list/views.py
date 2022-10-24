from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse('INDEX')
    return render(request, 'grocery_list/list.html')


# this needs to be updated.. Context can be added later.
# def list(request):
# #     context = {<something like completed and incompleted>}, will replace 
#     return render(request, 'grocery_list/list.html', {context})

    