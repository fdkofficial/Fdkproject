from django.shortcuts import render
from django.http import HttpResponse
def index2(req):
    return render(req,'blog/index.html')
