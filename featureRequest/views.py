from django.shortcuts import render
from .forms import PostForm
from .models import Post
import sys
import json
from django.http import HttpResponse

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
    
def get_details(request):
    if request.method=="GET":       
        d=request.GET['post_id']
        client1=d.split('_')[0]
        client_p=d.split('_')[1]       
        all_posts=Post.objects.filter(client=client1.split(' ')[1])       
        for each_post in all_posts:            
            if int(each_post.client_priority)==int(client_p):                                
                return HttpResponse(json.dumps(get_dict(each_post)),content_type="application/json")
        return HttpResponse(json.dumps({"val":0}),content_type="application/json")        
                
def get_dict(data):
    temp={}
    prod_area1={'P':'Policies','B':'Billing','C':'Claims','R':'Reports'}
    temp['title'] = data.title
    temp['client'] = 'Client '+data.client
    temp['client_priority']=data.client_priority
    temp['description'] = data.description
    temp['target_date']=data.target_date.strftime("%Y-%m-%d")
    temp['ticket_url']=data.ticket_url
    temp['prod_area']=prod_area1[data.prod_area]
    temp['val']=1
    return temp 
        
            
