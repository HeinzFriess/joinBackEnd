from django.contrib import admin

from tickets.models import Ticket, Category, Priority, State

admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(State)

