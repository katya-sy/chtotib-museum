from django.db import models
from pytils.translit import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Section(models.Model):
    name = models.CharField("Название раздела", max_length=20)
    description = models.CharField("Описание раздела", max_length=255)
    slug = models.SlugField("Слаг", max_length=30, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"


class TimePeriod(models.Model):
    name = models.CharField("Период времени в десятилетиях", max_length=20)
    slug = models.SlugField("Слаг", max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Период"
        verbose_name_plural = "Периоды"


class Article(models.Model):
    title = models.CharField("Название статьи", max_length=100)
    content = CKEditor5Field("Контент статьи")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Раздел")
    time_period = models.ForeignKey(TimePeriod, on_delete=models.CASCADE, verbose_name="Период времени")
    slug = models.SlugField("Слаг", max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images', verbose_name="Статья")
    image = models.ImageField("Изображение", upload_to='articles/images/')
    cover = models.BooleanField("Обложка", default=False)

    def __str__(self):
        return f"Изображение статьи {self.article.title}"

    class Meta:
        verbose_name = "Изображение статьи"
        verbose_name_plural = "Изображения статей"


class Tradition(models.Model):
    title = models.CharField("Название традиции", max_length=100)
    content = CKEditor5Field("Контент традиции")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Раздел")
    slug = models.SlugField("Слаг", max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Традиция"
        verbose_name_plural = "Традиции"


class TraditionImage(models.Model):
    tradition = models.ForeignKey(Tradition, on_delete=models.CASCADE, related_name='images', verbose_name="Традиция")
    image = models.ImageField("Изображение", upload_to='articles/images/')
    cover = models.BooleanField("Обложка", default=False)

    def __str__(self):
        return f"Изображение традиции {self.tradition.title}"

    class Meta:
        verbose_name = "Изображение традиции"
        verbose_name_plural = "Изображения традиций"


class MainPageContent(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = CKEditor5Field("Описание", max_length=1000)
    image = models.ImageField("Изображение", upload_to='main_page/images/')

    def __str__(self):
        return self.title

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Контент главной страницы"
        verbose_name_plural = "Контент главной страницы"
