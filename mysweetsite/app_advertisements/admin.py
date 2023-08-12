from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'is_auction', 'created_date', 'updated_date', 'image_adv']
    actions = ['make_auction_as_true', 'make_auction_as_false']
    list_filter = ['is_auction', 'created_at']

    fieldsets = (
        ('Общее', {'fields': ('title', 'description', 'user'), 'classes': ['collapse']}),
        ('Финансы', {'fields': ('price', 'is_auction'), 'classes': ['collapse']})
    )

    @admin.action(description='Сделать торг уместным')
    def make_auction_as_true(self, request, queryset):
        queryset.update(is_auction=True)

    @admin.action(description='Отменитьть торг')
    def make_auction_as_false(self, request, queryset):
        queryset.update(is_auction=False)

    @admin.display(description='Изображение')
    def image_adv(self, obj):
        from django.utils.safestring import mark_safe
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50"/>')


admin.site.register(Advertisement, AdvertisementAdmin)
