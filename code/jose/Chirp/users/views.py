from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.contrib.auth.models import User
# Create your views here.
class SignUpView(CreateView):
    form_class =UserCreationForm
    template_name: 'signup.html'
    success_url: reverse_lazy('login')

def chirperprofile(request, chirper):
    chirperprofile = get_object_or_404(User, chirpername = chirpername)
    context ={'chirperprofile': chirperprofile}
    return render(request, 'chirperprofile.html', context)