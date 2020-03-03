from django.shortcuts import render
from .models import Fort
from django.conf import settings
# Create your views here.
def index(request):
    forts = Fort.objects.all().order_by("-date_filled")
    # print(forts.count())o
    params = {
        'forts':forts,
        'media_url':settings.MEDIA_URL,
        'range':range(1,len(forts)+1),
    }
    return render(request,'app/index.html',params)