from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.question.views import CategoryListView, QuestionCreateView, QuestionListView, QuestionUpdateView, \
    QuestionDeleteView, AnswerViewSet

router = DefaultRouter()
router.register('answers', AnswerViewSet)

urlpatterns = [
    # 1
    # path('categories-list/', category_list)
    # 2
    # path('categories-list/', CategoryView.as_view()),
    # 3
    path('categories-list/', CategoryListView.as_view()),
    path('question-create/', QuestionCreateView.as_view()),
    path('questions-list/', QuestionListView.as_view()),
    path('question-update/<int:pk>/', QuestionUpdateView.as_view()),
    path('question-delete/<int:pk>/', QuestionDeleteView.as_view()),
    path('', include(router.urls)),
]
