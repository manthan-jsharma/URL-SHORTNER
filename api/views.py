from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import urlShortener
from .serializers import urlShortenerSerializer

import random


@api_view(['POST'])
def makeshorturl(request):
    data = request.data
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$-_"
    shorturl = ("".join(random.sample(s, 6)))
    urlShortener.objects.create(
        longurl=data['longurl'],
        shorturl=shorturl
    )
    longurl = data['longurl']
    shorturl = "http://127.0.0.1:8000/" + shorturl
    return Response({'longurl': longurl, 'shorturl': shorturl})


def redirectUrl(request, shorturl):
    try:
        obj = urlShortener.objects.get(shorturl=shorturl)
    except urlShortener.DoesNotExist:
        obj = None

    if obj is not None:
        return redirect(obj.longurl)

@api_view(['POST'])
def fetchallurl(request):
    allUrls = urlShortener.objects.all().values() 
    return Response(allUrls)
