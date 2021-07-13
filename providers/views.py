from django.db.models.aggregates import Min
from providers.serializeres import ProviderSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from providers.models import Provider
from django.conf import settings
from django.forms.models import model_to_dict


# Create your views here.
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def list(self, request):
        start = int(request.query_params["start"])
        limit = int(request.query_params["limit"])
        count = int(Provider.objects.count())
        min_id = Provider.objects.aggregate(Min("id"))
        start = start if start else min_id
        batch_size = limit if limit else settings.BATCH_SIZE
        batch = {"start": start, "limit": batch_size, "data": []}
        if count > batch_size:
            for data in Provider.objects.filter(id__gte=start)[:limit]:
                if len(batch["data"]) <= limit:
                    batch["data"].append(model_to_dict(data))
                else:
                    break
        else:
            batch["data"].append([model_to_dict(data) for data in self.queryset])
        return JsonResponse(batch)
