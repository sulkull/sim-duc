from django.db import models

# Create your models here.
# Tạo bảng liên hệ
class LienHe(models.Model):
    HoTen = models.CharField(max_length=200)
    Email = models.TextField()
    SDT = models.TextField()
    TinNhan = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.HoTen