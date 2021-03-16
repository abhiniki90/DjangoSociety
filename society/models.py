from django.db import models

# Create your models here.

class UserProfile(models.Model):
	about_me = models.CharField(max_length=1000)
	birth_date = models.DateField('Enter your Date of Birth')
	fav_movies = models.TextField()
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images')

	def __str__(self):
		return self.about_me

class Group(models.Model):
	name = models.CharField(max_length=200)
	members = models.CharField(max_length=3)
	description = models.TextField()
	category = models.TextField()
	website_url = models.TextField()
	creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Event(models.Model):
	creator_name = models.CharField(max_length=100)
	description = models.TextField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	location = models.TextField()
	event_title = models.CharField(max_length=500)
	creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

	def __str__(self):
		return self.creator_name

class Feed(models.Model):
	feed_type = models.TextField()
	total_likes = models.IntegerField()
	comments = models.TextField()
	content = models.TextField()

	def __str__(self):
		return self.feed_type

class Signup(models.Model):
	user_name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)


	def __str__(self):
		return self.username
