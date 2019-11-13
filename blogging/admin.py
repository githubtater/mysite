from django.contrib import admin

from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    """
    Class for displaying categories inline when making new posts.
    """
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    """
    Class to add CategoryInline to Posts
    """
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    """
    Class for adding categories to
    """
    inlines = [CategoryInline, ]
    exclude = ('post', )


# and a new admin registration
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)