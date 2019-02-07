from django.contrib import admin
from .models import Feedback
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')

admin.site.register(Feedback, FeedbackAdmin)
