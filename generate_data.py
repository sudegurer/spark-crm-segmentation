import pandas as pd
import numpy as np
import os

# 500.000 satırlık veri oluşturuyoruz 
NUM_RECORDS = 500000
OUTPUT_DIR = 'data'
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'crm_data.csv')

print(f"--- {NUM_RECORDS} satırlık CRM verisi oluşturuluyor... ---")

# Müşteri Kimlikleri
customer_ids = np.arange(100000, 100000 + NUM_RECORDS)

# Özellikler (Rastgele dağılımlar kullanarak)
data = {
    'customer_id': customer_ids,
    # Recency (Son Satın Alma Günü): Düşük değerler daha iyi (daha yakın zamanda satın almış)
    'recency_days': np.random.gamma(shape=2, scale=15, size=NUM_RECORDS).astype(int), 
    # Frequency (Satın Alma Sıklığı): 
    'frequency': np.random.poisson(lam=4, size=NUM_RECORDS).clip(min=1),
    # Monetary Value (Toplam Harcama): 
    'monetary_value': np.random.lognormal(mean=6, sigma=1.5, size=NUM_RECORDS).round(2),
    # Ülke
    'country': np.random.choice(['TR', 'US', 'DE', 'FR', 'UK'], size=NUM_RECORDS, p=[0.4, 0.3, 0.1, 0.1, 0.1]),
    # Segment (Noise için, model bunu tahmin edecek)
    'segment_true': np.random.choice(['High', 'Mid', 'Low'], size=NUM_RECORDS, p=[0.2, 0.5, 0.3])
}

df = pd.DataFrame(data)

# Veriyi kaydetme
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

df.to_csv(OUTPUT_FILE, index=False)
print(f"Veri seti başarıyla oluşturuldu: {OUTPUT_FILE} ({len(df)} satır)")
print("--- Veri Oluşturma Tamamlandı. ---")
