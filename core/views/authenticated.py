from core.views.base import BaseCreateView, BaseDeleteView, BaseDetailView, BaseListView, BaseUpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthenticatedListView(LoginRequiredMixin, BaseListView):
    pass


class AuthenticatedCreateView(LoginRequiredMixin, BaseCreateView):
    pass


class AuthenticationDeleteView(LoginRequiredMixin, BaseDeleteView):
    pass


class AuthenticationDetailView(LoginRequiredMixin, BaseDetailView):
    pass


class AuthenticationUpdateView(LoginRequiredMixin, BaseUpdateView):
    pass
