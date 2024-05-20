from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Permission
from .models import *
from datetime import datetime

@csrf_exempt
def login_user(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None  :
            login(request, user)
            send_data = {'status':1, 'msg':'Login Successfully...'}
        else:
            send_data = {'status':0, 'msg':'Invalid Credentials'}
        return JsonResponse(send_data)
    

@csrf_exempt
@permission_required('accounts.can_add_users')
def add_user(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    role = request.POST.get('role')

    can_manage_users = request.POST.get('can_manage_users') == 'True'
    can_schedule_interview = request.POST.get('can_schedule_interview') == 'True'

    permission_names = []
    if can_manage_users:
        permission_names.append('can_add_users')
    if can_schedule_interview:
        permission_names.append('can_schedule_interview')

    user = MyUser.objects.create_user(username=username, password=password, role = role)
    for codename in permission_names:
        try:
            permission = Permission.objects.filter(codename=codename, content_type__app_label='assessment_app').last()
            user.user_permissions.add(permission)
        except Permission.DoesNotExist:
            pass
        except Permission.MultipleObjectsReturned:
            pass

    user.save()
    msg = f'User added as a {role}'
    return JsonResponse({'status':1, 'msg':msg})



@csrf_exempt
@permission_required('accounts.can_schedule_interview')
def schedule_interview(request):
    title = request.POST.get('title')
    candidate_name = request.POST.get('candidate_name')
    interview_dt = request.POST.get('interview_dt')
    interviewer = request.POST.get('interviewer')
    notes = request.POST.get('notes')
    InterviewMaster.objects.create(title = title, candidate_name = candidate_name, interview_date = interview_dt , interviewer_id = interviewer, notes = notes , created_dt = datetime.now())
    return JsonResponse({'status':1, 'msg': 'Interview scheduled successfully.'} )


def logout_user(request):
    logout(request)
    return redirect('/')

