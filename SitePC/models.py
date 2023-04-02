from django.db import models
from django.urls import reverse

from accounts.models import User


class CPUs(models.Model):
    title = models.CharField(max_length=50, verbose_name="Наименование ЦПУ")
    socket = models.CharField(max_length=10, verbose_name="Сокет")
    count_core = models.IntegerField(verbose_name="Количество ядер")
    count_threads = models.IntegerField(verbose_name="Количество потоков")  # потоков
    value = models.FloatField(verbose_name="Частота процессора")  # ГГЦ
    max_value = models.FloatField(null=True, blank=True, verbose_name="Буст процессора")  # буст

    def __str__(self):
        return self.title


class video_cards_type(models.Model):
    name = models.CharField(max_length=25, verbose_name="Тип видеокарты")  # дискретная интегрированная

    def __str__(self):
        return self.name


class Video_Cards(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    type = models.ForeignKey('video_cards_type', on_delete=models.PROTECT, verbose_name="Тип")
    memory = models.IntegerField(null=True, blank=True, verbose_name="Количество памяти")
    value = models.IntegerField(null=True, blank=True, verbose_name="Частота работы видеочипа")  # ГГЦ
    max_value = models.IntegerField(null=True, blank=True, verbose_name="Турбочастота")  # буст
    type_memory = models.CharField(null=True, blank=True, max_length=15, verbose_name="Тип памяти")  # GDDR6X

    def __str__(self):
        return self.title


class Ram(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    type = models.CharField(max_length=10, verbose_name="Тип")
    memory = models.IntegerField(verbose_name="Память на 1 плашку")

    def __str__(self):
        return self.title


class Motherboard(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    socket = models.CharField(max_length=10, verbose_name="Сокет")

    def __str__(self):
        return self.title


class data_drives(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    memory = models.IntegerField(verbose_name="Количество памяти")

    def __str__(self):
        return self.title


class Oper_System_type(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")

    def __str__(self):
        return self.title


class PC(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="SLUG")
    content = models.TextField(blank=True, verbose_name="Контент")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)
    src = models.CharField(max_length=255, null=True)

    oc = models.ForeignKey('Oper_System_type', on_delete=models.PROTECT, verbose_name="Операционная система")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    cpu = models.ForeignKey('CPUs', on_delete=models.PROTECT, verbose_name="ЦПУ")
    video = models.ForeignKey('Video_Cards', on_delete=models.PROTECT, verbose_name="Видеокарта")
    ram = models.ForeignKey('Ram', on_delete=models.PROTECT, verbose_name="ОЗУ")
    mother = models.ForeignKey('Motherboard', on_delete=models.PROTECT, verbose_name="Материнская плата")
    data = models.ForeignKey('data_drives', on_delete=models.PROTECT, verbose_name="Накопитель данных")

    count_ram = models.IntegerField(default=1, verbose_name="Количество оперативной памяти")
    count_data = models.IntegerField(default=1, verbose_name="Количество накопителей данных")

    garant = models.IntegerField(verbose_name="Гарантия в мес.")  # Гарантия 12 мес
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Наименование категории")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="SLUG")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class orders_status(models.Model):
    name = models.CharField(max_length=50, null=False)

class Orders(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(PC, blank=True, related_name='models', through='Orders_PCs')
    status = models.ForeignKey(orders_status, on_delete=models.CASCADE)

class Orders_PCs(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Количество товара")

class Help(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, verbose_name="Сообщение")
    date = models.DateTimeField(auto_now_add=True)
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, verbose_name="Сообщение")
    grade = models.IntegerField(verbose_name="Оценка")
    date = models.DateTimeField(auto_now_add=True)