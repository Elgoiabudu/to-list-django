from django.contrib import admin

from todos.models import ToDo, UserAPI

admin.site.register(ToDo)
admin.site.register(UserAPI)
