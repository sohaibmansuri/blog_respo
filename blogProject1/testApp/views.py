from django.shortcuts import render,get_object_or_404
from testApp.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag
# Create your views here.
def post_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'testApp/list_display.html',{'post_list':post_list,'tag':tag})

from testApp import forms
def post_view_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day,status='published')
    comments=post.comment.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=forms.comment_form(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=forms.comment_form()
    return render(request,'testApp/list_detail.html',{'post':post,'comments':comments,'form':form,'csubmit':csubmit})
