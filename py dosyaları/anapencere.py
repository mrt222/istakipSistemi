from  PyQt5.QtWidgets import *
from anapencere_python_2 import Ui_MainWindow
from proje_ekleme import ProjeEklemeSayfa
from veritabani import veritabani

class AnapencereSayfa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.anapencereform = Ui_MainWindow()
        self.anapencereform.setupUi(self)
        self.projeEklemeform = ProjeEklemeSayfa()
        self.anavertabani = veritabani()

        self.anapencereform.proje_ekleme_sayfa.triggered.connect(self.sayfaGoster)
        self.kayitGoster()
        
        self.anapencereform.arama_yap_line_edit.textChanged[str].connect(self.kayitAra)


    def sayfaGoster(self):
        self.projeEklemeform.show()


    def kayitGoster(self):
     kolonlar = ["ID", "PROJE ADI", "PROJE SORUMLUSU", "ÇALIŞAN İŞÇİ", "PROJE DURUMU", "MALİYET", "ŞİRKET", "PROJE BAŞLANGIÇ TARİHİ", "PROJE BİTİŞ TARİHİ"]
     self.anapencereform.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.anapencereform.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla

     veriler = self.anavertabani.kayitGoster()
     if veriler:
        self.anapencereform.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.anapencereform.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.anapencereform.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

        # Sütun genişliklerini ayarla
        self.anapencereform.bilgi_tableWidget.setColumnWidth(0, 50)  # ID sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(1, 200)  # PROJE ADI sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(2, 150)  # PROJE SORUMLUSU sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(3, 100)  # ÇALIŞAN İŞÇİ sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(4, 120)  # PROJE DURUMU sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(5, 100)  # MALİYET sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(6, 150)  # ŞİRKET sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(7, 150)  # PROJE BAŞLANGIÇ TARİHİ sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(8, 150)  # PROJE BİTİŞ TARİHİ sütunu için genişlik ayarı

        # Son sütunu genişlet
        self.anapencereform.bilgi_tableWidget.horizontalHeader().setStretchLastSection(True)


    def kayitAra(self):
     kolonlar = ["ID", "PROJE ADI", "PROJE SORUMLUSU", "ÇALIŞAN İŞÇİ", "PROJE DURUMU", "MALİYET", "ŞİRKET", "PROJE BAŞLANGIÇ TARİHİ", "PROJE BİTİŞ TARİHİ"]
     self.anapencereform.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.anapencereform.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla
     proje_Adi = self.anapencereform.arama_yap_line_edit.text()

     veriler = self.anavertabani.ara( proje_Adi)
     if veriler:
        self.anapencereform.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.anapencereform.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.anapencereform.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

        # Sütun genişliklerini ayarla
        self.anapencereform.bilgi_tableWidget.setColumnWidth(0, 50)  # ID sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(1, 200)  # PROJE ADI sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(2, 150)  # PROJE SORUMLUSU sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(3, 100)  # ÇALIŞAN İŞÇİ sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(4, 120)  # PROJE DURUMU sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(5, 100)  # MALİYET sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(6, 150)  # ŞİRKET sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(7, 150)  # PROJE BAŞLANGIÇ TARİHİ sütunu için genişlik ayarı
        self.anapencereform.bilgi_tableWidget.setColumnWidth(8, 150)  # PROJE BİTİŞ TARİHİ sütunu için genişlik ayarı

        # Son sütunu genişlet
        self.anapencereform.bilgi_tableWidget.horizontalHeader().setStretchLastSection(True)


    

       


    
    
   




        

        
















app = QApplication([])
pencere = AnapencereSayfa()
pencere.show()
app.exec_()