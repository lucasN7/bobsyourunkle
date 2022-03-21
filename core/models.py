from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Contract(models.Model):
	""" """
	number = models.AutoField(primary_key=True)
	clients = models.ManyToManyField(User, related_name='contracts')
	start_dt = models.DateField()
	end_dt = models.DateField(null=True)
	cancel_dt = models.DateField(null=True)	
	created_dt = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contracts_created')
	modified_dt = models.DateTimeField(auto_now=True)
	modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contracts_modified_last')
	
	@property
	def status(self):
		""" Return the status on the contract:
		- "Canceled" if cancel_dt is set
		- "Pending" before the start_dt
		- "Active" between the start_dt and end_dt
		- "Finished" after the end_dt
	    """
		today = date.today()
		if self.cancel_dt: return "Canceled"
		if self.end_dt <= today: return "Finished"
		if self.start_dt <= today: return "Active"
		return 'Pending'


	def clean(self):
		cleaned_data = super().clean()
		if self.start_dt >= self.end_dt:
			raise ValidationError("Contract end date cannot be before its start date")

#TODO: extend user and make email mandatory? Remove username?