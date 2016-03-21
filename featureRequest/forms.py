from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #forms fields
        fields = ('title','client','client_priority','description','target_date','ticket_url','prod_area')        
