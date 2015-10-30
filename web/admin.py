from django.contrib import admin
from web.models import Web
#proje adı web modelin adı Web
# Register your models here.
#admin panelnde neler gözükecek.Model için Admin görünümü açtık
class WebAdmin(admin.ModelAdmin):
    list_display=('title','author','view_count','created_at')
    list_filter=('title','author')

admin.site.register(Web,WebAdmin)
