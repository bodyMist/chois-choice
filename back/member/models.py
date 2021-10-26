from django.db import models

# Create your models here.
class Members(models.Model):
    members_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    birth = models.DateTimeField()
    question_type = models.IntegerField()
    question_ans = models.CharField(max_length=50)

    def __str__(self):
        return self.account

    class Meta:
        managed = False
        db_table = 'members'