from django.contrib import admin
from . import models

admin.site.register(models.Course)
admin.site.register(models.Project)
admin.site.register(models.SwitchProposal)
