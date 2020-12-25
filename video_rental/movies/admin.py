from django.contrib import admin
from .models import Genre, Movie


'''This shows how models are displayed in the admin'''
class GenreAdmin(admin.ModelAdmin):
	list_display=('id', 'name')

class MovieAdmin(admin.ModelAdmin):
	exclude = ('date_created', )
	list_display = ('title', 'number_in_stock', 'daily_rate')
 

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.site_header = "Movie Rental Store"
admin.site.site_title = "Movie Admin Area"
admin.site.index_title = "Welcome to the Sumit Movie Store"


