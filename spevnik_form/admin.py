from django.contrib import admin

from .models import Song
from .models import Author

admin.site.register(Song)
admin.site.register(Author)
