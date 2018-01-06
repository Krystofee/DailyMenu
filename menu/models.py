import datetime
import uuid

from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _

from menu.utils import get_entries_for_menu


class Menu(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    user = models.ForeignKey(
        to="auth.User",
        related_name='menus',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    name = models.CharField(
        verbose_name=_('Name of the menu'),
        max_length=150
    )
    update_time = models.TimeField(
        verbose_name=_('Update hour'),
        help_text=_('This menu will be updated at time specified here.'),
        blank=True, null=True
    );

    url = models.URLField(
        verbose_name=_('Menu url'),
        blank=True, null=True
    )
    menu_element = models.CharField(
        max_length=150,
        blank=True, null=True
    )
    meal_element = models.CharField(
        max_length=150,
        blank=True, null=True
    )
    price_element = models.CharField(
        max_length=150,
        blank=True, null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def update_entries(self):
        entries = get_entries_for_menu(self)
        for entry in entries:
            MenuEntry.objects.create(
                name=entry[0].text,
                price=entry[1].text,
                menu=self
            )
        return entries

    def recent_entries(self, days=7, **kwargs):
        return self.entries.filter(created__gt=(timezone.now() - datetime.timedelta(days=days))).order_by('-created')

    def get_absolute_url(self):
        return reverse('index')

class MenuEntry(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    menu = models.ForeignKey(
        to=Menu,
        related_name='entries',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=150
    )
    price = models.CharField(
        verbose_name=_('Price'),
        max_length=150
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
