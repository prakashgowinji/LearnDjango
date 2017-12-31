from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessRecord, WebPage
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    mydict = {'insert_content': "Hello, I am from first App"}
    return render(request, 'first_app/index.html', context=date_dict)
