from drf_spectacular.utils import extend_schema
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from rest_framework.views import APIView
from rest_framework.response import Response

from .helper import CatFact
from .swagger import user_cat_data_schema


class UserCatDataView(APIView):
    @extend_schema(**user_cat_data_schema)
    @method_decorator(ratelimit(key='ip', rate='50/h', method='GET', block=False))
    def get(self, request):
        if getattr(request, 'limited', False):
            return Response({
                'error': 'Too many requests.'
            }, status=429)
        cat_fact = CatFact()
        cat_fact.fetch_cat_fact()
        return Response(cat_fact.get_response())
