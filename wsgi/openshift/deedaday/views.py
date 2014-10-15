# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


from deedaday.models import Deed

def index_fb(request):
	pass
	
def index_vk(request):
	pass


def index(request):
	import random
	deeds_list=Deed.objects.all()
	random_deed=random.choice(deeds_list)
	context = RequestContext(request, {
        'deeds_list': deeds_list,
        'random_deed': random_deed,
	})
	return render(request,'index/index.html', context)
    
def sendADeed(request):
    return HttpResponse("Hello, world. You're at the deed proposal page.")
    
def deed(request, deed_id):
	deed=Deed.objects.get(id=deed_id)
	context = RequestContext(request, {'deed': deed })
	return render(request,'deeds/deed.html', context)
	
def userpage(request,user_id):
	deeds_list=Deed.objects.all()
	context = RequestContext(request, {
		'user_name': "Маша Иванова",
		'user_deeds_num':len(deeds_list),
		'user_deeds': deeds_list,
		'friends_pledge':[{"user":"Анна Куранова", "deed":deeds_list[0]}, {"user":"Иван Иванов", "deed":deeds_list[2]}]
	})
	return render(request,'user/stat.html', context)

