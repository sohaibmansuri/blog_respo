from django.contrib import admin
from testApp.models import Post,Comments
# Register your models here.
class Post_Admin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','body','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','body')
    raw_id_fields=('author',)

class comment_admin(admin.ModelAdmin):
    list_display=['name','email','body','post','created','updated','active']

admin.site.register(Post,Post_Admin)
admin.site.register(Comments,comment_admin)
