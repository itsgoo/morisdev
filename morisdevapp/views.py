from django.shortcuts import render, redirect
from django.views.generic.base import View
# Create your views here.
from .busines_logic.main import *
from django.core.exceptions import ObjectDoesNotExist

from django.http import Http404 


from django.contrib import messages 

import json

from django.utils.safestring import mark_safe


#... def your_view(request) 
# 
# #... try: 
# 
# #... do something 
# 
# except: raise Http404 
# 
# #or return redirect('your-custom-error-view-name', error='error messsage') 


class Index(View):
    def get(self, request):
        try:
            ctx = index(self, request)
            return render(request, 'index.html', ctx)
        except:
            # raise ObjectDoesNotExist(self)
            var_self = self
            var_request = request
            ctx = {
               'var_self': var_self, 
               'var_request': var_request, 
            }
            return render(request, 'exception.html', ctx)


class Portfolio(View):
    def get(self, request):

        return render (request, 'portfolio.html')

class LiveChat(View):
    def get(self, request, room_name):
        print('room_name', room_name)
        ctx = {
            'room_name_json' : mark_safe(json.dumps(room_name))
        }

        return render (request, 'live_chat.html', ctx)