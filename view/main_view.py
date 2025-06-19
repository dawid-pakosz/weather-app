import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk, ImageDraw
import os

class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller #controller reference
        self.title("Weather App")
        self.geometry("900x650")
        self.resizable(False, False)

        # ------------------ Gradient background -------------------
        self.gradient = self.create_gradient(900, 650, (194, 17, 141), (255, 80, 60))
        self.canvas = tk.Canvas(self, width=900, height=650, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.gradient)

        # ------------------ main wrapper -------------------
        self.wrapper = tk.Frame(self, bg="#1a1a1a", bd=2, relief="solid", highlightbackground="white", highlightthickness=2)
        self.wrapper.place(relx=0.5, rely=0.5, anchor="center", width=800, height=600)

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
    # ------------------ upper -------------------
        top = tk.Frame(self.wrapper, bg="#1a1a1a")
        top.pack(fill="x", pady=(0, 10), ipady=10)

        # ------------------ label -------------------
        title = tk.Label(top, text="WEATHER APP", font=self.montserrat_bold, fg="white", bg="#1a1a1a")
        title.pack(pady=10)

        # ------------------ main frame -------------------
        main_info = tk.Frame(top, bg="#1a1a1a")
        main_info.pack(fill="x", pady=(10, 0))

    # ------------------ left side -------------------
        left = tk.Frame(main_info, bg="#1a1a1a")
        left.pack(side="left", padx=40)

        self.top_info_label = tk.Label(left, text="", font=("Helvetica", 32), fg="white", bg="#1a1a1a")
        self.top_info_label.pack()

        # ------------------ Search city field -------------------
        self.input_var = tk.StringVar()
        self.city_entry = tk.Entry(left, textvariable=self.input_var, font=("Helvetica", 16), fg="#dddddd", bg="#1a1a1a",
                                   insertbackground="white", borderwidth=0)
        self.city_entry.pack(pady=(10, 0), side="left")

        self.city_entry.insert(0, "Insert city name...")
        self.city_entry.bind('<Key>', self._on_key_press)
        self.city_entry.bind('<FocusIn>', self._on_entry_click)
        self.city_entry.bind('<FocusOut>', self._on_focusout)
        self.city_entry.bind("<Return>", lambda event: self._on_send_click())   # Obsługa naciśnięcia klawisza Enter

        # ------------------ button send -------------------
        button_border = tk.Frame(left, highlightbackground="white", highlightthickness=2, bd=0, bg="#1a1a1a")
        button_border.pack(side="left", padx=(20, 0), pady=(10, 0))

        self.send_btn = tk.Button(button_border,text="Send", font=("Helvetica", 12, "bold"), fg="white", bg="#1a1a1a", borderwidth=0, highlightthickness=0, padx=20, pady=8, cursor="hand2", activebackground="#dddddd", activeforeground="#333333")
        self.send_btn.pack()
        self.send_btn.config(command=self._on_send_click)

    # ------------------ right side -------------------

        # ------------------ icon frame -------------------
        right = tk.Frame(main_info, bg="#1a1a1a")
        right.pack(side="right", padx=40)

        # ------------------ weather icon -------------------
        icon_path = os.path.join("resources", "icons", "sun.png")
        img = Image.open(icon_path).resize((140, 140))
        self.weather_photo = ImageTk.PhotoImage(img)
        self.photo_label = tk.Label(right, image=self.weather_photo, bg="#1a1a1a")
        self.photo_label.pack()

    # ------------------ bottom -------------------
        bottom = tk.Frame(self.wrapper, bg="#1a1a1a")
        bottom.pack(fill="both", expand=True, pady=(10, 0))

        # ------------------ 1st white line  -------------------
        tk.Frame(bottom, bg="#dddddd", height=1).pack(fill="x", pady=(0, 0))

        # ------------------ weather headers -------------------
        headings = tk.Frame(bottom, bg="#1a1a1a")
        headings.pack(fill="x", pady=(0, 0))
        for text in ["WEATHER:", "TEMPERATURE:", "HUMIDITY:"]:
            tk.Label(headings, text=text, font=("Helvetica", 16, "bold"), fg="white", bg="#1a1a1a",
                     width=20, anchor="center").pack(side="left", expand=True, fill="x")

        # ------------------ current weather  -------------------
        tk.Frame(bottom, bg="#dddddd", height=1).pack(fill="x", pady=(0, 0))
        weather_info = tk.Frame(bottom, bg="#1a1a1a")
        weather_info.pack(fill="x", pady=(10, 0))
        self.weather_lbl = tk.Label(weather_info, text="", font=("Helvetica", 16), fg="white", bg="#1a1a1a", width=20)
        self.weather_lbl.pack(side="left", expand=True, fill="x")
        self.temp_lbl = tk.Label(weather_info, text="", font=("Helvetica", 16), fg="white", bg="#1a1a1a", width=20)
        self.temp_lbl.pack(side="left", expand=True, fill="x")
        self.humidity_lbl = tk.Label(weather_info, text="", font=("Helvetica", 16), fg="white", bg="#1a1a1a", width=20)
        self.humidity_lbl.pack(side="left", expand=True, fill="x")

        # ------------------ forecast -------------------
        self.forecast_frame = tk.Frame(self.wrapper, bg="#1a1a1a")
        self.forecast_frame.pack(pady=(0, 10), fill="x")

        # ------------------ buttons -------------------
        buttons_frame = tk.Frame(self.wrapper, bg="#1a1a1a")
        buttons_frame.pack(pady=(20, 10))

        self.city_info_btn = tk.Button(
            buttons_frame, text="More about city", font=("Helvetica", 12),
            command=self.city_info_placeholder, bg="#333", fg="white", padx=10, pady=5, cursor="hand2"
        )
        self.city_info_btn.pack(side="left", padx=10)

        self.export_txt_btn = tk.Button(
            buttons_frame, text="Export to TXT", font=("Helvetica", 12),
            command=self.export_txt, bg="#333", fg="white", padx=10, pady=5, cursor="hand2"
        )
        self.export_txt_btn.pack(side="left", padx=10)

        self.export_csv_btn = tk.Button(
            buttons_frame, text="Export to CSV", font=("Helvetica", 12),
            command=self.export_csv, bg="#333", fg="white", padx=10, pady=5, cursor="hand2"
        )
        self.export_csv_btn.pack(side="left", padx=10)

        self.clear_btn = tk.Button(
            buttons_frame, text="Clear", font=("Helvetica", 12),
            command=self.clear_all, bg="#333", fg="white", padx=10, pady=5, cursor="hand2"
        )
        self.clear_btn.pack(side="left", padx=10)

    def _on_send_click(self):
        city = self.input_var.get().strip()

        if city and city != "Insert city name...":
            self.clear_warning()
            self.show_loading()
            self.controller(city)   #wywołaj kontroler
        else:
            self.show_warning("Insert city name!")

    def _on_entry_click(self, event):
        if self.city_entry.get() == "Insert city name...":
            self.city_entry.delete(0, tk.END)
            self.city_entry.config(fg='white')

    def _on_focusout(self, event):
        if self.city_entry.get() == "":
            self.city_entry.insert(0, "Insert city name...")
            self.city_entry.config(fg='#dddddd')

    def _on_key_press(self, event):
        current_text = self.city_entry.get()

        if current_text == "Insert city name...":
            self.city_entry.delete(0, tk.END)
            self.city_entry.config(fg='white')

        return

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
        self.top_info_label.config(text="", fg="white")
        self.weather_lbl.config(text="")
        self.temp_lbl.config(text="")
        self.humidity_lbl.config(text="")

    def show_loading(self):
        self.top_info_label.config(text="Loading...", fg="white")
        self.weather_lbl.config(text="")
        self.temp_lbl.config(text="")
        self.humidity_lbl.config(text="")

        # Resetuj ikonę do unknown (placeholder)
        icon_path = os.path.join("resources", "icons", "unknown.png")
        if os.path.exists(icon_path):
            img = Image.open(icon_path).resize((140, 140))
            self.weather_photo = ImageTk.PhotoImage(img)
            self.photo_label.config(image=self.weather_photo)

    def clear_all(self):
        # self.input_var.set("")
        # self.top_info_label.config(text="", fg="white")
        # self.weather_lbl.config(text="")
        # self.temp_lbl.config(text="")
        # self.humidity_lbl.config(text="")
        # self.city_entry.insert(0, "Insert city name...")
        #
        # # Ustaw ikonę na unknown
        # icon_path = os.path.join("resources", "icons", "unknown.png")
        # if os.path.exists(icon_path):
        #     img = Image.open(icon_path).resize((140, 140))
        #     self.weather_photo = ImageTk.PhotoImage(img)
        #     self.photo_label.config(image=self.weather_photo)
        self.input_var.set("")
        self.top_info_label.config(text="", fg="white")
        self.weather_lbl.config(text="")
        self.temp_lbl.config(text="")
        self.humidity_lbl.config(text="")
        self.city_entry.delete(0, tk.END)
        self.city_entry.insert(0, "Insert city name...")
        self.city_entry.config(fg="#dddddd")



        # Ustaw ikonę na unknown
        icon_path = os.path.join("resources", "icons", "unknown.png")
        if os.path.exists(icon_path):
            img = Image.open(icon_path).resize((140, 140))
            self.weather_photo = ImageTk.PhotoImage(img)
            self.photo_label.config(image=self.weather_photo)

        # **Wyczyszczenie forecastu:**
        for widget in self.forecast_frame.winfo_children():
            widget.destroy()
        # Wyczyszczenie danych do eksportu, jeśli są
        self.forecast_export_data = []

    def city_info_placeholder(self):
        print("Kliknięto przycisk Info o mieście – funkcja w budowie.")

    def update_forecast(self, forecast_data):
        for widget in self.forecast_frame.winfo_children():
            widget.destroy()

        for item in forecast_data:
            card = tk.Frame(self.forecast_frame, bg="#222222", padx=10, pady=10, bd=1, relief="solid")
            card.pack(side="left", expand=True, fill="both", padx=5)

            day_label = tk.Label(card, text=item["day"], font=("Helvetica", 14, "bold"), fg="white", bg="#222222")
            day_label.pack(pady=(0, 5))

            icon_path = os.path.join("resources", "icons", f"{item['icon_name']}.png")
            if os.path.exists(icon_path):
                img = Image.open(icon_path).resize((50, 50))
                icon_img = ImageTk.PhotoImage(img)
                icon_label = tk.Label(card, image=icon_img, bg="#222222")
                icon_label.image = icon_img
                icon_label.pack()

            temp_label = tk.Label(card, text=f"{item['temperature']}°C", font=("Helvetica", 14), fg="white",
                                  bg="#222222")
            temp_label.pack(pady=(5, 0))

        # Zapisujemy dane do eksportu
        self.forecast_export_data = forecast_data

    def export_txt(self):
        if hasattr(self, "forecast_export_data"):
            with open("prognoza.txt", "w", encoding="utf-8") as f:
                f.write("Dzień | Temperatura | Ikona\n")
                for item in self.forecast_export_data:
                    f.write(f"{item['day']} | {item['temperature']}°C | {item['icon_name']}\n")

    def export_csv(self):
        if hasattr(self, "forecast_export_data"):
            import csv
            with open("prognoza.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Dzień", "Temperatura", "Ikona"])
                for item in self.forecast_export_data:
                    writer.writerow([item["day"], item["temperature"], item["icon_name"]])
