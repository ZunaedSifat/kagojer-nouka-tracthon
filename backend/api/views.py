from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Keyword


@api_view(http_method_names=['GET'])
def trending_keywords(request):

    keywords = Keyword.objects.values('word').annotate(count=Count('word')).order_by('-count')

    return Response(keywords)