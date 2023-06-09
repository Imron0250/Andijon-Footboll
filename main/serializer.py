from rest_framework.serializers import ModelSerializer
from .models import *


class CommantSerializer(ModelSerializer):
    class Meta:
        model = Commant
        fields = "__all__"

class Match_timeSerializer(ModelSerializer):
    class Meta:
        model = Match_time
        fields = "__all__"

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class Team_jerseySerializer(ModelSerializer):
    class Meta:
        model = Team_jersey
        fields = "__all__"


class QuarterSerializer(ModelSerializer):
    class Meta:
        model = Quarter
        fields = "__all__"

        
class StatisticSerializer(ModelSerializer):
    class Meta:
        model = Statistic
        fields = "__all__"

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"

class About_academySerializer(ModelSerializer):
    class Meta:
        model = About_academy
        fields = "__all__"

class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class Social_mediaSerializer(ModelSerializer):
    class Meta:
        model = Social_media
        fields = "__all__"
