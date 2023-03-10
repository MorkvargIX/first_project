from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_apps, name='main_page'),
    path('directors', views.all_directors),
    path('directors/<int:number_of_director>', views.one_director, name='one_dir'),
    path('actor/<int:character_id>', views.info, name='character'),
    path('<slug:slug_book>', views.one, name='one_book'),
]