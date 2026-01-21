import pandas as pd

df = pd.read_csv('lojistik_verisi.csv')

# Tarih sütunlarını datetime formatına çeviriyoruz
date_cols = ['Siparis_Tarihi', 'Depodan_Cikis_Tarihi', 'Subeye_Varis_Tarihi', 
             'Dagitima_Cikis_Tarihi', 'Teslim_Tarihi']

for col in date_cols:
    df[col] = pd.to_datetime(df[col])


# A. Depo İşleme Süresi (Sipariş -> Kargoya Veriliş)
df['Sure_Depo_Hazirlik'] = (df['Depodan_Cikis_Tarihi'] - df['Siparis_Tarihi']).dt.total_seconds() / 3600

# B. Aktarma/Yol Süresi (Kargo Çıkış -> Şubeye Varış)
df['Sure_Yolculuk'] = (df['Subeye_Varis_Tarihi'] - df['Depodan_Cikis_Tarihi']).dt.total_seconds() / 3600

# C. Şubede Bekleme Süresi (Şubeye Varış -> Dağıtıma Çıkış)
df['Sure_Sube_Bekleme'] = (df['Dagitima_Cikis_Tarihi'] - df['Subeye_Varis_Tarihi']).dt.total_seconds() / 3600

# D. Dağıtım Süresi (Dağıtıma Çıkış -> Teslimat)
df['Sure_Dagitim'] = (df['Teslim_Tarihi'] - df['Dagitima_Cikis_Tarihi']).dt.total_seconds() / 3600

# E. Toplam Süre (Sipariş -> Teslimat)
df['Sure_Toplam_Teslimat'] = (df['Teslim_Tarihi'] - df['Siparis_Tarihi']).dt.total_seconds() / 3600

# 4. Sonucu Kontrol Etme
print("Süreçlerin Ortalama Saatleri:")
print(df[['Sure_Depo_Hazirlik', 'Sure_Yolculuk', 'Sure_Sube_Bekleme', 'Sure_Dagitim']].mean().round(2))

print("\nVeri Setinin Son Hali (İlk 3 Satır):")
print(df[['Sehir', 'Sure_Depo_Hazirlik', 'Sure_Toplam_Teslimat']].head(3))



import matplotlib.pyplot as plt
import seaborn as sns

# Stil ayarı
sns.set_style("whitegrid")
plt.figure(figsize=(16, 6)) 

# --- GRAFİK A: Depo Süresi (Darboğaz) ---
plt.subplot(1, 2, 1)
sns.histplot(df['Sure_Depo_Hazirlik'], bins=30, kde=True, color="red")
plt.title('Depo Hazırlık Süresi Dağılımı\n(Bimodal Dağılım: Operasyonel Sorun Var)', fontsize=12)
plt.xlabel('Hazırlanma Süresi (Saat)')
plt.ylabel('Sipariş Sayısı')

# --- GRAFİK B: Yolculuk Süresi (Karşılaştırma) ---
plt.subplot(1, 2, 2)
sns.histplot(df['Sure_Yolculuk'], bins=30, kde=True, color="blue")
plt.title('Yolculuk Süresi Dağılımı\n(Normal Dağılım: Coğrafi Süreç)', fontsize=12)
plt.xlabel('Yolculuk Süresi (Saat)')
plt.ylabel('Sipariş Sayısı')

plt.tight_layout()
plt.savefig('lojistik_analiz_grafigi.png', dpi=300) 

plt.show()
