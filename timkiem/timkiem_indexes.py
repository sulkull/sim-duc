import datetime
from haystack import indexes
from sanpham.models import SanPham



class Add_Sim_PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    Mang = indexes.CharField(model_attr='Mang')
    LoaiSims = indexes.CharField(model_attr='LoaiSims')
    NamSinh = indexes.CharField(model_attr='NamSinh')
    date = indexes.DateTimeField(model_attr='created_at')
   # location = indexes.CharField(model_attr='location')

    SoSim = indexes.EdgeNgramField(model_attr='SoSim')

    def get_model(self):
        return SanPham
