from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('create/', views.create, name='create'),
<<<<<<< HEAD
    path('newblog/', views.blogpost, name="newblog"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]
>>>>>>> 078f311babc36f0b5b6d4936a860cf9b36c17171
