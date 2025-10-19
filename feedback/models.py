from django.db import models

from django.db import models

class Feedback(models.Model):
    name = models.CharField('Имя', max_length=60)
    email = models.EmailField('Email')
    message = models.TextField('Сообщение', max_length=1000)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"{self.name}: {self.message[:30]}"
