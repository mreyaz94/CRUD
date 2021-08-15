from django.shortcuts import render
from webapp.models import BeerDB
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class BeerCreateView(CreateView):
    model = BeerDB
    fields = ('name','taste','color','price')
    # get_absolute_url=reverse_lazy('abs')
    success_url = reverse_lazy('abs')

class BeerListView(ListView):
    model = BeerDB

class BeerDetailView(DetailView):
    model = BeerDB

class BeerUpdateView(UpdateView):
    model = BeerDB
    fields = ('taste','color', 'price')
    success_url = reverse_lazy('abs')

class BeerDeleteView(DeleteView):
    model = BeerDB
    success_url = reverse_lazy('abs')
