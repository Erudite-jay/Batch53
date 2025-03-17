from django.contrib.auth.models import User #sender
from django.contrib.auth.signals import user_logged_in # signal

from django.db.models.signals import pre_save,post_save
from Auth_app.models import Contact

from django.dispatch import receiver


def login_success(user,**kwargs): # reciever
    print("i am user logged in signal reciever function")
    print(kwargs)
    print(user.email)

    #write logic to send email to the user that you have successfully login at this time

#normal one
user_logged_in.connect(login_success,sender=User) #to connect sender+signal+reciever

#decorator method
@receiver(pre_save,sender=Contact)
def before_save(**kwargs):
    print("Hello i am presave signal reciever function")
    print(kwargs)


@receiver(post_save,sender=Contact)
def after_save(**kwargs):
    print("Hello i am post signal reciever function")
    print(kwargs)
