"""
2. ADIM: Veri Temizleme
Ham veriyi temizleyip processed klasörüne kaydetme
"""
import pandas as pd
import os

def main():
    print("=== 2. ADIM: VERİ TEMİZLEME ===")
    
    # Ham veriyi yükle
    if not os.path.exists('data/raw/titanic_original.csv'):
        print("❌ Ham veri bulunamadı! Önce 1_veri_indirme.py çalıştırın.")
        return
    
    df = pd.read_csv('data/raw/titanic_original.csv')
    print(f"📂 Ham veri yüklendi: {df.shape}")
    
    # Veri temizleme işlemleri
    df_clean = df.copy()
    
    # 1. Age sütunundaki eksik değerleri median ile doldur
    median_age = df_clean['age'].median()
    df_clean['age'] = df_clean['age'].fillna(median_age)
    print(f"✅ Age eksik değerleri {median_age:.1f} ile dolduruldu")
    
    # 2. Embarked sütunundaki eksik değerleri mode ile doldur
    mode_embarked = df_clean['embarked'].mode()[0]
    df_clean['embarked'] = df_clean['embarked'].fillna(mode_embarked)
    print(f"✅ Embarked eksik değerleri '{mode_embarked}' ile dolduruldu")
    
    # 3. Deck sütununu çıkar (çok fazla eksik değer var)
    if 'deck' in df_clean.columns:
        df_clean = df_clean.drop(['deck'], axis=1)
        print("✅ Deck sütunu çıkarıldı (çok fazla eksik değer)")
  
    
    # processed klasörünü oluştur ve kaydet
    os.makedirs('data/processed', exist_ok=True)
    df_clean.to_csv('data/processed/titanic_clean.csv', index=False)
    
    print(f"✅ Temizlenmiş veri kaydedildi: {df_clean.shape}")
    print(f"✅ Dosya: data/processed/titanic_clean.csv")
    print(f"✅ Kalan eksik değerler: {df_clean.isnull().sum().sum()}")
    print("burda bir değişiklik yaprım")

if __name__ == "__main__":
    main()