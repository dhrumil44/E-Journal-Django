from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
		list_display = ["Title","updated","timestamp"]
		list_display_links = ["timestamp"]
		list_editable = ["Title"]
		list_filter = ["updated","timestamp"]
		search_field = ["Title","Content"]
		class  Meta:
			model = Post
				

admin.site.register(Post,PostModelAdmin)