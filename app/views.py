from django.shortcuts import render, redirect
from django.contrib import messages
from app.auth import authentication, predict, valid, review_prediction,predict_final_feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .form import feedback_form, profile_form
from app.models import *
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse("This is Home page")    
    return render(request, "index.html")

def log_in(request):
    student = feedback.objects.all()
    if request.method == "POST":
        # return HttpResponse("This is Home page")  
        username = request.POST['username']
        password = request.POST['password']

        for std in student:
            if std.username == username :
                messages.error(request, "Your Feedback is already Recorded!!!")
                return redirect("log_in")
        else:
            user = authenticate(username = username, password = password)

            if user is not None:
                if str(user) == "admin@gmail.com":
                    login(request, user)
                    print(user)
                    messages.success(request, "Log In Successful...!")
                    return HttpResponseRedirect("all_report")
                else:
                    login(request, user)
                    messages.success(request, "Log In Successful...!")
                    return HttpResponseRedirect("dashboard")
            else:
                messages.error(request, "Invalid User...!")
                return redirect("log_in")
    return render(request, "log_in.html")

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def log_out(request):
    logout(request)
    messages.success(request, "Log out Successfuly...!")
    return redirect("/")

def register(request):
    context={
        'form' : profile_form()
    }
    try:
        student = profile_data.objects.all()
        if request.method == "POST":
            form = profile_form(request.POST, request.FILES)
            if form.is_valid():
                fname = form.cleaned_data['fname']
                lname = form.cleaned_data['lname']
                username = form.cleaned_data['username']
                designation = form.cleaned_data['designation']
                password = form.cleaned_data['password']
                password1 = form.cleaned_data['password1']
                email_check = valid(fname, lname, username, designation)
                if email_check:
                    verify = authentication(fname, lname, password, password1)
                    if verify == "success":
                        user = User.objects.create_user(username, password, password1)          #create_user
                        profile = profile_data(user = user, designation = designation)
                        user.first_name = fname
                        user.last_name = lname
                        user.save()
                        profile.save()
                        messages.success(request, "Your Account has been Created.")
                        return redirect("/")
                        
                    else:
                        messages.error(request, verify)
                        return redirect("register")
                        # return HttpResponse("This is Home page")
                else:
                    messages.error(request, "Details are Not Match with Database")
                    return redirect("register")
            else:
                messages.error(request, "Invalid Form")
                return redirect("register")
    except:
        messages.error(request, "Account is already present into the system")
        return redirect("register")
    return render(request, "register.html",context)

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def dashboard(request):
    student = profile_data.objects.all()
    data = profile_data.objects.get(user = request.user)
    context = {
        'fname': request.user.first_name,
        'lname' : request.user.last_name,
        'form' :feedback_form(),
        'designation' : data.designation,
    }
    if request.method == "POST":
        form = feedback_form(request.POST, request.FILES)
        if form.is_valid():
            q1 = form.cleaned_data['q1']
            q2 = form.cleaned_data['q2']
            q3 = form.cleaned_data['q3']
            q4 = form.cleaned_data['q4']
            q5 = form.cleaned_data['q5']
            q6 = form.cleaned_data['q6']
            q7 = form.cleaned_data['q7']
            q8 = form.cleaned_data['q8']
            q9 = form.cleaned_data['q9']
            q10 = form.cleaned_data['q10']
            q11 = form.cleaned_data['q11']
            q12 = form.cleaned_data['q12']
            q13 = form.cleaned_data['q13']
            q14 = form.cleaned_data['q14']
            q15 = form.cleaned_data['q15']
            feed = form.cleaned_data['feedback']
            name = request.user.first_name + " " + request.user.last_name
            
            feedback_pred, feedback_count = review_prediction(feed)
            pred  = predict(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15)
            final_pred = predict_final_feedback(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,feedback_count)

            username = request.user
            happiness_index = feedback(username= username, name =name, designation = data.designation, q1 = q1,q2 = q2,q3 = q3,q4 = q4,q5 = q5,q6 = q6,q7 = q6,q8 = q8,q9 = q9,q10 = q10,q11 = q11,q12= q12,q13 = q13,q14 = q14,q15 = q15, qus_pred = pred, feedback = feed, feedback_pred = feedback_pred, happiness_index = final_pred)
            happiness_index.date = datetime.today()
            happiness_index.save()
            messages.info(request, final_pred)
            return redirect('report')

        else:
            messages.error(request, "Invalid Form")
            return redirect("dashboard")
    return render(request, "dashboard.html",context)

@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def report(request):
    student = feedback.objects.last()
    context = {
        'fname': request.user.first_name,
        'lname' : request.user.last_name,
        'student' : student
    }
    return render(request, "report.html", context)


@login_required(login_url="log_in")
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def all_report(request):
    student = feedback.objects.all()
    happy = 0
    modarate_happy = 0
    not_happy = 0
    total = 0 
    for std in student:
        if std.happiness_index == "Happy":
            happy += 1
        elif std.happiness_index == "Moderate Happy":
            modarate_happy += 1
        else:
            not_happy += 1
        total+=1
    happy_percent = (happy/total)* 100
    modarate_happy_percent = (modarate_happy/total)* 100
    not_happy_percent = (not_happy/total)* 100
    context = {
        'fname': request.user.first_name, 
        'student' : student,
        'happy_percent' : float("{:.2f}".format(happy_percent)),
        'modarate_happy_percent' : float("{:.2f}".format(modarate_happy_percent)),
        'not_happy_percent' : float("{:.2f}".format(not_happy_percent))
    }
    
    return render(request, "all_report.html", context)