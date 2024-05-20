from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):
    return render(request, 'login.html')



@login_required(login_url='/')
def interviewers(request):
    user_obj = MyUser.objects.all().order_by('-id').exclude(username = 'admin')
    for i in user_obj:
        i.permissions =  i.get_all_permissions()
        
    add_user_access = False
    permissions = request.user.get_all_permissions()
    if 'assessment_app.can_add_users' in permissions:
        add_user_access = True
    return render(request, 'interviewers.html', {'user_obj': user_obj , 'user': request.user , 'add_user_access': add_user_access })



@login_required(login_url='/')
def interview(request):
    interview_access = False
    user_interview = MyUser.objects.filter(groups__name = 'interviewer').order_by('-id')
    interview_obj = InterviewMaster.objects.all().order_by('-id')
    permissions = request.user.get_all_permissions()
    if 'assessment_app.can_schedule_interview' in permissions:
        interview_access = True
    return render(request, 'interview.html', {'interview_obj': interview_obj , 'user': request.user , 'interview_access': interview_access})



@login_required(login_url='/')
def index(request):
    return render(request, 'index.html')