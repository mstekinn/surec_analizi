# 🚚 E-Ticaret Lojistik Süreç ve Darboğaz Analizi

Bu proje, bir e-ticaret firmasının "Siparişten Teslimata" (Order-to-Delivery) sürecini simüle ederek, toplam teslimat süresini etkileyen faktörleri analiz etmek amacıyla geliştirilmiştir.

## 🎯 Projenin Amacı
Müşteriye ulaşan kargonun toplam süresini uzatan ana faktörleri belirlemek ve operasyonel verimliliği artıracak noktaları tespit etmek.

## 🛠 Kullanılan Teknolojiler
* **Python:** Veri simülasyonu ve analizi.
* **Pandas:** Zaman damgası (timestamp) hesaplamaları ve metrik çıkarma.
* **Seaborn & Matplotlib:** Veri görselleştirme.

## 📊 Temel Bulgular (Insights) ve Karşılaştırmalı Analiz

Yapılan analizde **"Depo Hazırlık"** ve **"Yolculuk (Transfer)"** süreleri karşılaştırılmış ve kritik bir ayrım tespit edilmiştir:

**1. Yolculuk Süresi (Sağdaki Mavi Grafik):**
* Süreç ortalaması yüksektir ancak dağılım **Normal (Çan Eğrisi)** şeklindedir.
* **Yorum:** Bu durum, teslimat süresinin coğrafi mesafelere bağlı doğal bir sonuç olduğunu gösterir. Burada operasyonel bir hata değil, fiziksel bir kısıt vardır.

**2. Depo Hazırlık Süresi (Soldaki Kırmızı Grafik):**
* Dağılım **Bimodal (Çift Tepeli)** yapıdadır.
* **Yorum:** Siparişlerin büyük kısmı hızlı hazırlanırken, belirli bir grubun (%30) sistematik olarak 24+ saat beklediği görülmüştür. 
* **Sonuç:** Müdahale edilmesi gereken asıl **darboğaz burasıdır**; çünkü buradaki gecikme coğrafi değil, operasyoneldir.

## 🚀 Öneriler ve Aksiyon Planı

1.  **Lojistik Ağı Optimizasyonu:** Yolculuk sürelerini kısaltmak için bölgesel dağıtım merkezlerinin (Hub) sayısı artırılabilir veya en çok sipariş alan şehirlere ara depolar kurulabilir.
2.  **Depo Vardiya Düzenlemesi:** Depodaki "gizli gecikmeleri" önlemek için, hazırlık süresi 24 saati aşan siparişlere otomatik alarm kuran bir takip sistemi geliştirilmelidir.

---
