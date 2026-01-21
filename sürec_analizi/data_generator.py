import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Sabit Değişkenler
NUM_ORDERS = 1000  # Oluşturulacak sipariş sayısı
CITIES = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Adana']
CARGO_FIRMS = ['HızlıKargo', 'Yurtİçi', 'Aras', 'MNG']

data = []

# 2. Rastgele Veri Üretme Fonksiyonu
def generate_order_data(order_id):
    # a. Sipariş Tarihi (Son 3 ay içinde rastgele bir zaman)
    days_back = random.randint(1, 90)
    order_date = datetime.now() - timedelta(days=days_back)
    
    # Sipariş saati sabah 08:00 ile gece 23:00 arası olsun
    order_date = order_date.replace(hour=random.randint(8, 23), minute=random.randint(0, 59))
    
    # b. Depo Hazırlık Süresi (Burada GİZLİ BİR DARBOĞAZ yaratıyoruz)
    # Normalde 2-4 saat sürer ama %30 ihtimalle 1-2 gün sürüyor (Stok sorunu simülasyonu)
    if random.random() < 0.3: 
        prep_hours = random.randint(24, 48) # Sorunlu siparişler
    else:
        prep_hours = random.randint(2, 6)   # Normal siparişler
        
    shipped_date = order_date + timedelta(hours=prep_hours)
    
    # c. Transfer Merkezine Varış (Şehir uzaklığına göre değişir)
    city = random.choice(CITIES)
    if city == 'İstanbul':
        transit_hours = random.randint(2, 6) # İstanbul içi hızlı
    else:
        transit_hours = random.randint(10, 30) # Şehir dışı uzun
        
    hub_arrival_date = shipped_date + timedelta(hours=transit_hours)
    
    # d. Kargo Şubesinde Bekleme (Dağıtıma çıkmadan önceki bekleme)
    # Genelde sabah gelen kargo aynı gün, akşam gelen ertesi sabah çıkar
    dwell_hours = random.randint(1, 14)
    out_for_delivery_date = hub_arrival_date + timedelta(hours=dwell_hours)
    
    # e. Teslimat (Son Kilometre)
    # Kurye dağıtıma çıktıktan 1-5 saat sonra teslim eder
    last_mile_hours = random.randint(1, 5)
    delivery_date = out_for_delivery_date + timedelta(hours=last_mile_hours)
    
    return {
        'Siparis_ID': order_id,
        'Sehir': city,
        'Kargo_Firmasi': random.choice(CARGO_FIRMS),
        'Siparis_Tarihi': order_date,
        'Depodan_Cikis_Tarihi': shipped_date,
        'Subeye_Varis_Tarihi': hub_arrival_date,
        'Dagitima_Cikis_Tarihi': out_for_delivery_date,
        'Teslim_Tarihi': delivery_date
    }

# 3. Veri Setini Oluşturma
print("Veri üretiliyor, lütfen bekleyiniz...")
for i in range(1, NUM_ORDERS + 1):
    data.append(generate_order_data(1000 + i))

df = pd.DataFrame(data)

# CSV Olarak Kaydetme
df.to_csv('lojistik_verisi.csv', index=False)
print(f"{NUM_ORDERS} adet sipariş verisi 'lojistik_verisi.csv' olarak kaydedildi!")

# İlk 5 satırı göster
print("\nOluşturulan veriden örnekler:")
print(df.head())