import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("psswdChecker")
        self.geometry("1100x750")

        #1 колонка
        self.grid_columnconfigure(0, weight=1)


       # 1) Прямоугольник под заголовок
        self.title_frame = ctk.CTkFrame(
            self,
            corner_radius=12,
            fg_color="#2b2b2b"  # другой оттенок
        )
        self.title_frame.grid(row=0, column=0, pady=(40, 20))

        # 2) Текст внутри прямоугольника
        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text="Введите пароль:",
            font=ctk.CTkFont(size=36, weight="bold")
        )
        self.title_label.pack(padx=40, pady=20)


        # 2) Поле ввода
        self.password_entry = ctk.CTkEntry(
            self,
            width=700,
            height=70,
            placeholder_text="Введите пароль...",
            font=ctk.CTkFont(size=18),
        )
        self.password_entry.grid(row=1, column=0, pady=(0, 20))

        # 3) Кнопка
        self.check_button = ctk.CTkButton(
            self,
            text="Начать проверку",
            width=700,
            height=60,
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.on_check_clicked
        )
        self.check_button.grid(row=2, column=0, pady=(0, 30))

    def on_check_clicked(self):
        print("clicked:", self.password_entry.get())
    
    def on_checkbox_toggled(self):
        print("Checkbox toggled:", self.psswd_chekbox.get())


if __name__ == "__main__":
    App().mainloop()
