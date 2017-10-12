from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
	# get context of request from client
    context = RequestContext(request)
    # construct dictionary to pass template + context
    context_dict = {'boldmessage': "I am being sent from the server, woooooo"}

    #render and return to client
    return render_to_response('headstation/home.html', context_dict, context)