# 🚢 Titanic Veri Yönetimi ve Versiyonlama Eğitimi

Bu proje, ML projelerinde **veri yönetimi** ve **versiyonlama** konularını Titanic veri seti ile hands-on öğretmek için hazırlanmıştır.

## 🎯 Eğitim Hedefi

Öğrenciler şunları öğrenecek:
1. **Git** ile kod versiyonlama
2. **DVC** ile veri versiyonlama  
3. Veri pipeline'ı oluşturma
4. Veri değişikliklerini takip etme

## 🚀 Hızlı Başlangıç

### 1. Kurulum
```bash
# Python kütüphaneleri
source venv/bin/activate
pip install -r requirements.txt

# DVC kurulumu (sistem seviyesinde)
conda install -c conda-forge dvc
# veya
brew install dvc
```

### 2. Pipeline'ı Çalıştırın

**Seçenek 1: Tek tek adımlar**
```bash
python 1_veri_indirme.py
python 2_veri_temizleme.py
python 3_feature_engineering.py
python 4_analiz.py
```

**Seçenek 2: Tümünü birden**
```bash
python calistir.py
```

**Seçenek 3: DVC ile**
```bash
dvc repro
```

## 📊 Demo Adımları

### Adım 1: Ham Veri
- Seaborn'dan Titanic veri seti indirilir
- `data/raw/titanic_original.csv` dosyasına kaydedilir

### Adım 2: Veri Temizleme
- Eksik değerler doldurulur
- Gereksiz sütunlar çıkarılır
- `data/processed/titanic_clean.csv` dosyasına kaydedilir

### Adım 3: Feature Engineering
- Yeni feature'lar oluşturulur (family_size, is_alone, age_group)
- `data/processed/titanic_features.csv` dosyasına kaydedilir

## 🔄 Git ve DVC ile Versiyonlama

### Git ile Kod Versiyonlama
```bash
# İlk commit
git add veri_yonetimi_demo.py
git commit -m "Titanic veri demo script'i eklendi"

# Değişiklik yapıp commit
git add .
git commit -m "Veri temizleme iyileştirildi"
```

### DVC ile Veri Versiyonlama
```bash
# DVC'yi başlat
dvc init
git add .dvc .dvcignore
git commit -m "DVC kurulumu"

# Ham veriyi DVC ile takip et
dvc add data/raw/titanic_original.csv
git add data/raw/titanic_original.csv.dvc .gitignore
git commit -m "Ham Titanic verisi eklendi"

# İşlenmiş veriyi DVC ile takip et
dvc add data/processed/titanic_clean.csv
git add data/processed/titanic_clean.csv.dvc
git commit -m "Temizlenmiş veri eklendi"
```

## 🛠️ Pipeline Oluşturma

### DVC Pipeline (dvc.yaml)
```yaml
stages:
  data_download:
    cmd: python -c "import seaborn as sns; df=sns.load_dataset('titanic'); df.to_csv('data/raw/titanic_original.csv', index=False)"
    outs:
      - data/raw/titanic_original.csv

  data_clean:
    cmd: python veri_yonetimi_demo.py --step clean
    deps:
      - data/raw/titanic_original.csv
      - veri_yonetimi_demo.py
    outs:
      - data/processed/titanic_clean.csv

  feature_engineering:
    cmd: python veri_yonetimi_demo.py --step features
    deps:
      - data/processed/titanic_clean.csv
      - veri_yonetimi_demo.py
    outs:
      - data/processed/titanic_features.csv
```

### Pipeline Çalıştırma
```bash
# Tüm pipeline'ı çalıştır
dvc repro

# Pipeline görselleştir
dvc dag

# Belirli bir adımı çalıştır
dvc repro data_clean
```

## 🎓 Öğrenciler İçin Pratik Egzersizler

### Egzersiz 1: Temel Veri Yönetimi
1. Demo'yu çalıştırın
2. Her adımda oluşan dosyaları inceleyin
3. Veri boyutlarındaki değişimleri gözlemleyin

### Egzersiz 2: Git Versiyonlama
1. Demo script'inde bir değişiklik yapın (örn: farklı bir eksik değer doldurma yöntemi)
2. Değişikliği commit edin
3. Önceki versiyona geri dönüp farkları karşılaştırın

### Egzersiz 3: DVC ile Veri Takibi
1. Veri dosyalarını DVC ile takip edin
2. Veri preprocessing parametrelerini değiştirin
3. Yeni veri versiyonu oluşturun ve karşılaştırın

### Egzersiz 4: Pipeline Oluşturma
1. `dvc.yaml` dosyasını oluşturun
2. Her veri işleme adımını ayrı stage yapın
3. `dvc repro` ile pipeline'ı çalıştırın

## 📋 Öğrenme Kontrol Listesi

- [ ] Seaborn veri seti indirebildim
- [ ] Veri temizleme adımlarını anladım
- [ ] Git ile kod versiyonlama yapabiliyorum
- [ ] DVC ile veri versiyonlama yapabiliyorum
- [ ] `.dvc` dosyalarının mantığını anlıyorum
- [ ] DVC pipeline oluşturabilirim
- [ ] Veri değişikliklerini takip edebilirim

## 🔍 Pratik Senaryolar

### Senaryo 1: Veri Güncellemesi
"Titanic veri setinde yeni sütunlar eklendi. Nasıl güncellenir?"

### Senaryo 2: Farklı Preprocessing
"Farklı veri temizleme yöntemleri denemek istiyorum. Nasıl karşılaştırırım?"

### Senaryo 3: Takım Çalışması
"Takım arkadaşımla aynı veri üzerinde çalışıyoruz. Nasıl senkronize olurum?"

## 📚 Yararlı Komutlar

### Git
```bash
git status              # Durum kontrolü
git log --oneline       # Commit geçmişi
git diff                # Değişiklikleri görüntüle
git checkout <commit>   # Belirli commit'e git
```

### DVC
```bash
dvc status             # Pipeline durumu
dvc diff               # Veri değişikliklerini göster
dvc checkout           # Veri dosyalarını güncelle
dvc metrics show       # Metrikleri göster
```

---

**🎯 Bu basit demo ile veri yönetimi ve versiyonlamanın temellerini öğreneceksiniz!**