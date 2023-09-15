from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from tickets.models import Ticket, Category, Priority, State
from tickets.serializers import TicketSerializer, CategorySerializer, StateSerializer, UsersSerializer, PrioritySerializer, SignupSerializer, UsersEditSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


class TicketView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of the tickets.
        """
        tickets = Ticket.objects#.filter(author=request.user)
        serializer = TicketSerializer(tickets, many=True)
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
            'subtasks': request.data.get('subtasks'),
            'assigned': request.data.get('assigned'),
            'date': request.data.get('date'),
            'author': request.user.id
        }
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, ticket_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            return None

    def put(self, request, ticket_id, *args, **kwargs):
        '''
        Updates the ticket item with given ticket_id if exists
        '''
        ticket_instance = self.get_object(ticket_id)
        if not ticket_instance:
            return Response(
                {"res": "Object with ticket id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            "title": request.data.get('title'),
            "description": request.data.get('description'),
            "maintask": request.data.get('maintask'),
            "subtasks": request.data.get('subtasks'),
            "assigned": request.data.get('assigned'),
            "date": request.data.get('date'),
            "category": request.data.get('category'),
            "priority": request.data.get('priority'),
            "status": request.data.get('status')
        }
        serializer = TicketSerializer(
            instance=ticket_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
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
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'user_id': user.pk,
                'token': token.key,
                'email': user.email
                })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class signupview(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer

class adduserview(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer

class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):  # , *args, **kwargs):
        data = {
            'username': request.data.get('username'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'email': request.data.get('email')
        }
        serializer = UsersSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        #user = serializer
        token, created = Token.objects.get_or_create(user=serializer) # user=user
        return Response({
            'token': token.key,
            'user_id': serializer.pk, #user.pk
            'email': serializer.email #user.email
        })

class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, user_id):
        '''
        Helper method to get the object with given user_id
        '''
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def put(self, request, user_id, *args, **kwargs):
        '''
        Updates the ticket item with given user_id if exists
        '''
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "User with ticket id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            #"id": request.data.get('id'),
            "username": request.data.get('username'),
            "first_name": request.data.get('first_name'),
            "last_name": request.data.get('last_name'),
            "email": request.data.get('email')
        }
        serializer = UsersEditSerializer(
            instance=user_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)