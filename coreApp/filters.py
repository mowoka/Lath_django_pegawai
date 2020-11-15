import django_filters
from django_filters import CharFilter

from .models import *

class PegawaiFilter(django_filters.FilterSet):
    name = CharFilter(field_name = 'nama', lookup_expr='icontains')
    class Meta:
        model = Pegawai
        fields = '__all__'
        exclude = ['tempat_lahir','date_create','status','tgl_lahir','tempat_lahir','nip','nama']


class JabatanFilter(django_filters.FilterSet):
    jabatan = CharFilter(field_name = 'jabatan',lookup_expr='icontains')
    class Meta:
        model = Jabatan
        fields = '__all__'
        exclude = ['kd_jabatan','tmt_jabatan','mk_tahun','mk_bulan']


class PendidikanFilter(django_filters.FilterSet):
    jurusan = CharFilter(field_name = 'jurusan', lookup_expr='icontains')
    class Meta:
        model = Pendidikan
        fields = '__all__'
        exclude = ['nama_pendidikan','kd_pendidikan','tingkat_pendidikan','tahun_lulus']