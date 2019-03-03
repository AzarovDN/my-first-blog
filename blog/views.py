from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    # posts = Post
    # template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form = PostForm
    fields = ['title', 'text']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form = PostForm
    fields = ['title', 'text']
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('post_detail', pk=post.pk)
