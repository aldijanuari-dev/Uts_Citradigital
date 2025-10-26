

# MorfologiCitra — Operasi Morfologi pada Citra Biner

Proyek ini bertujuan untuk mempraktikkan materi pertemuan ke-5 mata kuliah Pengolahan Citra Digital, yaitu penerapan operasi morfologi pada citra biner menggunakan bahasa pemrograman Python dan pustaka OpenCV.

## Tujuan

Untuk memahami dan mampu menerapkan operasi morfologi dasar, meliputi:

* Erosion (erosi)
* Dilation (dilasi)
* Opening (buka)
* Closing (tutup)

Serta operasi turunan:

* Morphological Gradient
* Top Hat
* Black Hat

## Persiapan Proyek

### 1. Struktur Folder

Pastikan proyek memiliki struktur direktori sebagai berikut:

```
MorfologiCitra/
│
├── images/
│   └── Hirono2.jpeg     ← gambar contoh
│
├── main.py              ← file utama program
└── README.md            ← file dokumentasi
```

### 2. Instalasi Pustaka

Buka terminal pada PyCharm dan jalankan perintah berikut:

```bash
pip install opencv-python matplotlib numpy
```

## Penjelasan Kode Utama (`main.py`)

### 1. Import Library

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```

Digunakan untuk:

* `cv2`: melakukan pemrosesan citra.
* `numpy`: membuat kernel atau structuring element.
* `matplotlib`: menampilkan hasil visualisasi citra.

### 2. Membaca dan Mengonversi Citra

```python
image = cv2.imread('images/hirono2.jpeg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

Membaca citra dari direktori `images` dan mengubahnya menjadi format grayscale.

### 3. Konversi ke Citra Biner

```python
_, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
```

Mengubah citra menjadi dua tingkat warna, yaitu:

* 0 (hitam) untuk background
* 255 (putih) untuk objek

### 4. Membuat Structuring Element (Kernel)

```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
```

Structuring element atau kernel berfungsi sebagai acuan bentuk dalam operasi morfologi. Ukuran `(3,3)` menunjukkan area pengolahan 3x3 piksel.

### 5. Operasi Morfologi Dasar

#### a. Erosion

```python
erosion = cv2.erode(image_binary, kernel, iterations=1)
```

Mengikis batas objek, sehingga objek menjadi lebih kecil dan noise kecil dapat dihilangkan.

#### b. Dilation

```python
dilation = cv2.dilate(image_binary, kernel, iterations=1)
```

Memperlebar batas objek dan menutup celah atau lubang kecil pada citra.

#### c. Opening

```python
opening = cv2.morphologyEx(image_binary, cv2.MORPH_OPEN, kernel)
```

Melakukan erosi diikuti dilasi. Berguna untuk menghilangkan noise yang berada di luar objek.

#### d. Closing

```python
closing = cv2.morphologyEx(image_binary, cv2.MORPH_CLOSE, kernel)
```

Melakukan dilasi diikuti erosi. Berguna untuk menutup lubang kecil yang terdapat di dalam objek.

### 6. Operasi Morfologi Turunan

#### a. Gradient

```python
gradient = cv2.morphologyEx(image_binary, cv2.MORPH_GRADIENT, kernel)
```

Menghasilkan tepi atau garis luar objek melalui selisih antara hasil dilasi dan erosi.

#### b. Top Hat

```python
tophat = cv2.morphologyEx(image_binary, cv2.MORPH_TOPHAT, kernel)
```

Menampilkan area kecil yang lebih terang dari latar belakang.

#### c. Black Hat

```python
blackhat = cv2.morphologyEx(image_binary, cv2.MORPH_BLACKHAT, kernel)
```

Menampilkan area kecil yang lebih gelap dari latar belakang.

### 7. Menampilkan Hasil

```python
plt.figure(figsize=(15, 10))
for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
```

Menampilkan hasil dari setiap operasi morfologi dalam satu tampilan visual untuk memudahkan perbandingan.

## Ringkasan Operasi

| Operasi   | Tujuan                            | Fungsi OpenCV                           |
| --------- | --------------------------------- | --------------------------------------- |
| Erosion   | Mengecilkan objek                 | `cv2.erode()`                           |
| Dilation  | Memperbesar objek                 | `cv2.dilate()`                          |
| Opening   | Menghilangkan noise di luar objek | `cv2.morphologyEx(..., MORPH_OPEN)`     |
| Closing   | Menutup lubang dalam objek        | `cv2.morphologyEx(..., MORPH_CLOSE)`    |
| Gradient  | Menampilkan tepi objek            | `cv2.morphologyEx(..., MORPH_GRADIENT)` |
| Top Hat   | Menonjolkan area terang kecil     | `cv2.morphologyEx(..., MORPH_TOPHAT)`   |
| Black Hat | Menonjolkan area gelap kecil      | `cv2.morphologyEx(..., MORPH_BLACKHAT)` |

## Cara Menjalankan Program

1. Pastikan gambar contoh berada dalam folder `images/`.
2. Buka file `main.py`.
3. Klik kanan pada file dan pilih "Run 'main'".
4. Tunggu hingga hasil operasi morfologi muncul dalam jendela tampilan.

## Catatan Tambahan

* Ukuran kernel `(3,3)` dapat diubah menjadi `(5,5)` atau `(7,7)` untuk melihat perbedaan hasil operasi.
* Bentuk kernel juga dapat diubah menggunakan:

  ```python
  cv2.MORPH_ELLIPSE
  cv2.MORPH_CROSS
  ```
* Proyek ini dapat digunakan sebagai latihan dalam memahami konsep dasar operasi morfologi pada citra biner dalam mata kuliah Pengolahan Citra Digital.

---
