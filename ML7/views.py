from ML7.book import Book
from .serializers import BookAuthSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class book_list(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAuthSerializer


class book_detail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAuthSerializer

@api_view(('GET',))
def root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format),
    })
