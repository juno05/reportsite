from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.notification, name='notification'),
    path('report/app', views.report_app, name='report_app'),
    path('report/matrix', views.report_matrix, name='report_app'),
    path('report/applicationlog', views.report_application_log, name='report_applicationlog'),
    path('report/networklog', views.report_network_log, name='report_networklog'),
    path('report/incident', views.incident_report, name='incident_report'),
    path('login',  views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    #path('changepassword', auth_views.password_change, name='change_password'),
    path('changepassword', views.change_password, name='change_password'),
]
