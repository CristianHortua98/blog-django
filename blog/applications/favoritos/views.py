from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.views import View
from .models import Favorites
from applications.entrada.models import Entry

class UserFavoriteView(LoginRequiredMixin, ListView):

    template_name = "favoritos/perfil.html"
    context_object_name = "entradas_user"
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)
    

class AddFavoriteView(LoginRequiredMixin, View):

    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        #RECUPERAR USUARIO
        usuario = self.request.user
        #RECUPERAR ENTRADA
        entrada = Entry.objects.get(id = self.kwargs['id'])

        if not Favorites.objects.filter(user=usuario, entry=entrada):

            Favorites.objects.create(
                user=usuario,
                entry=entrada
            )

            return HttpResponseRedirect(reverse_lazy('favoritos_app:perfil'))
        
        else:

            print(f'La relacion ya existe.')
            return HttpResponseRedirect(reverse_lazy('favoritos_app:perfil'))

    

class FavoritesDeteleView(DeleteView):

    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')

    def get_object(self):
        id = self.kwargs.get("id")
        return Favorites.objects.get(id=id)