from django.contrib import admin
from TestProject.books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')
    search_fields = ('name', 'address', 'city')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    raw_id_fields = ('publisher',)
    filter_horizontal = ('authors',)
    #fields = ('title', 'authors', 'publisher', 'publication_date')

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)