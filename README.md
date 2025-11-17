# Proyek Pembelajaran Socket TCP dan UDP

Proyek ini berisi contoh implementasi komunikasi client–server menggunakan protokol TCP dan UDP. Seluruh contoh dibuat dengan Python untuk membantu memahami cara kerja socket pada kedua protokol tersebut.

## Penjelasan

### 1. TCP (Transmission Control Protocol)

TCP adalah protokol *connection-oriented*. Klien harus terhubung dulu ke server sebelum bisa bertukar data.

- **TCP/tcpServer.py** :
  - Membuat socket TCP ( `SOCK_STREAM` ) dan mengikatnya ke `127.0.0.1` port `12345` .
  - Server `listen` (mendengarkan) koneksi masuk.
  - Saat klien terhubung ( `server.accept()` ), server menerima pesan, mengubahnya jadi huruf kapital ( `string.upper()` ), dan mengirimkannya kembali ke klien.
  - Koneksi ditutup.

- **TCP/tcpSocket.py** :
  - Membuat socket TCP dan melakukan `connect` ke server di `127.0.0.1:12345` .
  - Meminta input dari pengguna ( masukkan pesan... ).
  - Mengirim pesan tersebut ke server, menerima balasannya (yang sudah di-uppercase), dan mencetaknya.

### 2. UDP (User Datagram Protocol)

UDP adalah protokol *connectionless*. Tidak perlu membuat koneksi, langsung kirim data.

- **UDP/udpServer.py** :
  - Membuat socket UDP ( `SOCK_DGRAM` ) dan mengikatnya ke `127.0.0.1` port `12345` .
  - Server menunggu data dengan `recvfrom()`, mengubah pesan ke huruf kapital.
  - Mengirim balasan ke alamat klien menggunakan `sendto()`.

- **UDP/udpSocket.py** :
  - Membuat socket UDP.
  - Meminta input dari pengguna.
  - Langsung mengirim data ke server menggunakan `sendto()` ke `127.0.0.1:12345`.
  - Menerima balasan dengan `recvfrom()` dan mencetaknya.

## Perbedaan TCP vs UDP

| Aspek | TCP | UDP |
|-------|-----|-----|
| Koneksi | Perlu koneksi (handshake) | Tanpa koneksi |
| Keandalan | Reliable, data pasti sampai | Unreliable, bisa hilang |
| Kecepatan | Lebih lambat | Lebih cepat |
| Urutan Data | Dijamin berurutan | Tidak dijamin |
| Overhead | Tinggi | Rendah |
| Use Case | Transfer file, web, email | Streaming, gaming, VoIP |

## Cara Menjalankan

### Jalankan TCP Server dan Socket

1. **Jalankan Server terlebih dahulu:**
```bash
python TCP/tcpServer.py
```

**Output Server:**

![TCP Server](https://raw.githubusercontent.com/agissillah/Phyton-For-Hacking/main/TCP/TcpServer.png)

2. **Di terminal lain, jalankan Socket:**
```bash
python TCP/tcpSocket.py
```

**Output Socket:**

![TCP Socket](https://raw.githubusercontent.com/agissillah/Phyton-For-Hacking/main/TCP/TcpSocket.png)

3. **Masukkan pesan** yang ingin dikirim, server akan membalas dengan huruf kapital.

### Jalankan UDP Server dan Client

1. **Jalankan Server terlebih dahulu:**
```bash
python UDP/udpServer.py
```

**Output Server:**

![UDP Server](./UDP/UdpServer.png)

2. **Di terminal lain, jalankan Client:**
```bash
python UDP/udpSocket.py
```

**Output Socket:**

![UDP Socket](./UDP/UdpSocket.png)

3. **Masukkan pesan** yang ingin dikirim, server akan membalas dengan huruf kapital.

## Struktur Proyek

```
.
├── README.md
├── TCP/
│   ├── tcpServer.py
│   └── tcpSocket.py
├── UDP/
   ├── udpServer.py
   └── udpSocket.py
```

## Catatan

- Pastikan port `12345` tidak digunakan oleh aplikasi lain
- Server harus dijalankan terlebih dahulu sebelum client
- Gunakan `Ctrl+C` untuk menghentikan server
- Untuk testing di jaringan lokal, ganti `127.0.0.1` dengan IP address server

