from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import markdown2
import requests
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'object_list': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    md_text = markdown2.markdown(post.body, extras=["fenced-code-blocks"])
    return render(request, 'blog/blog_detail.html', {'object': post, 'md_text': md_text})


def serialize_text(request, slug):
    post = get_object_or_404(Post, slug=slug)
    md_text = post.body
    response = HttpResponse(md_text, content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename="{}.md"'.format(slug)

    return response


def update_text(request, slug):
    if request.user.is_authenticated():
        user_name = "{}/".format(request.user.blogauthor.github_name)
    else:
        return redirect('dynamicblog:post_detail', slug=slug)
    post = get_object_or_404(Post, slug=slug)
    base_url = 'https://raw.githubusercontent.com/'
    path = 'howto/master/blog/posts/'
    file = "{}".format(slug)
    file_ending = ".md"
    url = base_url + user_name + path + file + file_ending
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
    post.body = decoded_content
    post.save()

    return redirect('dynamicblog:post_detail', slug=slug)
