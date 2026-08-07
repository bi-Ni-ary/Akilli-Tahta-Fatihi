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

| Case No | Event |
|---|---|
| 0 | Hiçbir şey yapmayan boş event |
| 1 | Windows Defender açma |
| 2 | Çok sayıda Notepad penceresi açma |
| 3 | Çok sayıda Hesap Makinesi penceresi açma |
| 4 | Masaüstüne gitme |
| 5 | Açık olan tüm pencereleri kapatma |
| 6 | Doğrudan bilgisayarı kapatma |
| 7 | Bir uyarı mesajı penceresi gösterip ardından bilgisayarı yeniden başlatma |
| 8 | System32 klasörünü açma |
| 9 | Ekrana otomatik ve çok sayıda rastgele tıklama yapma |
| 10 | Aralarında biraz bekleyerek CMD açma |
| 11 | Tarayıcıda Google veya YouTube açma |
| 12 | Explorer'ı solandırma |
| 13 | Ekran yönünü arka arkaya değiştirme |
| 14 | Arka arkaya hata mesajı pencereleri açma |
| 15 | Birkaç kez otomatik ve arka arkaya Alt + F4 yaparak pencereleri kapatma |
| 16 | Ekran görüntüsü alıp açarak ekranı donmuş gibi gösterme |
| 17 | Çok sayıda Paint penceresi açma |
| 18 | `Win + Ctrl + Shift +  B` klavye kısayolu ise birkaç kez ekranı karatma |
| 19 | `Win` tuşunu kullanarak başlat menüsünü bir süre boyunc açıp kapatma |
| 20 | Windows 10'un güncellenme ekranını taklit edip sonrasında yeinden başlatma |
| 21 | `Bilgisayarınız kapatılsın mı?` diye sorar ama `Evet` denirse hiçbir şey yapmaz, `Hayır` denirse kapatır | 
| 22 | Windows Oturumunu kapatma |
| 23 | İçinde `>_ Ni` yazan bir pencere açma |


#### Dikkat Gerektiren Eventler ⚠️

Bazı eventler sistem üzerinde daha güçlü etkilere sahiptir:

- Bilgisayarı kapatma veya yeniden başlatma  `(case 6, 7, 21)`
- Pencereleri kapatma  `(case 5, 15)`
- Explorer işlemleriyle etkileşim  `(case 12)`
- Klavye/fare kontrolü  `(case 9)`
- Çok sayıda uygulama açma  `(case 2, 3, 10, 17)`
- Ekranı değiştiren görsel efektler  `(case 16)`


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
