from django.shortcuts import render

from .models import Blog, Category, Slayder

def blog(request):
    slayder = Slayder.objects.all()
    category = Category.objects.all()
    blog = Blog.objects.order_by('created_at')
    context = {
        'slayder_list': slayder,
        'category_list':category,
        'blog_list': blog
    }
    return render(request, 'blog.html', context)
