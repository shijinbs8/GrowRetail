from django.contrib import admin
from .models import Image,VIPModel,MediumModel,LowModel

# Register your models here.

admin.site.register(Image)
admin.site.register(VIPModel)
admin.site.register(MediumModel)
admin.site.register(LowModel)