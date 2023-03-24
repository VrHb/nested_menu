from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

class ItemsView(TemplateView):
    template_name = 'items.html'

class OrdersView(TemplateView):
    template_name = 'orders.html'

