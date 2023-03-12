from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


@api_view(['GET'])
def get_info(request):
    info = Info.objects.last()
    info_ser = InfoSerializer(info)
    media = Social_media.objects.all()
    media_ser = Social_mediaSerializer(media, many=True)
    data = {
        "info" : info_ser.data,
        "media_url" : media_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_main_page(request):
    main_page = Main_pagea.objects.last()
    main_page_ser = Main_pageSerializer(main_page)
    match_time = Match_time.objects.all()
    match_time_ser = Match_timeSerializer(match_time, many=True)
    data = {
        "main_page": main_page_ser.data,
        "match_time": match_time_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_news(request):
    news = News.objects.all()
    news_ser = NewsSerializer(news, many=True)
    data = {
        "news": news_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_media(request):
    media = Media.objects.all()
    media_ser = MediaSerializer(media, many=True)
    data = {
        "media": media_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_team_joursey(request):
    team_joursey = Team_jersey.objects.all()
    team_joursey_ser = Team_jerseySerializer(team_joursey, many=True)
    other_forms = Other_forms.objects.all()
    other_forms_ser = Other_formsSerializer(other_forms, many=True)
    data = {
        "team_joursey": team_joursey_ser.data,
        "other_forms": other_forms_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_statistics(request):
    statistic = Statistic.objects.last()
    statistic_ser = StatisticSerializer(statistic)
    quarter = Quarter.objects.all()
    quarter_ser = QuarterSerializer(quarter, many=True)
    data = {
        "statistic": statistic_ser.data,
        "quarter": quarter_ser.data
    }
    return Response(data)   

@api_view(["GET"])
def get_info_about_players(request):
    info_about_player = Info_about_player.objects.all()
    info_about_player_ser = Info_about_playerSerializer(info_about_player, many=True)
    data = {
        "info_about_players": info_about_player_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_about_academy(request):
    about_academy = About_academy.objects.last()
    about_academy_ser = About_academySerializer(about_academy)
    data = {
        "about_academy": about_academy_ser.data
    }
    return Response(data)