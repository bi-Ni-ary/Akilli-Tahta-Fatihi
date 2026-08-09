# 🖥️ Akilli-Tahta-Fatihi

> 📌 README Language: Turkish/Türkçe 🇹🇷

&nbsp;

**Python** ile geliştirilmiş deneysel bir Windows **prank/automation** yazılımı.

Bu proje eski okul günlerinden kalma bir deneydir. İlk fikri, davranışları olasılıksal olarak değişebilen evrimsel bir sistem simülasyonu üzerine kuruluydu. Daha sonra lise döneminde akıllı tahtalarda eğlence ve deney amacıyla kullanılan nostaljik bir projeye dönüştü.


*Ni (bi-Ni-ary) tarafından 2025-2026 yıllarında **Windows 10 x64** için geliştirilmiştir.*

*Diğer Windows sürümlerinde de büyük ölçüde çalışması beklenmektedir **ancak tüm sürümlerde test edilmemiştir.***



## ⚠️ Uyarı

**Bu proje sonlandırılana kadar sürekli çalışan döngü yapıları kullanır, bazı sistem etkileşimleri gerçekleştirebilir ve kullanıcı deneyimini değiştirebilecek davranışlar içerebilir.**

- Yalnızca size ait veya kullanım izniniz olan cihazlarda çalıştırın.
- Test amacıyla güvenli ortamlarda kullanın.
- Yanış kullanımdan veya kullanımdan doğabilecek sonuçlardan kullanıcı sorumludur.

**Bu proje eğitim, deney ve nostaljik amaçlarla paylaşılmıştır.**



## 🔒 Gizlilik ve Ağ Kullanımı

Bu proje herhangi bir kullanıcı verisi **toplamaz**, **kaydetmez**
ve herhangi bir uzak sunucuya **göndermez.**

Programın normal çalışma mantığında herhangi bir ağ
iletişimi **bulunmamaktadır.**

Bazı eventler kullanıcı deneyimi amacıyla internet
tarayıcısını açabilir. Bu durumda internet erişimi,
yalnızca ilgili event tetiklendiğinde `Google` veya `YouTube`
gibi servisleri varsayılan tarayıcı üzerinden açmak için
kullanılır.

Bunun dışında:

- Kullanıcı dosyaları **okunmaz** veya **değiştirilmez.**
- Kişisel bilgiler **toplanmaz.**
- Arka planda veri gönderimi **yapılmaz.**
- Takip, analiz veya telemetri sistemi **bulunmaz.**

Programın gerçekleştirdiği sistem etkileşimleri **yalnızca
kodda belirtilen event davranışlarıyla sınırlıdır.**



## ✨ Genel Özellikler

Bu proje, `Windows` üzerinde çeşitli sistem etkileşimleri gerçekleştirebilen **deneysel bir otomasyon yazılımıdır.**

Başlıca özellikleri:

- Kullanıcı deneyimini değiştirebilecek **çeşitli sistem etkileşimleri** gerçekleştirebilir.
- **Klavye ve fare girişleri** üzerinde otomatik işlemler gerçekleştirebilir.
- **Açık pencereler ve masaüstü** üzerinde çeşitli işlemler yapabilir.
- **Görsel efektler** ve kullanıcı arayüzü tabanlı **deneysel ekranlar** oluşturabilir.
- **Bildirim, uyarı ve sahte sistem ekranı** benzeri görsel deneyimler oluşturabilir.
- Belirli eventler aracılığıyla **rastgele ve olasılıksal davranışlar** sergileyebilir.
- **Windows bileşenleri ve uygulamalarıyla etkileşim** kurabilir.
- **Deneysel davranış sistemi** sayesinde **farklı çalışma senaryoları** oluşturabilir.



## 📋 Gereksinimler

### Zorunlu

- `Windows 10` veya `Windows 11` (`64-bit` önerilir)
- `Python 3.10` veya üzeri
- Gerekli `Python` paketleri (`requirements.txt`)


### Opsiyonel
- `Git` *(Projeyi klonlamak için)*
- `PyInstaller` *(Yalnızca `.exe` oluşturmak için)*



## ⚙️ Kurulum

### 1. Projeyi Kurun

Projeyi iki farklı yöntemle indirebilirsiniz.


#### A. `Git` ile projeyi klonlayın (geliştiriciler için):

```bash
git clone https://github.com/bi-Ni-ary/Akilli-Tahta-Fatihi.git
```

ardından:

```bash
cd Akilli-Tahta-Fatihi
```


#### B. `ZIP` indirerek kurulum (normal kullanıcılar için):

1. `GitHub` sayfasından `Code → Download ZIP` seçeneğiyle projeyi indirin.
2. `ZIP` dosyasını çıkarın.
3. Proje klasöründe **terminal** açın.


### 2. Gerekli Kütüphaneleri Yükleyin

```bash
pip install -r requirements.txt
```

veya alternatif olarak kütüphaneleri manuel şekilde de yükleyebilirsiniz:

```bash
pip install pyautogui pygetwindow pillow
```



## ▶️ Kullanım

**Programı çalıştırarak tüm sorumluluğu kabul etmiş olduğunuzu unutmayın! Yalnızca kendi cihanızda veya çalıştırma izniniz olan ortamlarda çalıştırın.**

**Geliştirici, yazılımın yanlış kullanımından veya oluşabilecek
zararlardan sorumlu değildir.**

**Programın kapatılana kadar sürekli çalışan döngüler kullandığını unutmayın.**

&nbsp;

Kurulumu tamamladıktan sonra `src/main.py` dosyasını çalıştırın:

```bash
python src/main.py
```

> Daha fazla etki için **dikkatli olmak şartıyla** programı aynı anda birden fazla kez de çalıştırabilirsiniz.



## ⏹️ Durdurma

### Terminal üzerinden Python formatında çalıştırıldıysa:
- `CTRL + C` ile **işlemi sonlandırabilir** veya **terminali kapatabilirsiniz.**


### EXE dosyası üzerinden çalıştırıldıysa:

1. **Görev Yöneticisi**ni açın (`CTRL + SHIFT + ESC`)
2. İlgili işlemi (`Akilli-Tahta-Fatihi.exe`) bulun ve seçin
3. **Görevi sonlandır** seçeneğini kullanın

> Sadece **Görev Yöneticisi**nden ilgili görev veya görevleri sonlandırmak iki durumda da ve farklı durumlarda da büyük ihtimalle işe yarar ve yeterli olur.



## 📸 Demo

*(YAKINDA GELECEK)*



## 📦 EXE Oluşturma (PyInstaller)

Projeyi tek dosyalı `.exe` haline getirmek için `PyInstaller` kullanılabilir.


### PyInstaller kurulumu:

```bash
pip install pyinstaller
```

### EXE oluşturma:

```cmd
pyinstaller --onefile --windowed ^
--name Akilli-Tahta-Fatihi ^
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

Oluşturulan **EXE** dosyası: `dist/Akilli-Tahta-Fatihi.exe`

&nbsp;

#### Komut Açıklamaları

| Parametre | Açıklama |
|:---:|:---|
| `--onefile` | Tüm dosyaları tek bir `.exe` içerisinde toplar |
| `--windowed` | Konsol penceresi açmadan çalıştırır |
| `--name` | Oluşturulacak `.exe` dosyasının dosya adını belirler, **istenirse farklı ad verilebilir** |
| `--hidden-import` | `PyInstaller`'ın otomatik algılayamadığı paketleri dahil eder |
| `--add-data` | Harici dosyaları *(ör. GIF vb.*) `EXE` içine ekler |
| `src/main.py` | Ana `Python` dosyasını belirtir |


#### İkon Ekleme (Opsiyonel)

Bir `.ico` dosyası kullanarak oluşturulacak **EXE** dosyasına ikon eklemek için:

```cmd
--icon "assets/icon.ico"
```

parametresini kullanabilirsiniz. 

**`"assets/icon.ico"` yerine `.ico` dosyasının konumu neyse onu yazınız.**



## 🧠 Çalışma Mantığı

- Proje, rastgele seçilen olaylar (event) üzerine kurulu deneysel bir davranış sistemine sahiptir.

- Program belirli aralıklarla bir event seçer ve her eventin seçilme olasılığı `genome` adı verilen listeler üzerinden belirlenir.

- Eventlerin çalıştırılması için **Python 3.10** ile gelen `match / case` yapısı kullanılır.

- Durdurulana kadar sürekli çalışabilmesi için `While True:` döngüleri kullanılır.


### 🧬 Genome Sistemi

`genome0`:
- Eventler arasındaki **bekleme süresinin aralığını** belirler.

`genome1`:
- Her eventin **seçilme olasılığını** belirler.

Her döngüde sistem:
1. Belirlenen süre kadar bekler.
2. Olasılık değerlerine göre bir event seçer.
3. Seçilen eventi çalıştırır.
4. Yeni bir döngüye başlar.

*Bu yapı, projenin ilk fikri olan evrimsel davranış simülasyonu konseptinden bir kalıntıdır.*


### 🎲 Eventler

Toplamda `24` farklı event bulunmaktadır.

- **Event ID**: Kod içerisindeki `case` değerini temsil eden benzersiz event numarası.
- **Risk Seviyeleri**: 🟢 Güvenli | 🟡 Orta | 🟠 Yüksek | 🔴 Kritik


| Event ID | Risk Seviyesi | Açıklama |
|:---:|:---:|:---|
| 0 | 🟢 | Hiçbir işlem yapmayan **boş** event |
| 1 | 🟢 | `Windows Defender`'ı açma |
| 2 | 🟠 | Çok sayıda `Not Defteri` penceresi açma |
| 3 | 🟠 | Çok sayıda `Hesap Makinesi` penceresi açma |
| 4 | 🟡 | Açık pencereleri küçültüp **masaüstüne geçme**|
| 5 | 🟠 | Açık pencereleri **kapatma** |
| 6 | 🔴 | Bilgisayarı **doğrudan kapatma** |
| 7 | 🔴 | Uyarı mesajı gösterip bilgisayarı **yeniden başlatma** |
| 8 | 🟢 | `System32` klasörünü açma |
| 9 | 🟠 | Ekranda çok sayıda ve rastgele **fare tıklamaları** gerçekleştirme |
| 10 | 🟡 | Birden fazla `Komut İstemi (CMD)` penceresi açma |
| 11 | 🟢 | Tarayıcıda `Google` veya `YouTube` açma |
| 12 | 🟠 | `Windows Explorer` işlemini **sonlandırma** ve **yeniden başlatma** |
| 13 | 🟡 | Ekran yönünü değiştirerek **ekranı döndürme efekti** yapma |
| 14 | 🟡 | **Sahte hata mesajı** pencereleri gösterme |
| 15 | 🟠 | `Alt + F4` ile pencereleri kapatma |
| 16 | 🟡 | Ekran görüntüsü alıp **sahte donmuş ekran efekti** oluşturma |
| 17 | 🟠 | Çok sayıda `Paint` penceresi açma |
| 18 | 🟡 | Ekran sürücüsünü yenileyerek **kısa süreli görüntü kesintisi** oluşturma |
| 19 | 🟡 | `Başlat menüsü`nü sürekli açıp kapatma |
| 20 | 🔴 | `Windows Güncelleştirme` ekranını taklit etme ve **yeniden başlatma** |
| 21 | 🔴 | **Seçime göre ters çalışan** kapatma onayı penceresi gösterme **(`Hayır` seçilirse bilgisayar kapanır)** | 
| 22 | 🔴 | `Windows oturumu`nu kapatma |
| 23 | 🟢 | `>_ Ni` penceresi açma |


**Riskli eventler yalnızca test ortamında ve izin verilen cihazlarda kullanılmalıdır.**



## 🏛️ Projenin Durumu

Bu proje, **2025 yılında *(nisan, mayıs ve haziran aylarında)*** geliştirilmiş deneysel ve eğlence amaçlı kullanılmış nostaljik bir projedir.

Projenin mevcut kaynak kodu büyük ölçüde orijinal haliyle
korunmaktadır. Yeni özellikler eklemek veya kodu güncellemek
yerine projenin orijinal yapısını ve çalışma mantığını
korumak amaçlanmıştır.



## 🛠️ Teknolojiler

- Python
- Tkinter
- PyAutoGUI
- PyGetWindow
- Pillow
- PyInstaller &ensp;*(Opsiyonel, yalnızca **EXE** oluşturmak için)*



## ©️ Telif Hakkı

Copyright (c) 2025-2026 Ni (bi-Ni-ary)



## 📜 Lisanslar

Bu proje **MIT Lisansı** altında yayımlanmaktadır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.

Kullanılan üçüncü parti kütüphanelerin lisans bilgileri için: `THIRD_PARTY_LICENSES.md` dosyasına bakabilirsiniz.
