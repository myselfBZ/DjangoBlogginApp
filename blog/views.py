from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, CommentForm


@login_required
def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {"posts":posts})


@login_required
def blog(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    comment_form = CommentForm()
    return render(request, 'post.html', {"post":post, "comments":comments, "comment_form":comment_form})


@login_required
def create_blog(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    return render(request, 'createPost.html', {"form":form})

@login_required
def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f"http://127.0.0.1:8000/post/{post.pk}")
    
    form = PostForm(instance=post)

    return render(request, "updatePost.html", {"form":form})

@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect(f"http://127.0.0.1:8000/posts/")
    return render(request, 'deleteConfirm.html', {"post":post})

@login_required
def write_comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(f"http://127.0.0.1:8000/post/{post.pk}")
    
