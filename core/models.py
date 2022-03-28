from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date


class ContractOption(models.Model):
	name = models.CharField(max_length=20, unique=True,)
	description = models.TextField()


class Contract(models.Model):
	""" Contracts! """
	number = models.AutoField(primary_key=True)
	clients = models.ManyToManyField(User, related_name='contracts')
	options = models.ManyToManyField(ContractOption, related_name='contracts')
	start_dt = models.DateField()
	end_dt = models.DateField(null=True, blank=True)
	cancel_dt = models.DateField(null=True, blank=True)	
	created_dt = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User, null=True, blank=True, 
								   on_delete=models.SET_NULL, related_name='contracts_created')
	modified_dt = models.DateTimeField(auto_now=True)
	modified_by = models.ForeignKey(User, null=True, blank=True, 
								    on_delete=models.SET_NULL, related_name='contracts_modified_last')
	
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
		if self.start_dt >= self.end_dt:
			raise ValidationError("Contract end date cannot be before its start date")


		
	def save(self, *args, **kwargs):
		self.full_clean()
		super().save(*args, **kwargs)
