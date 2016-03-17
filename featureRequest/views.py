from django.shortcuts import render
from .forms import PostForm
from .models import Post

# Create your views here.

def post_list(request):
    posts=Post.objects.all().order_by('client_priority','target_date')
    final=[]
    prod_area1={'P':'Policies','B':'Billing','C':'Claims','R':'Reports'}
    for each_post in posts:
        temp=each_post
        temp.client='Client '+each_post.client            
        temp.prod_area=prod_area1[temp.prod_area]
        temp.description=temp.description[:20]               
    return render(request,'featureRequest/post_list.html',{'posts':posts})
    

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            cur=post.client_priority
            for each_post in Post.objects.filter(client=post.client).order_by('client_priority'):
                if each_post.client_priority==cur and post.client==each_post.client:
                    each_post.client_priority=each_post.client_priority+1
                    cur=cur+1
                    each_post.save()                               
            post.save()            
    else:
        form = PostForm()
    return render(request, 'featureRequest/post_edit.html', {'form': form}) 
