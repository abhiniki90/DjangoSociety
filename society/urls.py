from django.urls import path
from . import views
app_name = "society"
urlpatterns = [
	path('', views.landing, name='landing'),
	path('image-upload/', views.upload_image, name='upload_image'),
	path('user/', views.home, name='home'),
	path('event', views.event, name='event'),
	path('group', views.group, name='group'),
	path('user/<int:user_id>/', views.detail1, name='user_details'),
	path('event/<int:event_id>/', views.event_details, name='event_details'),
	path('group/<int:group_id>/', views.group_details, name='group_details')
]