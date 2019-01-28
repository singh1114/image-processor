from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):

    default_readonly_fields = ('uuid', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('uuid',)
