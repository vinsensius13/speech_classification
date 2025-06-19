**Nama**: Vinsensius Fendy Kurniawan

**Tugas**: Mini Project - Tugas 25

**Topik**: Speech Classification with CNN


# 🐾 Animal Sound Classifier (CNN-based)

Selamat datang di proyek **Speech Classification with CNN**, di mana kita akan membangun model deep learning untuk mengklasifikasi suara hewan yang ditirukan manusia ke dalam 5 kategori utama menggunakan **Convolutional Neural Network (CNN)**.

---

## 📀 Deskripsi Proyek

Tugas ini merupakan bagian dari **Tugas 25 - Mini Project: Speech Classification with CNN**, yang bertujuan untuk:

* Menggunakan CNN untuk klasifikasi suara.
* Melatih model dengan dataset suara hewan hasil tiruan manusia.
* Melakukan evaluasi, prediksi real-time, dan dokumentasi.

Model akan mendeteksi suara dari 5 hewan berdasarkan suara tiruan manusia:

* **Cow** ("moo")
* **Cat** ("meow")
* **Dog** ("woof")
* **Goat** ("mbee")
* **Bird** ("tweet")

---

## 📂 Struktur Folder Proyek

```
speech-classification-cnn/
├── data-suara/
│   ├── animal-soundprepros/     # Folder dataset audio (.wav), 1 folder per kelas
│   └── animal_sound.csv         # (Opsional) metadata label
├── venv/                          # Environment virtual (opsional jika pakai Colab)
├── bestmodel-rawr.pth             # Model CNN terbaik yang disimpan
├── temp.wav                       # Rekaman temporer untuk testing
├── test-audio.py                  # Skrip prediksi via rekaman audio
├── test-cuda.py                   # Skrip pengecekan device (GPU/CPU)
└── vocal.ipynb                  # Notebook utama (training, evaluasi, visualisasi)
```

---

## 🧰 Dataset

Dataset yang digunakan berasal dari Kaggle:

> [Sound Classification of Animal Voice](https://www.kaggle.com/datasets/rushibalajiputthewad/sound-classification-of-animal-voice)

Dataset ini telah diolah ke format:

* Mono channel `.wav`
* Durasi 2 detik (padding jika kurang)
* Sample rate: `32000 Hz`
* Struktur folder: `data-suara/animal-soundprepros/<nama_kelas>/*.wav`

---

## 💡 Arsitektur Model CNN

Model CNN terdiri dari:

* 2 blok: Conv2D → BatchNorm → ReLU → MaxPool → Dropout
* Diakhiri dengan fully connected layer (Linear)
* Input berupa **MFCC (40-koefisien)** dari audio

Output: jumlah kelas = 5 (Cow, Cat, Dog, Goat, Bird)

---

## 📊 Visualisasi & Evaluasi

Notebook `vocal.ipynb` menyertakan:

* Visualisasi **Waveform** & **MFCC** tiap kelas
* Evaluasi akurasi model dan **classification report**
* Deteksi **formant** via Welch Power Spectrum
* Plot loss dan akurasi selama training

---

## ⚖️ Cara Menjalankan

### 1. Install dependencies

```bash
pip install torch torchvision torchaudio librosa soundfile sounddevice matplotlib scikit-learn
```

### 2. Training (opsional)

Buka `vocal.ipynb`, jalankan semua sel:

* Ekstraksi MFCC
* Preprocessing data
* Training CNN selama 100 epoch
* Model terbaik disimpan otomatis (`bestmodel-rawr.pth`)

### 3. Testing via Rekaman

```bash
python test-audio.py
```

* Rekam suara tiruan 2 detik
* Proses MFCC
* Tampilkan confidence prediction tiap kelas

### 4. Tes Device Support

```bash
python test-cuda.py
```

Cek apakah training bisa menggunakan CUDA (GPU).

---

## 🔬 Hasil Model

| Metric         | Value    |
| -------------- | -------- |
| Train Accuracy | 100.00%  |
| Test Accuracy  | \~70.77% |

> *Model menunjukkan overfitting karena dataset kecil. Performa bisa ditingkatkan dengan augmentasi atau dataset yang lebih besar.*

---

## 🔹 Insight Tambahan

* Kode fleksibel: LABELS diambil otomatis dari folder dataset.
* Terdapat pipeline preprocessing audio: VAD, padding, normalization.
* File `temp.wav` digunakan untuk simulasi prediksi real-time.

---



**Nama**: Vinsensius Fendy Kurniawan
**Tugas**: Mini Project - Tugas 25
**Topik**: Speech Classification with CNN

---

Terima kasih telah mampir! Jangan lupa tirukan suara hewan dengan percaya diri ya\~ 🦚🐾🐱
