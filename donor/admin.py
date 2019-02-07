from django.contrib import admin
from .models import Donor, RevenueAdded, RevenueSpent
# Register your models here.
class DonorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'amount')
    search_fields = ('email',)

class AddedAdmin(admin.ModelAdmin):
    list_display = ('id', 'principal_amount', 'donor_id' ,'time')
    list_filter = ('donor_id',)

class SpentAdmin(admin.ModelAdmin):
    list_display = ('id', 'principal_amount', 'time')


admin.site.register(Donor, DonorAdmin)
admin.site.register(RevenueSpent, SpentAdmin)
admin.site.register(RevenueAdded,  AddedAdmin)