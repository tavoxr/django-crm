from django.contrib.auth.models import Group, User
from ..models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):

    if created:
        group = Group.objects.get(name ='customer')
        instance.groups.add(group) #instance is user was created

        Customer.objects.create(
            user = instance,
            name = instance.username,
            )
        print('Customer created')




