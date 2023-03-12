from django.db import models



class Commant(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="Comand_logo/", blank=True, null=True)

class Match_time(models.Model):
    first_command = models.ForeignKey(Commant, on_delete=models.CASCADE, related_name="team1")
    second_command = models.ForeignKey(Commant, on_delete=models.CASCADE, related_name="team2")
    date = models.DateTimeField()


class Media(models.Model):
    photo = models.ImageField(blank=True, null=True)
    video = models.FileField(upload_to="files/%Y/%m/%d")
    date = models.CharField(max_length=255)
    first_command_name = models.ForeignKey(Commant, on_delete=models.CASCADE,  related_name="teams1")
    second_command_name = models.ForeignKey(Commant, on_delete=models.CASCADE, related_name="teams2")
    what_account = models.CharField(max_length=255)


class News(models.Model):
    photo = models.ImageField(upload_to='news/', blank=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()

class Other_forms(models.Model):
    color = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    photo_T_short = models.ImageField(upload_to='T-short/', blank=True, null=True)
    purchase = models.ImageField(upload_to='purchase/', blank=True, null=True)
    cup = models.ImageField(upload_to='cup/', blank=True, null=True)
    command = models.ForeignKey(Commant, on_delete=models.CASCADE)


class Team_jersey(models.Model):
    Choose_the_form = models.ImageField(blank=True, null=True)
    other_forms = models.ForeignKey(Other_forms, on_delete=models.CASCADE)

class Quarter(models.Model):
    quarter_number = models.CharField(max_length=255)
    first_command = models.ForeignKey(Commant, on_delete=models.CASCADE,  related_name="teames1")
    second_command = models.ForeignKey(Commant, on_delete=models.CASCADE, related_name="teames2")

class Statistic(models.Model):
    match = models.ForeignKey(Match_time, on_delete=models.CASCADE)


class Info_about_player(models.Model):
    photo = models.ImageField(upload_to="players-phot/", blank=True, null=True)
    number = models.IntegerField()
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    games_played = models.IntegerField()
    minuts_played = models.IntegerField()
    start = models.IntegerField()
    sub_off = models.IntegerField()

class About_academy(models.Model):
    photo = models.ImageField(upload_to="about-academy/", blank=True, null=True)
    text = models.TextField()
    name = models.CharField(max_length=255)

class Info(models.Model):
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)

class Social_media(models.Model):
    logo = models.ImageField(upload_to='Social_media/', blank=True, null=True)
    url = models.URLField()


class Main_pagea(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    description = models.CharField(max_length=255)



