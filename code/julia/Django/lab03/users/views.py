from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic






class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/index.html'
    # return render(requests,'users/index.html', {'form': form})

def login(request):
    return HttpResponse('Hello')




# def loginPage(request):
#     user = User.objects.create_user('jane', 'jane@gmail.com', 'janespassword')




# def createUser(requests):
#     form = UserCreationForm()
    


#     return render(requests, 'users/index.html', {'form': form})


