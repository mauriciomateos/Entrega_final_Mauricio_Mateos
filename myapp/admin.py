from django.contrib import admin
from myapp.models import Page, Message

class PageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Page, PageAdmin)

class MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Message, MessageAdmin)
