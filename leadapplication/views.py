from django.shortcuts import render
from django.db.models import Count

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from leadapplication.models import Lead
from leadapplication.serializers import LeadSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class LeadListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    queryset = Lead.objects.all()

    serializer_class = LeadSerializer


class LeadUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    queryset = Lead.objects.all()

    serializer_class = LeadSerializer

class LeadSummaryView(APIView):

    def get(self, request, *args, **kwargs):

        summary = Lead.objects.values("status").annotate(total = Count('status'))

        total_count = Lead.objects.all().count()

        data = {
            "total_count" : total_count,
            "summary" : summary
        }

        return Response(data=summary)






