from django.db import models
from django.db.models.constraints import UniqueConstraint

class Case(models.Model):
	date = models.DateField()
	state = models.CharField(max_length=100)
	tcin = models.IntegerField()
	tcfn = models.IntegerField()
	cured = models.IntegerField()
	death = models.IntegerField()

	UniqueConstraint(fields = ['date', 'state'], name = 'unique_state_and_date')
