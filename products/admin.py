from django.contrib import admin
from .models import Review, CategoryWaters, Waters

admin.site.register(CategoryWaters)
admin.site.register(Waters)
admin.site.register(Review)