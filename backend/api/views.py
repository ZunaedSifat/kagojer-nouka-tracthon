from datetime import datetime, timedelta

from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Keyword


@api_view(http_method_names=['GET'])
def trending_keywords(request):

    period = request.GET.get('period')
    count = request.GET.get('count')

    keywords = Keyword.objects.all()
    end = datetime.now()

    if period == 'days':
        start = end - timedelta(days=int(count))
        keywords = keywords.filter(content__upload_datetime__gte=start, content__upload_datetime__lte=end)
    elif period == 'weeks':
        start = end - timedelta(weeks=int(count))
        keywords = keywords.filter(content__upload_datetime__gte=start, content__upload_datetime__lte=end)
    else:
        # all-time
        pass

    keywords = keywords.values('word').annotate(count=Count('word')).order_by('-count')

    return Response(keywords)
