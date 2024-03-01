from django.db import models


class Pinner(models.Model):
    # user posting pin
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255, null=True, blank=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pin(models.Model):
    # object that the Pinner posts
    id = models.IntegerField(primary_key=True)
    pinner_id = models.ForeignKey(Pinner, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    # pictures in pin
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.url


class Board(models.Model):
    # pin feed
    id = models.IntegerField(primary_key=True)
    pinner_id = models.ForeignKey(Pinner, on_delete=models.CASCADE, null=True, blank=True)


# ----------------------non-functional block-----------------------#

class Pin_in_board(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    pin_id = models.ForeignKey(Pin, on_delete=models.CASCADE)


class Image_in_pin(models.Model):
    pin_id = models.ForeignKey(Pin, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
