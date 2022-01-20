from django.shortcuts import render,redirect
from .forms import InfoForm
from .models import info
from django.contrib import messages


def home(request):
    form = InfoForm()

    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your messages are dilevered to Nazrul Huda Shanto')
            return redirect('home')
        else:
            messages.error(request, 'Sorry, We could not deliver the message. Please try again')
        
    context = {'form':form}
           
    return render(request,'base/index.html',context)

# Create your views here.
