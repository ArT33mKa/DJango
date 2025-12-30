from django.db import models


class Genre(models.Model):
    title = models.CharField()

    def __str__(self):
        return f"{self.title}"

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    memory_required = models.DecimalField(max_digits=5, decimal_places=2)
    processor_required = models.CharField()
    videocard_required = models.CharField()
    count_installs = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True, related_name='games')

    def __str__(self):
        return f"{self.title}, {self.description}"


class Comment(models.Model):
    text = models.TextField()
    nickname = models.CharField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return f"{self.nickname}: {self.text}"