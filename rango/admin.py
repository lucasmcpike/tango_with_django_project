from django.contrib import admin
from rango.models import Category, Page

# Define how you want the Page list to look
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register the models
admin.site.register(Category)
# Pass PageAdmin as the second argument here!
admin.site.register(Page, PageAdmin)