from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User

from tickets.models import Ticket, Category, Priority, State
from tickets.serializers import TicketSerializer, CategorySerializer, StateSerializer, PrioritySerializer, UsersSerializer

class TicketView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of the tickets.
        """
        todos = Ticket.objects.filter(author=request.user) 
        serializer = TicketSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the ticket with given data
        '''
        data = {
            'title': request.data.get('title'),
            'category': request.data.get('category'),
            'description': request.data.get('description'),
            'priority': request.data.get('priority'),
            'status': request.data.get('status'),
            'maintask': request.data.get('maintask'),
            'assigned': request.data.get('assigned'),
            'date': request.data.get('date'),
            'author' : request.user.id
        }
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of the Categories.
        """
        todos = Category.objects.all()  
        serializer = CategorySerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the Category with given data
        '''
        data = {
            'name': request.data.get('name')
        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriorityView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of the Priorities.
        """
        todos = Priority.objects.all() 
        serializer = PrioritySerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the Priority with given data
        '''
        data = {
            'name': request.data.get('name')
        }
        serializer = PrioritySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StateView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of the States.
        """
        todos = State.objects.all() 
        serializer = StateSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the Priority with given data
        '''
        data = {
            'name': request.data.get('name')
        }
        serializer = StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class loginview(ObtainAuthToken):
    
    def post(self, request): #, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                    context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
             'token': token.key,
             'user_id': user.pk,
             'email': user.email
            })
    
class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def get(self, request, format=None):
    #     """
    #     Return a list of all users.
    #     """
    #     usernames = [user.username for user in User.objects.all()]
    #     return Response(User.objects.all())
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        users = User.objects.all() 
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)