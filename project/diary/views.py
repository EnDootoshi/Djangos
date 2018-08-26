from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day

class IndexView(generic.ListView):
    model = Day
    paginate_by = 3


class AddView(LoginRequiredMixin,generic.CreateView): #半角スペースを入れたらだめ
    model = Day
    form_class = DayCreateForm #fields = '__all__'でも同じ
    success_url = reverse_lazy('diary:index') #リダイレクトする



class UpdateView(LoginRequiredMixin,generic.UpdateView):#半角スペースを入れたらだめ
    model = Day
    form_class = DayCreateForm #fields = '__all__'でも同じ
    success_url = reverse_lazy('diary:index') #リダイレクトする



class DeleteView(LoginRequiredMixin,generic.DeleteView):#半角スペースを入れたらだめ
    model = Day
    success_url = reverse_lazy('diary:index') #リダイレクトする


class DetailView(generic.DetailView):
    model = Day
