from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
def about(request):
    return render(request, 'blog/about.html', {})
def maria(request):
    return render(request, 'blog/maria.html', {})
def home(request):
    return render(request, 'blog/home.html', {})
def bazowy(request):
    return render(request, 'blog/bazowy.html', {})
