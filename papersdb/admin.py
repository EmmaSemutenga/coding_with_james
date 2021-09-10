from django.contrib import admin
from django.db import models

# Register your models here.
from papersdb.models import Paper, Author
from django.forms import CheckboxSelectMultiple

class PaperAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    # }
    # list_display = ('title', 'publication_date', 'categories', 'link', 'keyword', 'notes', 'published')
    list_display = ('title', 'publication_date', 'published')
    change_list_template = 'admin/papersdb/paper/paper_change_list.html'

    def changelist_view(self, request, extra_context={}):
        extra_context['papers'] = Paper.objects.all()
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Paper, PaperAdmin)
admin.site.register(Author)

