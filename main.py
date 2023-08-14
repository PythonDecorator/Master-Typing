import customtkinter as ctk
from styling import *
from PIL import Image
from data import tip_1, tip_2, get_sentence_to_type
import pygame
import sys
import os


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BG_COLOR)
        self.title(" Master Typing")
        self.resizable(False, False)
        self.iconbitmap(self.resource_path("files/images/logo.ico"))

        app_width = 1000
        app_height = 700
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_cor = int((screen_width / 2) - (app_width / 2))
        y_cor = int((screen_height / 2) - (app_height / 2))
        self.geometry("{}x{}+{}+{}".format(app_width, app_height, x_cor, y_cor))

        # MUSIC
        pygame.init()
        self.bg_music = pygame.mixer.Sound(self.resource_path("files/sound/not_started.mp3"))
        self.bg_music.set_volume(0.5)
        self.bg_music.play(loops=-1)
        self.typing_music = pygame.mixer.Sound(self.resource_path("files/sound/typing.mp3"))
        self.logo_effect_sound = pygame.mixer.Sound(self.resource_path("files/sound/sound effect.mp3"))
        self.logo_effect_sound.set_volume(0.1)

        # VARIABLES
        self.start_btn_var = ctk.StringVar(value="Start")
        self.timer_int_var = ctk.IntVar(value=60)
        self.timer_menu_var = ctk.StringVar(value="60 sec")

        # LAYOUT DESIGN
        # LOGO FRAME
        LogoFrame(self, self.resource_path)

        #  WORD COUNT FRAME
        self.word_count = WordCountFrame(self)

        # TIMER FRAME
        self.timer = TimerFrame(self)

        # MENU AND START BUTTON FRAME
        self.start_btn = MenuAndStartButtonFrame(self)

        #  SCROLLABLE FRAME
        self.scrollable_frame = ScrollableFrame(self)

        # # LEFT CANVAS FRAME
        LeftTipFrame(self)

        # RIGHT CANVAS FRAME
        RightTipFrame(self)

        # BOTTOM TEXT LABEL
        bottom_text = ctk.CTkLabel(self, text="Designed by Amos @PythonDecorator",
                                   text_color=BOTTOM_TEXT_COLOR, font=BOTTOM_FONT)
        bottom_text.place(relx=0.5, rely=0.976, anchor="center")

        self.start_btn_var.trace_add("write", self.update_music)
        self.start_btn_var.trace_add("write", self.timer.update_timer)
        self.timer_int_var.trace_add("write", self.detect_time_up)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def detect_time_up(self, *args):
        time_left = self.timer_int_var.get()

        if self.start_btn_var.get() == "Started":
            if time_left > 30:
                self.timer.canvas.itemconfigure(self.timer.timer, fill=TIME_COUNT_COLOR)
            else:
                self.timer.canvas.itemconfigure(self.timer.timer, fill=STARTED_BG_COLOR)

        if not self.timer_int_var.get():
            for label, entry in self.scrollable_frame.label_and_entry_list:
                entry.configure(state="disabled")

            self.start_btn_var.set(value="Restart")
            self.timer_int_var.set(value=int(self.timer_menu_var.get().split(" ")[0]))

            self.timer.canvas.itemconfigure(self.timer.timer, fill=STARTED_BG_COLOR)
            self.start_btn.start_btn.configure(text=self.start_btn_var.get(), fg_color=RESTART_HOVER_COLOR,
                                               state="normal", hover_color=TIME_COUNT_COLOR)

    def update_music(self, *args):
        if self.start_btn_var.get() == "Started":
            self.start_btn_var.set(value="Started")
            self.bg_music.stop()
            self.typing_music.play(loops=-1)
        else:
            self.bg_music.play(loops=-1)
            self.typing_music.stop()


class LogoFrame(ctk.CTkFrame):
    def __init__(self, parent: App, get_image_func):
        super().__init__(master=parent, fg_color=SCROLL_COLOR, corner_radius=0)
        self.place(relx=0.2, rely=0.024, relwidth=0.7, relheight=0.18)
        self.parent = parent
        self.path = get_image_func

        self.ctk_image_list = []
        self.logo_image_frames = self.get_images()
        self.current_frame = 0
        self.last_frame = len(self.logo_image_frames) - 1

        self.logo_label = ctk.CTkLabel(self, text="")
        self.logo_label.place(relx=0, rely=0.15, relwidth=0.87, relheight=0.98)

        self.parent.start_btn_var.trace_add("write", self.update_animation)
        self.parent.start_btn_var.trace_add("write", self.play_logo_sound)
        self.play_logo_sound()
        self.update_animation()

    def play_logo_sound(self, *args):
        if self.parent.start_btn_var.get() != "Started":
            self.parent.logo_effect_sound.play()
            self.after(2000, self.play_logo_sound)
        else:
            self.parent.logo_effect_sound.stop()

    def update_animation(self, *args):
        self.logo_label.configure(image=self.logo_image_frames[self.current_frame])

        if self.parent.start_btn_var.get() != "Started":
            if self.current_frame < self.last_frame:
                self.current_frame += 1
                self.after(40, self.update_animation)
            else:
                self.current_frame = 0
                self.after(40, self.update_animation)
        else:
            self.logo_label.configure(image=self.logo_image_frames[49])
            self.current_frame = 0

    def get_images(self):
        dark = [Image.open(self.path(f"files/logo/logo/{n}.png")) for n in range(1, 51)]
        light = [Image.open(self.path(f"files/logo/logo/{n}.png")) for n in range(1, 51)]
        self.ctk_image_list = [ctk.CTkImage(light_image=light[n], dark_image=dark[n], size=(550, 109))
                               for n in range(len(dark))]
        return self.ctk_image_list


class WordCountFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent, fg_color=FRAME_COLOR, corner_radius=0)
        self.place(relx=0.022, rely=0.024, relwidth=0.2, relheight=0.18)
        self.parent = parent

        self.canvas = ctk.CTkCanvas(self, bg=FRAME_COLOR, highlightthickness=0)
        self.canvas.create_line((90, 160, 400, 160), fill=SCROLL_COLOR, width=10)
        self.canvas.pack(expand=True, fill="both")

        self.typed_words = self.canvas.create_text((250, 90), text="0",
                                                   fill=SCROLL_COLOR, font=WORD_COUNT_FONT)
        self.total_words = self.canvas.create_text((250, 225), fill=SCROLL_COLOR, font=WORD_COUNT_FONT)


class TimerFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent, fg_color=FRAME_COLOR, corner_radius=0)
        self.place(relx=0.779, rely=0.024, relwidth=0.2, relheight=0.18)
        self.parent = parent

        self.canvas = ctk.CTkCanvas(self, bg=FRAME_COLOR, highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")

        self.timer = self.canvas.create_text((250, 160), text=str(self.parent.timer_int_var.get()),
                                             fill=SCROLL_COLOR, font=TIMER_FONT)

    def update_timer(self, *args):
        time_left = self.parent.timer_int_var.get()
        time_left -= 1
        self.parent.timer_int_var.set(value=time_left)
        self.canvas.itemconfigure(self.timer, text=str(time_left))

        if time_left > 0:
            self.after(1000, self.update_timer)


class MenuAndStartButtonFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent, fg_color=BG_COLOR, corner_radius=0)
        self.place(relx=0.022, rely=0.2128, relwidth=0.958, relheight=0.04)
        self.parent = parent

        # TIMER LABEL
        self.timer_label = ctk.CTkLabel(self, text="Timer", fg_color=BG_COLOR, font=TIMER_LABEL_FONT,
                                        text_color=FRAME_COLOR)
        self.timer_label.place(relx=0.735, rely=0.01, relwidth=0.2, relheight=0.9)

        # WORD COUNT LABEL
        self.word_count_label = ctk.CTkLabel(self, text="Word Count", fg_color=BG_COLOR, font=TIMER_LABEL_FONT,
                                             text_color=FRAME_COLOR)
        self.word_count_label.pack(side="left", padx=25)

        # TIMER MENU
        self.timer_menu = ctk.CTkOptionMenu(self, fg_color=FRAME_COLOR, text_color=SCROLL_COLOR, font=TIPS_FONT,
                                            values=["60 sec", "90 sec", "120 sec", "180 sec", "250 sec", "300 sec",
                                                    "400 sec", "500 sec"], dropdown_fg_color=BG_COLOR,
                                            width=80, button_hover_color=MENU_HOVER_COLOR, button_color=MENU_BTN_COLOR,
                                            dropdown_text_color=FRAME_COLOR, dropdown_hover_color=MENU_HOVER_COLOR,
                                            command=self.update_timer_seconds, variable=self.parent.timer_menu_var)
        self.timer_menu.pack(side="right", padx=10)

        # START BUTTON
        self.start_btn = ctk.CTkButton(self, text=self.parent.start_btn_var.get(), font=TIMER_LABEL_FONT,
                                       fg_color=FRAME_COLOR, text_color=START_BTN_COLOR, hover_color=MENU_HOVER_COLOR,
                                       command=self.update_button)
        self.start_btn.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=1, anchor="center")

    def update_timer_seconds(self, *args):
        selected_time = int(self.parent.timer_menu_var.get().split(" ")[0])
        if self.parent.start_btn_var.get() != "Started":
            self.parent.timer_int_var.set(value=selected_time)
            self.parent.timer.canvas.itemconfigure(self.parent.timer.timer, text=selected_time, fill=SCROLL_COLOR)

    def update_button(self, *args):
        if self.parent.start_btn_var.get() == "Start" or "Restart":
            self.parent.start_btn_var.set(value="Started")
            self.start_btn.configure(text=self.parent.start_btn_var.get(), fg_color=STARTED_BG_COLOR, state="disabled")

        if self.parent.start_btn_var.get() == "Started":
            self.parent.scrollable_frame.sentence_list = get_sentence_to_type()
            word_count_list = len([word for sentence in self.parent.scrollable_frame.sentence_list
                                   for word in sentence.split(" ")])

            for index, (label, entry) in enumerate(self.parent.scrollable_frame.label_and_entry_list):
                label.configure(text=f" {self.parent.scrollable_frame.sentence_list[index]}",
                                text_color=TYPE_TEXT_COLOR)
                entry.configure(state="normal")
                entry.delete(0, 'end')

            self.parent.word_count.canvas.itemconfigure(self.parent.word_count.total_words, text=f"{word_count_list}")


class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent, fg_color=SCROLL_COLOR, corner_radius=0,
                         scrollbar_button_hover_color=MENU_HOVER_COLOR, scrollbar_button_color=BG_COLOR)
        self.place(relx=0.218, rely=0.26, relwidth=0.56, relheight=0.696)
        self.parent = parent

        self.entry_var_list = [ctk.StringVar() for _ in range(8)]

        self.label_and_entry_list = []
        self.sentence_list = get_sentence_to_type()
        word_count_list = [word for sentence in self.sentence_list for word in sentence.split(" ")]
        word_count = len(word_count_list)
        self.parent.word_count.canvas.itemconfigure(self.parent.word_count.total_words, text=f"{word_count}")

        for n in range(8):
            label = ctk.CTkLabel(self, text=f" {self.sentence_list[n]}", fg_color=BG_COLOR, font=ENTRY_FONT, anchor="w")
            entry = ctk.CTkEntry(self, fg_color=BG_COLOR, font=ENTRY_FONT, border_color=MENU_HOVER_COLOR,
                                 textvariable=self.entry_var_list[n])
            self.label_and_entry_list.append((label, entry))

        for label, entry in self.label_and_entry_list:
            label.pack(expand=True, fill="both", pady=10, padx=10)
            entry.pack(expand=True, fill="both", pady=10, padx=10)

        for entry_var in self.entry_var_list:
            entry_var.trace_add("write", self.update_word_count)

    def update_word_count(self, *args):
        score = 0

        correct_sentence_list = [label.cget("text")[1:] for label, entry in self.label_and_entry_list]
        sentence_typed_list = [entry_var.get() for entry_var in self.entry_var_list]

        correct_words_list = [word.split(" ") for word in correct_sentence_list]
        words_typed_list = [entry_var.get().split(" ") for entry_var in self.entry_var_list]

        for n in range(len(correct_sentence_list)):
            if correct_sentence_list[n] == sentence_typed_list[n]:
                self.label_and_entry_list[n][0].configure(text=f" {correct_sentence_list[n]} ✅",
                                                          text_color=TIME_COUNT_COLOR)

            current_input_word_list = correct_words_list[n]
            current_input_typed = words_typed_list[n]
            for x in range(len(current_input_typed) - 1):
                if current_input_typed[x] == current_input_word_list[x]:
                    score += 1

        self.parent.word_count.canvas.itemconfigure(self.parent.word_count.typed_words,
                                                    text=score)


class LeftTipFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent, fg_color=FRAME_COLOR, corner_radius=0)
        self.place(relx=0.022, rely=0.26, relwidth=0.2, relheight=0.695)
        self.parent = parent

        self.canvas = ctk.CTkCanvas(self, bg=FRAME_COLOR, highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")

        self.canvas.create_text((40, 40), text=tip_1, fill=TIPS_COLOR, font=CANVAS_TIP_FONT, width=430, anchor="nw")


class RightTipFrame(ctk.CTkFrame):
    def __init__(self, parent: App):
        super().__init__(master=parent, fg_color=FRAME_COLOR, corner_radius=0)
        self.place(relx=0.779, rely=0.26, relwidth=0.2, relheight=0.695)
        self.parent = parent

        self.canvas = ctk.CTkCanvas(self, bg=FRAME_COLOR, highlightthickness=0)
        self.canvas.pack(expand=True, fill="both")

        self.canvas.create_text((40, 40), text=tip_2, fill=TIPS_COLOR, font=CANVAS_TIP_FONT, width=430, anchor="nw")


if __name__ == "__main__":
    app = App()
    app.mainloop()
