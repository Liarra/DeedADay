# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


from deedaday.models import Deed, DeedUser
from django.contrib.auth import authenticate, login

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
	
def userpage(request):
	#TODO: Vk integration here
	user = authenticate(username="Liarra1", password="123")
	if user is not None:
		if user.is_active:
			login(request, user)

	deed_user=DeedUser.objects.get(id=user.id)
	deeds_list=Deed.objects.all()
	user_deeds=deed_user.deeds.all()
	
	#return HttpResponse("Hello, world. You're at the deeds of user {0}: {1}".format(str(deed_user), str(user_deeds)))
	
	context = RequestContext(request, {
		'user_deeds':user_deeds,
		'user_deeds_len':len(user_deeds),
		'friends_pledge':[{"user":"Анна Куранова", "deed":deeds_list[0]}, {"user":"Иван Иванов", "deed":deeds_list[0]}]
	})
	
	return render(request,'user/stat.html', context)

