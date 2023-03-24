from django.shortcuts import render

from .models import Menu


def show_menu(request):
    menus = {'menus': Menu.objects.all()}
    return render(request, template_name='menu.html', context=menus)

