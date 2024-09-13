from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import GamingYoutuber
from .forms import GamingYoutuberForm

class YoutuberListView(ListView):
    model = GamingYoutuber
    template_name = 'youtuber_list.html'
    context_object_name = 'youtubers'

class YoutuberDetailView(DetailView):
    model = GamingYoutuber
    template_name = 'youtuber_detail.html'

class YoutuberCreateView(CreateView):
    model = GamingYoutuber
    form_class = GamingYoutuberForm
    template_name = 'youtuber_form.html'
    success_url = reverse_lazy('youtuber_list')

class YoutuberUpdateView(UpdateView):
    model = GamingYoutuber
    form_class = GamingYoutuberForm
    template_name = 'youtuber_form.html'
    success_url = reverse_lazy('youtuber_list')

class YoutuberDeleteView(DeleteView):
    model = GamingYoutuber
    template_name = 'youtuber_confirm_delete.html'
    success_url = reverse_lazy('youtuber_list')