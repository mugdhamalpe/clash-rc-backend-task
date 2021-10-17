# from core.task3.users.models import student
from django.contrib.auth.models import User
from django.contrib.messages.api import info
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import re


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username} :) You can now login with your credentials!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    return render(request, 'users/profile.html')

def textchecker(request):
    if request.method=="POST":

        inputstring = str(request.POST.get('name'))
        performfunc = str(request.POST.get('function'))
        context=dict()
        extracted=[]

        if not inputstring:
            messages.error(request, f'Enter valid input string')

        else:
            if performfunc=="numfromstr":
                regex_pattern = re.compile(r'[1-9][0-9][0-9]+')
                findmatch = regex_pattern.finditer(inputstring)
                for match in findmatch:
                    extracted.append(match.group(0))
                return render(request, 'users/textformat.html', {'numbers': extracted})

            if performfunc=="extractdate":
                regex_pattern = re.compile(r'([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])')
                findmatch = regex_pattern.finditer(inputstring)
                for match in findmatch:
                    extracted.append(match.group(0))
                return render(request, 'users/textformat.html', {'numbers': extracted})

            if performfunc=="extractstr":
                regex_pattern = re.compile(r".*'([^']*)'.*")
                findmatch = regex_pattern.finditer(inputstring)
                for match in findmatch:
                    extracted.append(match.group(1))
                return render(request, 'users/textformat.html', {'numbers': extracted})

            if performfunc=="emailvalidate":
                regex_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

                if(re.fullmatch(regex_pattern, inputstring)):
                    extracted = "Valid Email"
                    #print(extracted)

                else:
                    extracted = "Invalid Email"
                    #print(extracted)
                return render(request, 'users/textformat.html', {'numbers': extracted})

            if performfunc=="ipaddress":
                regex_pattern1 = re.compile(r"(([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])\\.){3}"\
            "([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])")
                regex_pattern2 = "((([0-9a-fA-F]){1,4})\\:){7}([0-9a-fA-F]){1,4}"

                if(re.search(regex_pattern1, inputstring)):
                    extracted = "Valid IPv4"
                    #print(extracted)

                elif(re.search(regex_pattern2, inputstring)):
                    extracted = "Valid IPv6"
                    #print(extracted)

                else:
                    extracted = "Invalid IP address"
                    #print(extracted)
                return render(request, 'users/textformat.html', {'numbers': extracted})


            if performfunc=="macaddress":
                regex_pattern = ("^([0-9A-Fa-f]{2}[:-])" + "{5}([0-9A-Fa-f]{2})|" + "([0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4}\\." + "[0-9a-fA-F]{4})$")

                if(re.fullmatch(regex_pattern, inputstring)):
                    extracted = "Valid MAC address"
                    #print(extracted)

                else:
                    extracted = "Invalid MAC address"
                    #print(extracted)
                return render(request, 'users/textformat.html', {'numbers': extracted})


            if performfunc=="cameltosnake":
                regex_pattern = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', inputstring)
                extracted = re.sub('([a-z0-9])([A-Z])', r'\1_\2', regex_pattern).lower()
                return render(request, 'users/textformat.html', {'numbers': extracted})
    return render(request, 'users/textformat.html')


def search(request):
    if request.method=="POST":
        srch = request.POST['srh']

        if srch:
            match = User.objects.filter(Q(username__icontains=srch))

            if match:
                return render(request, 'users/searchuser.html', {'sr':match})
            else:
                messages.error(request, 'no result found')

        else:
            return HttpResponseRedirect('/search/')

    return render(request, 'users/searchuser.html')

