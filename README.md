1. Ana Pencere İşlevleri
Ana pencere, mevcut projelerin listelendiği başlangıç noktasıdır. Ana pencerede aşağıdaki işlevlere erişebilirsiniz:

Proje Ekleme:
Menü çubuğundan Proje Ekle seçeneğini tıklayarak yeni bir proje ekleyebilirsiniz.
Açılan formda gerekli bilgileri girerek Ekle butonuna tıklayın.
Proje Düzenleme ve Silme:
Tablodaki bir projeyi seçerek sağ tıkladığınızda düzenleme veya silme işlemleri gerçekleştirebilirsiniz.
Proje Arama:
Arama çubuğuna proje adını girerek ilgili projeleri filtreleyebilirsiniz.

2. Proje Ekleme Sayfası
Yeni proje eklemek için kullanılır. Proje ekleme sayfasında aşağıdaki işlevlere erişebilirsiniz:

Proje Ekle:
Gerekli alanları doldurduktan sonra Ekle butonuna tıklayarak yeni bir proje ekleyebilirsiniz.
Proje Güncelleme:
Mevcut bir projeyi seçerek bilgilerini güncelleyebilirsiniz.
Değişiklikleri yaptıktan sonra Güncelle butonuna tıklayarak güncelleme işlemini tamamlayabilirsiniz.
Proje Silme:
Mevcut bir projeyi seçerek Sil butonuna tıklayarak proje kaydını silebilirsiniz.

3. Veritabanı Bağlantısı
Veritabanı işlemleri için veritabani.py dosyası kullanılmaktadır. Bu dosyada aşağıdaki işlevler bulunmaktadır:

kayitEkle(_id, proje_adi, sorumlu, isci_sayisi, durum, maliyet, sirket, baslangic_tarihi, bitis_tarihi): Yeni bir proje kaydı ekler.
kayitGoster(): Tüm proje kayıtlarını listeler.
projeGuncelle(_id, proje_adi, sorumlu, isci_sayisi, durum, maliyet, sirket, baslangic_tarihi, bitis_tarihi): Mevcut bir proje kaydını günceller.
sil(_id): Belirtilen ID'ye sahip proje kaydını siler.
ara(proje_adi): Proje adına göre arama yapar.

4. Uygulamanın Başlatılması
Uygulamayı başlatmak için anapencere.py dosyasını çalıştırın. Ana pencere uygulaması başladığında, mevcut projelerin listesi görüntülenecektir.

Kaynak Kodları Sayfaları:
anapencere.py
proje_ekleme.py
veritabani.py
