from django.contrib import admin

from openshift.models.models import Deed, Tag, Hardness, DeedUser

admin.site.register(Tag)
admin.site.register(Hardness)
admin.site.register(Deed)
admin.site.register(DeedUser)
# Register your models here.
