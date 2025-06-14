# # view/main_view.py
#
# import customtkinter as ctk
#
#
# class MainView(ctk.CTk):
#     def __init__(self, controller_callback):
#         super().__init__()
#
#         self.title("WeatherWay 🌤️")
#         self.geometry("400x300")
#         self.configure(bg_color="#EAF4F4")
#
#         ctk.set_appearance_mode("light")
#         ctk.set_default_color_theme("blue")
#
#         self.controller_callback = controller_callback
#
#         # --- Nagłówek ---
#         self.label_title = ctk.CTkLabel(self, text="Sprawdź pogodę", font=("Helvetica", 20, "bold"))
#         self.label_title.pack(pady=(30, 10))
#
#         # --- Pole do wpisania miasta ---
#         self.entry_city = ctk.CTkEntry(self, placeholder_text="Wpisz miasto...", width=240)
#         self.entry_city.pack(pady=10)
#
#         # --- Przycisk ---
#         self.button_check = ctk.CTkButton(self, text="Pobierz pogodę", command=self._on_check_weather)
#         self.button_check.pack(pady=10)
#
#         # --- Pole wynikowe ---
#         self.label_result = ctk.CTkLabel(self, text="", font=("Helvetica", 14), wraplength=320)
#         self.label_result.pack(pady=20)
#
#     def _on_check_weather(self):
#         city_name = self.entry_city.get()
#         if city_name:
#             self.controller_callback(city_name)
#
#     def display_weather(self, weather_text: str):
#         self.label_result.configure(text=weather_text)
#
#     def display_error(self, error_text: str):
#         self.label_result.configure(text=f"❌ {error_text}", text_color="red")























































# drugie podejscie
# import customtkinter as ctk
# from PIL import Image, ImageTk
# import os
#
# class WeatherApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#
#         # Konfiguracja głównego okna
#         self.title("WeatherWay")
#         self.geometry("500x400")
#         self.resizable(False, False)
#
#         # Gradientowe tło przez frame
#         self.bg_frame = ctk.CTkFrame(self, corner_radius=0)
#         self.bg_frame.pack(fill="both", expand=True)
#
#         # Układ grid
#         self.bg_frame.grid_columnconfigure((0, 1, 2), weight=1)
#         self.bg_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
#
#         # Pole tekstowe do wpisania miasta
#         self.city_entry = ctk.CTkEntry(self.bg_frame, placeholder_text="Wpisz nazwę miasta...")
#         self.city_entry.grid(row=0, column=0, padx=10, pady=(20, 10), columnspan=2, sticky="ew")
#
#         # Przycisk wysyłania zapytania
#         self.search_button = ctk.CTkButton(self.bg_frame, text="Sprawdź", command=self.on_search_click)
#         self.search_button.grid(row=0, column=2, padx=10, pady=(20, 10))
#
#         # Obrazek z ikoną pogody
#         self.weather_icon_label = ctk.CTkLabel(self.bg_frame, text="")
#         self.weather_icon_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))
#
#         # Separator
#         self.separator1 = ctk.CTkLabel(self.bg_frame, text="────────────", text_color="gray")
#         self.separator1.grid(row=2, column=0, columnspan=3)
#
#         # Nagłówki
#         self.header_weather = ctk.CTkLabel(self.bg_frame, text="Weather", font=ctk.CTkFont(size=14, weight="bold"))
#         self.header_weather.grid(row=3, column=0)
#
#         self.header_temp = ctk.CTkLabel(self.bg_frame, text="Temperature", font=ctk.CTkFont(size=14, weight="bold"))
#         self.header_temp.grid(row=3, column=1)
#
#         self.header_humidity = ctk.CTkLabel(self.bg_frame, text="Humidity", font=ctk.CTkFont(size=14, weight="bold"))
#         self.header_humidity.grid(row=3, column=2)
#
#         # Separator
#         self.separator2 = ctk.CTkLabel(self.bg_frame, text="────────────", text_color="gray")
#         self.separator2.grid(row=4, column=0, columnspan=3)
#
#         # Dane pogodowe
#         self.weather_label = ctk.CTkLabel(self.bg_frame, text="–")
#         self.weather_label.grid(row=5, column=0)
#
#         self.temperature_label = ctk.CTkLabel(self.bg_frame, text="–")
#         self.temperature_label.grid(row=5, column=1)
#
#         self.humidity_label = ctk.CTkLabel(self.bg_frame, text="–")
#         self.humidity_label.grid(row=5, column=2)
#
#         # Styl globalny
#         ctk.set_appearance_mode("light")
#         ctk.set_default_color_theme("blue")
#
#     def on_search_click(self):
#         # Demo: przykładowe dane na sztywno
#         city = self.city_entry.get()
#         weather_type = "sun"  # <- normalnie ustalane na podstawie API
#         temp_c = "22°C"
#         humidity = "60%"
#
#         # Aktualizacja etykiet
#         self.weather_label.configure(text="Sunny")
#         self.temperature_label.configure(text=temp_c)
#         self.humidity_label.configure(text=humidity)
#
#         # Wczytanie obrazka z folderu
#         icon_path = os.path.join("resources", "icons", f"{weather_type}.png")
#         try:
#             image = Image.open(icon_path).resize((80, 80))
#             icon = ImageTk.PhotoImage(image)
#             self.weather_icon_label.configure(image=icon)
#             self.weather_icon_label.image = icon  # <- referencja!
#         except FileNotFoundError:
#             self.weather_icon_label.configure(text="(brak ikony)")
#
# if __name__ == "__main__":
#     app = WeatherApp()
#     app.mainloop()









# podejscie 3 perplexity
# import tkinter as tk
# from tkinter import font
# from PIL import Image, ImageTk, ImageDraw
#
# # Funkcja tworząca gradient tła
# def create_gradient(width, height, color1, color2):
#     image = Image.new("RGB", (width, height), color1)
#     draw = ImageDraw.Draw(image)
#     for i in range(height):
#         ratio = i / height
#         r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
#         g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
#         b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
#         draw.line([(0, i), (width, i)], fill=(r, g, b))
#     return ImageTk.PhotoImage(image)
#
# root = tk.Tk()
# root.title("Weather App")
# root.geometry("900x500")
# root.resizable(False, False)
#
# # Gradient tła
# gradient = create_gradient(900, 500, (194, 17, 141), (255, 80, 60))
# canvas = tk.Canvas(root, width=900, height=500, highlightthickness=0)
# canvas.pack(fill="both", expand=True)
# canvas.create_image(0, 0, anchor="nw", image=gradient)
#
# # Wrapper (ramka główna)
# # wrapper = tk.Frame(root, bg="#000000CC", bd=2, relief="solid", highlightbackground="white", highlightcolor="white", highlightthickness=2)
# wrapper = tk.Frame(root, bg="#1a1a1a", bd=2, relief="solid", highlightbackground="white", highlightcolor="white", highlightthickness=2)
# wrapper.place(relx=0.5, rely=0.5, anchor="center", width=800, height=440)
#
# # Czcionki
# try:
#     montserrat_bold = font.Font(family="Montserrat", size=32, weight="bold")
#     montserrat_regular = font.Font(family="Montserrat", size=20)
# except:
#     montserrat_bold = font.Font(family="Helvetica", size=32, weight="bold")
#     montserrat_regular = font.Font(family="Helvetica", size=20)
#
# # Górna część (top)
# # top = tk.Frame(wrapper, bg="#00000000")
# top = tk.Frame(wrapper, bg="#1a1a1a")
# top.pack(fill="x", pady=(0, 10), ipady=10)
#
# title = tk.Label(top, text="WEATHER APP", font=montserrat_bold, fg="white", bg="#1a1a1a")
# title.pack(pady=10)
#
# main_info = tk.Frame(top, bg="#1a1a1a")
# main_info.pack(fill="x", pady=(10, 0))
#
# # Lewa część: input + button + warning
# left = tk.Frame(main_info, bg="#1a1a1a")
# left.pack(side="left", padx=40)
#
# city_name = tk.Label(left, text="", font=("Helvetica", 32), fg="white", bg="#1a1a1a")
# city_name.pack()
#
# input_var = tk.StringVar()
# city_entry = tk.Entry(left, textvariable=input_var, font=("Helvetica", 16), fg="white", bg="#1a1a1a", insertbackground="white", borderwidth=0)
# city_entry.pack(pady=(10, 0), side="left")
# city_entry.config(highlightthickness=0)
# city_entry.insert(0, "Wpisz nazwę miasta...")
#
# def on_entry_click(event):
#     if city_entry.get() == "Wpisz nazwę miasta...":
#         city_entry.delete(0, tk.END)
#         city_entry.config(fg='white')
#
# def on_focusout(event):
#     if city_entry.get() == "":
#         city_entry.insert(0, "Wpisz nazwę miasta...")
#         city_entry.config(fg='#dddddd')
#
# city_entry.bind('<FocusIn>', on_entry_click)
# city_entry.bind('<FocusOut>', on_focusout)
# city_entry.config(fg="#dddddd")
#
# send_btn = tk.Button(left, text="WYŚLIJ", font=("Helvetica", 12, "bold"), fg="white", bg="#1a1a1a", borderwidth=0, highlightthickness=0, padx=10, pady=5, cursor="hand2", activebackground="#dddddd", activeforeground="#333333")
# send_btn.pack(side="left", padx=(20, 0))
#
# warning = tk.Label(left, text="", font=("Helvetica", 14), fg="tomato", bg="#1a1a1a")
# warning.pack(pady=(10, 0))
#
# # Prawa część: obrazek pogody
# right = tk.Frame(main_info, bg="#1a1a1a")
# right.pack(side="right", padx=40)
#
# # Użyj własnej ścieżki do obrazka!
# # weather_img = Image.open("sun.png").resize((140, 140))
# weather_img = Image.open(r"C:\Users\Admin\Desktop\Dudek\studia\ProjektZaliczenie\projekt_PY\weather_app\resources\icons\sun.png").resize((140, 140))
# weather_photo = ImageTk.PhotoImage(weather_img)
# photo_label = tk.Label(right, image=weather_photo, bg="#1a1a1a")
# photo_label.pack()
#
# # Dolna część (bottom)
# bottom = tk.Frame(wrapper, bg="#1a1a1a")
# bottom.pack(fill="both", expand=True, pady=(10, 0))
#
# # Nagłówki
# headings = tk.Frame(bottom, bg="#1a1a1a")
# headings.pack(fill="x", pady=(10, 0))
# for text in ["WEATHER:", "TEMPERATURE:", "HUMIDITY:"]:
#     tk.Label(headings, text=text, font=("Helvetica", 16, "bold"), fg="white", bg="#1a1a1a", width=20, anchor="center").pack(side="left", expand=True, fill="x")
#
# # Linie górna/dolna
# tk.Frame(bottom, bg="#dddddd", height=1).pack(fill="x", pady=(0, 0))
#
# # Dane pogodowe
# weather_info = tk.Frame(bottom, bg="#1a1a1a")
# weather_info.pack(fill="x", pady=(10, 0))
# weather_lbl = tk.Label(weather_info, text="", font=("Helvetica", 20), fg="white", bg="#1a1a1a", width=20)
# weather_lbl.pack(side="left", expand=True, fill="x")
# temp_lbl = tk.Label(weather_info, text="", font=("Helvetica", 20), fg="white", bg="#1a1a1a", width=20)
# temp_lbl.pack(side="left", expand=True, fill="x")
# humidity_lbl = tk.Label(weather_info, text="", font=("Helvetica", 20), fg="white", bg="#1a1a1a", width=20)
# humidity_lbl.pack(side="left", expand=True, fill="x")
#
# tk.Frame(bottom, bg="#dddddd", height=1).pack(fill="x", pady=(0, 0))
#
# root.mainloop()
#
#
#




#po code review przez chatgpt
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

        self.city_name = tk.Label(left, text="", font=("Helvetica", 32), fg="white", bg="#1a1a1a")
        self.city_name.pack()

        self.input_var = tk.StringVar()
        self.city_entry = tk.Entry(left, textvariable=self.input_var, font=("Helvetica", 16), fg="#dddddd", bg="#1a1a1a",
                                   insertbackground="white", borderwidth=0)
        self.city_entry.pack(pady=(10, 0), side="left")
        self.city_entry.insert(0, "Wpisz nazwę miasta...")
        self.city_entry.bind('<FocusIn>', self._on_entry_click)
        self.city_entry.bind('<FocusOut>', self._on_focusout)


        self.send_btn = tk.Button(left, text="WYŚLIJ", font=("Helvetica", 12, "bold"), fg="white", bg="#1a1a1a",
                                  borderwidth=0, highlightthickness=0, padx=10, pady=5, cursor="hand2",
                                  activebackground="#dddddd", activeforeground="#333333")
        self.send_btn.pack(side="left", padx=(20, 0))

        # Callback
        self.send_btn.config(command=self._on_send_click)

        self.warning = tk.Label(left, text="", font=("Helvetica", 14), fg="tomato", bg="#1a1a1a")
        self.warning.pack(pady=(10, 0))

        # Prawa część: obrazek pogody
        right = tk.Frame(main_info, bg="#1a1a1a")
        right.pack(side="right", padx=40)

        icon_path = os.path.join("resources", "icons", "sun.png")
        img = Image.open(icon_path).resize((140, 140))
        self.weather_photo = ImageTk.PhotoImage(img)
        self.photo_label = tk.Label(right, image=self.weather_photo, bg="#1a1a1a")
        self.photo_label.pack()

        # Dolna część
        bottom = tk.Frame(self.wrapper, bg="#1a1a1a")
        bottom.pack(fill="both", expand=True, pady=(10, 0))

        headings = tk.Frame(bottom, bg="#1a1a1a")
        headings.pack(fill="x", pady=(10, 0))
        for text in ["WEATHER:", "TEMPERATURE:", "HUMIDITY:"]:
            tk.Label(headings, text=text, font=("Helvetica", 16, "bold"), fg="white", bg="#1a1a1a",
                     width=20, anchor="center").pack(side="left", expand=True, fill="x")

        tk.Frame(bottom, bg="#dddddd", height=1).pack(fill="x")

        weather_info = tk.Frame(bottom, bg="#1a1a1a")
        weather_info.pack(fill="x", pady=(10, 0))
        self.weather_lbl = tk.Label(weather_info, text="", font=("Helvetica", 20), fg="white", bg="#1a1a1a", width=20)
        self.weather_lbl.pack(side="left", expand=True, fill="x")
        self.temp_lbl = tk.Label(weather_info, text="", font=("Helvetica", 20), fg="white", bg="#1a1a1a", width=20)
        self.temp_lbl.pack(side="left", expand=True, fill="x")
        self.humidity_lbl = tk.Label(weather_info, text="", font=("Helvetica", 20), fg="white", bg="#1a1a1a", width=20)
        self.humidity_lbl.pack(side="left", expand=True, fill="x")

        tk.Frame(bottom, bg="#dddddd", height=1).pack(fill="x")

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
        self.city_name.config(text=self.input_var.get())

        icon_path = os.path.join("resources", "icons", f"{icon_name}.png")
        if os.path.exists(icon_path):
            img = Image.open(icon_path).resize((140, 140))
            self.weather_photo = ImageTk.PhotoImage(img)
            self.photo_label.config(image=self.weather_photo)

    def show_warning(self, msg):
        self.warning.config(text=msg)

    def clear_warning(self):
        self.warning.config(text="")







