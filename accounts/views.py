from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def registerUser(request):
    return HTTPResponse("this is test")