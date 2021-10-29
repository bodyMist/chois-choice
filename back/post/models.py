from django.db import models
from member import models as member_models
from estimate import models as estimate_models

# Create your models here.

class Likes(models.Model):
    likes_id = models.IntegerField(primary_key=True)
    members = models.ForeignKey(member_models.Members, models.DO_NOTHING)
    posts = models.ForeignKey('Posts', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'likes'


class Posts(models.Model):
    posts_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=100)
    type = models.IntegerField()
    content = models.TextField()
    written = models.DateTimeField()
    members = models.ForeignKey(member_models.Members, models.DO_NOTHING)
    estimations = models.ForeignKey(estimate_models.Estimation, models.DO_NOTHING, blank=True, null=True)
    upper_post = models.ForeignKey('self', models.DO_NOTHING, blank=True ,null=True)

    class Meta:
        managed = False
        db_table = 'posts'



class Reports(models.Model):
    reports_id = models.IntegerField(primary_key=True)
    members = models.ForeignKey(member_models.Members, models.DO_NOTHING)
    posts = models.ForeignKey(Posts, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reports'

