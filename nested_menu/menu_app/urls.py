from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, ItemsView, OrdersView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('items/', ItemsView.as_view(), name='items'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

