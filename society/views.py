from django.shortcuts import render
from django.template import loader
from .forms import ImageForm
from django.http import HttpResponse
from .models import Signup
from .models import UserProfile
from .models import Group
from .models import Event


	

def landing(request):
	#return HttpResponse("Hello, World!")

	#latest_user_list=UserProfile.objects.all()
	#template = loader.get_template('SocialMedia/landing.html')
	#context= {
	#	'latest_user_list': latest_user_list,
	#}
	#return HttpResponse(template.render(context,request))
		return render(request, "society/landing.html")

def upload_image(request):
	if request.method == 'POST':
		image_form = ImageForm(request.POST, request.FILES)
		if image_form.is_valid():
			image_form.save()
			image_form=ImageForm()
		context={
			"form": image_form,
			"img_obj": image_form.instance
		}
		return render(request,'society/image_upload.html', context)
	else:
		image_form=ImageForm()
		return render(request,'society/image_upload.html', {'form': image_form})


def home(request):
	#return HttpResponse("Hello, World!")

	latest_user_list=UserProfile.objects.all()
	count=UserProfile.objects.all().count()
	template = loader.get_template('society/user.html')
	context= {
		'latest_user_list': latest_user_list,
		'count': count
	}
	return HttpResponse(template.render(context,request))


def detail1(request,user_id):
	latest_user_detail=UserProfile.objects.get(id=user_id)
	template = loader.get_template('society/user_details.html')
	context= {
		'Details_user': latest_user_detail,
	}	
	return HttpResponse(template.render(context,request))

def event(request):
	#return HttpResponse("Hello, World!")

	latest_event_list=Event.objects.all()
	count=Event.objects.all().count()
	template = loader.get_template('society/event.html')
	context= {
		'latest_event_list': latest_event_list,
		'count': count
	}
	return HttpResponse(template.render(context,request))


def event_details(request,event_id):
	latest_event_detail=Event.objects.get(id=event_id)
	user_info=UserProfile.objects.get(pk=event_id)
	context= {
		'Details_event': latest_event_detail,
		'user_info': user_info
	}	
	#return HttpResponse(template.render(context,request))
	return render(request, 'society/event_details.html', context)

def group(request):
	#return HttpResponse("Hello, World!")

	latest_group_list=Group.objects.all()
	count=Event.objects.all().count()
	template = loader.get_template('society/group.html')
	context= {
		'latest_group_list': latest_group_list,
		'count': count
	}
	return HttpResponse(template.render(context,request))


def group_details(request,group_id):
	latest_group_detail=Group.objects.get(id=group_id)
	user_info=UserProfile.objects.get(pk=group_id)
	template = loader.get_template('society/group_details.html')
	context= {
		'Details': latest_group_detail,
		'user_info': user_info
	}	
	return HttpResponse(template.render(context,request))
#def index(request):
#	return HttpResponse("Social Media 2021")