"""
1. ADIM: Veri İndirme
Seaborn'dan Titanic veri setini indirip kaydetme
"""
import seaborn as sns
import pandas as pd
import os

def main():
    print("=== 1. ADIM: VERİ İNDİRME ===")
    
    # data/raw klasörünü oluştur
    os.makedirs('data/raw', exist_ok=True)
    
    # Titanic veri setini yükle
    titanic = sns.load_dataset('titanic')
    
    # Ham veriyi kaydet
    titanic.to_csv('data/raw/titanic_original.csv', index=False)
    
    print(f"✅ Titanic veri seti indirildi")
    print(f"✅ Dosya boyutu: {titanic.shape}")
    print(f"✅ Kaydedilen dosya: data/raw/titanic_original.csv")
    
    # Veri hakkında temel bilgiler
    print(f"\n📊 Veri Seti Bilgileri:")
    print(f"- Satır sayısı: {len(titanic)}")
    print(f"- Sütun sayısı: {len(titanic.columns)}")
    print(f"- Sütunlar: {list(titanic.columns[:5])}...")
    print(f"- Eksik değerler: {titanic.isnull().sum().sum()}")

if __name__ == "__main__":
    main()