from django.contrib import admin
from import_export import resources, fields
from .models import Post


class PostResorce(resources.ModelResource):
    is_active = fields.Field()
    created = fields.Field()
    class Meta:
        model = Post
        fieds = ('id', 'title', 'description', 'is_active', 'created')
        export_order = ('id', 'description', 'is_active', 'title', 'created')

    def dehydrate_is_active(self, obj):
        if obj.is_active:
            return "yes"
        return "no"

    def dehydrate_created(self, obj):
        return obj.created.strftime("%d-%m-%Y %H:%M:%S")



admin.site.register(Post)

