from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

def hello(request):
    request.session['dj4e_cookie'] = '5951917c'
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse(f"<h1>Hello 5951917c</h1><p>view count={num_visits}")
    resp.set_cookie('dj4e_cookie', '5951917c', max_age=1000)
    return resp