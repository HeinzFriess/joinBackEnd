from django.contrib import admin
from django.urls import path
from tickets.views import TicketView, loginview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginview.as_view()),
    path('todos/', TicketView.as_view()),
    #path('todos/<int:todo_id>/', TodoDetailView.as_view()),
]
