import sqlite3 
import os 

class veritabani():
    def __init__(self):
        dizin_yol = os.path.dirname(os.path.abspath(__file__))
        self.db = os.path.join(dizin_yol,'is_takip_yonetim.db')
        print(self.db)
        

    def vtac(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()


    def vtkapat(self):
        self.cursor.close()

    
    def kayitEkle(self,_id,proje_adi,sorumlu,isci_sayisi,durum,maliyet,sirket,baslangic_tarihi,bitis_tarihi):
       try:
        self.vtac()
        sql = "insert into proje (id,proje_adi,sorumlu,isci_sayisi,durum,maliyet,sirket,baslangic_tarihi,bitis_tarihi ) values (?,?,?,?,?,?,?,?,?)"
        self.cursor.execute(sql,(_id,proje_adi,sorumlu,isci_sayisi,durum,maliyet,sirket,baslangic_tarihi,bitis_tarihi))
        self.conn.commit()
        return True
       except:
          return False
       finally:
          self.vtkapat()


    def kayitGoster(self):
       try:
          self.vtac()
          sql = "select * from proje order by id "
          self.cursor.execute(sql)
          veriler = self.cursor.fetchall()
          return veriler
       except:
          return False
       finally:
          self.vtkapat



    def _Guncelle(self,_id,proje_adi,sorumlu,isci_sayisi,durum,maliyet,sirket,baslangic_tarihi,bitis_tarihi):
     try:
        self.vtac()
        sql =sql = "UPDATE proje SET proje_adi = ?, sorumlu = ?, isci_sayisi = ?, durum = ?, maliyet = ?, sirket = ?, baslangic_tarihi = ?, bitis_tarihi = ? WHERE id = ?"
        self.cursor.execute(sql, (proje_adi, sorumlu, isci_sayisi, durum, maliyet, sirket, baslangic_tarihi, bitis_tarihi, _id))
        self.conn.commit()
        return True
     except Exception as e:
        print(f'Hata: {e}')
     finally:
        self.vtkapat()   


    def sil(self, _id):
       try:
          self.vtac()
          sql = "DELETE FROM proje WHERE id = ?"
          self.cursor.execute(sql, (_id,))
          self.conn.commit()
          return True
       except sqlite3.Error as e:
          print("SQLite Hatası:", e) 
          return False
       finally:
        self.vtkapat()
          
    


    def ara(self, proje_adi):
      try:
        self.vtac()
        sql = "SELECT * FROM proje WHERE proje_adi LIKE ? ORDER BY id DESC"
        # LIKE operatörü için parametreli sorgu kullanımı
        self.cursor.execute(sql, ('%' + proje_adi + '%',))
        veriler = self.cursor.fetchall()
        return veriler
      except Exception as e:
        print("Arama hatası:", e)
        return False
      finally:
        self.vtkapat()
