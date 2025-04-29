import os#temp ve prefetch için
import ctypes
import shutil
import tkinter as tk#ana arayüz
from tkinter import messagebox#hata ve uyarı mesajları
import winreg#regedit e giriş
import subprocess
import webbrowser

####################################################################################

# tkinter kodları
root = tk.Tk()
root.geometry('400x500')
root.title('PCCLEANUP')
root.configure(bg='royalblue')





# sağ alt signature
title_label = tk.Label(root,text='By Yiğit Murat', font=('Arial', 10), fg='#000000', bg='white')
title_label.pack(pady=3, side='bottom', anchor='e')



####################################################################################





        

####################################################################################

def temp_prefetch_download_del():
    response = messagebox.askquestion("Cache Dosyaları Temizleme İşlemi", "Bu işlem Prefetch ve Temp klasörlerinde biriken gereksiz çerez dosyaları siler.Devam etmek istiyor musunuz?")
    if response == 'yes':
        # temp clean
        temp_folder = os.environ.get('SystemRoot') + '\\Temp'
        for filename in os.listdir(temp_folder):
            filepath = os.path.join(temp_folder, filename)
            try:
                os.remove(filepath)
            except:
                pass

        # prefetch clean
        prefetch_folder = os.environ.get('SystemRoot') + '\\Prefetch'
        for filename in os.listdir(prefetch_folder):
            if filename.endswith('.pf'):
                filepath = os.path.join(prefetch_folder, filename)
                try:
                    os.remove(filepath)
                except:
                    pass


        # İndirilenler klasörü del
        download_folder = os.environ.get('USERPROFILE') + '\\Downloads'
        response = messagebox.askquestion("İndirilenler Klasörü Silme İşlemi", "İndirilenler klasöründeki tüm dosyaları silmek istediğinize emin misiniz?")
        if response == 'yes':
            shutil.rmtree(download_folder)
            tk.messagebox.showinfo("İşlem Tamamlandı", "İndirilenler klasöründeki tüm dosyalar başarıyla silindi.")
        else:
            tk.messagebox.showwarning("İşlem İptal Edildi", "İndirilenler klasöründeki dosyalar silinmedi.")
    else:
        tk.messagebox.showwarning("İşlem İptal Edildi", "Program durduruluyor.")

####################################################################################
def masaustunu_düzenle_wallpaper_duzenle():
    response = messagebox.askquestion("Masaüstü Temizleme İşlemi", "Bu işlem masaüstünde bulunan tüm dosyaları C diskinin içinde Masaüstü adında bir klasör oluşturarak bir klasöre toplayacak. Ayrıca duvar kağıdı rengini siyah yapacak. Devam etmek istiyor musunuz?")
    if response == 'yes':
        # C:\Masaüstü klasörünün yolu
        target_folder = r"C:/Masaüstü"

        # Eğer Masaüstü klasörü zaten varsa sil
        if os.path.exists(target_folder):
            shutil.rmtree(target_folder)

        # Yeni Masaüstü klasörünü oluştur
        os.makedirs(target_folder)

        # Mevcut kullanıcının Masaüstü klasörünün yolu
        desktop_folder = os.path.expanduser("~\\Desktop")

        # Masaüstündeki tüm dosya ve klasörleri al
        files = os.listdir(desktop_folder)

        # Dosyaları ve klasörleri Masaüstü klasörüne taşı
        for file in files:
            source_path = os.path.join(desktop_folder, file)
            target_path = os.path.join(target_folder, file)
            shutil.move(source_path, target_path)
        
        # YmeFast klasörünü oluştur
        ymefast_folder = "C:/YmeFast"
        os.makedirs(ymefast_folder)
        
        # Siyahwp.png dosyasını YmeFast klasörüne kopyala
        source_path = "./Yıl Sonu Projesi/Siyahwp.png"
        target_path = os.path.join(ymefast_folder, "Siyahwp.png")
        shutil.copy(source_path, target_path)

        # Duvar kağıdını değiştir
        SPI_SETDESKWALLPAPER = 20
        SPI_SETDESKCOLOR = 1
        wallpaper_path = "C:/YmeFast/Siyahwp.png"
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 0)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKCOLOR, 0, 0)

        tk.messagebox.showinfo("İşlem Tamamlandı", "Masaüstü düzenleme işlemi ve duvar kağıdı değiştirme işlemi başarıyla tamamlandı.")
    else:
        tk.messagebox.showwarning("İşlem İptal Edildi", "Masaüstü düzenlenmedi.")
        
        



def cop_temizle():
    response = messagebox.askquestion("Geri Dönüşüm Kutusu Temizleme İşlemi", "Bu işlem Geri Dönüşüm kutusundaki tüm dosyaları siler. Devam etmek istiyor musunuz?")
    if response == 'yes':
        trash_folder = os.environ.get('USERPROFILE') + '\\AppData\\Local\\Microsoft\\Windows\\Explorer'
        os.system('PowerShell.exe -NoProfile -Command Clear-RecycleBin -Force')
        tk.messagebox.showinfo("İşlem Tamamlandı", "Geri Dönüşüm Kutusundaki tüm dosyalar başarıyla silindi.")
    else:
        tk.messagebox.showwarning("İşlem İptal Edildi", "Geri Dönüşüm kutusundaki dosyalar silinmedi.")




def web_site():
    webbrowser.open("https://teknoparkankara.meb.k12.tr/")
####################################################################################

#çöp sil buton
empty_trash_button = tk.Button(root, text='Geri Dönüşüm Kutusunu Temizle', font=('Arial', 12), fg='#000000', bg='white', command=cop_temizle)
empty_trash_button.pack(pady=20)

#dosya sil buton
delete_button = tk.Button(root, text='Çerez Dosyalarını Temizle', font=('Arial', 12), fg='#000000', bg='white', command=temp_prefetch_download_del)
delete_button.pack(pady=20)

####################################################################################





# duvar kağıdı + masaüstü buton uygula butonu
duvar_kagıdı_masasutunu_duzenle_buton = tk.Button(root, text='Masaüstünü Düzenle', font=('Arial', 12), fg='#000000', bg='white', command=masaustunu_düzenle_wallpaper_duzenle)
duvar_kagıdı_masasutunu_duzenle_buton.pack(pady=20)



# website buton
website_button = tk.Button(root, text="Web Sitesine Git", font=("Arial", 12), fg="#000000", bg="white", command=web_site)
website_button.pack(pady=20)



#yuksek performansa alma
def yuksek_perform_al():
    response = messagebox.askquestion("İşlemci Hızını Arttırma İşlemi", "Bu işlem işlemcinin GHz değerini artırarak performans artışına neden olur. Eğer işlemcinizin soğutma desteği yeterli değilse bu işlemden vazgeçin. Devam etmek istiyor musunuz?")
    if response == 'yes':
        try:
            subprocess.run(["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"], capture_output=True, text=True)
            messagebox.showinfo("İşlem Tamamlandı.", "Güç ayarları yüksek performansa alınarak işlemcinin GHz değerleri arttırıldı.")
        except Exception as e:
            messagebox.showerror("İşlem Başarısız", "Güç ayarları değiştirilemedi: " + str(e))
    else:
        messagebox.showwarning("İşlem İptal Edildi", "İşlemcinin GHz değeri artırılmadı.")
    #not:186-191 arası satırlardaki kod powershelle erişiyor oradan değiştiriyor.

#yüksek performans buton
yuksek_performans_buton = tk.Button(root, text="İşlemciyi Hızlandır", font=("Arial",12),fg="#000000", bg="white",command=yuksek_perform_al)
yuksek_performans_buton.pack(pady=20)




####################################################################################

#Asagı kısım not

# Metin kutusunun font,yükseklik v.b
metinkutu_yazı = tk.Text(root, font=('Arial', 12), wrap='word', height=8)

# Not
note_text = "'Geri Dönüşüm Kutusunu Temizle' tuşuna basarak geri dönüşüm kutusundaki dosyaları temizleyebilirsiniz.'Çerez Dosyalarını Temizle' tuşuna basarak bilgisayarınızda zamanla oluşan çerez dosyalarını silebilirsiniz.Ayrıca indirilenler klasörünü temizleyebilirsiniz.'Masaüstünü Düzenle' tuşuna basarak ise masaüstü arkaplan renginizi siyah yapabilirsiniz.Ayrıca masaüstünde bulunan simgeleri yerel diskinizde Masaüstü adlı klasöre taşıyabilirsiniz.'Web Sitesine Git' tuşuna basarak okuduğum okulun websitesini ziyaret edebilirsiniz.'İşlemciyi Hızlandır' tuşuna basarak işlemcinizin daha hızlı çalışmasını sağlayabilirsiniz.Program ile herhangi bir sorun oluşursa yigitmuraterenulug@gmail.com adresine mail atabilirsiniz."

# Not add metin box
metinkutu_yazı.insert('1.0', note_text)
metinkutu_yazı.configure(state='disabled')  

# metin box yeri
metinkutu_yazı.pack(pady=10)

####################################################################################

root.mainloop()



