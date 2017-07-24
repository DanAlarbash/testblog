from __future__ import unicode_literals
from django.contrib import admin

from .models import DDD

class DDDModelAdmin(admin.ModelAdmin):
	list_display = ["name", "timestamp", "updated"]
	list_filter = ["timestamp"]
	search_fields = ["Name", "CV"]
	list_display_links = ['timestamp']
	list_editable = ["name"]
    
	class Meta:
		model = DDD

admin.site.register(DDD, DDDModelAdmin)

