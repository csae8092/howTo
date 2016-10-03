import markdown2
import requests
import lxml.etree as ET
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.templatetags.staticfiles import static
from haystack.query import SearchQuerySet
from django.http import HttpResponse
from .models import Post, Book


def search_posts(request):
    context = {}
    try:
        groupname = request.user.groups.all()[0].name
        if groupname == 'ACDH-CORE':
            usergroups = ['ACDH-CORE', 'ACDH-EXTENDED', 'PUBLIC']
        elif groupname == 'ACDH-EXTENDED':
            usergroups = ['ACDH-EXTENDED', 'PUBLIC']
    except:
        usergroups = ['PUBLIC']
    if 'q' in request.GET:
        searchstring = request.GET.get('q', '')
        results = SearchQuerySet().filter(content=searchstring, audience__in=usergroups).load_all()
        total_results = results.count()
    else:
        searchstring = None
        total_results = None
        results = None
    context['searchstring'] = searchstring
    context['total_results'] = total_results
    context['results'] = results
    return render(request, 'blog/blog_search.html', context)


def filter_posts_by_usergroups(user):
    """filters posts matching its audience target"""
    try:
        group = user.groups.all()[0].name
        if group == 'ACDH-CORE':
            posts = Post.objects.all()
        elif group == 'ACDH-EXTENDED':
            posts = Post.objects.filter(audience__in=['ACDH-EXTENDED', 'PUBLIC'])
    except:
        posts = Post.objects.filter(audience='PUBLIC')
    return posts


def tei_to_html(url, tei):
    """fetches as stylesheet from the given url and transforms an
    xslt transformation on the given TEI-encoded text"""
    try:
        r = requests.get(url)
        xslt = ET.XSLT(ET.fromstring(r.text))
        xml = ET.fromstring(tei)
        html = xslt(xml)
        result = ET.tostring(html)
    except:
        result = "unfortunately something went wrong"
    return result


def books(request, slug):
    book = get_object_or_404(Book, slug=slug)
    userobject = request.user
    posts = filter_posts_by_usergroups(userobject).filter(book=book)
    # posts = Post.objects.filter(book=book)
    context = {}
    context["object_list"] = posts
    context["book"] = book
    return render(request, 'blog/blog_list.html', context)


def post_list(request):
    userobject = request.user
    posts = filter_posts_by_usergroups(userobject)
    return render(request, 'blog/blog_list.html', {'object_list': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {}
    prefix = 'https://' if request.is_secure() else 'http://'
    url = prefix + request.get_host() + static('blog/xslt/tei-to-html.xsl')
    if post.encoding == "markdown":
        md_text = markdown2.markdown(post.body, extras=["fenced-code-blocks"])
        tei_text = None
    else:
        md_text = None
        tei_text = tei_to_html(url, post.body)
    context['object'] = post
    context['md_text'] = md_text
    context['tei_text'] = tei_text
    return render(request, 'blog/blog_detail.html', context)


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
