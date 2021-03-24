from testApp.models import Post
from django import template
register=template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('testApp/latest.html')
def show_latest_post_show():
    latest_show=Post.objects.order_by('-publish')[:2]
    return {'latest_show':latest_show}

from django.db.models import Count
@register.assignment_tag
def most_commented():
    return Post.objects.annotate(total=Count('comment')).order_by('total')
