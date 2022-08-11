from django.shortcuts import render
from django.views.generic import View
from .models import blog

class blogHome(View):
    def get(self, request, *args, **kwargs):
        blogs = blog.objects.all()
        context = {
            'blogs' : blogs,
        }
        return render(request, 'blog/blogHome.html', context)

