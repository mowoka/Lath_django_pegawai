from django import forms
from django.forms import ModelForm


from .models import Jabatan
from .models import Pendidikan
from .models import Pegawai

class JabatanForm(ModelForm):
    class Meta:
        model = Jabatan
        fields = '__all__'

class PendidikanForm(ModelForm):
    class Meta:
        model = Pendidikan
        fields = '__all__'

class PegawaiForm(ModelForm):
    class Meta:
        model = Pegawai
        fields = '__all__'