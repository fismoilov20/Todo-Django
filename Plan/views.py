from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def students(request):
    data = {
        'students': Student.objects.all,
    }
    return render(request, 'students.html', data)

def student_edit(request, num):
    if request.method == 'POST':
        Student.objects.filter(id=num).update(
            name = request.POST.get('name'),
            age=request.POST.get('age'),
            course=request.POST.get('course'),
            std_id=request.POST.get('std_id'),
        )
        return redirect('/students/')
    data = {
        'student': Student.objects.get(id=num)  
    }
    return render(request, 'student_edit.html', data)

def plans(request):
    if request.method == 'POST':
        if request.POST.get('done') is None:
            result = False
        else:
            result = True
        Plan.objects.create(
            heading=request.POST.get('heading'),
            date = request.POST.get('date'),
            details = request.POST.get('details'),
            done = result,
            student = Student.objects.get(id=request.POST.get('student'))
        )
    data = {
        'plans': Plan.objects.all,
        'students': Student.objects.all,
    }
    return render(request, 'plans.html', data)

def plan_edit(request, num):
    if request.method == 'POST':
        if request.POST.get('done') is None:
            result = False
        else:
            result = True
        Plan.objects.filter(id=num).update(
            heading = request.POST.get('heading'),
            date=request.POST.get('date'),
            details=request.POST.get('details'),
            done=result,
            student = Student.objects.get(id=request.POST.get('student'))
        )
        return redirect('/plans/')
    data = {
        'plan': Plan.objects.get(id=num),
        'students': Student.objects.all,  
    }
    return render(request, 'plan_edit.html', data)

def donefalse(request):
    data = {
        'plans': Plan.objects.filter(done=False),
    }
    return render(request, 'donefalse.html', data)

def seniors(request):
    data = {
        'students': Student.objects.filter(course__gt=2),
    }
    return render(request, 'seniors.html', data)

def plans_delete(request, num):
    Plan.objects.get(id=num).delete()
    return redirect('/plans/')

def todo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('done') == 'on':
                s=True
            else:
                s=False
            Todo.objects.create(
                heading=request.POST.get('heading'),
                details=request.POST.get('details'),
                date=request.POST.get('date'),
                done=s,
                student=Account.objects.get(user=request.user),
            )
        data = {
            'todos': Todo.objects.filter(student__user=request.user),
        }
        return render(request, 'todo.html', data)
    else:
        return redirect('/')

def loginView(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'),)

        if user is None:
            return redirect('/')

        login(request, user)

        return redirect('/todo/')

    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def todo_delete(req, num):                  ## request is NEEDED
    if req.user.is_authenticated:
        td = Todo.objects.get(id=num)
        if req.user == td.student.user:
            td.delete()
        return redirect('/todo/')

def signup(request):
    if request.method == 'POST':
        u = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        Account.objects.create(
            fullname=request.POST.get('fullname'),
            tel=request.POST.get('tel'),
            student_id=request.POST.get('student_id'),
            user=u,
        )
        return redirect('/todo/')
    return render(request, 'signup.html')