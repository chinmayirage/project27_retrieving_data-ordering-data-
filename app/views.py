from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length


def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='cricket')
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='cricket')
    QSW=Webpage.objects.exclude(topic_name='cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.order_by('-name')
    QSW=Webpage.objects.filter(topic_name='kabaddi').order_by('-name')
    QSW=Webpage.objects.all().order_by(Length('name'))
    QSW=Webpage.objects.all().order_by(Length('name').desc())

    
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

def display_AccessRecords(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.all().order_by('date')
    d={'AccessRecords':QSA}
    return render(request,'display_AccessRecords.html',d)   