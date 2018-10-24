from django.shortcuts import render, redirect
from .models import Report, Code, App, ApplicationLog, NetworkLog, EscalationMatrix, Incident
from django.utils import timezone
import logging.handlers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic.edit import CreateView
from .forms import AppForm, ApplicationLogForm, NetworkLogForm, IncidentForm
from datetime import datetime, timedelta
from django.db.models import Avg, Count, Sum
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

import json
import requests


logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


# Create your views here.
def notification(request):

    target_start = (timezone.now() - timedelta(days=1))
    target_end = timezone.now()

    incident_count = Incident.objects.filter(created_date__range=[target_start, target_end]).count()
    app_count = App.objects.filter(created_date__range=[target_start, target_end]).count()
    application_count = ApplicationLog.objects.filter(created_date__range=[target_start, target_end]).count()
    network_count = NetworkLog.objects.filter(created_date__range=[target_start, target_end]).count()

    incident_categroy = Incident.objects.filter(created_date__range=[target_start, target_end]).values('category__name').annotate(Count('category'))

    latest_app = App.objects.all().order_by('-id')[:1]
    latest_appl = ApplicationLog.objects.all().order_by('-id')[:1]
    latest_network = NetworkLog.objects.all().order_by('-id')[:1]

    return render(request, 'dashboard/notification.html',
                  {'incident_count':incident_count,
                   'application_count':application_count,
                   'network_count':network_count,
                   'app_count':app_count,
                   'latest_app':latest_app,
                   'latest_appl':latest_appl,
                   'latest_network':latest_network,
                   'incident_categroy':incident_categroy})


def report_app(request):
    logger.debug('===============  report_app ====================')
    default_form = AppForm()

    if request.method == 'POST':
        # save
        logger.debug(request.META)
        form = AppForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.author = request.user
            app.created_date = timezone.now()
            app.save()
    target_start  = (timezone.now() - timedelta(days=1))
    target_end = timezone.now()
    recent = App.objects.filter(created_date__range=[target_start, target_end]).order_by('-created_date')


    return render(request, 'dashboard/report_app.html', {'form':default_form, 'recent':recent})

def report_application_log(request):
    logger.debug('===============  report_application log ====================')
    default_form = ApplicationLogForm()
    logger.debug(default_form)

    if request.method == 'POST':
        # save
        logger.debug(request.META)
        input_form = ApplicationLogForm(request.POST)
        if input_form.is_valid():
            report = input_form.save(commit=False)
            report.author = request.user
            report.created_date = timezone.now()
            report.save()
    target_start = (timezone.now() - timedelta(days=1))
    target_end = timezone.now()
    recent = ApplicationLog.objects.filter(created_date__range=[target_start, target_end]).order_by('-created_date')
    chart_data = make_chart_data()


    return render(request, 'dashboard/report_application_log.html', {'form':default_form, 'recent':recent, 'chart_data':chart_data})

def report_network_log(request):
    logger.debug('===============  report_network_log log ====================')
    default_form = NetworkLogForm()
    logger.debug(default_form)

    if request.method == 'POST':
        # save
        logger.debug(request.META)
        input_form = NetworkLogForm(request.POST)
        if input_form.is_valid():
            report = input_form.save(commit=False)
            report.author = request.user
            report.created_date = timezone.now()
            report.save()
    target_start = (timezone.now() - timedelta(days=1))
    target_end = timezone.now()
    recent = NetworkLog.objects.filter(created_date__range=[target_start, target_end]).order_by('-created_date')

    target_start = target_start - timedelta(days=1)
    target_end = target_end - timedelta(days=1)
    yesterday = NetworkLog.objects.filter(created_date__range=[target_start, target_end]).order_by('-created_date')
    #chart_data = make_chart_data()

    return render(request, 'dashboard/report_network_log.html', {'form':default_form, 'recent':recent, 'yesterday':yesterday})

def incident_report(request):
    logger.debug('===============  incident_report ====================')
    default_form = IncidentForm()
    logger.debug(default_form)

    if request.method == 'POST':
        # save
        logger.debug(request.META)
        input_form = IncidentForm(request.POST,request.FILES)
        logger.debug(input_form)
        if input_form.is_valid():
            incidents = input_form.save(commit=False)
            incidents.author = request.user
            incidents.created_date = timezone.now()
            incidents.save()
            send_msg_slack("From:"+ request.user.username +"\n" + request.POST["description"])
    target_start = (timezone.now() - timedelta(days=3))
    target_end = timezone.now()
    recent = Incident.objects.filter(created_date__range=[target_start, target_end]).order_by('-created_date')

    return render(request, 'dashboard/incident_report.html', {'form':default_form, 'recent':recent})


def report_matrix(request):
    logger.debug('===============  report_matrix  ====================')

    first = EscalationMatrix.objects.filter(level=0).order_by('responsibility')
    second = EscalationMatrix.objects.filter(level=1).order_by('responsibility')
    final = EscalationMatrix.objects.filter(level__gt=1).order_by('responsibility')

    return render(request, 'dashboard/report_matrix.html', {'first':first, 'second':second, 'final':final})

def make_chart_data():
    logger.debug('++++++++++++++++  make_chart_data+++++++++++++++++++++++++++++++')
    logger.debug('++++++++++++++++  make_chart_data+++++++++++++++++++++++++++++++')

    rtn =[]
    info_set =[]
    warn_set =[]
    error_set =[]
    cs_set =[]
    time_set =[]

    target_start = (timezone.now() - timedelta(days=1))

    for row in range(0,25):
        target_end = target_start + timedelta(hours=1)
        time_set.append(target_end.strftime('%H'))

        info = ApplicationLog.objects.filter(created_date__range=[target_start, target_end])

        if info:
            for i in info:
                logger.debug('++++++++++++++++++++++ [%d][%d][%d][%d] ', i.info,i.warn,i.error,i.cs)
                info_set.append(i.info)
                warn_set.append(i.warn)
                error_set.append(i.error)
                cs_set.append(i.cs)
        else :
            info_set.append(0)
            warn_set.append(0)
            error_set.append(0)
            cs_set.append(0)

        target_start = target_end

    logger.debug(info_set)
    logger.debug('++++++++++++++++  make_chart_data+++++++++++++++++++++++++++++++')
    logger.debug('++++++++++++++++  make_chart_data+++++++++++++++++++++++++++++++')
    rtn.append(time_set)
    rtn.append(info_set)
    rtn.append(error_set)

    return rtn


def login_view(request):
    logger.debug(request.method)
    if request.method == 'GET':
        return render(request, 'dashboard/login.html', {})
    else :
        username = request.POST['username']
        password = request.POST['password']
        logger.debug(username+':'+password)
        user = authenticate(request, username=username, password=password)
        logger.debug(user)
        if user is not None:
            login(request, user)
            return redirect('/')
            #return render(request, 'dashboard/notification.html', {})
        else:
            return render(request, 'dashboard/login.html', {})

def logout_view(request):
    logout(request)
    return redirect('/login')

def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/setting.html', {
        'form': form
    })

def send_msg_slack(msg):

    url = "https://hooks.slack.com/services/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"
    slack_message = {
        'username': 'Monitor alert',
        # 'icon_emoji': ':monkey_face:',
        'channel': '#monitor_alert',
        'text':  msg
    }
    query = json.dumps(slack_message)
    headers = {'content-type': 'application/json'}
    logger.debug("request url is %s", url)
    logger.debug("request url is %s", query)

    try:
        # remove in prodution
        logger.debug("request open start")
        response = requests.post(url, data=query, headers=headers)
        # remove in prodution
        logger.debug("response is %s ", response)
        # remove in prodution
        logger.debug("Message post result [%s]", response.text)
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)