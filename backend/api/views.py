from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer,RegisterSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.

class TransactionListCreateView(generics.ListCreateAPIView):
    # queryset = Transaction.objects.all()  # pylint: disable=no-member
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Transaction.objects.all()  # pylint: disable=no-member
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):  
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })