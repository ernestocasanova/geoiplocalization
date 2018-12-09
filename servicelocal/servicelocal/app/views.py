"""
Definition of views.
"""
from app import models
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

class LoadLogsAPIView(APIView):

#    permission_classes = (APIKeyPermission,)

    def get(self, request):
        try:
            import socket, requests, urllib
            ip = socket.gethostbyname(socket.gethostname())
            f = requests.request('GET', 'http://myip.dnsomatic.com')
            publicip = f.text
            headerip = newremoteip = request.META.get("HTTP_X_FORWARDED_FOR", None)
            if headerip:
                # X_FORWARDED_FOR returns client1, proxy1, proxy2,...
                headerip = ip.split(", ")[0]
            else:
                headerip = ''
            remoteip = request.META.get("REMOTE_ADDR", "")

            with requests.get('http://myip.dnsomatic.com', stream=True) as r:
                print(r.raw._original_response.fp.raw._sock.getpeername())
                newremoteip = r.raw._original_response.fp.raw._sock.getpeername()[0]
                r.status_code
            
            #coord = urllib.request.urlopen("http://api.hostip.info/get_html.php?ip={}&position=true".format(headerip)).read()

            result = {ip, publicip, headerip, remoteip, newremoteip}
            try:
                models.RequestLogs.objects.create(localip=ip)
            except:
                pass
            return Response(result)
        except (ValueError, TypeError) as value:
            # If save() raised, the form will a have a non
            # field error containing an informative message.
            return HttpResponse({'status':'false', "error": value}, status=500)
