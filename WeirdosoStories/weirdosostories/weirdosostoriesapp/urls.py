from django.urls import path
from .views import HomeView, BookDetailView, AddBookPostView, ReadingListsView, UpdateBookPostView, DeleteBookPostView, LikeView, AddCommentView, SubscribersView, AddSubscriberView
from . import views

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('weirdosostories/book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('weirdosostories/add_bookpost/', AddBookPostView.as_view(), name='add_bookpost'),
    path('weirdosostories/reading_lists/', ReadingListsView.as_view(), name='reading_lists'),
    path('weirdosostories/book/edit/<int:pk>', UpdateBookPostView.as_view(), name='update_bookpost'),
    path('weirdosostories/book/edit/<int:pk>/delete', DeleteBookPostView.as_view(), name='delete_bookpost'),
    path('weirdosostories/like/<int:pk>', LikeView, name='like_bookpost'),
    path('weirdosostories/book/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('weirdosostories/subscribers', SubscribersView.as_view(), name="subscribers"),
    path('weirdosostories/terms-and-policy', views.terms, name="terms"),
    path('weirdosostories/subscription/', AddSubscriberView.as_view(), name='add_subscribers'),
]
