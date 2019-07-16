from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from blog.models import Post
from django.urls import reverse

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # return redirect(reverse('blog:detail', kwargs={'pk': post.pk}))
            return redirect(post.get_absolute_url())
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list,
            }
            return render(request, 'blog/detail.html', context=context)

    return redirect(post.get_absolute_url())

