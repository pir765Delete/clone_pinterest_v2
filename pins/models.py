from django.db import models
from django.db.models import ImageField


class Pinner(models.Model):
    # user posting pin
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255, null=True, blank=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<name>/<filename>
    return 'images/' + 'user_{0}/{1}'.format(instance.pinner_id, filename)


class Pin(models.Model):
    # object that the Pinner posts
    id = models.IntegerField(primary_key=True)
    pinner_id = models.ForeignKey(Pinner, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)
    image: ImageField = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Board(models.Model):
    # pin feed
    id = models.IntegerField(primary_key=True)
    pinner_id = models.ForeignKey(Pinner, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Панель постов'


# ----------------------non-functional block-----------------------#

class Pin_in_board(models.Model):
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    pin_id = models.ForeignKey(Pin, on_delete=models.CASCADE)
