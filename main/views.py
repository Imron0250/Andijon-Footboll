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
    banner = News.objects.filter(is_banner=True)
    banner_ser = NewsSerializer(banner, many=True)
    match = Match_time.objects.all()
    match_ser = Match_timeSerializer(match, many=True)
    data = {
        "banner": banner_ser.data,
        "match_time": match_ser.data
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
    info_about_player = Player.objects.all()
    info_about_player_ser = PlayerSerializer(info_about_player, many=True)
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


@api_view(['GET'])
def get_shop(request):
    product = Shop.objects.all()
    product_ser = ShopSerializer(product, many=True)
    data = {
        "product": product_ser.data
    }
    return Response(data)











