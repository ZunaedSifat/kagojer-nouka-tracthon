from collections import OrderedDict
from datetime import datetime, timedelta, date

from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Keyword, Content


@api_view(http_method_names=['GET'])
def trending_keywords(request):

    period = request.GET.get('period')
    count = request.GET.get('count')

    keywords = Keyword.objects.all()
    end = date.today()

    if period == 'days':
        start = end - timedelta(days=int(count))
        keywords = keywords.filter(content__upload_date__gte=start, content__upload_date__lte=end)
    elif period == 'weeks':
        start = end - timedelta(weeks=int(count))
        keywords = keywords.filter(content__upload_date__gte=start, content__upload_date__lte=end)
    else:
        # all-time
        pass

    keywords = keywords.values('word').annotate(count=Count('word')).order_by('-count')

    return Response(keywords)


@api_view(http_method_names=['GET'])
def fake_data(request):

    data = request.GET.copy()
    model = data.pop('model', None)[0]
    count = data.pop('count', 0)[0]

    data = {key: value for key, value in data.items()}

    obj = globals().get(model)
    if obj and hasattr(obj, 'generate_fake') and callable(getattr(obj, 'generate_fake')):
        for _ in range(int(count)):
            obj.generate_fake(**data)
        return Response(f'Generated {count} {model}(s)')
    else:
        raise ValueError('Model Does Not Exist')


@api_view(http_method_names=['GET'])
def trending_keyword_history(request):

    word = request.GET.get('word')

    words = list(Keyword.objects.filter(word=word).values('content__upload_date')
                 .annotate(count=Count('content__upload_date')).order_by('content__upload_date'))
    return Response(words)


@api_view(http_method_names=['GET'])
def trending_keyword_top(request):

    count = request.GET.get('count', 5)

    words = list(Keyword.objects.values('word').annotate(count=Count('word')).order_by('-count')[:int(count)])

    results = OrderedDict()

    for w in words:
        results[w['word']] = list(Keyword.objects.filter(word=w['word']).values('content__upload_date')
                          .annotate(count=Count('content__upload_date')).order_by('content__upload_date'))

    return Response(results)
