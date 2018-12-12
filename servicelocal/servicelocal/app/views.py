"""
Definition of views.
"""
from app import models
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

class LoadLogsAPIView(APIView):

#    permission_classes = (APIKeyPermission,)

    def get(self, request):
        try:
            import socket, requests, urllib, re, uuid, json
            hostname = socket.gethostname()    
            IPAddr = socket.gethostbyname(hostname)  
            publicip = request.META.get("HTTP_X_FORWARDED_FOR", "")
            url = "https://api.hackertarget.com/geoip/?q="+publicip
            connect_timeout, read_timeout = 5.0, 30.0
            response = requests.get(url, timeout=(connect_timeout, read_timeout))
            data = { "publicip": publicip, "privateip": IPAddr, "geo": response}
            try:
                models.RequestLogs.objects.create(localip=publicip, raw_details=data)
            except:
                pass
            return Response(data) 
        except (ValueError, TypeError) as value:
            # If save() raised, the form will a have a non
            # field error containing an informative message.
            return HttpResponse({'status':'false', "error": value}, status=500)
