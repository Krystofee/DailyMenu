from django import forms

from core.forms.mixins import UserModelFormMixin
from menu.models import Menu


class MenuModelForm(UserModelFormMixin, forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'name',
            'url',
            'update_time',
            'menu_element',
            'meal_element',
            'price_element'
        ]
