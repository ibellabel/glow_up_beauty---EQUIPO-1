import json
from django.views import View
from django.http import JsonResponse

from core.services import OrdenService
from tienda.models import Usuario


class CrearOrdenView(View):
    def post(self, request):
        data = json.loads(request.body)
        usuario = Usuario.objects.get(id=data["usuario_id"])
        service = OrdenService()
        orden = service.crear_orden(usuario, data["productos_ids"])
        return JsonResponse({"orden_id": orden.id, "estado": orden.estado})