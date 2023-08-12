from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=60)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    is_auction = models.BooleanField('уместен ли торг', help_text='Отметьте, если торг по объявлению уместен.')
    updated_at = models.DateTimeField('дата обновления', auto_now=True)
    created_at = models.DateTimeField('дата публикации', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='advertisements/')

    @admin.display(description='Дата публикации')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                "<span style='color: green; font-weight: bold'>Сегодня в {}<span/>", created_time
            )
        return self.created_at.strftime('%d.%m.%Y - %H:%M')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                "<span style='color: blue; font-weight: bold'>Сегодня в {}<span/>", updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y - %H:%M')

    # @admin.display(description='Изображение')
    # def image_adv(self):
    #     if self.image:
    #         return format_html('<img src="{}" width="50" height="50"/>', self.image)


# новый вывод
    def __str__(self):
        return f'Advertisement(id={self.pk}, title={self.title}, price={self.price})'

# новое имя
    class Meta:
        db_table = 'advertisements'


