from django.contrib import admin
from rango.models import Category, Page, UserProfile

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class pageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")


admin.site.register(Category, categoryAdmin)
admin.site.register(Page, pageAdmin)
admin.site.register(UserProfile)