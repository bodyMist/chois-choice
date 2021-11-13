from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Members(models.Model):
    members_id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth = models.DateTimeField()
    question_type = models.IntegerField()
    question_ans = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'members'
    
    @receiver(post_save, sender=User)
    def create_user_members(sender, instance, created, **kwargs):
        if created:
            Members.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_members(sender, instance, **kwargs):
        instance.members.save()