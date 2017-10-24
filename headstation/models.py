from datetime import datetime, date, time
from django.db import models

# for online access perhaps? or just different local logins with different privilages
class User(models.Model):
	user_id =  models.AutoField(max_length=128, unique=True, primary_key=True)
	user_name = models.CharField(max_length=256, unique=True)
	password_hash = models.CharField(max_length=256)
	last_login = models.DateTimeField(auto_now=False, auto_now_add=False).default = datetime.today()

	def __str__(self):
		return self.last_login

# all sensor data since time began
class TemperatureReading(models.Model):
	measurement_id = models.AutoField(max_length=128, unique=True, primary_key=True) # unique id, of the measurement, for relational db
	sensor_id = models.IntegerField()
	date_time = models.DateTimeField(auto_now=False, auto_now_add=False).default = datetime.today()
	temperature = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.measurement_id

class HumidityReading(models.Model):
	measurement_id = models.AutoField(max_length=128, unique=True, primary_key=True) # unique id, of the measurement, for relational db
	sensor_id = models.IntegerField()
	date_time = models.DateTimeField(auto_now=False, auto_now_add=False).default = datetime.today()
	humidity = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.measuremnt_id

class co2Reading(models.Model):
	measurement_id = models.AutoField(max_length=128, unique=True, primary_key=True) # unique id, of the measurement, for relational db
	sensor_id = models.IntegerField()
	date_time = models.DateTimeField(auto_now=False, auto_now_add=False).default = datetime.today()
	co2 = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.measuremnt_id

# log all errors for monitoring and correcting
class ErrorLog(models.Model):
	error_id = models.AutoField(max_length=128, unique=True, primary_key=True) # unique id of error
	date_time = models.DateTimeField(auto_now=False, auto_now_add=False).default = datetime.today()
	message_id = models.IntegerField() # id of message, might not use - e.g 400 server error, all that
	error_message = models.CharField(max_length=256)
	error_temperature = models.DecimalField(max_digits=10, decimal_places=2)
	error_humidity = models.DecimalField(max_digits=10, decimal_places=2)
	error_co2 = models.DecimalField(max_digits=10, decimal_places=2)



	def __str__(self):
		return self.error_id





