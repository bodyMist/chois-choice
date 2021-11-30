from django.db import models
from component import models as component_models
from member import models as member_models

# Create your models here.

class Estimation(models.Model):
    estimations_id = models.IntegerField(primary_key=True)
    users = models.ForeignKey(member_models.Members, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'estimation'


class EstimationHasComponent(models.Model):
    estimation_estimations = models.OneToOneField(Estimation, models.DO_NOTHING, primary_key=True)
    component_component = models.ForeignKey(component_models.Component, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'estimation_has_component'
        unique_together = (('estimation_estimations', 'component_component'),)


class Evaluations(models.Model):
    evaluations_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    written = models.DateTimeField()
    members_members = models.ForeignKey(member_models.Members, models.DO_NOTHING)
    component_component = models.ForeignKey(component_models.Component, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'evaluations'


class Annotations(models.Model):
    annotation_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    explain = models.TextField()

    class Meta:
        managed = True
        db_table = 'annotations'


class Uses(models.Model):
    uses_id = models.IntegerField(primary_key=True)
    type = models.PositiveIntegerField()
    game_genre = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    least_processor = models.CharField(max_length=100, blank=True, null=True)
    least_graphics = models.CharField(max_length=100, blank=True, null=True)
    least_memory = models.CharField(max_length=30, blank=True, null=True)
    rec_processor = models.CharField(max_length=100, blank=True, null=True)
    rec_graphics = models.CharField(max_length=100, blank=True, null=True)
    rec_memory = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'uses'

class BenchMark(models.Model):
    benchmark_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    score = models.FloatField(blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'benchmark'