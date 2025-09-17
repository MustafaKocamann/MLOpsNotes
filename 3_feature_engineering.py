"""
3. ADIM: Feature Engineering
Temizlenmiş veriye yeni özellikler ekleme
"""
import pandas as pd
import os

def main():
    print("=== 3. ADIM: FEATURE ENGİNEERİNG ===")
    
    # Temizlenmiş veriyi yükle
    if not os.path.exists('data/processed/titanic_clean.csv'):
        print("❌ Temizlenmiş veri bulunamadı! Önce 2_veri_temizleme.py çalıştırın.")
        return
    
    df = pd.read_csv('data/processed/titanic_clean.csv')
    print(f"📂 Temizlenmiş veri yüklendi: {df.shape}")
    
    # Feature engineering işlemleri
    df_features = df.copy()
    
    # 1. Aile büyüklüğü
    df_features['family_size'] = df_features['sibsp'] + df_features['parch'] + 1
    print("✅ family_size feature'ı eklendi (sibsp + parch + 1)")
    
    # 2. Yalnız mı?
    df_features['is_alone'] = (df_features['family_size'] == 1).astype(int)
    print("✅ is_alone feature'ı eklendi (1: yalnız, 0: aile ile)")
    
    # 3. Yaş grupları
    df_features['age_group'] = pd.cut(
        df_features['age'], 
        bins=[0, 18, 35, 60, 100], 
        labels=['Child', 'Young', 'Adult', 'Senior']
    )
    print("✅ age_group feature'ı eklendi (Child, Young, Adult, Senior)")
    
    # 4. Ücret kategorisi
    df_features['fare_category'] = pd.cut(
        df_features['fare'], 
        bins=[0, 10, 50, 100, 1000], 
        labels=['Low', 'Medium', 'High', 'Premium']
    )
    print("✅ fare_category feature'ı eklendi (Low, Medium, High, Premium)")
    
    # Final veriyi kaydet
    df_features.to_csv('data/processed/titanic_features.csv', index=False)
    
    print(f"✅ Feature engineering tamamlandı: {df_features.shape}")
    print(f"✅ Dosya: data/processed/titanic_features.csv")
    print(f"✅ Yeni feature'lar: family_size, is_alone, age_group, fare_category")
    
    # Özet istatistikler
    print(f"\n📊 Feature Özeti:")
    print(f"- Ortalama aile büyüklüğü: {df_features['family_size'].mean():.1f}")
    print(f"- Yalnız yolcu oranı: %{(df_features['is_alone'].mean() * 100):.1f}")
    print(f"- En çok yaş grubu: {df_features['age_group'].mode()[0]}")

if __name__ == "__main__":
    main()