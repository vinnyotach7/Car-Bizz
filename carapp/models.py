from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import numpy as np


class Driver(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def save_model(self):
        self.save()

    def delete_model(self):
        self.delete()

class Rider(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def save_make(self):
        self.save()

    def delete_make(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Profile(models.Model):
  '''
  class that contains user Profile properties
  '''
  profile_pic = models.ImageField(upload_to='images/',null=True, blank=True)
  bio = models.TextField()
  contact = models.IntegerField(blank=True, null=True,)
  email = models.EmailField(blank=True,null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

  def __str__(self):
    return self.bio


  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
          if created:
                  Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
          instance.profile.save()

  post_save.connect(save_user_profile, sender=User)

  def save_profile(self):
    self.save()

  def update_profile(self):
    self.update()

  def delete_profile(self):
    self.delete()

  @classmethod
  def get_profile(cls):
      profile = Profile.objects.all()
      return profile

  @classmethod
  def get_profile_by_id(cls, id):
      user_profile = Profile.objects.get(user=id)
      return user_profile

  @classmethod
  def get_profile_by_username(cls, user):
      profile_info = cls.objects.filter(user__contains=user)
      return profile_info

  @classmethod
  def filter_by_id(cls, id):
      profile = Profile.objects.filter(user = id).first()
      return profile

class Image(models.Model):
  '''
  class that contains Image properties
  '''
  LOCATION_CHOICES = (
    ('Trade Car View Customer Center Kenya','Trade Car View Customer Center Kenya,Nairobi'),
    ('Auto Assistant','Auto Assistant,Nairobi'),
    ('Toyota Kenya','Toyota Kenya,Nairobi'),
    ('Toyotsu Kenya','Toyotsu Kenya,Nairobi'),
    ('Motorshop.co.ke','Motorshop.co.ke,Nairobi'),
    ('Toyopet Automobiles K LTD','Toyopet Automobiles K LTD,Mombasa'),
    ('Sabaki Commercial Agencies','Sabaki Commercial Agencies,Mombasa'),
    ('Al- Husain Motors Ltd','Al- Husain Motors Ltd,Mombasa'),
    ('Osaka Motors Limited','Osaka Motors Limited,Mombasa'),
    ('Fahari Cars Limited','Fahari Cars Limited,Mombasa'),
    ('Ukerio Motors','Ukerio Motors,Eldoret'),
    ('Sagoo’s Garage Limited','Sagoo’s Garage Limited,Eldoret'),
    ('Trans Africa Motors Limited','Trans Africa Motors Limited,Eldoret'),
  )
  image = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=40)
  posted_on = models.DateTimeField(auto_now_add=True)
  location = models.CharField(max_length=150,choices= LOCATION_CHOICES)
  description = models.TextField()
#   engine_type = models.TextField()
#   engine_rating = models.TextField(blank=True,null=True)
#   engine_power = models.TextField()
#   rating = models.TextField(blank=True,null=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE,default="",blank=True,null=True)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default="",blank=True,null=True)
  year = models.IntegerField(blank=True, null=True)
  driver = models.ForeignKey(Driver,blank=True,null=True)
  rider = models.ForeignKey(Rider)


  def __str__(self):
      return self.name

  def save_image(self):
      self.save()

  def delete_image(self):
      self.delete()

  class Meta:
    ordering = ['posted_on']

  @classmethod
  def get_all_images(cls):
      images = cls.objects.order_by()
      return images

  @classmethod
  def get_image(cls, id):
      image = cls.objects.get(id=id)
      return image

  @classmethod
  def get_image_by_id(cls, id):
          image = Image.objects.filter(user_id=id).all()
          return image

  @classmethod
  def filter_by_model(cls, id):
      images = cls.objects.filter(model_id=id)
      return images

  @classmethod
  def filter_by_make(cls,id):
      images = cls.objects.filter(make_id=id)
      return images

  @classmethod
  def filter_by_location(cls,id):
      images = cls.objects.filter(location_id=id)
      return images

  def average_body(self):
    total_ratings = list(map(lambda x: x.rating, self.bodyrating_set.all()))
    return np.mean(total_ratings)

  def average_usability(self):
        total_ratings = list(map(lambda x: x.rating, self.usabilityrating_set.all()))
        return np.mean(total_ratings)

  def average_engine(self):
        total_ratings = list(map(lambda x: x.rating, self.enginerating_set.all()))
        return np.mean(total_ratings)


  @classmethod
  def search_images(cls,name):
    image =  cls.objects.filter(name__icontains=name)
    return image


  @property
  def count_likes(self):
      likes = self.likes.count()
      return likes


  @property
  def count_comments(self):
      comments = self.comments.count()
      return comments





class Comment(models.Model):
        """
        Class that contains comment details
        """
        comment = models.TextField()
        posted_on = models.DateTimeField(auto_now=True)
        image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comment')
        user = models.ForeignKey(User, on_delete=models.CASCADE,null="True")

        def __str__(self):
                return self.comment

        class Meta:
                ordering = ['posted_on']
         
        def save_comment(self):
                self.save()

        def del_comment(self):
                self.delete()

        @classmethod
        def get_comments_by_image_id(cls, image):
                comments = Comment.objects.get(image_id=image)
                return comments



class Likes(models.Model):
    who_liked=models.ForeignKey(User,on_delete=models.CASCADE, related_name='likes')
    liked_image =models.ForeignKey(Image, on_delete=models.CASCADE, related_name='likes')

    def save_like(self):
        self.save() 

    def __str__(self):
      return self.who_liked


class BodyRating(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    image = models.ForeignKey(Image)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=CHOICES, default=0)


class UsabilityRating(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    image = models.ForeignKey(Image)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=CHOICES, default=0)


class EngineRating(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    image = models.ForeignKey(Image)
    pub_date = models.DateTimeField(auto_now_add=True,)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=CHOICES, default=0)



class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()