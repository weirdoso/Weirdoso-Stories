from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BookPost, Comment, Subscribers
from .forms import BookPostForm, EditBookForm, CommentForm, SubscribersForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    bookpost = get_object_or_404(BookPost, id=request.POST.get('bookpost_id'))
    liked = False
    if bookpost.likes.filter(id=request.user.id).exists():
        bookpost.likes.remove(request.user)
        liked = False
    else:
        bookpost.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('book-detail', args=[str(pk)]))


class HomeView(ListView):
    model = BookPost
    template_name = 'home.html'


class BookDetailView(DetailView):
    model = BookPost
    template_name = 'book_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BookDetailView, self).get_context_data()
        new = get_object_or_404(BookPost, id=self.kwargs['pk'])
        total_likes = new.total_likes()

        liked = False
        if new.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddBookPostView(CreateView):
    model = BookPost
    template_name = 'add_bookpost.html'
    # fields = ('title', 'body')
    form_class = BookPostForm
    success_url = reverse_lazy('home')


class AddSubscriberView(CreateView):
    model = Subscribers
    template_name = 'add_subscribers.html'
    # fields = ('title', 'body')
    form_class = SubscribersForm
    success_url = reverse_lazy('home')


class SubscribersView(ListView):
    model = Subscribers
    template_name = 'subscribers.html'


def terms(request):
    return render(request, 'terms.html', {})


class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    ordering = ['-id']
    # fields = ('title', 'body')
    form_class = CommentForm

    def form_valid(self, form):  # Saving form under the right user
        form.instance.bookpost_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')


class ReadingListsView(ListView):
    model = BookPost
    template_name = 'reading_lists.html'
    ordering = ['-id']


class UpdateBookPostView(UpdateView):
    model = BookPost
    form_class = EditBookForm
    template_name = 'update_bookpost.html'
    #fields = ['title', 'body']


class DeleteBookPostView(DeleteView):
    model = BookPost
    template_name = 'delete_bookpost.html'
    success_url = reverse_lazy('home')

