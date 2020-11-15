from django.db import models

# Create your models here.


class Pendidikan(models.Model):
    kd_pendidikan = models.CharField(max_length=200, null=True)
    nama_pendidikan = models.CharField(max_length=200, null=True)
    jurusan = models.CharField(max_length=200, null=True)
    tingkat_pendidikan = models.CharField(max_length=200, null=True)
    tahun_lulus = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.kd_pendidikan


class Jabatan(models.Model):
    kd_jabatan = models.CharField(max_length=200, null=True)
    jabatan = models.CharField(max_length=200, null=True)
    tmt_jabatan = models.CharField(max_length=200, null=True)
    mk_tahun = models.IntegerField()
    mk_bulan = models.IntegerField()


    def __str__(self):
        return self.kd_jabatan


class Pegawai(models.Model):
    nip = models.CharField(max_length=200, null=True)
    nama = models.CharField(max_length=200, null=True)
    kd_jabatan = models.ForeignKey(Jabatan, on_delete=models.SET_NULL, blank=True, null=True)
    kd_pendidikan = models.ForeignKey(Pendidikan, on_delete=models.SET_NULL, blank=True, null=True)
    golongan = models.CharField(max_length=200, null=True)
    tempat_lahir = models.CharField(max_length=200, null=True)
    tgl_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    agama = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
