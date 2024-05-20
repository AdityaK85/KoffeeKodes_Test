from django.urls import path
from .views import *
from .views_aj import *
from django.conf import settings
from django.conf.urls.static import static


nr_url = [

    path('', login_page),
    path('home/', interviewers),
    path('interview/', interview),

] 

ajax_url = [

    path('login_handler/', login_user),
    path('add_user/', add_user),
    path('schedule_interview/', schedule_interview),
    path('logout_user/', logout_user),

] 


urlpatterns = [ *nr_url, *ajax_url ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)