import tkinter as tk
from enum import Enum, auto
from tkinter import colorchooser
from PIL import Image
import os

list_colours = (
    "snow", "ghost white", "white smoke", "gainsboro", "floral white", "old lace", "linen", "antique white",
    "papaya whip", "blanched almond", "bisque", "peach puff", "navajo white", "lemon chiffon", "mint cream", "azure",
    "alice blue", "lavender", "lavender blush", "misty rose", "dark slate gray", "dim gray", "slate gray",
    "light slate gray", "gray", "light grey", "midnight blue", "navy", "cornflower blue", "dark slate blue",
    "slate blue", "medium slate blue", "light slate blue", "medium blue", "royal blue", "blue", "dodger blue",
    "deep sky blue", "sky blue", "light sky blue", "steel blue", "light steel blue", "light blue", "powder blue",
    "pale turquoise", "dark turquoise", "medium turquoise", "turquoise", "cyan", "light cyan", "cadet blue",
    "medium aquamarine", "aquamarine", "dark green", "dark olive green", "dark sea green", "sea green",
    "medium sea green", "light sea green", "pale green", "spring green", "lawn green", "medium spring green",
    "green yellow", "lime green", "yellow green", "forest green", "olive drab", "dark khaki", "khaki",
    "pale goldenrod", "light goldenrod yellow", "light yellow", "yellow", "gold", "light goldenrod", "goldenrod",
    "dark goldenrod", "rosy brown", "indian red", "saddle brown", "sandy brown", "dark salmon", "salmon",
    "light salmon", "orange", "dark orange", "coral", "light coral", "tomato", "orange red", "red", "hot pink",
    "deep pink", "pink", "light pink", "pale violet red", "maroon", "medium violet red", "violet red", "medium orchid",
    "dark orchid", "dark violet", "thistle", "snow2", "snow3", "snow4", "seashell2", "seashell3", "seashell4",
    "AntiqueWhite1", "AntiqueWhite2", "AntiqueWhite3", "AntiqueWhite4", "bisque2", "bisque3", "bisque4", "PeachPuff2",
    "PeachPuff3", "PeachPuff4", "NavajoWhite2", "NavajoWhite3", "NavajoWhite4", "LemonChiffon2", "LemonChiffon3",
    "LemonChiffon4", "cornsilk2", "cornsilk3", "cornsilk4", "ivory2", "ivory3", "ivory4", "honeydew2", "honeydew3",
    "honeydew4", "LavenderBlush2", "LavenderBlush3", "LavenderBlush4", "MistyRose2", "MistyRose3", "MistyRose4",
    "azure2", "azure3", "azure4", "SlateBlue1", "SlateBlue2", "SlateBlue3", "SlateBlue4", "RoyalBlue1", "RoyalBlue2",
    "RoyalBlue3", "RoyalBlue4", "blue2", "blue4", "DodgerBlue2", "DodgerBlue3", "DodgerBlue4", "SteelBlue1",
    "SteelBlue2", "SteelBlue3", "SteelBlue4", "DeepSkyBlue2", "DeepSkyBlue3", "DeepSkyBlue4", "SkyBlue1", "SkyBlue2",
    "SkyBlue3", "SkyBlue4", "LightSkyBlue1", "LightSkyBlue2", "LightSkyBlue3", "LightSkyBlue4", "SlateGray1",
    "SlateGray2", "SlateGray3", "SlateGray4", "LightSteelBlue1", "LightSteelBlue2", "LightSteelBlue3",
    "LightSteelBlue4", "LightBlue1", "LightBlue2", "LightBlue3", "LightBlue4", "LightCyan2", "LightCyan3",
    "LightCyan4", "PaleTurquoise1", "PaleTurquoise2", "PaleTurquoise3", "PaleTurquoise4", "CadetBlue1", "CadetBlue2",
    "CadetBlue3", "CadetBlue4", "turquoise1", "turquoise2", "turquoise3", "turquoise4", "cyan2", "cyan3", "cyan4",
    "DarkSlateGray1", "DarkSlateGray2", "DarkSlateGray3", "DarkSlateGray4", "aquamarine2", "aquamarine4",
    "DarkSeaGreen1", "DarkSeaGreen2", "DarkSeaGreen3", "DarkSeaGreen4", "SeaGreen1", "SeaGreen2", "SeaGreen3",
    "PaleGreen1", "PaleGreen2", "PaleGreen3", "PaleGreen4", "SpringGreen2", "SpringGreen3", "SpringGreen4", "green2",
    "green3", "green4", "chartreuse2", "chartreuse3", "chartreuse4", "OliveDrab1", "OliveDrab2", "OliveDrab4",
    "DarkOliveGreen1", "DarkOliveGreen2", "DarkOliveGreen3", "DarkOliveGreen4", "khaki1", "khaki2", "khaki3", "khaki4",
    "LightGoldenrod1", "LightGoldenrod2", "LightGoldenrod3", "LightGoldenrod4", "LightYellow2", "LightYellow3",
    "LightYellow4", "yellow2", "yellow3", "yellow4", "gold2", "gold3", "gold4", "goldenrod1", "goldenrod2",
    "goldenrod3", "goldenrod4", "DarkGoldenrod1", "DarkGoldenrod2", "DarkGoldenrod3", "DarkGoldenrod4", "RosyBrown1",
    "RosyBrown2", "RosyBrown3", "RosyBrown4", "IndianRed1", "IndianRed2", "IndianRed3", "IndianRed4", "sienna1",
    "sienna2", "sienna3", "sienna4", "burlywood1", "burlywood2", "burlywood3", "burlywood4", "wheat1", "wheat2",
    "wheat3", "wheat4", "tan1", "tan2", "tan4", "chocolate1", "chocolate2", "chocolate3", "firebrick1", "firebrick2",
    "firebrick3", "firebrick4", "brown1", "brown2", "brown3", "brown4", "salmon1", "salmon2", "salmon3", "salmon4",
    "LightSalmon2", "LightSalmon3", "LightSalmon4", "orange2", "orange3", "orange4", "DarkOrange1", "DarkOrange2",
    "DarkOrange3", "DarkOrange4", "coral1", "coral2", "coral3", "coral4", "tomato2", "tomato3", "tomato4",
    "OrangeRed2", "OrangeRed3", "OrangeRed4", "red2", "red3", "red4", "DeepPink2", "DeepPink3", "DeepPink4",
    "HotPink1", "HotPink2", "HotPink3", "HotPink4", "pink1", "pink2", "pink3", "pink4", "LightPink1", "LightPink2",
    "LightPink3", "LightPink4", "PaleVioletRed1", "PaleVioletRed2", "PaleVioletRed3", "PaleVioletRed4", "maroon1",
    "maroon2", "maroon3", "maroon4", "VioletRed1", "VioletRed2", "VioletRed3", "VioletRed4", "magenta2", "magenta3",
    "magenta4", "orchid1", "orchid2", "orchid3", "orchid4", "plum1", "plum2", "plum3", "plum4", "MediumOrchid1",
    "MediumOrchid2", "MediumOrchid3", "MediumOrchid4", "DarkOrchid1", "DarkOrchid2", "DarkOrchid3", "DarkOrchid4",
    "purple1", "purple2", "purple3", "purple4", "MediumPurple1", "MediumPurple2", "MediumPurple3", "MediumPurple4",
    "thistle1", "thistle2", "thistle3", "thistle4", "gray1", "gray2", "gray3", "gray4", "gray5", "gray6", "gray7",
    "gray8", "gray9", "gray10", "gray11", "gray12", "gray13", "gray14", "gray15", "gray16", "gray17", "gray18",
    "gray19", "gray20", "gray21", "gray22", "gray23", "gray24", "gray25", "gray26", "gray27", "gray28", "gray29",
    "gray30", "gray31", "gray32", "gray33", "gray34", "gray35", "gray36", "gray37", "gray38", "gray39", "gray40",
    "gray42", "gray43", "gray44", "gray45", "gray46", "gray47", "gray48", "gray49", "gray50", "gray51", "gray52",
    "gray53", "gray54", "gray55", "gray56", "gray57", "gray58", "gray59", "gray60", "gray61", "gray62", "gray63",
    "gray64", "gray65", "gray66", "gray67", "gray68", "gray69", "gray70", "gray71", "gray72", "gray73", "gray74",
    "gray75", "gray76", "gray77", "gray78", "gray79", "gray80", "gray81", "gray82", "gray83", "gray84", "gray85",
    "gray86", "gray87", "gray88", "gray89", "gray90", "gray91", "gray92", "gray93", "gray94", "gray95", "gray97",
    "gray98", "gray99", "white", "white", "white", "black")


class Brushes(Enum):
    OVAL = auto()
    LINE = auto()
    ERASER = auto()


class PainTk:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PainTk")
        self.window.minsize(width=720, height=480)
        self.window.resizable(False, False)

        self.img_new = tk.PhotoImage(file="icons/new.png")
        self.img_save = tk.PhotoImage(file="icons/save.png")
        self.img_line = tk.PhotoImage(file="icons/line.png")
        self.img_oval = tk.PhotoImage(file="icons/oval.png")
        self.img_square = tk.PhotoImage(file="icons/square.png")
        self.img_eraser = tk.PhotoImage(file="icons/eraser.png")

        self.chosen_colour = list_colours[-1]
        self.chosen_brush = Brushes.OVAL

        self.top_menu_bar = tk.Frame(self.window, bg="#3b3b3b", height=50, padx=5)
        self.top_menu_bar.pack(fill="x")

        self.text_chosen_colour = tk.Label(self.top_menu_bar, text="Select Colour:", fg="white", bg="#3b3b3b", padx=10)
        self.text_chosen_colour.pack(side="left")

        self.button_chosen_colour = tk.Button(self.top_menu_bar, image=self.img_square, bd=0,
                                              command=self.select_colour_palette)
        self.button_chosen_colour.pack(side="left")

        self.text_options = tk.Label(self.top_menu_bar, text="Options:", fg="white", bg="#3b3b3b", padx=10)
        self.text_options.pack(side="left")

        self.button_new = tk.Button(self.top_menu_bar, bg="#3b3b3b", image=self.img_new, bd=0,
                                    command=self.clear_canvas)
        self.button_new.pack(side="left")
        self.button_save = tk.Button(self.top_menu_bar, bg="#3b3b3b", image=self.img_save, bd=0,
                                     command=self.save_canvas)
        self.button_save.pack(side="left")

        self.text_brushes = tk.Label(self.top_menu_bar, text="Brushes:", fg="white", bg="#3b3b3b", padx=10)
        self.text_brushes.pack(side="left")

        self.button_line = tk.Button(self.top_menu_bar, bg="#3b3b3b", image=self.img_line, bd=0,
                                     command=lambda: self.select_brush(Brushes.LINE))
        self.button_line.pack(side="left")
        self.button_oval = tk.Button(self.top_menu_bar, bg="#3b3b3b", image=self.img_oval, bd=0,
                                     command=lambda: self.select_brush(Brushes.OVAL))
        self.button_oval.pack(side="left")
        self.button_eraser = tk.Button(self.top_menu_bar, bg="#3b3b3b", image=self.img_eraser, bd=0,
                                       command=lambda: self.select_brush(Brushes.ERASER))
        self.button_eraser.pack(side="left")

        self.text_brush_size = tk.Label(self.top_menu_bar, text="Size:", fg="white", bg="#3b3b3b", padx=10)
        self.text_brush_size.pack(side="left")

        self.chosen_size = tk.StringVar(self.top_menu_bar)
        self.brush_size = tk.Spinbox(self.top_menu_bar, from_=1, to=50, textvariable=self.chosen_size)
        self.brush_size.pack(side="left")
        self.chosen_size.set("16")

        self.drawing_area = tk.Canvas(self.window)  # , height=310)
        self.drawing_area.pack(fill="both")
        self.default_bg = self.drawing_area.cget('bg')

        self.bottom_menu_bar = tk.Frame(self.window, bg="#3b3b3b", height=50, padx=5)
        self.bottom_menu_bar.pack(fill="x")

        self.text_colour = tk.Label(self.bottom_menu_bar, text="Colours:", fg="white", bg="#3b3b3b", padx=10)
        self.text_colour.pack(side="left")

        self.frame_colours = tk.Frame(self.bottom_menu_bar, bg="#3b3b3b", padx=5)
        self.frame_colours.pack(side="left")

        self.frame_colours_line0 = tk.Frame(self.frame_colours, bg="#3b3b3b")
        self.frame_colours_line1 = tk.Frame(self.frame_colours, bg="#3b3b3b")
        self.frame_colours_line2 = tk.Frame(self.frame_colours, bg="#3b3b3b")
        self.frame_colours_line3 = tk.Frame(self.frame_colours, bg="#3b3b3b")
        self.frame_colours_line4 = tk.Frame(self.frame_colours, bg="#3b3b3b")
        self.frame_colours_line5 = tk.Frame(self.frame_colours, bg="#3b3b3b")
        self.frame_colours_line6 = tk.Frame(self.frame_colours, bg="#3b3b3b")
        self.frame_colours_line7 = tk.Frame(self.frame_colours, bg="#3b3b3b")
        self.frame_colours_line8 = tk.Frame(self.frame_colours, bg="#3b3b3b")
        self.frame_colours_line9 = tk.Frame(self.frame_colours, bg="#3b3b3b")

        self.frame_colours_line0.pack()
        self.frame_colours_line1.pack()
        self.frame_colours_line2.pack()
        self.frame_colours_line3.pack()
        self.frame_colours_line4.pack()
        self.frame_colours_line5.pack()
        self.frame_colours_line6.pack()
        self.frame_colours_line7.pack()
        self.frame_colours_line8.pack()
        self.frame_colours_line9.pack()

        for i, colour in enumerate(list_colours):
            row_index = i % 10
            if row_index == 0:
                tk.Button(self.frame_colours_line0, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")
            elif row_index == 1:
                tk.Button(self.frame_colours_line1, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")
            elif row_index == 2:
                tk.Button(self.frame_colours_line2, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")
            elif row_index == 3:
                tk.Button(self.frame_colours_line3, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")
            elif row_index == 4:
                tk.Button(self.frame_colours_line4, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")
            elif row_index == 5:
                tk.Button(self.frame_colours_line5, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")
            elif row_index == 6:
                tk.Button(self.frame_colours_line6, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")
            elif row_index == 7:
                tk.Button(self.frame_colours_line7, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")
            elif row_index == 8:
                tk.Button(self.frame_colours_line8, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")
            elif row_index == 9:
                tk.Button(self.frame_colours_line9, bg=colour, activebackground=colour, width=2, height=1,
                          command=lambda col=colour: self.select_colour(col), bd=0).pack(side="left")

        # key binds
        self.drawing_area.bind("<B1-Motion>", self.drawn)
        self.window.bind("<Control-s>", self.save_canvas_envelop)
        self.window.bind("<Control-d>", self.clear_canvas_envelop)

        self.window.mainloop()

    def drawn(self, event):
        x1, y1 = event.x, event.y
        x2, y2 = event.x, event.y
        if self.chosen_brush == Brushes.OVAL:
            self.drawing_area.create_oval(x1, y1, x2, y2, fill=self.chosen_colour, outline=self.chosen_colour,
                                          width=self.brush_size.get())
        elif self.chosen_brush == Brushes.LINE:
            self.drawing_area.create_line(x1 - 5, y1 - 5, x2, y2, fill=self.chosen_colour, width=self.brush_size.get())
        elif self.chosen_brush == Brushes.ERASER:
            self.drawing_area.create_oval(x1, y1, x2, y2, fill=self.default_bg, outline=self.default_bg,
                                          width=self.brush_size.get())
        else:
            self.chosen_brush = Brushes.OVAL

    def select_colour(self, colour):
        self.chosen_colour = colour

    def select_brush(self, brush):
        if isinstance(brush, Brushes):
            self.chosen_brush = brush

    def clear_canvas_envelop(self, event):
        self.clear_canvas()

    def clear_canvas(self):
        self.drawing_area.delete("all")

    def save_canvas_envelop(self, event):
        self.save_canvas()

    def save_canvas(self):
        self.drawing_area.postscript(file="image.eps")
        img = Image.open("image.eps")
        img.save("image.png", "png")
        img.close()
        os.remove("image.eps")

    def select_colour_palette(self):
        color = tk.colorchooser.askcolor()
        self.select_colour(color[1])


PainTk()
