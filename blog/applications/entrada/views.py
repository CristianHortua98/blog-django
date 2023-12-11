from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Entry, Category

class EntryListView(ListView):

    template_name = "entrada/lista.html"
    context_object_name = "entradas"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)

        if self.request.GET.get('kword', ''):
            context["busqueda"] = self.request.GET.get('kword', '')
        else:
            context["busqueda"] = self.request.GET.get('categoria', '')
        

        context["categorias"] = Category.objects.all()
        return context

    def get_queryset(self):

        kword = self.request.GET.get('kword', '')
        categoria = self.request.GET.get('categoria', '')
        #BUSQUEDA
        resultado = Entry.objects.buscar_entrada(kword, categoria)
        return resultado
    
class EntryDetailView(DetailView):

    model = Entry
    template_name = "entrada/detail.html"
    context_object_name = "entrada"

    # def get_object(self):
    #     id = self.kwargs.get("id")
    #     return Entry.objects.get(id=id)