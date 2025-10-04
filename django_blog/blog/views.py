# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

from .models import Post, Comment
from .forms import (
    UserRegistrationForm, UserUpdateForm, ProfileForm,
    PostForm, CommentForm
)


# -------------------
# Authentication
# -------------------
def register_view(request):
    if request.user.is_authenticated:
        return redirect('blog:profile')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('blog:profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'


@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('blog:profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        u_form = UserUpdateForm(instance=user)
        p_form = ProfileForm(instance=user.profile)
    return render(request, 'blog/profile.html', {'u_form': u_form, 'p_form': p_form})


# -------------------
# Post CRUD
# -------------------
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        # return published posts only for public listing
        return Post.objects.filter(status='published')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.status == 'draft' and self.request.user != obj.author:
            raise Http404("Post not found")
        return obj

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['comments'] = self.object.comments.all()
        ctx['comment_form'] = CommentForm()
        return ctx


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    extra_context = {'action': 'create'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.pk})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    extra_context = {'action': 'update'}

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# -------------------
# Comment CRUD
# -------------------
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        # ensure post exists
        self.post = get_object_or_404(Post, pk=kwargs.get('post_pk'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.post.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
