from PyQt5.QtWidgets import *
from proje_ekleme_python_2 import Ui_Form
from veritabani import veritabani

class ProjeEklemeSayfa(QWidget):
    def __init__(self):
        super().__init__()
        self.eklemeSayfa = Ui_Form()  # Ui_Form sınıfını oluştur
        self.eklemeSayfa.setupUi(self)  # setupUi metodunu çağırarak arayüzü oluştur

        self.everitabani = veritabani()


        self.eklemeSayfa.ekle_buton.clicked.connect(self.projeEkle)
        self.eklemeSayfa.sil_buton.clicked.connect(self.projeSil)
        self.eklemeSayfa.guncelle_buton.clicked.connect(self.projeGuncelle)


    def projeEkle(self):
        _id = self.eklemeSayfa.id_line_edit.text()
        proje_adi = self.eklemeSayfa.proje_adi_line_edit.text()
        sorumlu = self.eklemeSayfa.proje_sorumlusu_line_edit.text()
        isci_sayisi = self.eklemeSayfa.calisan_isci_line_edit.text()
        durum = self.eklemeSayfa.proje_durumu_line_edit.text()
        maliyet = self.eklemeSayfa.maliyet_line_edit.text()
        sirket = self.eklemeSayfa.sirket_line_edit.text()
        baslangic_tarihi = self.eklemeSayfa.proje_baslangic_tarihi_line_Edit.text()
        bitis_tarihi = self.eklemeSayfa.proje_bitis_tarihi_line_edit.text()


        if _id.strip() == "":
            QMessageBox.warning(self,"Uyarı","ID kısmı boş bırakılamaz!")
        else:
            
            veriler = self.everitabani.kayitEkle(_id,proje_adi,sorumlu,isci_sayisi,durum,maliyet,sirket,baslangic_tarihi,bitis_tarihi)

        
        if veriler:
            
            QMessageBox.information(self, 'Başarılı', 'Kayıt başarıyla eklendi.')
        else:
            QMessageBox.warning(self, 'Hata', 'Kayıt eklenirken bir hata oluştu.')
        
    def projeSil(self):
        _id = self.eklemeSayfa.id_line_edit.text()
        sil = self.everitabani.sil(_id)

        if sil:
            
            QMessageBox.information(self,"Bilgi","Kayıt Başarıyla Silindi")
        else:
            QMessageBox.warning(self,"Bilgi","Kayıt Silinemedi.")

        
    def projeGuncelle(self):
        _id = self.eklemeSayfa.id_line_edit.text()
        proje_adi = self.eklemeSayfa.proje_adi_line_edit.text()
        sorumlu = self.eklemeSayfa.proje_sorumlusu_line_edit.text()
        isci_sayisi = self.eklemeSayfa.calisan_isci_line_edit.text()
        durum = self.eklemeSayfa.proje_durumu_line_edit.text()
        maliyet = self.eklemeSayfa.maliyet_line_edit.text()
        sirket = self.eklemeSayfa.sirket_line_edit.text()
        baslangic_tarihi = self.eklemeSayfa.proje_baslangic_tarihi_line_Edit.text()
        bitis_tarihi = self.eklemeSayfa.proje_bitis_tarihi_line_edit.text()


        if _id.strip() == "":
            QMessageBox.warning(self,"Uyarı","ID kısmı boş bırakılamaz!")
        else:
            
            veriler = self.everitabani._Guncelle(_id,proje_adi,sorumlu,isci_sayisi,durum,maliyet,sirket,baslangic_tarihi,bitis_tarihi)




        if veriler:
            
            QMessageBox.information(self, 'Başarılı', 'Kayıt başarıyla güncellendi.')
        else:
            QMessageBox.warning(self, 'Hata', 'Kayıt güncellenirken bir hata oluştu.')
        







