from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CO2Data
from .serializers import Co2DataSerializer


# API: データ登録と取得
class Co2DataListCreateView(generics.ListCreateAPIView):
    queryset = CO2Data.objects.all().order_by("-timestamp")  # 最新データを先頭に
    serializer_class = Co2DataSerializer


# Webアプリ: データ表示
@login_required
def co2_data_table(request):
    data = CO2Data.objects.all().order_by("-timestamp")  # 最新データを先頭に
    return render(request, "co2data/table.html", {"data": data})
