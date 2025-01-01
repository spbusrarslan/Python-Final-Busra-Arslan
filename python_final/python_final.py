

# Gerekli kütüphaneleri yükleme
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Shapefile dosyasını yükleme
shp_path = "C:/Users/Beyza/Desktop/ALISTIRMA/turkıye_ıl.shp"  # Shapefile dosyasının tam yolu
data = gpd.read_file(shp_path)

# Veri kontrolü
print(data.columns)  # Kolon isimlerini kontrol et
print(data[['NÜF_YOG']].describe())  # NÜF_YOG kolonunu analiz et

# Manuel eşik değerleri oluşturma
bins = [0, 50, 100, 200, 400, 800, 1600]  # Yoğunluk aralıkları
labels = ['0-50', '50-100', '100-200', '200-400', '400-800', '800+']  # Aralıklara isim ver
data['density_bin'] = np.digitize(data['NÜF_YOG'], bins)

# Harita oluşturma
data.plot(column='density_bin', cmap='Reds', legend=True, figsize=(12, 8))
plt.title("Türkiye İllerine Göre Nüfus Yoğunluğu (Dengeli)")
plt.xlabel("Enlem")
plt.ylabel("Boylam")
plt.show()
