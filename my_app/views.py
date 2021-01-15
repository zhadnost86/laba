from django.shortcuts import render
from .models import Post
from .forms import PostForm

def posts_list(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'my_app/posts_list.html', {'posts': posts})

def post_new(request):
	form = PostForm()
	if form.is_valid():
		post = form.save(commit=False)
		post.author = request.user
		post.created_date = timezone.now()
		post.save()
		return redirect('posts_list')
	else: 
		return render(request, 'my_app/post_edit.html',{'form': form})

	
