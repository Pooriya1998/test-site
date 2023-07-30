from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status','login_require', 'published_date', 'created_date')
    list_filter = ('status', 'author', 'category')
    search_fields = ('title', 'content')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'updated_date', 'created_date')
    list_filter = ('post', 'approved')
    search_fields = ('name', 'post')


admin.site.register(Category)
