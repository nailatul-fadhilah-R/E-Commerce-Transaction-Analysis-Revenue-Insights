import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os
from datetime import datetime

# --- Konfigurasi Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OnlineRetailBusinessIntelligence:
    """
    Sistem analisis data ritel profesional dengan fitur auto-export hasil.
    """
    
    def __init__(self, file_path, output_dir='analysis_results'):
        self.file_path = file_path
        self.output_dir = output_dir
        self.df = None
        self.df_cleaned = None
        
        # Membuat folder output otomatis jika belum ada
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logging.info(f"Folder '{self.output_dir}' telah dibuat.")

    def load_data(self):
        """Memuat data dengan penanganan error yang kuat."""
        try:
            logging.info(f"Memuat dataset: {self.file_path}")
            # Menggunakan read_excel karena file Anda berformat .xlsx
            self.df = pd.read_excel(self.file_path, engine='openpyxl')
            logging.info(f"Berhasil memuat {len(self.df)} baris data.")
        except Exception as e:
            logging.error(f"Gagal memuat file: {e}")
            raise

    def process_pipeline(self):
        """Pipeline pembersihan data lengkap dalam satu metode."""
        if self.df is None: return
        
        logging.info("Menjalankan pipeline pembersihan data...")
        
        # 1. Sampling 10% (Project Requirement)
        df_work = self.df.sample(frac=0.1, random_state=42).copy()
        
        # 2. Data Cleaning
        df_work['InvoiceDate'] = pd.to_datetime(df_work['InvoiceDate'])
        df_work = df_work.dropna(subset=['CustomerID'])
        
        # Filter: Hanya ambil Quantity > 0 dan UnitPrice > 0
        # Secara profesional, ini menghapus 'Returns', 'Bad Debt', dan 'Adjustments'
        df_work = df_work[(df_work['Quantity'] > 0) & (df_work['UnitPrice'] > 0)]
        
        # 3. Feature Engineering
        df_work['Revenue'] = df_work['Quantity'] * df_work['UnitPrice']
        
        self.df_cleaned = df_work
        logging.info("Pembersihan dan Transformasi data selesai.")

    def export_top_countries_report(self):
        """Menghitung top 10 negara dan mengekspor hasilnya sebagai CSV dan Gambar."""
        if self.df_cleaned is None: return
        
        logging.info("Menghitung metrik bisnis dan membuat visualisasi...")
        
        # Agregasi data
        top_countries = (
            self.df_cleaned.groupby('Country')['Revenue']
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
        
        # --- PROSES VISUALISASI ---
        plt.figure(figsize=(12, 8))
        sns.set_style("whitegrid")
        
        # Membuat plot horizontal agar nama negara terlihat jelas
        palette = sns.color_palette("viridis", len(top_countries))
        ax = sns.barplot(x=top_countries.values, y=top_countries.index, palette=palette)
        
        # Menambahkan label angka di ujung bar (Professional Formatting)
        for i, v in enumerate(top_countries.values):
            ax.text(v + (v * 0.01), i, f'£{v:,.0f}', color='black', va='center', fontweight='bold')

        plt.title('Top 10 Countries by Total Revenue\nRetail Dataset Analysis', fontsize=16, pad=20)
        plt.xlabel('Total Revenue (GBP)', fontsize=12)
        plt.ylabel('Country', fontsize=12)
        plt.tight_layout()
        
        # --- AUTO-SAVE KE FOLDER ---
        timestamp = datetime.now().strftime("%Y%md_%H%M")
        chart_filename = f"top_10_countries_{timestamp}.png"
        data_filename = f"revenue_summary_{timestamp}.csv"
        
        # Simpan grafik (High Resolution 300 DPI)
        chart_path = os.path.join(self.output_dir, chart_filename)
        plt.savefig(chart_path, dpi=300)
        
        # Simpan data ringkasan ke CSV (Profesional: Selalu sertakan data mentah di balik grafik)
        csv_path = os.path.join(self.output_dir, data_filename)
        top_countries.to_csv(csv_path)
        
        logging.info(f"HASIL TERSEDIA DI FOLDER '{self.output_dir}':")
        logging.info(f"1. Grafik: {chart_filename}")
        logging.info(f"2. Data CSV: {data_filename}")
        
        plt.show()

# --- EKSEKUSI ---
if __name__ == "__main__":
    # Inisialisasi dengan path file Anda
    analyzer = OnlineRetailBusinessIntelligence(file_path='Online Retail.xlsx')
    
    try:
        analyzer.load_data()
        analyzer.process_pipeline()
        analyzer.export_top_countries_report()
        print("\n[SUCCESS] Semua hasil telah disimpan otomatis ke folder 'analysis_results'.")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {e}")