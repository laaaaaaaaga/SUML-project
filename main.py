"""Gui app for Diamonds evaluation SUML project"""
import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlencode

import requests


def open_popup(value):
    """function for opening popup with given value as pricing."""
    top = tk.Toplevel()
    top.wm_title("Price of diamond")
    top_label = tk.Label(top, text="suggested price = " + str(value))
    top_label.pack(fill="x")
    button_close = tk.Button(top, text="close", command=top.destroy)
    button_close.pack(fill="x")


def open_error(args):
    """function for opening errorbox with given args"""
    tk.messagebox.showerror("error has occurred", args)


class MyGUI:
    """Main GUI application body"""

    def __init__(self):
        self.webhook_url = "https://diamonds-jcvkxdo2ba-lz.a.run.app/diamond_price"
        self.root = tk.Tk()
        self.cut_value = tk.StringVar(value="Ideal")
        self.color_value = tk.StringVar(value="D")
        self.clarity_value = tk.StringVar(value="SI1")
        self.x_value = tk.DoubleVar(value=1)
        self.y_value = tk.DoubleVar(value=1)
        self.z_value = tk.DoubleVar(value=1)
        self.carat_value = tk.DoubleVar(value=1)
        self.depth_value = tk.DoubleVar(value=1)
        self.table_value = tk.DoubleVar(value=1)
        self.price_value = tk.IntVar(value=1)
        # self.root.geometry("600x500")
        self.root.title("Diamonds value calculating app")
        self.radio_frame = tk.Frame(self.root)
        self.radio_frame.rowconfigure(0, weight=1)
        self.radio_frame.rowconfigure(1, weight=1)
        self.radio_frame.rowconfigure(2, weight=1)
        self.radio_frame.rowconfigure(3, weight=1)
        self.radio_frame.columnconfigure(0, weight=2)
        self.radio_frame.columnconfigure(1, weight=1)
        self.radio_frame.columnconfigure(2, weight=1)
        self.radio_frame.columnconfigure(3, weight=1)
        self.radio_frame.columnconfigure(4, weight=1)
        self.radio_frame.columnconfigure(5, weight=1)
        self.radio_frame.columnconfigure(6, weight=1)
        self.radio_frame.columnconfigure(7, weight=1)
        self.radio_frame.columnconfigure(8, weight=1)
        self.radio_frame.columnconfigure(9, weight=1)
        self.cut_label = tk.Label(self.radio_frame, text="cut")
        self.cut_label.grid(row=0, column=0)
        self.color_label = tk.Label(self.radio_frame, text="color")
        self.color_label.grid(row=1, column=0)
        self.clarity_label = tk.Label(self.radio_frame, text="clarity")
        self.clarity_label.grid(row=2, column=0)
        self.cut_ideal = tk.Radiobutton(self.radio_frame, text="Ideal", value="Ideal",
                                        variable=self.cut_value, padx=10, pady=10,
                                        command=self.selection_cut, )
        self.cut_ideal.grid(row=0, column=1)
        self.cut_premium = tk.Radiobutton(self.radio_frame, text="Premium", value="Premium",
                                          variable=self.cut_value, padx=10, pady=10,
                                          command=self.selection_cut, )
        self.cut_premium.grid(row=0, column=2)
        self.cut_very_good = tk.Radiobutton(self.radio_frame, text="Very Good", value="Very_good",
                                            variable=self.cut_value, padx=10, pady=10,
                                            command=self.selection_cut, )
        self.cut_very_good.grid(row=0, column=3)
        self.cut_good = tk.Radiobutton(self.radio_frame, text="Good", value="Good",
                                       variable=self.cut_value, padx=10, pady=10,
                                       command=self.selection_cut, )
        self.cut_good.grid(row=0, column=4)
        self.cut_fair = tk.Radiobutton(self.radio_frame, text="Fair", value="Fair",
                                       variable=self.cut_value, padx=10, pady=10,
                                       command=self.selection_cut, )
        self.cut_fair.grid(row=0, column=5)
        self.color_d = tk.Radiobutton(self.radio_frame, text="D", value="D",
                                      variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color, )
        self.color_d.grid(row=1, column=1)
        self.color_e = tk.Radiobutton(self.radio_frame, text="E", value="E",
                                      variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color, )
        self.color_e.grid(row=1, column=2)
        self.color_f = tk.Radiobutton(self.radio_frame, text="F", value="F",
                                      variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color, )
        self.color_f.grid(row=1, column=3)
        self.color_g = tk.Radiobutton(self.radio_frame, text="G", value="G",
                                      variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color, )
        self.color_g.grid(row=1, column=4)
        self.color_h = tk.Radiobutton(self.radio_frame, text="H", value="H",
                                      variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color, )
        self.color_h.grid(row=1, column=5)
        self.color_i = tk.Radiobutton(self.radio_frame, text="I", value="I",
                                      variable=self.color_value, padx=10, pady=10,
                                      command=self.selection_color, )
        self.color_i.grid(row=1, column=6)
        self.clarity_si1 = tk.Radiobutton(self.radio_frame, text="SI1", value="SI1",
                                          variable=self.clarity_value, padx=10, pady=10,
                                          command=self.selection_clarity, )
        self.clarity_si1.grid(row=2, column=1)
        self.clarity_si2 = tk.Radiobutton(self.radio_frame, text="SI2", value="SI2",
                                          variable=self.clarity_value, padx=10, pady=10,
                                          command=self.selection_clarity, )
        self.clarity_si2.grid(row=2, column=2)
        self.clarity_vs1 = tk.Radiobutton(self.radio_frame, text="VS1", value="VS1",
                                          variable=self.clarity_value, padx=10, pady=10,
                                          command=self.selection_clarity, )
        self.clarity_vs1.grid(row=2, column=3)
        self.clarity_vs2 = tk.Radiobutton(self.radio_frame, text="VS2", value="VS2",
                                          variable=self.clarity_value, padx=10, pady=10,
                                          command=self.selection_clarity, )
        self.clarity_vs2.grid(row=2, column=4)
        self.clarity_vvs1 = tk.Radiobutton(self.radio_frame, text="VVS1", value="VVS1",
                                           variable=self.clarity_value, padx=10, pady=10,
                                           command=self.selection_clarity, )
        self.clarity_vvs1.grid(row=2, column=5)
        self.clarity_vvs2 = tk.Radiobutton(self.radio_frame, text="VVS2", value="VVS2",
                                           variable=self.clarity_value, padx=10, pady=10,
                                           command=self.selection_clarity, )
        self.clarity_vvs2.grid(row=2, column=6)
        self.clarity_i1 = tk.Radiobutton(self.radio_frame, text="I1", value="I1",
                                         variable=self.clarity_value, padx=10, pady=10,
                                         command=self.selection_clarity, )
        self.clarity_i1.grid(row=2, column=7)
        self.clarity_if = tk.Radiobutton(self.radio_frame, text="IF", value="IF",
                                         variable=self.clarity_value, padx=10, pady=10,
                                         command=self.selection_clarity, )
        self.clarity_if.grid(row=2, column=8)
        self.radio_frame.pack(fill="x")
        self.text_fields_frame = tk.Frame(self.root)
        self.carat_label = tk.Label(self.text_fields_frame, text="Carats")
        self.carat_label.grid(row=0, column=0)
        self.entry_carat = tk.Entry(self.text_fields_frame, insertwidth=2,
                                    textvariable=self.carat_value)
        self.entry_carat.grid(row=1, column=0)
        self.depth_label = tk.Label(self.text_fields_frame, text="Depth")
        self.depth_label.grid(row=0, column=1)
        self.entry_depth = tk.Entry(self.text_fields_frame, insertwidth=2,
                                    textvariable=self.depth_value)
        self.entry_depth.grid(row=1, column=1)
        self.table_label = tk.Label(self.text_fields_frame, text="Table")
        self.table_label.grid(row=0, column=2)
        self.entry_table = tk.Entry(self.text_fields_frame, insertwidth=2,
                                    textvariable=self.table_value)
        self.entry_table.grid(row=1, column=2)
        self.x_label = tk.Label(self.text_fields_frame, text="Length in mm")
        self.x_label.grid(row=0, column=3)
        self.entry_x = tk.Entry(self.text_fields_frame, insertwidth=2, textvariable=self.x_value)
        self.entry_x.grid(row=1, column=3)
        self.y_label = tk.Label(self.text_fields_frame, text="Width in mm")
        self.y_label.grid(row=0, column=4)
        self.entry_y = tk.Entry(self.text_fields_frame, insertwidth=2, textvariable=self.y_value)
        self.entry_y.grid(row=1, column=4)
        self.z_label = tk.Label(self.text_fields_frame, text="Depth in mm")
        self.z_label.grid(row=0, column=5)
        self.entry_z = tk.Entry(self.text_fields_frame, insertwidth=2, textvariable=self.z_value)
        self.entry_z.grid(row=1, column=5)
        self.text_fields_frame.pack()
        self.send_button = tk.Button(self.root, text="price", padx=10, command=self.send)
        self.send_button.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def selection_cut(self):
        """function responsible for changing name of cut label"""
        cut_selection = "you chose " + str(self.cut_value.get())
        self.cut_label.config(text=cut_selection)

    def selection_color(self):
        """function responsible for changing name of color label"""
        color_selection = "you chose " + str(self.color_value.get())
        self.color_label.config(text=color_selection)

    def selection_clarity(self):
        """function responsible for changing name of clarity label"""
        clarity_selection = "you chose " + str(self.clarity_value.get())
        self.clarity_label.config(text=clarity_selection)

    def send(self):
        """main data request method"""
        try:
            if self.carat_value.get() < 0 or self.depth_value.get() < 0:
                raise ValueError
            if self.table_value.get() < 0:
                raise ValueError
            if self.x_value.get() < 0 or self.y_value.get() < 0 or self.z_value.get() < 0:
                raise ValueError
            data = {"carat": self.carat_value.get(), "cut": self.cut_value.get(),
                    "color": self.color_value.get(), "clarity": self.clarity_value.get(),
                    "depth": self.depth_value.get(), "table": self.table_value.get(),
                    "x": self.x_value.get(), "y": self.y_value.get(), "z": self.z_value.get(), }
            url_params = urlencode(data)
            response = requests.get(f"{self.webhook_url}?{url_params}", timeout=10000)
            if response.status_code == 200:
                prediction = response.json()["prediction"]
                open_popup(prediction)  # print(prediction)
        except tk.TclError:
            open_error("please input float value")
        except ValueError:
            open_error("The value is incorrect, please use value that\'s above 0")
        except:
            open_error("Something is wrong, please contact the developer")

    def on_closing(self):
        """method asking for confirmation on app closing"""
        if messagebox.askyesno(title="Quit?", message="do you want to quit the program?"):
            self.root.destroy()


# --- main ---
MyGUI()
