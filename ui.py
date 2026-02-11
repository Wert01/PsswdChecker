import tkinter as tk
import customtkinter as ctk

from psswd import analyze_password


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


COLORS = {
    "bg_top": "#f7f2e8",
    "bg_bottom": "#e1eef4",
    "ink": "#1c1c1c",
    "muted": "#5a5a5a",
    "card": "#ffffff",
    "card_border": "#d9d2c7",
    "accent": "#2b6d5a",
    "accent_hover": "#35806a",
    "warn": "#d94f3d",
    "mid": "#d9a441",
    "good": "#2b6d5a",
    "great": "#1f7a6a",
}


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PsswdChecker")
        self.geometry("1100x780")
        self.minsize(980, 700)

        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self._draw_background)

        self.container = ctk.CTkFrame(
            self,
            fg_color=COLORS["card"],
            border_color=COLORS["card_border"],
            border_width=2,
            corner_radius=10,
            width=980,
            height=650,
        )
        self.container.place(relx=0.5, rely=0.5, anchor="center")
        self.container.grid_propagate(False)

        self.container.grid_columnconfigure(0, weight=1)

        self._build_header()
        self._build_input()
        self._build_status()
        self._build_criteria()

        self.after(120, lambda: self.password_entry.focus())

    def _build_header(self):
        header = ctk.CTkFrame(self.container, fg_color="transparent")
        header.grid(row=0, column=0, sticky="n", pady=(26, 10))

        title = ctk.CTkLabel(
            header,
            text="Проверка надежности пароля",
            font=ctk.CTkFont(family="Avenir Next", size=34, weight="bold"),
            text_color=COLORS["ink"],
        )
        title.pack()

        subtitle = ctk.CTkLabel(
            header,
            text="Быстрая оценка по длине, символам и повторяемости",
            font=ctk.CTkFont(family="Avenir", size=14),
            text_color=COLORS["muted"],
        )
        subtitle.pack(pady=(6, 0))

    def _build_input(self):
        form = ctk.CTkFrame(self.container, fg_color="transparent")
        form.grid(row=1, column=0, pady=(16, 6))

        self.password_entry = ctk.CTkEntry(
            form,
            width=720,
            height=54,
            placeholder_text="Введите пароль…",
            font=ctk.CTkFont(family="Avenir", size=16),
            fg_color="#fbfbfb",
            text_color=COLORS["ink"],
            placeholder_text_color="#9a9a9a",
            border_color=COLORS["card_border"],
            border_width=2,
            show="•",
        )
        self.password_entry.grid(row=0, column=0, padx=(0, 12))

        self.show_var = tk.BooleanVar(value=False)
        show_toggle = ctk.CTkSwitch(
            form,
            text="Показать",
            variable=self.show_var,
            command=self._toggle_show,
            font=ctk.CTkFont(family="Avenir", size=13),
            text_color=COLORS["muted"],
            fg_color=COLORS["accent"],
            progress_color=COLORS["accent"],
        )
        show_toggle.grid(row=0, column=1)

        self.check_button = ctk.CTkButton(
            self.container,
            text="Проверить",
            width=720,
            height=48,
            fg_color=COLORS["accent"],
            hover_color=COLORS["accent_hover"],
            text_color="#f7f7f7",
            font=ctk.CTkFont(family="Avenir Next", size=16, weight="bold"),
            corner_radius=6,
            command=self.on_check_clicked,
        )
        self.check_button.grid(row=2, column=0, pady=(8, 12))

    def _build_status(self):
        status = ctk.CTkFrame(
            self.container,
            fg_color="#f8f6f0",
            border_color=COLORS["card_border"],
            border_width=2,
            corner_radius=10,
        )
        status.grid(row=3, column=0, padx=80, pady=(4, 12), sticky="ew")
        status.grid_columnconfigure(0, weight=1)

        self.level_label = ctk.CTkLabel(
            status,
            text="Введите пароль для оценки",
            font=ctk.CTkFont(family="Avenir Next", size=20, weight="bold"),
            text_color=COLORS["ink"],
        )
        self.level_label.grid(row=0, column=0, pady=(16, 4))

        self.message_label = ctk.CTkLabel(
            status,
            text="",
            font=ctk.CTkFont(family="Avenir", size=13),
            text_color=COLORS["muted"],
        )
        self.message_label.grid(row=1, column=0, pady=(0, 12))

        self.progress = ctk.CTkProgressBar(
            status,
            width=520,
            height=14,
            corner_radius=8,
            fg_color="#e8e1d7",
            progress_color=COLORS["accent"],
        )
        self.progress.grid(row=2, column=0, pady=(0, 16))
        self.progress.set(0)

    def _build_criteria(self):
        grid = ctk.CTkFrame(self.container, fg_color="transparent")
        grid.grid(row=4, column=0, pady=(2, 18))

        for col in range(2):
            grid.grid_columnconfigure(col, weight=1, minsize=300)

        self.criteria = [
            ("length_12", "Длина минимум 12 символов"),
            ("digit", "Есть цифры"),
            ("upper", "Есть заглавные буквы"),
            ("lower", "Есть строчные буквы"),
            ("special", "Есть специальные символы"),
            ("no_long_repeat", "Нет длинных повторов"),
        ]

        self.criteria_boxes = {}
        for index, (key, label) in enumerate(self.criteria):
            row = index // 2
            col = index % 2
            box = ctk.CTkFrame(
                grid,
                fg_color="#ffffff",
                border_color=COLORS["card_border"],
                border_width=2,
                corner_radius=8,
                width=340,
                height=76,
            )
            box.grid(row=row, column=col, padx=16, pady=10)
            box.grid_propagate(False)

            cb = ctk.CTkCheckBox(
                box,
                text=label,
                font=ctk.CTkFont(family="Avenir", size=13, weight="bold"),
                text_color=COLORS["ink"],
                checkbox_width=20,
                checkbox_height=20,
                corner_radius=4,
                fg_color=COLORS["accent"],
                hover_color=COLORS["accent_hover"],
                border_color=COLORS["card_border"],
                checkmark_color="#ffffff",
            )
            cb.place(relx=0.5, rely=0.5, anchor="center")
            cb.configure(state="disabled")
            self.criteria_boxes[key] = cb

    def _toggle_show(self):
        self.password_entry.configure(show="" if self.show_var.get() else "•")

    def _draw_background(self, event):
        self.canvas.delete("bg")
        width = event.width
        height = event.height
        steps = 60
        for i in range(steps):
            blend = i / (steps - 1)
            color = self._blend(COLORS["bg_top"], COLORS["bg_bottom"], blend)
            y0 = int(i * height / steps)
            y1 = int((i + 1) * height / steps)
            self.canvas.create_rectangle(0, y0, width, y1, fill=color, outline="", tags="bg")

        dot_color = "#ffffff"
        for x in range(40, width, 160):
            self.canvas.create_oval(x, 80, x + 6, 86, fill=dot_color, outline="", tags="bg")
        for x in range(120, width, 200):
            self.canvas.create_oval(x, height - 140, x + 8, height - 132, fill=dot_color, outline="", tags="bg")

    def _blend(self, c1, c2, t):
        def to_rgb(hex_color):
            hex_color = hex_color.lstrip("#")
            return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

        r1, g1, b1 = to_rgb(c1)
        r2, g2, b2 = to_rgb(c2)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        return f"#{r:02x}{g:02x}{b:02x}"

    def on_check_clicked(self):
        password = self.password_entry.get()
        evaluation = analyze_password(password)

        for key, cb in self.criteria_boxes.items():
            if evaluation.criteria.get(key):
                cb.select()
            else:
                cb.deselect()

        level_color = self._level_color(evaluation.level)
        self.level_label.configure(text=f"Уровень: {evaluation.level}", text_color=level_color)
        self.message_label.configure(text=evaluation.message)

        target = evaluation.score / max(len(self.criteria), 1)
        self._animate_progress(target, level_color)

    def _level_color(self, level: str) -> str:
        if level in {"Слишком простой", "Очень короткий", "Слабый"}:
            return COLORS["warn"]
        if level in {"Средний"}:
            return COLORS["mid"]
        if level in {"Хороший"}:
            return COLORS["good"]
        return COLORS["great"]

    def _animate_progress(self, target: float, color: str):
        self.progress.configure(progress_color=color)
        current = self.progress.get()
        steps = 18
        delta = (target - current) / steps

        def step(count=0, value=current):
            new_value = value + delta
            self.progress.set(max(0.0, min(1.0, new_value)))
            if count < steps:
                self.after(15, step, count + 1, new_value)

        step()


if __name__ == "__main__":
    App().mainloop()
