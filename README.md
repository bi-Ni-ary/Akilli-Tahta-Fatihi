# 🖥️ Akilli-Tahta-Fatihi


> 📌 README Language: Turkish/Türkçe 🇹🇷


Python ile geliştirilmiş deneysel bir Windows prank/automation yazılımı.

Bu proje eski okul günlerinden kalma bir deneydir. İlk fikri, davranışları olasılıksal olarak değişebilen evrimsel bir sistem simülasyonu üzerine kuruluydu. Daha sonra lise döneminde akıllı tahtalarda eğlence ve deney amacıyla kullanılan nostaljik bir projeye dönüştü.

*Ni (bi-Ni-ary) tarafından 2025-2026 yıllarında Windows 10 x64 için geliştirilmiştir.*

*Diğer Windows sürümlerinde de büyük ölçüde çalışması beklenmektedir ancak tüm sürümlerde test edilmemiştir.*



## ⚠️ Uyarı

Bu proje bazı sistem etkileşimleri gerçekleştirebilir ve kullanıcı deneyimini değiştirebilecek davranışlar içerebilir.

- Yalnızca size ait veya kullanım izniniz olan cihazlarda çalıştırın.
- Test amacıyla güvenli ortamlarda kullanın.
- Kullanımdan doğabilecek sonuçlardan kullanıcı sorumludur.

Bu proje eğitim, deney ve nostaljik amaçlarla paylaşılmıştır.



## 📋 Gereksinimler

- `Windows 10` veya `Windows 11` (`64-bit` önerilir)
- `Python 3.10` veya üzeri
- Gerekli Python paketleri (`requirements.txt`)



## ⚙️ Kurulum

### Projeyi klonlayın:

```bash
git clone https://github.com/bi-Ni-ary/Akilli-Tahta-Fatihi.git
```

ardından:

```bash
cd Akilli-Tahta-Fatihi
```


### Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

Alternatif olarak manuel kurulum:

```bash
pip install pyautogui pygetwindow pillow
```



## ▶️ Kullanım

Kurulumu tamamladıktan sonra `src/main.py` dosyasını çalıştırın.

```bash
python src/main.py
```

komutuyla çalıştırabilirsiniz.

> Daha fazla etki için programı aynı anda birden fazla kez de çalıştırabilirsiniz.



## 📦 EXE Oluşturma (PyInstaller)

Projeyi tek dosyalı `.exe` haline getirmek için `PyInstaller` kullanılabilir.


### PyInstaller kurulumu:

```bash
pip install pyinstaller
```

### EXE oluşturma:

```cmd
pyinstaller --onefile --windowed ^
--hidden-import=tkinter ^
--hidden-import=pyautogui ^
--hidden-import=pygetwindow ^
--hidden-import=PIL ^
--hidden-import=PIL.Image ^
--hidden-import=PIL.ImageTk ^
--hidden-import=mouseinfo ^
--hidden-import=pymsgbox ^
--hidden-import=pyperclip ^
--hidden-import=pyscreeze ^
--hidden-import=pytweening ^
--add-data "assets/loading.gif;assets" ^
src/main.py
```

Oluşturulan **EXE** dosyası: `dist/main.exe`



## 🧠 Çalışma Mantığı

- Proje, rastgele seçilen olaylar (event) üzerine kurulu deneysel bir davranış sistemine sahiptir.

- Program belirli aralıklarla bir event seçer ve her event'in seçilme olasılığı `genome` adı verilen listeler üzerinden belirlenir.

- Event seçimi için **Python 3.10**'da gelen `match / case` yapısını kullanır. 

### 🧬 Genome Sistemi

`genome0`:
- Eventler arasındaki bekleme süresinin aralığını belirler.

`genome1`:
- Her event'in seçilme olasılığını belirler.

Her döngüde sistem:
1. Belirlenen süre kadar bekler.
2. Olasılık değerlerine göre bir event seçer.
3. Seçilen event'i çalıştırır.
4. Yeni bir döngüye başlar.

*Bu yapı, projenin ilk fikri olan evrimsel davranış simülasyonu konseptinden bir kalıntıdır.*


### 🎲 Eventler

Toplamda `24` farklı event bulunmaktadır.

- **Event ID**: Kod içerisindeki `case` değerini temsil eden benzersiz event numarası.
- **Risk Seviyeleri**: 🟢 Güvenli | 🟡 Orta | 🟠 Yüksek | 🔴 Kritik


| Event ID | Risk Seviyesi | Açıklama |
|:---:|:---:|:---|
| 0 | 🟢 | Hiçbir işlem yapmayan boş event |
| 1 | 🟢 | `Windows Defender`'ı açma |
| 2 | 🟠 | Çok sayıda `Not Defteri` penceresi açma |
| 3 | 🟠 | Çok sayıda `Hesap Makinesi` penceresi açma |
| 4 | 🟡 | Masaüstüne geçme |
| 5 | 🟠 | Açık pencereleri kapatma |
| 6 | 🔴 | Bilgisayarı doğrudan kapatma |
| 7 | 🔴 | Uyarı mesajı gösterip bilgisayarı yeniden başlatma |
| 8 | 🟢 | `System32` klasörünü açma |
| 9 | 🟠 | Ekranda çok sayıda ve rastgele `fare tıklamaları` gerçekleştirme |
| 10 | 🟡 | Birden fazla `Komut İstemi (CMD)` penceresi açma |
| 11 | 🟢 | Tarayıcıda `Google` veya `YouTube` açma |
| 12 | 🟠 | `Windows Explorer` işlemini sonlandırma ve yeniden başlatma |
| 13 | 🟡 | Ekran yönünü değiştirme |
| 14 | 🟡 | Hata mesajı pencereleri gösterme |
| 15 | 🟠 | `Alt + F4` ile pencereleri kapatma |
| 16 | 🟡 | Ekran görüntüsü alıp sahte donmuş ekran efekti oluşturma |
| 17 | 🟠 | Çok sayıda `Paint` penceresi açma |
| 18 | 🟡 | Ekran sürücüsü yenileyerek ekranı karartma |
| 19 | 🟡 | `Başlat menüsü`nü sürekli açıp kapatma|
| 20 | 🟠 | `Windows Güncelleştirme` ekranını taklit etme ve yeniden başlatma |
| 21 | 🔴 | Seçime göre ters çalışan kapatma onayı penceresi gösterme | 
| 22 | 🔴 | Windows oturumunu kapatma |
| 23 | 🟢 | `>_ Ni` penceresi açma |


**Riskli eventler yalnızca test ortamında ve izin verilen cihazlarda kullanılmalıdır.**



## 🛠️ Teknolojiler

- Python
- Tkinter
- PyAutoGUI
- PyGetWindow
- Pillow



## ©️ Telif Hakkı

Copyright (c) 2025-2026 Ni (bi-Ni-ary)



## 📜 Lisanslar

**MIT Lisansı** ve **Üçüncü Parti Lisanslar**

Detaylar için `LICENSE` ve `THIRD_PARTY_LICENSES.md` dosyalarına bakabilirsiniz.
