from django.urls import path
from . import views

app_name = "favoritos_app"

urlpatterns = [
    path('perfil/', views.UserFavoriteView.as_view(), name='perfil'),
    path('perfil/<int:id>/', views.AddFavoriteView.as_view(), name='add-favorite'),
    path('perfil/delete-favorite/<int:id>/', views.FavoritesDeteleView.as_view(), name='delete-favorite')
]