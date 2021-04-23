from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models
from admin_auto_filters.filters import AutocompleteFilter


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


class AuthorFilter(AutocompleteFilter):
    title = 'Author'  # display title
    field_name = 'authors'  # name of the foreign key field


class PublisherFilter(AutocompleteFilter):
    title = 'Publisher'  # display title
    field_name = 'publisher'  # name of the foreign key field


class BookAdmin(admin.ModelAdmin):
    list_filter = (PublisherFilter, AuthorFilter,)
    search_fields = ['title', ]


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name', ]


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', ]


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)

