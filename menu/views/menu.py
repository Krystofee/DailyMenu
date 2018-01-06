import datetime

from django.urls import reverse_lazy
from django.utils import timezone

from core.views import authenticated
from core.views.mixins import UserFormViewMixin
from menu.forms import MenuModelForm
from menu.models import Menu


class MenuListView(authenticated.AuthenticatedListView):
    model = Menu

    def get_queryset(self):
        return Menu.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)
        context['date_from'] = timezone.now()
        context['date_to'] = timezone.now() - datetime.timedelta(days=7)
        return context


class MenuCreateView(UserFormViewMixin, authenticated.AuthenticatedCreateView):
    model = Menu
    form_class = MenuModelForm


class MenuUpdateView(UserFormViewMixin, authenticated.AuthenticationUpdateView):
    model = Menu
    form_class = MenuModelForm

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.update_entries()
        return super().post(request, *args, **kwargs)


class MenuDeleteView(authenticated.AuthenticationDeleteView):
    model = Menu
    success_url = reverse_lazy('index')

