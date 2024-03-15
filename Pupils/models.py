from django.db import models

# Create your models here.
class PupilsModels(models.Model):
    name = models.CharField(max_length=150, verbose_name="Name")
    spec = models.CharField(max_length=100, verbose_name="Speciality")
    pupil_img = models.ImageField(verbose_name="Pupil Image")
    res_1 = models.IntegerField(verbose_name="Birinchi oy natijasi")
    res_2 = models.IntegerField(verbose_name="Ikkinchi oy natijasi")
    res_3 = models.IntegerField(verbose_name="Uchinchi oy natijasi")
    res_4 = models.IntegerField(verbose_name="To'rtinchi oy natijasi")
    res_5 = models.IntegerField(verbose_name="Beshinchi oy natijasi")


    def __str__(self) -> str:
        return f"{self.pk}  {self.name}"