from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from .models import (
    Video,
    VideoViewed,
)
from .serializers import (
    VideoSerializer,
    VideoViewedSerializer,
)

import datetime
import collections
import random


class TenSetPag(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class VideoListView(ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        lst_tup_pop = []
        lst_pop = []
        Vid = collections.namedtuple('Video', 'id pop')
        today = datetime.date.today()
        this_month = today.month
        pop = 0
        lks = 10
        dlks = 5
        comm = 1
        tdy = 100
        qs = Video.objects.filter(publicado__date__month=datetime.date.today().month)
        qsd = qs.filter(publicado__date__day=datetime.date.today().day).order_by('-id')[:5]
        if qsd is not None:
            for data in qsd:
                pop = data.likes.all().count() * lks
                pop = pop - (data.dislikes.all().count()*dlks)
                pop = pop + (data.comments.all().count()*comm)
                if data.publicado.date().day == datetime.date.today().day:
                    pop = pop + tdy
                vid = Vid(id=data.id, pop=pop)
                lst_tup_pop.append(vid)
            lst_tup_pop.sort(key=lambda x:x.pop, reverse=True)
            for data in lst_tup_pop:
                lst_pop.append(data[0])
            st = set(lst_pop)
            if len(st) == 1:
                return qsd.order_by('?')
            else:
                srtd_qsd = sorted(qsd, key=lambda x: lst_pop.index(x.id))

                return srtd_qsd
        else:
            for data in qs:
                pop = data.likes.all().count() * lks
                pop = pop - (data.dislikes.all().count()*dlks)
                pop = pop + (data.comments.all().count()*comm)
                vid = Vid(id=data.id, pop=pop)
                lst_tup_pop.append(vid)
            lst_tup_pop.sort(key=lambda x:x.pop, reverse=True)
            for data in lst_tup_pop:
                lst_pop.append(data[0])
            st = set(lst_pop)
            if len(st) == 1:
                return qs.order_by('?')
            else:
                srtd_qs = sorted(qs, key=lambda x: lst_pop.index(x.id))
                return srtd_qs
        if not qs and not qsd:
            return Video.objects.all().order_by('?')[:5]


class VideoRU(RetrieveUpdateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = "id"


class VideoHistoryListView(ListAPIView):
    serializer_class = VideoViewedSerializer
    pagination_class = TenSetPag
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        return VideoViewed.objects.filter(user=user).order_by('-viewed_at',)
