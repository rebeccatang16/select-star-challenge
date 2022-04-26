from django.contrib import admin
from folder_view.folder_view.models import Prefix, Word


# Register your models here.

class PrefixAdmin(admin.ModelAdmin):
    pass

class WordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prefix, PrefixAdmin)
admin.site.register(Word, WordAdmin)
