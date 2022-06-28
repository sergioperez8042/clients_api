import json
from multiprocessing.connection import Client
from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from .models import Clients
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class ClientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0):
        if (id>0):
            clients = list(Clients.objects.filter(id=id).values())
            if(len(clients)>0):
                client = clients[0]
                datos = {'message':"Success," , 'clients':client}
            else:
                datos = {'message':"Client not found..."}
            return JsonResponse(datos)
            
        else:
            clients = list(Clients.objects.values())
            if len(clients) > 0:
                datos = {'message':"success", 'clients': clients}
            else:
                datos={'message':"Clients no found..."}
            return JsonResponse(datos)
           
        
    
    def post(self,request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Clients.objects.create(name=jd['name'], price=jd['price'])
        datos = {'message':"success"}
        return JsonResponse(datos)

    
    def put(self,request,id):
        jd = json.loads(request.body)
        clients = list(Clients.objects.filter(id=id).values())
        if len(clients) > 0:
            client = Clients.objects.get(id=id)
            client.name = jd['name'],
            client.price = jd['price']
            client.save()
            datos = {'message':"success"}
        else:
            datos = {'message':"Client not found..."}
            
        return JsonResponse(datos)
    
    
    def delete(self,request,id):
        clients = list(Clients.objects.filter(id=id).values())
        if len(clients) > 0:
            Clients.objects.filter(id=id).delete()
            datos = {'message':"success"}
            
        else:
            datos = {'message':"Client not found..."}
        return JsonResponse(datos)    
        
