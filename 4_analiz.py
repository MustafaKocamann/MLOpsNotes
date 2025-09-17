"""
4. ADIM: Veri Analizi ve Görselleştirme
Feature'ları analiz etme ve görselleştirme
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    print("=== 4. ADIM: VERİ ANALİZİ ===")
    
    # Feature'lı veriyi yükle
    if not os.path.exists('data/processed/titanic_features.csv'):
        print("❌ Feature'lı veri bulunamadı! Önce 3_feature_engineering.py çalıştırın.")
        return
    
    df = pd.read_csv('data/processed/titanic_features.csv')
    print(f"📂 Feature'lı veri yüklendi: {df.shape}")
    
    # Analiz sonuçları klasörü
    os.makedirs('results', exist_ok=True)
    
    # 1. Temel istatistikler
    print("\n📊 TEMEL İSTATİSTİKLER:")
    print(f"- Hayatta kalma oranı: %{(df['survived'].mean() * 100):.1f}")
    print(f"- Ortalama yaş: {df['age'].mean():.1f}")
    print(f"- Ortalama ücret: ${df['fare'].mean():.2f}")
    
    # 2. Sınıf bazında hayatta kalma
    print("\n🎫 SINIF BAZINDA HAYATTA KALMA:")
    survival_by_class = df.groupby('pclass')['survived'].mean()
    for pclass, rate in survival_by_class.items():
        print(f"- {pclass}. Sınıf: %{(rate * 100):.1f}")
    
    # 3. Cinsiyet bazında hayatta kalma
    print("\n👥 CİNSİYET BAZINDA HAYATTA KALMA:")
    survival_by_sex = df.groupby('sex')['survived'].mean()
    for sex, rate in survival_by_sex.items():
        print(f"- {sex.title()}: %{(rate * 100):.1f}")
    
    # 4. Yaş grubu bazında hayatta kalma
    print("\n📅 YAŞ GRUBU BAZINDA HAYATTA KALMA:")
    survival_by_age = df.groupby('age_group')['survived'].mean()
    for age_group, rate in survival_by_age.items():
        if pd.notna(age_group):
            print(f"- {age_group}: %{(rate * 100):.1f}")
    
    # 5. Aile büyüklüğü analizi
    print("\n👨‍👩‍👧‍👦 AİLE BÜYÜKLÜĞÜ ANALİZİ:")
    survival_by_family = df.groupby('family_size')['survived'].mean()
    for size, rate in survival_by_family.head().items():
        print(f"- Aile büyüklüğü {size}: %{(rate * 100):.1f}")
    
    # Görselleştirmeler oluştur
    create_visualizations(df)
    
    print(f"\n✅ Analiz tamamlandı!")
    print(f"✅ Görselleştirmeler results/ klasörüne kaydedildi")

def create_visualizations(df):
    """Temel görselleştirmeleri oluştur"""
    
    # Grafik stili
    plt.style.use('default')
    sns.set_palette("husl")
    
    # 1. Hayatta kalma oranları
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Cinsiyet bazında
    sns.barplot(data=df, x='sex', y='survived', ax=axes[0,0])
    axes[0,0].set_title('Cinsiyet Bazında Hayatta Kalma')
    axes[0,0].set_ylabel('Hayatta Kalma Oranı')
    
    # Sınıf bazında
    sns.barplot(data=df, x='pclass', y='survived', ax=axes[0,1])
    axes[0,1].set_title('Sınıf Bazında Hayatta Kalma')
    axes[0,1].set_ylabel('Hayatta Kalma Oranı')
    
    # Yaş grubu bazında
    sns.barplot(data=df, x='age_group', y='survived', ax=axes[1,0])
    axes[1,0].set_title('Yaş Grubu Bazında Hayatta Kalma')
    axes[1,0].set_ylabel('Hayatta Kalma Oranı')
    axes[1,0].tick_params(axis='x', rotation=45)
    
    # Aile büyüklüğü bazında
    family_survival = df.groupby('family_size')['survived'].mean().head(6)
    family_survival.plot(kind='bar', ax=axes[1,1])
    axes[1,1].set_title('Aile Büyüklüğü Bazında Hayatta Kalma')
    axes[1,1].set_ylabel('Hayatta Kalma Oranı')
    axes[1,1].set_xlabel('Aile Büyüklüğü')
    
    plt.tight_layout()
    plt.savefig('results/hayatta_kalma_analizi.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Yaş dağılımı
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='age', hue='survived', bins=30, alpha=0.7)
    plt.title('Yaş Dağılımı - Hayatta Kalanlar vs Kaybedilenler')
    plt.xlabel('Yaş')
    plt.ylabel('Kişi Sayısı')
    plt.savefig('results/yas_dagilimi.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    main()