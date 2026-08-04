# Akilli-Tahta-Fatihi

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

Kurulumu tamamladıktan sonra `main.py` dosyasını çalıştırın.

```bash
python main.py
```

komutuyla çalıştırabilirsiniz.



## Çalışma Mantığı

Proje, rastgele seçilen olaylar (event) üzerine kurulu deneysel bir davranış sistemine sahiptir.

Program belirli aralıklarla bir event seçer ve seçilen eventin olasılığı `genome` adı verilen listeler üzerinden belirlenir.

### Genome Sistemi

`genome0`:
- Eventler arasındaki bekleme süresini belirler.

`genome1`:
- Her eventin seçilme olasılığını belirler.

Her döngüde sistem:
1. Belirlenen süre kadar bekler.
2. Olasılık değerlerine göre bir event seçer.
3. Seçilen event'i çalıştırır.
4. Yeni bir döngüye başlar.

Bu yapı, projenin ilk fikri olan evrimsel davranış simülasyonu konseptinden kalıntıdır.


### Eventler

Projede farklı davranış türleri bulunmaktadır:

- Uygulama açma/kapatma davranışları
- Pencere yönetimi
- Görsel efektler
- Klavye ve fare etkileşimleri
- Sahte sistem ekranları
- Eğlence amaçlı kullanıcı arayüzleri


Hiçbir şey yapmama dahil toplam 24 farklı event vardır.


#### Dikkat Gerektiren Eventler ⚠️

Bazı eventler sistem üzerinde daha güçlü etkilere sahiptir:

- Bilgisayarı kapatma veya yeniden başlatma
- Pencereleri kapatma
- Explorer işlemleriyle etkileşim
- Klavye/fare kontrolü
- Çok sayıda uygulama açma
- Ekranı değiştiren görsel efektler

Bu eventler yalnızca test ortamında ve izin verilen cihazlarda kullanılmalıdır.



## Teknolojiler

- Python
- Tkinter
- PyAutoGUI
- PyGetWindow
- Pillow



## Telif Hakkı

Copyright (c) 2025-2026 Ni (bi-Ni-ary)



## Lisans

MIT Lisansı

Detaylar için `LICENSE` ve `THIRD_PARTY_LICENSES.md` dosyalarına bakabilirsiniz.
