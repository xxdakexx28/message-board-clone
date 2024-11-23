from django.shortcuts import render
from django.views.generic import ListView
from .models import Publication

# Create your views here.

class PostlistView(ListView):
    model = Publication
    template_name = "post_list.html"
