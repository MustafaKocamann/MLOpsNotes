"""
Metrik Görüntüleme Script'i
DVC metriklerini güzel bir şekilde gösterir
"""
import json
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def load_metrics(metrics_file="results/metrics.json"):
    """JSON metrik dosyasını yükle"""
    if Path(metrics_file).exists():
        with open(metrics_file, 'r') as f:
            return json.load(f)
    return {}

def display_current_metrics():
    """Mevcut metrikleri güzel formatta göster"""
    metrics = load_metrics()
    
    if not metrics:
        print("❌ Metrik dosyası bulunamadı!")
        return
    
    print("🎯 MEVCUT MODEL PERFORMANSI")
    print("=" * 40)
    
    # Ana performans metrikleri
    performance_metrics = ["accuracy", "precision", "recall", "f1_score"]
    
    for metric in performance_metrics:
        if metric in metrics:
            value = metrics[metric]
            print(f"📊 {metric.title():12}: {value:.4f} ({value*100:.2f}%)")
    
    print("\n⚙️ MODEL VE VERİ BİLGİLERİ")
    print("-" * 40)
    
    # Diğer bilgiler
    other_metrics = ["training_time_seconds", "model_size_mb", "feature_count", "data_points"]
    
    for metric in other_metrics:
        if metric in metrics:
            value = metrics[metric]
            if metric == "training_time_seconds":
                print(f"⏱️  Eğitim Süresi  : {value:.1f} saniye")
            elif metric == "model_size_mb":
                print(f"💾 Model Boyutu   : {value:.1f} MB")
            elif metric == "feature_count":
                print(f"🔢 Feature Sayısı : {int(value)}")
            elif metric == "data_points":
                print(f"📈 Veri Noktası   : {int(value)}")

def create_metrics_plot():
    """Metrikleri grafik olarak göster"""
    metrics = load_metrics()
    
    if not metrics:
        print("❌ Metrik dosyası bulunamadı!")
        return
    
    # Performans metrikleri için bar chart
    performance_metrics = ["accuracy", "precision", "recall", "f1_score"]
    values = [metrics.get(m, 0) for m in performance_metrics]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(performance_metrics, values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    
    # Bar'ların üstüne değerleri yaz
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                f'{value:.3f}', ha='center', va='bottom', fontweight='bold')
    
    plt.title('Model Performans Metrikleri', fontsize=16, fontweight='bold')
    plt.ylabel('Değer', fontsize=12)
    plt.ylim(0, 1.1)
    plt.grid(axis='y', alpha=0.3)
    
    # Y eksenini yüzde olarak göster
    plt.gca().set_yticklabels([f'{x:.0%}' for x in plt.gca().get_yticks()])
    
    plt.tight_layout()
    plt.savefig('results/metrics_chart.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Grafik results/metrics_chart.png dosyasına kaydedildi")

def compare_models():
    """Farklı model versiyonlarını karşılaştır"""
    # Bu örnek için simüle edilmiş veri
    comparison_data = {
        'Model Version': ['v1.0', 'v1.1', 'v1.2', 'v2.0 (Current)'],
        'Accuracy': [0.8234, 0.8345, 0.8410, 0.8456],
        'F1-Score': [0.8220, 0.8301, 0.8367, 0.8398],
        'Training Time (s)': [52.3, 48.7, 46.2, 45.6]
    }
    
    df = pd.DataFrame(comparison_data)
    
    print("\n📈 MODEL KARŞILAŞTIRMASI")
    print("=" * 50)
    print(df.to_string(index=False))
    
    # Trend grafiği
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.plot(df['Model Version'], df['Accuracy'], 'o-', linewidth=2, markersize=8)
    plt.title('Accuracy Trendi')
    plt.ylabel('Accuracy')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 2)
    plt.plot(df['Model Version'], df['F1-Score'], 'o-', color='orange', linewidth=2, markersize=8)
    plt.title('F1-Score Trendi')
    plt.ylabel('F1-Score')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 3)
    plt.bar(df['Model Version'], df['Training Time (s)'], color='green', alpha=0.7)
    plt.title('Eğitim Süresi')
    plt.ylabel('Saniye')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 4)
    # İyileşme yüzdesi
    improvement = [(acc - df['Accuracy'][0]) / df['Accuracy'][0] * 100 for acc in df['Accuracy']]
    colors = ['red' if imp < 0 else 'green' for imp in improvement]
    plt.bar(df['Model Version'], improvement, color=colors, alpha=0.7)
    plt.title('Baseline\'den İyileşme (%)')
    plt.ylabel('İyileşme Yüzdesi')
    plt.xticks(rotation=45)
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results/model_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Karşılaştırma grafiği results/model_comparison.png dosyasına kaydedildi")

def main():
    """Ana fonksiyon - tüm metrik görüntüleme seçenekleri"""
    print("🎯 METRİK GÖRÜNTÜLEyİCİ")
    print("=" * 50)
    
    # 1. Mevcut metrikleri göster
    display_current_metrics()
    
    # 2. Performans grafiği oluştur
    print("\n📊 Performans grafikleri oluşturuluyor...")
    create_metrics_plot()
    
    # 3. Model karşılaştırması
    compare_models()
    
    print("\n✅ Tüm metrik görüntüleme işlemleri tamamlandı!")
    print("\n🔄 DVC komutları ile metrik takibi:")
    print("   dvc metrics show")
    print("   dvc metrics diff")
    print("   dvc plots show")

if __name__ == "__main__":
    main()