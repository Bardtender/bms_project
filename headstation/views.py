from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .models import TemperatureReading, HumidityReading, co2Reading

import json

# REMEBER
# django view = MVC controller
# django templates = MVC view

def index(request):
	# get context of request from client
	context = RequestContext(request)
	# construct dictionary to pass template + context
	context_dict = {'buildingName': 'The Diamond',
					'boldmessage': 'Random message here from the server'}

	#render and return to client
	return render_to_response('headstation/home.html', context_dict, context)

# upload data from a node to the db
@csrf_exempt
def upload_data(request):
	if (request.method == 'POST'):
		data = json.loads(request.body.decode("utf-8"))
		if (data['action'] == 'uploadData'):
			# create temperature object, save to database
			temperature = data['temperature']
			newReading = TemperatureReading(sensor_id = 1, temperature = temperature)
			newReading.save()

			response = {"status": "success"}
		else:
			response = {"status": "oh no"}

		return JsonResponse(response)
			
			#get data from request
	return


# get data from database to plot on control panel
@csrf_exempt
def chart_data(request):

	if (request.method == 'POST'):
		# get all data from db
		if (request.POST.get('action') == 'getData'):
			# get all data into objects
			temperatureObj = TemperatureReading.objects.all()
			# loop through and get time/values
			timeData = [i.date_time for i in temperatureObj]
			temperatureData = [i.temperature for i in temperatureObj]

			#time = [0,10,20,30,40,50,60]
			#dataY = [26.0,23.2,25,24.0,24.5,27.1,25.5]
			# data json
			data = {"time": timeData,
					"value": temperatureData}
			errors = []

			response = {
						"status": "okay",
						"errors": errors,
						"data": data
						}

		# get only new data from db
		elif (request.action == 'updateData'):
			# get new data into objects
			temperatureObj = TemperatureReading.objects.all()
	else:
		response = {"x": "no",
					"y": "no"}

	return JsonResponse(response)