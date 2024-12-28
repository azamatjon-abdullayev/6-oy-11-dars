from django.db import models

# Create your models here.
class Turlar(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tur "
        verbose_name_plural = "Turlar"


class Gullar(models.Model):
    title = models.CharField(max_length=250, verbose_name="gul nomi")
    content = models.TextField(blank=True, null=True, verbose_name="gul matni")
    photo = models.ImageField(upload_to="post/photos/", null=True, blank=True, verbose_name="Rasmi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    category = models.ForeignKey(Turlar, on_delete=models.CASCADE, verbose_name="Kategororiyasi")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish",
                                    help_text="Belgilangan bo'lsa, saytga chiqaradi!")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Gul "
        verbose_name_plural = "Gullar"
        ordering = ['-created']