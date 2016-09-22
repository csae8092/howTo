from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import markdown2
import requests
from .models import Post, Book


@login_required
def books(request, slug):
    book = get_object_or_404(Book, slug=slug)
    posts = Post.objects.filter(book=book)
    context = {}
    context["object_list"] = posts
    context["book"] = book
    return render(request, 'blog/blog_list.html', context)


@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'object_list': posts})


@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    md_text = markdown2.markdown(post.body, extras=["fenced-code-blocks"])
    return render(request, 'blog/blog_detail.html', {'object': post, 'md_text': md_text})


@login_required
def serialize_text(request, slug):
    post = get_object_or_404(Post, slug=slug)
    md_text = post.body
    response = HttpResponse(md_text, content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename="{}.md"'.format(slug)

    return response


@login_required
def update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        url = request.POST.get('url', '')
        with requests.Session() as s:
            try:
                r = s.get(url)
                if r.status_code == requests.codes.ok:
                    print("past eh ois", r.status_code)
                    decoded_content = r.content.decode('utf-8')
                    post.body = decoded_content
                    post.save()
                    md_text = markdown2.markdown(post.body, extras=["fenced-code-blocks"])
                    return render(
                        request, 'blog/blog_detail.html',
                        {'object': post, 'md_text': md_text, 'updated': 'Text successfully updated'}
                    )
                else:
                    print("oho", r.status_code)
                    return render(
                        request, 'blog/blog_detail.html',
                        {'object': post, 'md_text': md_text, 'error': r.status_code}
                    )
            except:
                print("soemthing is wrong", url)
                md_text = markdown2.markdown(post.body, extras=["fenced-code-blocks"])
                return render(
                    request, 'blog/blog_detail.html',
                    {'object': post, 'md_text': md_text, 'error': 'something went wrong'})
    else:
        md_text = markdown2.markdown(post.body, extras=["fenced-code-blocks"])
        return render(request, 'blog/blog_detail.html', {'object': post, 'md_text': md_text})
