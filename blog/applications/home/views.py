import datetime
from django.http import HttpResponse
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView, CreateView
)
from django.views.generic.edit import FormView

from applications.entrada.models import Entry
from .models import Home, Suscribers
from .forms import SuscribersForm, ContactForm

class HomePageView(FormView):

    template_name = "home/index.html"
    form_class = SuscribersForm
    success_url = reverse_lazy('home_app:home')

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        #CONTEXTO HOME
        context["home"] = Home.objects.latest('created')

        #CONTEXTO PORTADA
        context["portada"] = Entry.objects.entrada_en_portada()

        #CONTEXTO 4 ARTICULOS HOME
        context["entradas_home"] = Entry.objects.entradas_en_home()

        #CONTEXTO ENTRADAS RECIENTES
        context["entradas_recientes"] = Entry.objects.entradas_recientes()

        #ENVIAR FORMULARIO DE SUSCRIPCION
        context["form"] = SuscribersForm

        return context
    
    def form_valid(self, form):
        
        if form.is_valid():

            try:

                suscriber = Suscribers(
                    email = form.cleaned_data['email']
                )

                suscriber.save()

            except Exception as e:
                print("Entró al bloque except")
                print(f"Error al guardar el Suscriber: {e}")
                raise

        return super(HomePageView, self).form_valid(form)
    
class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('home_app:home')