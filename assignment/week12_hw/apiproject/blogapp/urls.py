from django.urls import path
from .views import BlogDetail, BlogList, CommentList, CommentView

urlpatterns = [
    path('blog/', BlogList.as_view()),
    path('blog/<int:pk>', BlogDetail.as_view()),
    path('comment/', CommentList.as_view()),
    path('comment/<int:pk>', CommentView.as_view()),
]