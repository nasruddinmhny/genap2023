from django.db import models

# Create your models here.
class kegiatan(models.Model):
    isi = models.CharField(max_length=255, null=False, blank=False)
    keterangan = models.BooleanField(default=False)
    tanggal = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.isi
    

    

