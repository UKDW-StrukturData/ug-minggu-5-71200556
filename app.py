import csv
import streamlit as st

# --- Fungsi untuk load data ---
def load_news(filename):
    """Baca file news_data.csv ke list of dict"""
    # TODO: buka file CSV (filename) dan baca dengan csv.DictReader
    with open(filename, 'r', newline='') as datafile:
        reader = csv.DictReader(datafile)
    # kembalikan hasilnya dalam bentuk list
        return list(reader)

def load_comments(filename):
    """Baca file comment_news.csv ke list of dict"""
    # TODO: sama seperti load_news tapi untuk file komentar
    with open(filename, 'r', newline='') as komentar:
        reader = csv.DictReader(komentar)
        return list(reader)

# --- Fungsi untuk memproses data ---
def process_data(news_list, comments_list):
    """
    Gabungkan berita dan komentar,
    hitung jumlah komentar & rata-rata rating.
    Hasilnya list of dict.
    """
    # TODO: Buat dictionary untuk kumpulkan komentar per idBerita
    comments_per_news = {}
    for comment in comments_list:
        idberita = comment['idberita']
        rating = int(comment["rating"])
        if idberita not in comments_per_news:
            comments_per_news[idberita] = {'rating': [], 'count': 0}
        comments_per_news[idberita]['rating'].append(rating)
        comments_per_news[idberita]['count'] += 1
    

    # TODO: isi comments_per_news dari comments_list
    # hint: per idBerita simpan ratings (list) dan count

    # TODO: Buat list hasil gabungan
    result = []
    for n in news_list:
        idb = n['idBerita']
        headline = n['Headline']
        if n in news_list:
            idberita = n['idberita']
            headline = n['headline']
            if idberita in comments_per_news:
                jumlah = comments_per_news[idberita]['count']
                rata = sum(comments_per_news[idberita]['rating']) / jumlah
            else:
                rata = 0  # ganti dengan hitungan
                jumlah = 0  # ganti dengan hitungan
                result.append({
                    'ID Berita': idb,
                    'Headline': headline,
                    'Rata-rata Rating': round(rata, 2),
                    'Jumlah Komentar': jumlah
        })
        # TODO: cek apakah idb ada di comments_per_news,
        # hitung rata-rata rating dan jumlah komentar
       

    # --- Urutkan berdasarkan rating pakai fungsi biasa ---
    def ambil_rating(item):
        return item['Rata-rata Rating']

    # TODO: urutkan result berdasarkan ambil_rating reverse=True
    result = sorted(result, kay=ambil_rating, reverse=True)
    return result

# --- Fungsi untuk tampilkan di Streamlit ---
def main():
    st.title("Analisis Sentimen & Popularitas Berita")
    st.write("Menampilkan ID, Headline, Rata-rata Rating, dan Jumlah Komentar, diurutkan dari rating tertinggi.")

    # TODO: baca data CSV
    news_data = load_news('news_data.csv')   # ganti dengan pemanggilan load_news
    comment_data = load_comments('comment_news.csv')  # ganti dengan pemanggilan load_comments

    # TODO: proses data
    hasil = process_data(news_data, comment_data)  
    # hint: gunakan st.table(hasil)
    st.table(hasil)

if __name__ == '__main__':
    main()
