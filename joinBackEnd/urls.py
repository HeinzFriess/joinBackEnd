from django.contrib import admin
from django.urls import path
from tickets.views import TicketView, loginview, PriorityView, CategoryView, StateView, UserView, TicketDetailView, signupview, UserDetailView, adduserview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginview.as_view()),
    path('signup/', signupview.as_view()),
    path('ticket/', TicketView.as_view()),
    path('ticket/<int:ticket_id>/', TicketDetailView.as_view()),
    path('priority/', PriorityView.as_view()),
    path('category/', CategoryView.as_view()),
    path('state/', StateView.as_view()),
    path('user/', UserView.as_view()),
    path('user/<int:user_id>/', UserDetailView.as_view()),
    path('adduser/', adduserview.as_view())
]
