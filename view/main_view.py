import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk, ImageDraw
import os

class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller #zapisz referencje do kontrolera

        self.title("Weather App")
        self.geometry("900x500")
        self.resizable(False, False)

        # Gradient tła
        self.gradient = self.create_gradient(900, 500, (194, 17, 141), (255, 80, 60))
        self.canvas = tk.Canvas(self, width=900, height=500, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.gradient)

        # Główna ramka (wrapper)
        self.wrapper = tk.Frame(self, bg="#1a1a1a", bd=2, relief="solid", highlightbackground="white", highlightthickness=2)
        self.wrapper.place(relx=0.5, rely=0.5, anchor="center", width=800, height=440)

        self._setup_fonts()
        self._create_layout()

    def create_gradient(self, width, height, color1, color2):
        image = Image.new("RGB", (width, height), color1)
        draw = ImageDraw.Draw(image)
        for i in range(height):
            ratio = i / height
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        return ImageTk.PhotoImage(image)

    def _setup_fonts(self):
        try:
            self.montserrat_bold = font.Font(family="Montserrat", size=32, weight="bold")
            self.montserrat_regular = font.Font(family="Montserrat", size=20)
        except:
            self.montserrat_bold = font.Font(family="Helvetica", size=32, weight="bold")
            self.montserrat_regular = font.Font(family="Helvetica", size=20)

    def _create_layout(self):

        # Górna część
        top = tk.Frame(self.wrapper, bg="#1a1a1a")
        top.pack(fill="x", pady=(0, 10), ipady=10)

        title = tk.Label(top, text="WEATHER APP", font=self.montserrat_bold, fg="white", bg="#1a1a1a")
        title.pack(pady=10)

        main_info = tk.Frame(top, bg="#1a1a1a")
        main_info.pack(fill="x", pady=(10, 0))

        # Lewa część
        left = tk.Frame(main_info, bg="#1a1a1a")
        left.pack(side="left", padx=40)

        self.top_info_label = tk.Label(left, text="", font=("Helvetica", 32), fg="white", bg="#1a1a1a")
        self.top_info_label.pack()

        self.input_var = tk.StringVar()
        self.city_entry = tk.Entry(left, textvariable=self.input_var, font=("Helvetica", 16), fg="#dddddd", bg="#1a1a1a",
                                   insertbackground="white", borderwidth=0)
        self.city_entry.pack(pady=(10, 0), side="left")
        self.city_entry.insert(0, "Wpisz nazwę miasta...")
        self.city_entry.bind('<FocusIn>', self._on_entry_click)
        self.city_entry.bind('<FocusOut>', self._on_focusout)


        button_border = tk.Frame(left, highlightbackground="white", highlightthickness=2, bd=0, bg="#1a1a1a")
        button_border.pack(side="left", padx=(20, 0), pady=(10, 0))

        self.send_btn = tk.Button(button_border,text="WYŚLIJ", font=("Helvetica", 12, "bold"), fg="white", bg="#1a1a1a", borderwidth=0, highlightthickness=0, padx=20, pady=8, cursor="hand2", activebackground="#dddddd", activeforeground="#333333")
        self.send_btn.pack()

        # Callback
        self.send_btn.config(command=self._on_send_click)

        # Prawa część: obrazek pogody
        right = tk.Frame(main_info, bg="#1a1a1a")
        right.pack(side="right", padx=40)

        icon_path = os.path.join("resources", "icons", "sun.png")
        img = Image.open(icon_path).resize((140, 140))
        self.weather_photo = ImageTk.PhotoImage(img)
        self.photo_label = tk.Label(right, image=self.weather_photo, bg="#1a1a1a")
        self.photo_label.pack()



        # Dolna część (bottom)
        bottom = tk.Frame(self.wrapper, bg="#1a1a1a")
        bottom.pack(fill="both", expand=True, pady=(10, 0))

        # Pierwsza biała linia
        tk.Frame(bottom, bg="#dddddd", height=1).pack(fill="x", pady=(0, 0))

        # Nagłówki pomiędzy liniami
        headings = tk.Frame(bottom, bg="#1a1a1a")
        headings.pack(fill="x", pady=(0, 0))
        for text in ["WEATHER:", "TEMPERATURE:", "HUMIDITY:"]:
            tk.Label(headings, text=text, font=("Helvetica", 16, "bold"), fg="white", bg="#1a1a1a",
                     width=20, anchor="center").pack(side="left", expand=True, fill="x")

        # Druga biała linia
        tk.Frame(bottom, bg="#dddddd", height=1).pack(fill="x", pady=(0, 0))

        # Wyniki pod nagłówkami i liniami
        weather_info = tk.Frame(bottom, bg="#1a1a1a")
        weather_info.pack(fill="x", pady=(10, 0))
        self.weather_lbl = tk.Label(weather_info, text="", font=("Helvetica", 16), fg="white", bg="#1a1a1a", width=20)
        self.weather_lbl.pack(side="left", expand=True, fill="x")
        self.temp_lbl = tk.Label(weather_info, text="", font=("Helvetica", 16), fg="white", bg="#1a1a1a", width=20)
        self.temp_lbl.pack(side="left", expand=True, fill="x")
        self.humidity_lbl = tk.Label(weather_info, text="", font=("Helvetica", 16), fg="white", bg="#1a1a1a", width=20)
        self.humidity_lbl.pack(side="left", expand=True, fill="x")

    def _on_send_click(self):
        city = self.input_var.get()
        if city and city != "Wpisz nazwę miasta...":
            self.clear_warning()
            self.controller(city)   #wywołaj kontroler
        else:
            self.show_warning("Podaj nazwę miasta!")



    def _on_entry_click(self, event):
        if self.city_entry.get() == "Wpisz nazwę miasta...":
            self.city_entry.delete(0, tk.END)
            self.city_entry.config(fg='white')

    def _on_focusout(self, event):
        if self.city_entry.get() == "":
            self.city_entry.insert(0, "Wpisz nazwę miasta...")
            self.city_entry.config(fg='#dddddd')

    def update_weather_data(self, weather, temperature, humidity, icon_name):
        self.weather_lbl.config(text=weather)
        self.temp_lbl.config(text=f"{temperature}°C")
        self.humidity_lbl.config(text=f"{humidity}%")
        # self.city_name.config(text=self.input_var.get())
        self.top_info_label.config(text=self.input_var.get(), fg="white")

        icon_path = os.path.join("resources", "icons", f"{icon_name}.png")
        if os.path.exists(icon_path):
            img = Image.open(icon_path).resize((140, 140))
            self.weather_photo = ImageTk.PhotoImage(img)
            self.photo_label.config(image=self.weather_photo)

    def show_warning(self, msg):
        #self.warning.config(text=msg)
        # self.top_info_label.config(text=msg, fg="tomato")
        self.top_info_label.config(text=msg, fg="tomato")
        self.weather_lbl.config(text="")
        self.temp_lbl.config(text="")
        self.humidity_lbl.config(text="")
        # Reset ikony
        icon_path = os.path.join("resources", "icons", "unknown.png")
        if os.path.exists(icon_path):
            img = Image.open(icon_path).resize((140, 140))
            self.weather_photo = ImageTk.PhotoImage(img)
            self.photo_label.config(image=self.weather_photo)

    def clear_warning(self):
        #self.warning.config(text="")
        #self.top_info_label.config(text="", fg="white")
        self.top_info_label.config(text="", fg="white")
        self.weather_lbl.config(text="")
        self.temp_lbl.config(text="")
        self.humidity_lbl.config(text="")











