"""
TÜM PIPELINE'I ÇALIŞTIRMA SCRIPT'İ
Tüm adımları sırayla çalıştırır
"""

import subprocess
import sys

def run_script(script_name):
    """Bir Python script'ini çalıştır"""
    print(f"\n🚀 {script_name} çalıştırılıyor...")
    print("-" * 50)
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            print(f"✅ {script_name} başarıyla tamamlandı!")
        else:
            print(f"❌ {script_name} hata verdi:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ {script_name} çalıştırılırken hata: {e}")
        return False
    
    return True

def main():
    """Tüm pipeline'ı sırayla çalıştır"""
    
    print("🚢 TİTANİC VERİ PIPELINE BAŞLIYOR")
    print("=" * 60)
    
    # Çalıştırılacak script'ler sırasıyla
    scripts = [
        "1_veri_indirme.py",
        "2_veri_temizleme.py", 
        "3_feature_engineering.py",
        "4_analiz.py"
    ]
    
    # Her script'i sırayla çalıştır
    for script in scripts:
        success = run_script(script)
        if not success:
            print(f"\n💥 Pipeline {script} adımında durdu!")
            sys.exit(1)
    
    print("\n" + "=" * 60)
    print("🎉 TÜM PIPELINE BAŞARIYLA TAMAMLANDI!")
    print("\nOluşturulan dosyalar:")
    print("📁 data/raw/titanic_original.csv")
    print("📁 data/processed/titanic_clean.csv") 
    print("📁 data/processed/titanic_features.csv")
    print("📁 results/hayatta_kalma_analizi.png")
    print("📁 results/yas_dagilimi.png")
    
    print("\n🔄 Şimdi Git ve DVC ile versiyonlayın:")
    print("git add .")
    print("git commit -m 'Titanic veri pipeline tamamlandı'")
    print("dvc add data/raw/titanic_original.csv")

if __name__ == "__main__":
    main()