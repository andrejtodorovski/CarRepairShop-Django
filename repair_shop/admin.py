from django.contrib import admin

# Register your models here.

from .models import Repair, Car, RepairShop, CarBrand, RepairShopRepairsCarBrand


class RepairShopRepairsCarBrandInline(admin.TabularInline):
    model = RepairShopRepairsCarBrand
    extra = 0


class RepairShopAdmin(admin.ModelAdmin):
    inlines = [RepairShopRepairsCarBrandInline]

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CarAdmin(admin.ModelAdmin):
    list_display = ['type', 'max_speed', ]


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ['name', ]

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True


class RepairAdmin(admin.ModelAdmin):
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Repair, RepairAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(RepairShop, RepairShopAdmin)
admin.site.register(CarBrand, CarBrandAdmin)
