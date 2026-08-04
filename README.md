# Akilli-Tahta-Fatihi

Python ile geliştirilmiş deneysel bir Windows prank/automation yazılımı.

Bu proje eski okul günlerinden kalma bir deneydir. İlk fikri, davranışları olasılıksal olarak değişebilen evrimsel bir sistem simülasyonu üzerine kuruluydu. Daha sonra lise döneminde akıllı tahtalarda eğlence ve deney amacıyla kullanılan nostaljik bir projeye dönüştü.

Ni (bi-Ni-ary) tarafından Windows 10 x64 için geliştirilmiştir.

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


## Teknolojiler

- Python
- Tkinter
- PyAutoGUI
- PyGetWindow
- Pillow


## Lisans

MIT Lisansı

Detaylar için `LICENSE` ve `THIRD_PARTY_LICENSES.md` dosyalarına bakabilirsiniz.
