from django.contrib import admin

from stories.models import Story

# admin.py is called with an object (obj)


class StoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'lower_case_title', 'domain', 'moderator', 'created_at', 'updated_at',)

    def lower_case_title(self, obj):
        return obj.title.lower()
    lower_case_title.short_description = 'Title (lower case)'

    list_filter = ('created_at', 'updated_at', 'moderator')
    search_fields = ('title',
                     'moderator__username',
                     'moderator__first_name',
                     'moderator__last_name',)
    # fields = ('title', 'url', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)

    fieldsets = [
        ('Story', {
            'classes': (),
            'fields':('title', 'url', 'points', 'created_at',),
        }),
        ('Moderator', {
            'classes': ('collapse',),
            'fields': ('moderator',),
        }),
        ('Change History', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at'),
        })
    ]


admin.site.register(Story, StoryAdmin)
