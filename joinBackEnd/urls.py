from django.contrib import admin
from django.urls import path
from tickets.views import TicketView, loginview, PriorityView, CategoryView, StateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginview.as_view()),
    path('ticket/', TicketView.as_view()),
    #path('todos/<int:todo_id>/', TodoDetailView.as_view()),
    path('priority/', PriorityView.as_view()),
    path('category/', CategoryView.as_view()),
    path('state/', StateView.as_view()),
]
