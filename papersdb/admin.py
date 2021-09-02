from django.contrib import admin

# Register your models here.
from papersdb.models import Paper, Author

admin.site.register(Paper)
admin.site.register(Author)

