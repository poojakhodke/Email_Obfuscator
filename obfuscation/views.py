from django.http import request , HttpResponse 
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import mailId
from .forms import EmailForm
import re

def save(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            form.save()
            print(form)
            return redirect('obfuscate', email=form.cleaned_data['email'])
       
    else:
        form = EmailForm()
    return render(request, "home.html", {"form": form})

def obfuscate(request, email, r='*', s=3, e=0):
    if '@' in email:
        a = email.split('@')
        if e == 0:
            e = len(email)
        return render(request, 'obfuscate.html', { 'email':email.replace(a[0][s:e], r * (len(a[0][s:e])))})
    if e == 0:
        e = len(email)
    return render(request, 'obfuscate.html',{'email': email.replace(email[s:e], r * len(email[s:e]))})
    
    

if __name__ == "__main__":
    email = input()

    obfuscate(email)
