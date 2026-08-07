# Akilli-Tahta-Fatihi


> 📌 README Language: Turkish/Türkçe 🇹🇷


Python ile geliştirilmiş deneysel bir Windows prank/automation yazılımı.

Bu proje eski okul günlerinden kalma bir deneydir. İlk fikri, davranışları olasılıksal olarak değişebilen evrimsel bir sistem simülasyonu üzerine kuruluydu. Daha sonra lise döneminde akıllı tahtalarda eğlence ve deney amacıyla kullanılan nostaljik bir projeye dönüştü.

Ni (bi-Ni-ary) tarafından 2025-2026 yıllarında Windows 10 x64 için geliştirilmiştir.

Diğer Windows sürümlerinde de büyük ölçüde çalışması beklenmektedir ancak tüm sürümlerde test edilmemiştir.



## Uyarı ⚠️

Bu proje bazı sistem etkileşimleri gerçekleştirebilir ve kullanıcı deneyimini değiştirebilecek davranışlar içerebilir.

- Yalnızca size ait veya kullanım izniniz olan cihazlarda çalıştırın.
- Test amacıyla güvenli ortamlarda kullanın.
- Kullanımdan doğabilecek sonuçlardan kullanıcı sorumludur.

Bu proje eğitim, deney ve nostaljik amaçlarla paylaşılmıştır.



## Kurulum

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



## Kullanım

Kurulumu tamamladıktan sonra `src/main.py` dosyasını çalıştırın.

```bash
python src/main.py
```

komutuyla çalıştırabilirsiniz.

> Daha fazla etki için programı aynı anda birden fazla kez de çalıştırabilirsiniz.



## EXE Oluşturma (PyInstaller)

Projeyi tek dosyalı `.exe` haline getirmek için PyInstaller kullanılabilir.


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

Oluşturulan EXE dosyası: `dist/main.exe`



## Çalışma Mantığı

Proje, rastgele seçilen olaylar (event) üzerine kurulu deneysel bir davranış sistemine sahiptir.

Program belirli aralıklarla bir event seçer ve her event'in seçilme olasılığı `genome` adı verilen listeler üzerinden belirlenir.

### Genome Sistemi

`genome0`:
- Eventler arasındaki bekleme süresinin aralığını belirler.

`genome1`:
- Her event'in seçilme olasılığını belirler.

Her döngüde sistem:
1. Belirlenen süre kadar bekler.
2. Olasılık değerlerine göre bir event seçer.
3. Seçilen event'i çalıştırır.
4. Yeni bir döngüye başlar.

Bu yapı, projenin ilk fikri olan evrimsel davranış simülasyonu konseptinden bir kalıntıdır.


### Eventler

Projede farklı davranış türleri bulunmaktadır:

- Uygulama açma/kapatma davranışları
- Pencere yönetimi
- Görsel efektler
- Klavye ve fare etkileşimleri
- Sahte sistem ekranları
- Eğlence amaçlı kullanıcı arayüzleri


"Hiçbir şey yapmama" event'i dahil toplamda `24` farklı event vardır.


#### Dikkat Gerektiren Eventler ⚠️

Bazı eventler sistem üzerinde daha güçlü etkilere sahiptir:

- Bilgisayarı kapatma veya yeniden başlatma  `(case 6, 7, 21)`
- Pencereleri kapatma  `(case 5, 15)`
- Explorer işlemleriyle etkileşim  `(case 12)`
- Klavye/fare kontrolü  `(case 9)`
- Çok sayıda uygulama açma  `(case 2, 3, 10, 17)`
- Ekranı değiştiren görsel efektler  `(case 16)`

| Event | Case |
|---|---|
| Python | İyi |
| React | Orta |

Bu eventler yalnızca test ortamında ve izin verilen cihazlarda kullanılmalıdır.



## Teknolojiler

- Python
- Tkinter
- PyAutoGUI
- PyGetWindow
- Pillow



## Telif Hakkı

Copyright (c) 2025-2026 Ni (bi-Ni-ary)



## Lisanslar

MIT Lisansı ve Üçüncü Parti Lisanslar

Detaylar için `LICENSE` ve `THIRD_PARTY_LICENSES.md` dosyalarına bakabilirsiniz.
