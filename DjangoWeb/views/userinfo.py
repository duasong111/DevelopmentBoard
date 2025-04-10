import json
import subprocess
from django.shortcuts import render
from django.http import JsonResponse

def login(request):


    render(request,'login.html')
