##
##  DomainCTRL - Domain Kontrol Programı
##
##  Copyright (C) 2017 - Şerif İnanır
##  e-mail: sheriffnnr[at]gmail.com
##
##  DomainCTRL is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by the
## Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## DomainCTRL is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program.  If not, see <http://www.gnu.org/licenses/>.
#####################################################################################


#  PROGRAM MANTIĞI
#
# Siteye 'requests' isimli 3. parti modül ile
# bağlanmaya çalışır. Bağlanırsa böyle bir site var
# demektir ve 'Kullanılamaz' çıktısını verir. Eğer
# bağlantı sağlanamazsa girilen alan adını
# 'Kullanılabilir' olarak nitelendirir.


#-*- coding: utf-8 -*-
from tkinter import*
import requests
class Domain(Tk):
    def __init__(self,_title):
        Tk.__init__(self)

        # GENEL TKİNTER FONKSİYONLARI
        self.geometry("+200+90")
        self.title(_title)
        self.widgets()
        self.resizable(False,False)


    # ARAYÜZ KODLARI
    def widgets(self):
        # ARKAPLAN RENGİ
        backcolor=Label(width=500,height=500,
                        bg=_bg)
        backcolor.place(x=-5,y=-5)

        # PROGRAM İSMİ
        process_name=Label(text="     Ctrl-Domain     \n",
                           font=("Purisa",32,"bold"),
                           bg=_bg,fg=_fg)
        process_name.pack()

        # URL AÇIKLAMA
        info=Label(text="Site URL (ÖRN: siteismi.com)",
                   bg=_bg,fg=_fg,
                   font=("Ubuntu",13))
        info.pack()

        # GİRDİ KISMI
        self.url=Entry(width=30,
                  font=("Ubuntu",12,"bold"),
                  bg="#dcdcdc",
                  fg="#363636")
        self.url.pack()

        a123=Label(text="",bg=_bg)
        a123.pack()

        # KONTROL BUTONU
        ctrl=Button(text="Kontrol Et",
                    bg="#1c1c1c",fg=_fg,
                    border=0,
                    font=("Ubuntu",13,"bold"),
                    activebackground="#828282",
                    command=self.entry_control)
        ctrl.pack()

        # PROGRAM BİLGİSİ
        self.info=Label(text="DURUM",
                        font=("Ubuntu",14,"bold"),
                        bg=_bg,fg="#c0c0c0")
        self.info.pack()

        # PROGRAMCI BİLGİSİ
        my=Label(text="\nŞerif İnanır~ Alanya Alaaddin Keykubat University",
                 font=("Ubuntu",11),
                 bg=_bg,fg="#828282")
        my.pack()





    # GİRDİ KONTROL KISMI
    def entry_control(self):
        _url_=self.url.get()
        if not _url_:
            self.info["text"]="URL Girmedin"
            self.info["fg"]="#c0c0c0"
        else:
            self.connect(_url_)

    # BAĞLANTI KISMI
    def connect(self,_url_):
        try:
            INET=requests.get("https://www.google.com")
            try:
                domain_control=requests.get("http://www."+_url_)
                self.info["text"]="Kullanılamaz"
                self.info["fg"]=_error
            except:
                self.info["text"]="KULLANILABİLİR"
                self.info["fg"]=_accept
        except:
            self.info["text"]="Bağlantın Kötü"
            self.info["fg"]=_error

_bg="#363636"
_fg="#f2f2f2"

_error="#c60000"
_accept="#00ff00"

if __name__=="__main__":
    try:
        root=Domain("LapRooz~ Ctrl-Domain").mainloop()
    finally:
        pass
