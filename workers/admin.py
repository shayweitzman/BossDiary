
from django.contrib import admin
from workers.models import Worker,Job

# class WorkerAdmin(admin.ModelAdmin):
#     search_fields = ['name','author_name','key_words','genre','Grade',]
#     list_display = ('name','author_name','genre','Grade','key_words',)
#
# class AudioBookAdmin(admin.ModelAdmin):
#     search_fields = ['name', 'key_words', 'genre']
#     list_display = ('name', 'genre', 'key_words',)

admin.site.register(Worker)
admin.site.register(Job)
# Register your models here.
