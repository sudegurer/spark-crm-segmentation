#PySpark CRM Segmentation and Clustering (Big Data Customer Analytics)

Bu proje, Apache Spark (PySpark) dağıtık hesaplama yeteneklerini kullanarak 500.000 satırlık sentetik Müşteri İlişkileri Yönetimi (CRM) verisi üzerinde uçtan uca müşteri segmentasyonu gerçekleştirmektedir. Proje, sadece Büyük Veri işleme becerilerini değil, aynı zamanda iş sonuçlarına odaklanan analitik çıkarım yeteneğini de kanıtlar.

##Proje Amacı
-Büyük hacimli (500K+) veriyi tek makine limitasyonları olmadan (Pandas yerine PySpark ile) etkin bir şekilde işlemek.

-Müşterileri davranışlarına (RFM metrikleri) göre anlamlı gruplara ayırmak için denetimsiz öğrenme (Unsupervised Learning) modeli olan K-Means Clustering uygulamak.

-Elde edilen segmentleri iş (marketing/sales) kararlarını destekleyecek şekilde yorumlamak.

##Teknik Yığın (Tech Stack)
Kategori,Araçlar
Büyük Veri İşleme,Apache Spark (PySpark)
Altyapı,"Docker, Docker Compose (İzole geliştirme ortamı için)"
Veri Bilimi,"PySpark ML (K-Means, VectorAssembler, StandardScaler)"
Dil,Python 3
Geliştirme Ortamı,Jupyter Lab


##Proje Adımları ve Metodoloji
Proje, aşağıdaki temel Veri Mühendisliği ve Veri Bilimi adımlarını izlemiştir:

1.Veri Oluşturma: Pandas ve NumPy kullanılarak 500.000 satırlık RFM (Recency, Frequency, Monetary) özelliklerini içeren sentetik veri seti oluşturulması.

2.Dağıtık Veri Yükleme: Verinin diskten PySpark DataFrame formatına verimli bir şekilde yüklenmesi.

3.Özellik Mühendisliği (Feature Engineering): K-Means modelinin performansını artırmak için monetary_value değişkenine Log Dönüşümü uygulanması.

4.Veri Ön İşleme: Özelliklerin modele uygun hale getirilmesi için VectorAssembler ve StandardScaler (Ölçeklendirme) uygulaması.

5.Model Uygulama: K-Means Clustering algoritmasının, K=5 segment belirlemek üzere PySpark ML üzerinde dağıtık olarak eğitilmesi.

6.Sonuç Kaydetme: Segmentasyon sonuçlarının büyük veri formatı olan Parquet dosyası olarak diske kaydedilmesi.

##Analiz ve İş Çıkarımı
Modelden elde edilen 5 segment, iş stratejilerini belirlemek amacıyla yorumlanmıştır. :
Segment,Temel Özellikler,İş Çıkarımı
0 (En Değerli),"En yüksek harcama (Avg Mon: **$2930**), İyi Recency.",Sadık Elitler: Şirketin ana gelir kaynağı. Elde tutma ve özel hizmet programları ile memnuniyetleri sürekli kılınmalı.
1,"En iyi Recency (16 gün), En düşük harcama.","Yeni/Yükseltme Adayları: Yeni kazanılmış müşteriler. Hızlı bir şekilde, daha yüksek değerli ürünler için Yükseltme (Upgrade) teklifleri ile hedeflenmeli."
4 (Riskli VIP),"Yüksek geçmiş harcama ($1564), En yüksek Recency (76 gün).","Kaybetme Riski Olan VIP'ler: Kaybedilmesi en maliyetli segment. Özel, kişiselleştirilmiş Geri Kazanım (Reactivation) kampanyaları acilen başlatılmalı."
Diğer Segmentler,"Ortalamanın üstü sıklık (Frequency), Orta değer.",Düzenli Kullanıcılar: Satın alma sıklıklarını korumaya yönelik promosyonlarla hedeflenmeli.


##Kurulum ve Çalıştırma
Bu projeyi yerel olarak çalıştırmak için Docker gereklidir.

1.Repo'yu Klonlama:
git clone https://github.com/sudegurer/spark-crm-segmentation.git
cd spark-crm-segmentation

2.Ortamı Başlatma (Jupyter + PySpark):
docker compose up -d

3.Veri Oluşturma: Projenin root dizininde generate_data.py dosyasını çalıştırın.
pip install pandas numpy
python3 generate_data.py

4.Notebook'a Erişim: 
Tarayıcıda http://localhost:8888 adresine giderek Pyspark_CRM_Segmentation.ipynb dosyasını çalıştırın.

5.Durdurma:
docker compose down


