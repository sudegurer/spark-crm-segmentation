# PySpark CRM Segmentation and Clustering

### Big Data Customer Analytics Project

Bu proje, **Apache Spark (PySpark)** dağıtık hesaplama yeteneklerini kullanarak 500.000 satırlık sentetik Müşteri İlişkileri Yönetimi (CRM) verisi üzerinde uçtan uca müşteri segmentasyonu gerçekleştirmektedir. Proje, sadece Büyük Veri işleme becerilerini değil, aynı zamanda iş sonuçlarına odaklanan analitik çıkarım yeteneğini de kanıtlar.



## Proje Amaçları

* Büyük hacimli veriyi tek makine limitasyonları olmadan (**PySpark** ile) etkin bir şekilde işlemek.
* Müşterileri davranışlarına (RFM metrikleri) göre anlamlı gruplara ayırmak için **K-Means Clustering** uygulamak.
* Elde edilen segmentleri pazarlama ve satış kararlarını destekleyecek şekilde yorumlamak.

## Teknik Yığın (Tech Stack)

| Kategori | Araçlar |
| :--- | :--- |
| **Büyük Veri İşleme** | Apache Spark (PySpark) |
| **Altyapı** | Docker, Docker Compose |
| **Veri Bilimi** | PySpark ML (K-Means, VectorAssembler, StandardScaler) |
| **Dil** | Python 3 (Pandas, NumPy) |
| **Ortam** | Jupyter Lab |

## Proje Adımları ve Metodoloji

Proje, aşağıdaki temel Veri Mühendisliği ve Veri Bilimi adımlarını izlemiştir:

1.  **Veri Oluşturma:** Pandas ve NumPy kullanılarak 500.000 satırlık RFM (Recency, Frequency, Monetary) özelliklerini içeren sentetik veri seti oluşturulması.
2.  **Dağıtık Veri Yükleme:** Verinin diskten **PySpark DataFrame** formatına verimli bir şekilde yüklenmesi.
3.  **Özellik Mühendisliği:** K-Means modelinin performansını artırmak için `monetary_value` değişkenine **Log Dönüşümü** uygulanması.
4.  **Veri Ön İşleme:** Özelliklerin modele uygun hale getirilmesi için **VectorAssembler** ve **StandardScaler** (Ölçeklendirme) uygulaması.
5.  **Model Uygulama:** **K-Means Clustering** algoritmasının, **K=5** segment belirlemek üzere PySpark ML üzerinde dağıtık olarak eğitilmesi.

## Analiz ve İş Çıkarımı

Modelden elde edilen 5 segment, iş stratejilerini belirlemek amacıyla yorumlanmıştır. Segmentler arasında tespit edilen kritik gruplar şunlardır:

| Segment | Recency (Gün) | Monetary (USD) | İş Çıkarımı |
| :---: | :---: | :---: | :--- |
| **0 (En Değerli)** | $\approx$ 21 | **$\approx$ 2930** | Şirketin ana gelir kaynağı. Elde tutulmaya odaklanılmalı. |
| **1 (Yeni Aday)** | **$\approx$ 16** | $\approx$ 153 | **En iyi Recency**; yeni kazanılmış müşteriler. Yükseltme (Upgrade) teklifleriyle hedeflenmeli. |
| **4 (Riskli VIP)** | **$\approx$ 76** | $\approx$ 1564 | Yüksek geçmiş harcama ancak uzun süredir inaktif. Acil **Geri Kazanım (Reactivation)** kampanyaları gereklidir. |



## Kurulum ve Çalıştırma Talimatları

Bu projeyi yerel olarak çalıştırmak için Docker ve Python Sanal Ortamı gereklidir.

1.  **Projeyi Klonlama:**
    ```bash
    git clone [https://github.com/sudegurer/spark-crm-segmentation.git](https://github.com/sudegurer/spark-crm-segmentation.git)
    cd spark-crm-segmentation
    ```
2.  **Gereksinimleri Yükleme ve Veri Oluşturma:**
    ```bash
    # Sanal ortamı aktive et
    python3 -m venv venv
    source venv/bin/activate
    # Gereken kütüphaneleri yükle
    pip install pandas numpy
    # 500K veriyi oluştur
    python3 generate_data.py
    ```
3.  **Spark Ortamını Başlatma:**
    ```bash
    docker compose up -d
    ```
4.  **Notebook'a Erişim:** Tarayıcıda `http://localhost:8888` adresine giderek **`Pyspark_CRM_Segmentation.ipynb`** Notebook'unu çalıştırın.
5.  **Ortamı Kapatma:**
    ```bash
    docker compose down
    deactivate
    ```
