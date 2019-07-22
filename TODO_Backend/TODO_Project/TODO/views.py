from rest_framework import generics

from .models import TODO
from .serializers import TODOSerializer

# Create your views here.
class ListTODO(generics.ListCreateAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class DetailsTODO(generics.RetrieveUpdateDestroyAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
