from django.shortcuts import render
import requests
import pandas as pd
from . import dash_app

def dash_view(request):
    return render(request, 'dash.html')