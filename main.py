from customtkinter import *
from PIL import Image
import os
import sys

app = CTk()
app.title("Astronomers Guide")
app.geometry("700x700")
app.resizable(False, False)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


bg_image_path=resource_path('assests/bgimage.jfif')
bg_image=CTkImage(
    light_image=Image.open(bg_image_path),
    dark_image=Image.open(bg_image_path),
    size=(700, 700)
)

Planets_image_path=resource_path('assests/Planets.jfif')
Planets_image=CTkImage(
    light_image=Image.open(Planets_image_path),
    dark_image=Image.open(Planets_image_path),
    size=(250, 250)
)

Solar_System_image_path=resource_path('assests/Solar Sysyem.jfif')
Solar_System_image=CTkImage(
    light_image=Image.open(Solar_System_image_path),
    dark_image=Image.open(Solar_System_image_path),
    size=(250, 250)
)

ExoPlanets_image_path=resource_path('assests/Exoplanets.jfif')
ExoPlanets_image=CTkImage(
    light_image=Image.open(ExoPlanets_image_path),
    dark_image=Image.open(ExoPlanets_image_path),
    size=(250, 250)
)

Stars_image_path=resource_path('assests/Stars.jfif')
Stars_image=CTkImage(
    light_image=Image.open(Stars_image_path),
    dark_image=Image.open(Stars_image_path),
    size=(250, 250)
)

Galaxies_image_path=resource_path('assests/Galaxies.jfif')
Galaxies_image=CTkImage(
    light_image=Image.open(Galaxies_image_path),
    dark_image=Image.open(Galaxies_image_path),
    size=(250, 250)
)

Mercury_image_path=resource_path('assests/Mercury.jfif')
Mercury_image=CTkImage(
    light_image=Image.open(Mercury_image_path),
    dark_image=Image.open(Mercury_image_path),
    size=(250, 250)
)

Venus_image_path=resource_path('assests/Venus.jfif')
Venus_image=CTkImage(
    light_image=Image.open(Venus_image_path),
    dark_image=Image.open(Venus_image_path),
    size=(250, 250)
) 

Earth_image_path=resource_path('assests/Earth.jfif')
Earth_image=CTkImage(
    light_image=Image.open(Earth_image_path),
    dark_image=Image.open(Earth_image_path),
    size=(250, 250)
)

Mars_image_path=resource_path('assests/Mars.jfif')
Mars_image=CTkImage(
    light_image=Image.open(Mars_image_path),
    dark_image=Image.open(Mars_image_path),
    size=(250, 250)
)

Jupiter_image_path=resource_path('assests/Jupiter.jfif')
Jupiter_image=CTkImage(
    light_image=Image.open(Jupiter_image_path),
    dark_image=Image.open(Jupiter_image_path),
    size=(250, 250)
)

Saturn_image_path=resource_path('assests/Saturn.jfif')
Saturn_image=CTkImage(
    light_image=Image.open(Saturn_image_path),
    dark_image=Image.open(Saturn_image_path),
    size=(250, 250)
)

Uranus_image_path=resource_path('assests/Uranus.jfif')
Uranus_image=CTkImage(
    light_image=Image.open(Uranus_image_path),
    dark_image=Image.open(Uranus_image_path),
    size=(250, 250)
)

Neptune_image_path=resource_path('assests/Neptune.jfif')
Neptune_image=CTkImage(
    light_image=Image.open(Neptune_image_path),
    dark_image=Image.open(Neptune_image_path),
    size=(250, 250)
)

Sirius_image_path=resource_path('assests/Sirius A.jfif')
Sirius_image=CTkImage(
    light_image=Image.open(Sirius_image_path),
    dark_image=Image.open(Sirius_image_path),
    size=(250, 250)
)

Canopus_image_path=resource_path('assests/Canopus.jfif')
Canopus_image=CTkImage(
    light_image=Image.open(Canopus_image_path),
    dark_image=Image.open(Canopus_image_path),
    size=(250, 250)
)

Arcturus_image_path=resource_path('assests/arcturus.jfif')
Arcturus_image=CTkImage(
    light_image=Image.open(Arcturus_image_path),
    dark_image=Image.open(Arcturus_image_path),
    size=(250, 250)
)

Alpha_image_path=resource_path('assests/Alpha Centauri A.jfif')
Alpha_image=CTkImage(
    light_image=Image.open(Alpha_image_path),
    dark_image=Image.open(Alpha_image_path),
    size=(250, 250)
)

Vega_image_path=resource_path('assests/Vega.jfif')
Vega_image=CTkImage(
    light_image=Image.open(Vega_image_path),
    dark_image=Image.open(Vega_image_path),
    size=(250, 250)
)

Capella_image_path=resource_path('assests/Capella.jfif')
Capella_image=CTkImage(
    light_image=Image.open(Capella_image_path),
    dark_image=Image.open(Capella_image_path),
    size=(250, 250)
)

Rigel_image_path=resource_path('assests/Rigel.jfif')
Rigel_image=CTkImage(
    light_image=Image.open(Rigel_image_path),
    dark_image=Image.open(Rigel_image_path),
    size=(250, 250)
)

Procyon_image_path=resource_path('assests/Procyon.jfif')
Procyon_image=CTkImage(
    light_image=Image.open(Procyon_image_path),
    dark_image=Image.open(Procyon_image_path),
    size=(250, 250)
)

Sun_image_path=resource_path('assests/Sun.jfif')
Sun_image=CTkImage(
    light_image=Image.open(Sun_image_path),
    dark_image=Image.open(Sun_image_path),
    size=(250, 250)
)

def start():
    for widget in app.winfo_children():
        widget.destroy()
    lbl = CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Planets_image
    )
    lbl.place(relx=175/700, rely=175/700, anchor="center")    

    lbl = CTkLabel(
        master=app,
        text="",
        image=Stars_image
    )
    lbl.place(relx=525/700, rely=175/700, anchor="center")

    lbl = CTkLabel(
        master=app,
        text="",
        image=Galaxies_image
    )
    lbl.place(relx=175/700, rely=475/700, anchor="center") 

    lbl = CTkLabel(
        master=app,
        text="",
        image=Sun_image
    )
    lbl.place(relx=525/700, rely=475/700, anchor="center")

    Planetsbtn = CTkButton(
        master=app,
        text="Planets",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Planets,
        hover="#000000"
    )
    Planetsbtn.place(relx=175/700, rely=175/700, anchor="center")  

    Starsbtn = CTkButton(
        master=app,
        text="Stars",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=stars,
        hover="#000000"
    )
    Starsbtn.place(relx=525/700, rely=175/700, anchor="center")      

    Galaxiesbtn = CTkButton(
        master=app,
        text="Galaxies",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Galaxies,
        hover="#000000"
    )
    Galaxiesbtn.place(relx=175/700, rely=475/700, anchor="center") 

    Sunbtn = CTkButton(
        master=app,
        text="Sun",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Sun,
        hover="#000000"        
    )
    Sunbtn.place(relx=525/700, rely=475/700, anchor="center")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=home,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Planets():
    for widget in app.winfo_children():
        widget.destroy()
    lbl = CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Solar_System_image
    )
    lbl.place(relx=175/700, rely=0.5, anchor="center")    

    lbl = CTkLabel(
        master=app,
        text="",
        image=ExoPlanets_image
    )
    lbl.place(relx=525/700, rely=0.5, anchor="center")

    SolarSystembtn = CTkButton(
        master=app,
        text="Solar System",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=SolarSystem,
        hover="#000000"
    )
    SolarSystembtn.place(relx=175/700, rely=0.5, anchor="center")  

    ExoPlanetsbtn = CTkButton(
        master=app,
        text="Exoplanets",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Exoplanets,
        hover="#000000"
    )
    ExoPlanetsbtn.place(relx=525/700, rely=0.5, anchor="center")      
 
    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=start,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def stars():
    for widght in app.winfo_children():
        widght.destroy()
    
    lbl = CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=start,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center")   

    buttons_frame= CTkFrame(
        master=app,
        fg_color="#000000"
    )
    buttons_frame.place(relx=0.5, rely=0.45, anchor="center")

    Siriusbtn=CTkButton(
        master=buttons_frame,
        text="Sirius A",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Sirius,
        hover="#000000"        
    )
    Siriusbtn.pack(pady=20)

    Canopusbtn=CTkButton(
        master=buttons_frame,
        text="Canopus",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Canopus,
        hover="#000000"        
    )
    Canopusbtn.pack(pady=20)

    Arcturusbtn=CTkButton(
        master=buttons_frame,
        text="Arcturus",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Arcturus,
        hover="#000000"        
    )
    Arcturusbtn.pack(pady=20)

    Alphabtn=CTkButton(
        master=buttons_frame,
        text="Alpha Centauri A",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Alpha,
        hover="#000000"        
    )
    Alphabtn.pack(pady=20)

    Vegabtn=CTkButton(
        master=buttons_frame,
        text="Vega",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Vega,
        hover="#000000"        
    )
    Vegabtn.pack(pady=20)

    Capellabtn=CTkButton(
        master=buttons_frame,
        text="Capella",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Capella,
        hover="#000000"        
    )
    Capellabtn.pack(pady=20)

    Rigelbtn=CTkButton(
        master=buttons_frame,
        text="Rigel",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Rigel,
        hover="#000000"        
    )
    Rigelbtn.pack(pady=20)

    Procyonbtn=CTkButton(
        master=buttons_frame,
        text="Procyon",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Procyon,
        hover="#000000"        
    )
    Procyonbtn.pack(pady=20)      

def Galaxies():
    for widght in app.winfo_children():
        widght.destroy()
    
    lbl = CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=start,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center")    

    buttons_frame= CTkFrame(
        master=app,
        fg_color="#000000"
    )
    buttons_frame.place(relx=0.5, rely=0.45, anchor="center")

    LMCbtn=CTkButton(
        master=buttons_frame,
        text="Large Magellanic Cloud",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=CommingSoon,
        hover="#000000"        
    )
    LMCbtn.pack(pady=20)

    SMCbtn=CTkButton(
        master=buttons_frame,
        text="Small Magellanic Cloud",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=CommingSoon,
        hover="#000000"        
    )
    SMCbtn.pack(pady=20)

    Sagbtn=CTkButton(
        master=buttons_frame,
        text="SagDEG",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=CommingSoon,
        hover="#000000"        
    )
    Sagbtn.pack(pady=20)

    Canisbtn=CTkButton(
        master=buttons_frame,
        text="Canis Major Dwarf",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=CommingSoon,
        hover="#000000"        
    )
    Canisbtn.pack(pady=20)

    Andromedabtn=CTkButton(
        master=buttons_frame,
        text="Andromeda",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=CommingSoon,
        hover="#000000"        
    )
    Andromedabtn.pack(pady=20)


def SolarSystem():
    for widght in app.winfo_children():
        widght.destroy()
    
    lbl = CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Planets,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center")   

    buttons_frame= CTkFrame(
        master=app,
        fg_color="#000000"
    )
    buttons_frame.place(relx=0.5, rely=0.45, anchor="center")

    Mercurybtn=CTkButton(
        master=buttons_frame,
        text="Mercury",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Mercury,
        hover="#000000"        
    )
    Mercurybtn.pack(pady=20)

    Venusbtn=CTkButton(
        master=buttons_frame,
        text="Venus",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Venus,
        hover="#000000"        
    )
    Venusbtn.pack(pady=20)

    Earthbtn=CTkButton(
        master=buttons_frame,
        text="Eearth",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Earth,
        hover="#000000"        
    )
    Earthbtn.pack(pady=20)

    Marsbtn=CTkButton(
        master=buttons_frame,
        text="Mars",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Mars,
        hover="#000000"        
    )
    Marsbtn.pack(pady=20)

    Jupiterbtn=CTkButton(
        master=buttons_frame,
        text="Jupiter",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Jupiter,
        hover="#000000"        
    )
    Jupiterbtn.pack(pady=20)

    Saturnbtn=CTkButton(
        master=buttons_frame,
        text="Saturn",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Saturn,
        hover="#000000"        
    )
    Saturnbtn.pack(pady=20)

    Uranusbtn=CTkButton(
        master=buttons_frame,
        text="Uranus",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Uranus,
        hover="#000000"        
    )
    Uranusbtn.pack(pady=20)

    Neptunebtn=CTkButton(
        master=buttons_frame,
        text="Neptune",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Neptune,
        hover="#000000"        
    )
    Neptunebtn.pack(pady=20)

def Exoplanets():
    for widght in app.winfo_children():
        widght.destroy()
    
    lbl = CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Planets,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center")  

    buttons_frame= CTkFrame(
        master=app,
        fg_color="#000000"
    )
    buttons_frame.place(relx=0.5, rely=0.45, anchor="center")

    cancribtn=CTkButton(
        master=buttons_frame,
        text="55 Cancri e",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Commingsoon,
        hover="#000000"        
    )
    cancribtn.pack(pady=20)

    Keplr16btn=CTkButton(
        master=buttons_frame,
        text="Kepler 16b",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Commingsoon,
        hover="#000000"        
    )
    Keplr16btn.pack(pady=20)

    Pegasibtn=CTkButton(
        master=buttons_frame,
        text="51 Pegasi b",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Commingsoon,
        hover="#000000"        
    )
    Pegasibtn.pack(pady=20)

    PSObtn=CTkButton(
        master=buttons_frame,
        text="PSO J318.5-22",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Commingsoon,
        hover="#000000"        
    )
    PSObtn.pack(pady=20)

    HDbtn=CTkButton(
        master=buttons_frame,
        text="HD 40307g",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Commingsoon,
        hover="#000000"        
    )
    HDbtn.pack(pady=20)

    Keplrfbtn=CTkButton(
        master=buttons_frame,
        text="Kepler 186f",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Commingsoon,
        hover="#000000"        
    )
    Keplrfbtn.pack(pady=20)

    Trappistbtn=CTkButton(
        master=buttons_frame,
        text="TRAPPIST-1e",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Commingsoon,
        hover="#000000"        
    )
    Trappistbtn.pack(pady=20)

def home():
    for widght in app.winfo_children():
        widght.destroy()
    lbl = CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl2 = CTkLabel(
        master=app,
        text="Astronomers Guide",
        font=('Modern', 50),
        text_color="#FDFD96",
        bg_color='#000000'
    )
    lbl2.place(relx=0.5, rely=0.4, anchor="center")

    lbl3 = CTkLabel(
        master=app,
        text="A Tour Through The Universe",
        font=("modern", 20),
        text_color="#FDFD96",
        bg_color="#000000"
    )
    lbl3.place(relx=0.5, rely=0.5, anchor="center")

    Startbtn = CTkButton(
        master=app,
        text="Start",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=start,
        hover="#000000"
    )
    Startbtn.place(relx=0.5, rely=0.7, anchor="center")        

def Commingsoon():
    for widght in app.winfo_children():
        widght.destroy()

    lbl = CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)        

    lbl2 = CTkLabel(
        master=app,
        text="Coming Soon",
        font=('Modern', 50),
        text_color="#FDFD96",
        bg_color='#000000'
    )
    lbl2.place(relx=0.5, rely=0.5, anchor="center")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Exoplanets,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 


def CommingSoon():
    for widght in app.winfo_children():
        widght.destroy()

    lbl = CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)        

    lbl2 = CTkLabel(
        master=app,
        text="Coming Soon",
        font=('Modern', 50),
        text_color="#FDFD96",
        bg_color='#000000'
    )
    lbl2.place(relx=0.5, rely=0.5, anchor="center")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=Galaxies,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Mercury():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Mercury_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Semimajor axis (10^6 km): 57.9\n")
    textbox.insert("end", "Semimajor axis (AU): 0.387\n")
    textbox.insert("end", "Sidereal period (years): 0.241\n")
    textbox.insert("end", "Sidereal period (days): 87.969\n")
    textbox.insert("end", "Synodic period (days): 115.88\n")
    textbox.insert("end", "Average orbital speed (km/s): 47.9\n")
    textbox.insert("end", "Orbital eccentricity: 0.206\n")
    textbox.insert("end", "Inclination of orbit to ecliptic (\u00b0): 7.00\n")
    textbox.insert("end", "Equatorial diameter (km): 4880\n")
    textbox.insert("end", "Equatorial diameter (Earth = 1): 0.383\n")
    textbox.insert("end", "Mass (kg): 3.302 × 10^23\n")
    textbox.insert("end", "Mass (Earth = 1): 0.0553\n")
    textbox.insert("end", "Average density (kg/m^3): 5430\n")
    textbox.insert("end", "Rotation period* (solar days): 58.646\n")
    textbox.insert("end", "Inclination of equator to orbit (°): 0.5\n")
    textbox.insert("end", "Surface gravity (Earth = 1): 0.38\n")
    textbox.insert("end", "Albedo: 0.12\n")
    textbox.insert("end", "Escape speed (km/s): 4.3\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=SolarSystem,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Venus():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Venus_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Semimajor axis (10^6 km): 108.2\n")
    textbox.insert("end", "Semimajor axis (AU): 0.723\n")
    textbox.insert("end", "Sidereal period (years): 0.615\n")
    textbox.insert("end", "Sidereal period (days): 224.70\n")
    textbox.insert("end", "Synodic period (days): 583.92\n")
    textbox.insert("end", "Average orbital speed (km/s): 35.0\n")
    textbox.insert("end", "Orbital eccentricity: 0.007\n")
    textbox.insert("end", "Inclination of orbit to ecliptic (\u00b0): 3.39\n")
    textbox.insert("end", "Equatorial diameter (km): 12,104\n")
    textbox.insert("end", "Equatorial diameter (Earth = 1): 0.949\n")
    textbox.insert("end", "Mass (kg): 4.868 × 10^24\n")
    textbox.insert("end", "Mass (Earth = 1): 0.815\n")
    textbox.insert("end", "Average density (kg/m^3): 5243\n")
    textbox.insert("end", "Rotation period* (solar days): 243.01 r\n")
    textbox.insert("end", "Inclination of equator to orbit (°): 177.4\n")
    textbox.insert("end", "Surface gravity (Earth = 1): 0.91\n")
    textbox.insert("end", "Albedo: 0.59\n")
    textbox.insert("end", "Escape speed (km/s): 10.4\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=SolarSystem,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Earth():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Earth_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Semimajor axis (10^6 km): 149.6\n")
    textbox.insert("end", "Semimajor axis (AU): 1.000\n")
    textbox.insert("end", "Sidereal period (years): 1.000\n")
    textbox.insert("end", "Sidereal period (days): 365.256\n")
    textbox.insert("end", "Average orbital speed (km/s): 29.79\n")
    textbox.insert("end", "Orbital eccentricity: 0.017\n")
    textbox.insert("end", "Inclination of orbit to ecliptic (\u00b0): 0.00\n")
    textbox.insert("end", "Equatorial diameter (km): 12,756\n")
    textbox.insert("end", "Equatorial diameter (Earth = 1): 1.000\n")
    textbox.insert("end", "Mass (kg): 5.974 × 10^24\n")
    textbox.insert("end", "Mass (Earth = 1): 1.000\n")
    textbox.insert("end", "Average density (kg/m^3): 5515\n")
    textbox.insert("end", "Rotation period* (solar days): 0.997\n")
    textbox.insert("end", "Inclination of equator to orbit (°): 23.45\n")
    textbox.insert("end", "Surface gravity (Earth = 1): 1.000\n")
    textbox.insert("end", "Albedo: 0.39\n")
    textbox.insert("end", "Escape speed (km/s): 11.2\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=SolarSystem,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Mars():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Mars_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Semimajor axis (10^6 km): 227.9\n")
    textbox.insert("end", "Semimajor axis (AU): 1.524\n")
    textbox.insert("end", "Sidereal period (years): 1.88\n")
    textbox.insert("end", "Sidereal period (days): 686.98\n")
    textbox.insert("end", "Synodic period (days): 779.94\n")
    textbox.insert("end", "Average orbital speed (km/s): 24.1\n")
    textbox.insert("end", "Orbital eccentricity: 0.093\n")
    textbox.insert("end", "Inclination of orbit to ecliptic (\u00b0): 1.85\n")
    textbox.insert("end", "Equatorial diameter (km): 6794\n")
    textbox.insert("end", "Equatorial diameter (Earth = 1): 0.533\n")
    textbox.insert("end", "Mass (kg): 6.418 × 10^23\n")
    textbox.insert("end", "Mass (Earth = 1): 0.107\n")
    textbox.insert("end", "Average density (kg/m^3): 3934\n")
    textbox.insert("end", "Rotation period* (solar days): 1.026\n")
    textbox.insert("end", "Inclination of equator to orbit (°): 25.19\n")
    textbox.insert("end", "Surface gravity (Earth = 1): 0.38\n")
    textbox.insert("end", "Albedo: 0.15\n")
    textbox.insert("end", "Escape speed (km/s): 5.0\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=SolarSystem,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Jupiter():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Jupiter_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Semimajor axis (10^6 km): 778.3\n")
    textbox.insert("end", "Semimajor axis (AU): 5.203\n")
    textbox.insert("end", "Sidereal period (years): 11.86\n")
    textbox.insert("end", "Synodic period (days): 398.9\n")
    textbox.insert("end", "Average orbital speed (km/s): 13.3\n")
    textbox.insert("end", "Orbital eccentricity: 0.048\n")
    textbox.insert("end", "Inclination of orbit to ecliptic (\u00b0): 1.30\n")
    textbox.insert("end", "Equatorial diameter (km): 142,984\n")
    textbox.insert("end", "Equatorial diameter (Earth = 1): 11.209\n")
    textbox.insert("end", "Mass (kg): 1.899 × 10^27\n")
    textbox.insert("end", "Mass (Earth = 1): 317.8\n")
    textbox.insert("end", "Average density (kg/m^3): 1326\n")
    textbox.insert("end", "Rotation period* (solar days): 0.414\n")
    textbox.insert("end", "Inclination of equator to orbit (°): 3.12\n")
    textbox.insert("end", "Surface gravity (Earth = 1): 2.36\n")
    textbox.insert("end", "Albedo: 0.44\n")
    textbox.insert("end", "Escape speed (km/s): 60.2\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=SolarSystem,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Saturn():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Saturn_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Semimajor axis (10^6 km): 1429\n")
    textbox.insert("end", "Semimajor axis (AU): 9.554\n")
    textbox.insert("end", "Sidereal period (years): 29.46\n")
    textbox.insert("end", "Synodic period (days): 378.1\n")
    textbox.insert("end", "Average orbital speed (km/s): 9.64\n")
    textbox.insert("end", "Orbital eccentricity: 0.053\n")
    textbox.insert("end", "Inclination of orbit to ecliptic (\u00b0): 2.48\n")
    textbox.insert("end", "Equatorial diameter (km): 120,536\n")
    textbox.insert("end", "Equatorial diameter (Earth = 1): 9.449\n")
    textbox.insert("end", "Mass (kg): 5.685 × 10^26\n")
    textbox.insert("end", "Mass (Earth = 1): 95.16\n")
    textbox.insert("end", "Average density (kg/m^3): 687\n")
    textbox.insert("end", "Rotation period* (solar days): 0.444\n")
    textbox.insert("end", "Inclination of equator to orbit (°): 26.73\n")
    textbox.insert("end", "Surface gravity (Earth = 1): 1.1\n")
    textbox.insert("end", "Albedo: 0.47\n")
    textbox.insert("end", "Escape speed (km/s): 35.5\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=SolarSystem,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Uranus():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Uranus_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Semimajor axis (10^6 km): 2871\n")
    textbox.insert("end", "Semimajor axis (AU): 19.194\n")
    textbox.insert("end", "Sidereal period (years): 84.10\n")
    textbox.insert("end", "Synodic period (days): 369.7\n")
    textbox.insert("end", "Average orbital speed (km/s): 6.83\n")
    textbox.insert("end", "Orbital eccentricity: 0.043\n")
    textbox.insert("end", "Inclination of orbit to ecliptic (\u00b0): 0.77\n")
    textbox.insert("end", "Equatorial diameter (km): 51,118\n")
    textbox.insert("end", "Equatorial diameter (Earth = 1): 4.007\n")
    textbox.insert("end", "Mass (kg): 8.682 × 10^25\n")
    textbox.insert("end", "Mass (Earth = 1): 14.53\n")
    textbox.insert("end", "Average density (kg/m^3): 1318\n")
    textbox.insert("end", "Rotation period* (solar days): 0.718 r\n")
    textbox.insert("end", "Inclination of equator to orbit (°): 97.86\n")
    textbox.insert("end", "Surface gravity (Earth = 1): 0.92\n")
    textbox.insert("end", "Albedo: 0.56\n")
    textbox.insert("end", "Escape speed (km/s): 21.3\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=SolarSystem,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Neptune():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Neptune_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Semimajor axis (10^6 km): 4498\n")
    textbox.insert("end", "Semimajor axis (AU): 30.066\n")
    textbox.insert("end", "Sidereal period (years): 164.86\n")
    textbox.insert("end", "Synodic period (days): 367.5\n")
    textbox.insert("end", "Average orbital speed (km/s): 5.5\n")
    textbox.insert("end", "Orbital eccentricity: 0.010\n")
    textbox.insert("end", "Inclination of orbit to ecliptic (\u00b0): 1.77\n")
    textbox.insert("end", "Equatorial diameter (km): 49,528\n")
    textbox.insert("end", "Equatorial diameter (Earth = 1): 3.883\n")
    textbox.insert("end", "Mass (kg): 1.024 × 10^26\n")
    textbox.insert("end", "Mass (Earth = 1): 17.15\n")
    textbox.insert("end", "Average density (kg/m^3): 1638\n")
    textbox.insert("end", "Rotation period* (solar days): 0.671\n")
    textbox.insert("end", "Inclination of equator to orbit (°): 29.56\n")
    textbox.insert("end", "Surface gravity (Earth = 1): 1.1\n")
    textbox.insert("end", "Albedo: 0.51\n")
    textbox.insert("end", "Escape speed (km/s): 23.5\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=SolarSystem,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Sirius():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Sirius_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Designation: α CMa A\n")
    textbox.insert("end", "Distance (parsecs): 2.63\n")
    textbox.insert("end", "Distance (light years): 8.58\n")
    textbox.insert("end", "Spectraltype: A1 V\n")
    textbox.insert("end", "Radial Velocity (km/s): -7.6\n")
    textbox.insert("end", "Proper Motion(arcsec/year): 1.34\n")
    textbox.insert("end", "Appearant visual magnitude: -1.43\n")
    textbox.insert("end", "Appearant visual brightness (Sirius = 1): 1.000\n")
    textbox.insert("end", "Absolute visual magnitude: +1.46\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=stars,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Canopus():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Canopus_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Designation: α Car\n")
    textbox.insert("end", "Distance (parsecs): 95.9\n")
    textbox.insert("end", "Distance (light years): 313\n")
    textbox.insert("end", "Spectraltype: F0 II\n")
    textbox.insert("end", "Radial Velocity (km/s): +20.5\n")
    textbox.insert("end", "Proper Motion(arcsec/year): 0.03\n")
    textbox.insert("end", "Appearant visual magnitude: -0.72\n")
    textbox.insert("end", "Appearant visual brightness (Sirius = 1): 0.520\n")
    textbox.insert("end", "Absolute visual magnitude: -5.63\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=stars,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Arcturus():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Arcturus_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Designation: α Boo A\n")
    textbox.insert("end", "Distance (parsecs): 11.3\n")
    textbox.insert("end", "Distance (light years): 36.7\n")
    textbox.insert("end", "Spectraltype: K1.5 III\n")
    textbox.insert("end", "Radial Velocity (km/s): -5.2\n")
    textbox.insert("end", "Proper Motion(arcsec/year): 2.28\n")
    textbox.insert("end", "Appearant visual magnitude: -0.04\n")
    textbox.insert("end", "Appearant visual brightness (Sirius = 1): 0.278\n")
    textbox.insert("end", "Absolute visual magnitude: -0.30\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=stars,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Alpha():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Alpha_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Designation: α Cen A\n")
    textbox.insert("end", "Distance (parsecs): 1.34\n")
    textbox.insert("end", "Distance (light years): 4.36\n")
    textbox.insert("end", "Spectraltype: G2 V\n")
    textbox.insert("end", "Radial Velocity (km/s): -25\n")
    textbox.insert("end", "Proper Motion(arcsec/year): 3.71\n")
    textbox.insert("end", "Appearant visual magnitude: -0.01\n")
    textbox.insert("end", "Appearant visual brightness (Sirius = 1): 0.270\n")
    textbox.insert("end", "Absolute visual magnitude: +4.36\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=stars,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Vega():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Vega_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Designation: α Lyr\n")
    textbox.insert("end", "Distance (parsecs): 7.76\n")
    textbox.insert("end", "Distance (light years): 25.3\n")
    textbox.insert("end", "Spectraltype: A0 V\n")
    textbox.insert("end", "Radial Velocity (km/s): -13.9\n")
    textbox.insert("end", "Proper Motion(arcsec/year): 0.35\n")
    textbox.insert("end", "Appearant visual magnitude: +0.03\n")
    textbox.insert("end", "Appearant visual brightness (Sirius = 1): 0.261\n")
    textbox.insert("end", "Absolute visual magnitude: +0.58\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=stars,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Capella():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Capella_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Designation: α Aur\n")
    textbox.insert("end", "Distance (parsecs): 12.9\n")
    textbox.insert("end", "Distance (light years): 42.2\n")
    textbox.insert("end", "Spectraltype: G5 III\n")
    textbox.insert("end", "Radial Velocity (km/s): +30.2\n")
    textbox.insert("end", "Proper Motion(arcsec/year): 0.43\n")
    textbox.insert("end", "Appearant visual magnitude: +0.08\n")
    textbox.insert("end", "Appearant visual brightness (Sirius = 1): 0.249\n")
    textbox.insert("end", "Absolute visual magnitude: -0.48\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=stars,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Rigel():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Rigel_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Designation: α Ori A\n")
    textbox.insert("end", "Distance (parsecs): 237\n")
    textbox.insert("end", "Distance (light years): 773\n")
    textbox.insert("end", "Spectraltype: B8 Ia\n")
    textbox.insert("end", "Radial Velocity (km/s): +20.7\n")
    textbox.insert("end", "Proper Motion(arcsec/year): 0.002\n")
    textbox.insert("end", "Appearant visual magnitude: +0.12\n")
    textbox.insert("end", "Appearant visual brightness (Sirius = 1): 0.240\n")
    textbox.insert("end", "Absolute visual magnitude: -6.75\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=stars,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Procyon():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Procyon_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Designation: α CMi A\n")
    textbox.insert("end", "Distance (parsecs): 3.50\n")
    textbox.insert("end", "Distance (light years): 11.4\n")
    textbox.insert("end", "Spectraltype: F5 IV-V\n")
    textbox.insert("end", "Radial Velocity (km/s): -3.2\n")
    textbox.insert("end", "Proper Motion(arcsec/year): 1.26\n")
    textbox.insert("end", "Appearant visual magnitude: +0.34\n")
    textbox.insert("end", "Appearant visual brightness (Sirius = 1): 0.196\n")
    textbox.insert("end", "Absolute visual magnitude: +2.62\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=stars,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 

def Sun():
    for widght in app.winfo_children():
        widght.destroy()

    lbl=CTkLabel(
        master=app,
        text="",
        image=bg_image
    )
    lbl.place(x=0, y=0)

    lbl = CTkLabel(
        master=app,
        text="",
        image=Sun_image
    )
    lbl.place(relx=0.5, rely=0.2, anchor="center")

    textbox = CTkTextbox(
        master=app, 
        width=480, 
        height=250, 
        font=("Modern", 20),
        text_color="#FDFD96",
        fg_color="#000000"
    )
    textbox.place(relx=0.5, rely=0.6, anchor="center")
    textbox.insert("end", "Mass (kg): 1.989 × 10^30\n")
    textbox.insert("end", "Equatorial diameter (km): 1,391,000\n")
    textbox.insert("end", "Surface temperature (K): 5778\n")
    textbox.insert("end", "Luminosity (watts): 3.828 × 10^26\n")
    textbox.insert("end", "Age (billion years): 4.6\n")
    textbox.insert("end", "Escape velocity (km/s): 617.7\n")
    textbox.insert("end", "Average density (kg/m^3): 1408\n")
    textbox.insert("end", "Rotation period (days at equator): 25.4\n")
    textbox.insert("end", "Gravitational acceleration (m/s^2): 274\n")
    textbox.insert("end", "Core temperature (K): 15,000,000\n")
    textbox.insert("end", "Distance to Earth (AU): 1\n")
    textbox.insert("end", "Composition (Hydrogen %): 74\n")
    textbox.insert("end", "Composition (Helium %): 24\n")
    textbox.insert("end", "Spectral type: G2V\n")
    textbox.insert("end", "Apparent magnitude: -26.74\n")
    textbox.insert("end", "Absolute magnitude: 4.83\n")
    textbox.configure(state="disabled")

    Backbtn = CTkButton(
        master=app,
        text="Back",
        font=("modern", 20),
        text_color="#FDFD96",
        fg_color="#000000",
        command=start,
        hover="#000000"
    )
    Backbtn.place(relx=0.5, rely=0.9, anchor="center") 


lbl = CTkLabel(
    master=app,
    text="",
    image=bg_image
)
lbl.place(x=0, y=0)

lbl2 = CTkLabel(
    master=app,
    text="Astronomers Guide",
    font=('Modern', 50),
    text_color="#FDFD96",
    bg_color='#000000'
)
lbl2.place(relx=0.5, rely=0.4, anchor="center")

lbl3 = CTkLabel(
    master=app,
    text="A Tour Through The Universe",
    font=("modern", 20),
    text_color="#FDFD96",
    bg_color="#000000"
)
lbl3.place(relx=0.5, rely=0.5, anchor="center")

Startbtn = CTkButton(
    master=app,
    text="Start",
    font=("modern", 20),
    text_color="#FDFD96",
    fg_color="#000000",
    command=start,
    hover="#000000"
)
Startbtn.place(relx=0.5, rely=0.7, anchor="center")

app.mainloop()


