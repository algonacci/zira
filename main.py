from googlesearch import search

# Masukkan query pencarian
query = "cara belajar python untuk pemula"

# Lakukan pencarian dan tampilkan hasilnya
for hasil in search(query, num_results=10):
    print(hasil)
