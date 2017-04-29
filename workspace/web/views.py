from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Options, Blog
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your views here.


def index(request):
    latest_option_list = Options.objects.order_by('-pub_date')[:5]
    context = {'latest_option_list': latest_option_list}
    return render(request, 'web/index.html', context)
    
def bloglist(request):
    blog_list = Blog.objects.order_by('-pub_date')
    context = {'blog_list' : blog_list}
    return render(request, 'web/blogs.html', context)
    
def blog(request, blog_id):
    blaugh = get_object_or_404(Blog, pk=blog_id)
    context = {'blaugh': blaugh}
    return render(request, 'web/blog.html', context)
    
def new(request):
    b = Blog(blog_text="", pub_date=timezone.now())
    try:
        
        b.blog_text = request.POST['body']
        
    except (KeyError, Blog.DoesNotExist):
        return render(request, 'web/blankblog.html', {
            'b': b,
            
        })
    else:
        
        b.save()
        return HttpResponseRedirect(reverse('web:index'))