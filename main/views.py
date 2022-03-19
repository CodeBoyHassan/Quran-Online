from this import d
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'index.html')


def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    else:
        name = request.POST['full-name']
        email = request.POST['email']
        phone = request.POST['phone']
        nationality = request.POST['nationality']
        message  = request.POST['message']
        

        try:
            send_mail("Trial Application", "Name: " + name + "\nEmail: " + email + "\nPhone Number: " + phone + "\nNationality: " + nationality + "\n \n Additional Message" + message, 'hasrayrah970@gmail.com', ['ih3352804680@gmail.com', 'hasrayrah970@gmail.com'])

        except BadHeaderError:
            return HttpResponse('Something Went Wrong')
        
        return redirect('success')
    return render(request, 'register.html')


def faq(request):
    return render(request, 'faq.html')


def success(request):
    return render(request, 'success.html')