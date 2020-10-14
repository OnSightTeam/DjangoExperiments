from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save

class Product(models.Model):
	product_name = models.CharField(max_length=150)
	product_type = models.CharField(max_length=25)
	product_description = models.TextField()
	product_price = models.IntegerField()


# class Profile(models.Model):  
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	cart = models.ManyToManyField(Product)

# 	@receiver(post_save, sender=User) 
# 	def create_user_profile(sender, instance, created, **kwargs):
# 		if created:
# 			Profile.objects.create(user=instance)

# 	@receiver(post_save, sender=User) 
# 	def save_user_profile(sender, instance, **kwargs):
# 		instance.profile.save()