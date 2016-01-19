from djangular_polls.serializers import PollSerializer,PollItemSerializer
from djangular_polls.models import Poll,PollItem
from rest_framework import generics,mixins

class PollCollection(generics.ListCreateAPIView):
    queryset=Poll.objects.all()
    serializer_class=PollSerializer

    # def get(self,request):
    #     return self.list(request)
    #
    # def post(self,request):
    #     return self.create(request)

class PollMember(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset=Poll.objects.all()
    serializer_class=PollSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class PollItemCollection(generics.ListCreateAPIView):
    queryset=PollItem.objects.all()
    serializer_class=PollItemSerializer

    # def get(self,request):
    #     return self.list(request)
    #
    # def post(self,request):
    #     return self.create(request)

class PollItemMember(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset=PollItem.objects.all()
    serializer_class=PollItemSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)