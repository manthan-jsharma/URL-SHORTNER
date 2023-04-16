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
    shorturl = "https://url-shortner-backend-production-6c89.up.railway.app/" + shorturl
    return Response({'longurl': longurl, 'shorturl': shorturl})


def redirectUrl(request, shorturl):
    try:
        obj = urlShortener.objects.get(shorturl=shorturl)
    except urlShortener.DoesNotExist:
        obj = None

    if obj is not None:
        return redirect(obj.longurl)
