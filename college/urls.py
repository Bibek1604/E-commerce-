from django.urls import path
from django.conf import settings
from Project.views import store, cart, checkout,main
from django.conf.urls.static import static
urlpatterns = [
    path('', store, name='store'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='cart'),
    path('main/',main, name='main'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)