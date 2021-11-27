
import qrcode
import tkinter as tk
import ttkbootstrap as ttkb
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import NO, showinfo


class Gui:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('QR maker')
        self.style = ttkb.Style('cosmo')
        self.input_text = ScrolledText()
        self.data_entry()
        self.make_qr_btton()
        self.switch_theme_button()
        self.root.mainloop()

    def data_entry(self) -> None:
        input_label = ttkb.ttk.Label(self.root, text="Input",)
        input_label.grid(row=1, column=1, padx=5, pady=5)
        self.input_text = ScrolledText(self.root, bd=1, height=5)
        self.input_text.grid(row=1, column=2, columnspan=3, padx=5, pady=5)

    def make_qr_btton(self) -> None:
        button = ttkb.ttk.Button(self.root, text='Generate', command=self.qr_generator)
        button.grid(row=1, column=5, rowspan=1, padx=5, pady=5)
    
    def switch_theme_button(self) -> None:
        button = ttkb.ttk.Button(self.root, text='Switch theme', command=self.switch_theme)
        button.grid(row=2, column=5, rowspan=1, padx=5, pady=5)
        
    def qr_generator(self) -> None:
        text = self.input_text.get('1.0', 'end-1c')
        qr = qrcode.QRCode(
            version=1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=1,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qr.png')

        self.show_complete()

    def show_complete(self) -> None:
        showinfo('Info', 'Completed !')
        self.root.destroy()
    
    def switch_theme(self) -> None:
        # print(self.style.theme.name)

        if  self.style.theme.name == 'cosmo':
            self.style = ttkb.Style('superhero')
        else:
            self.style = ttkb.Style('cosmo')        

def main() -> None:
    Gui()

if __name__ == '__main__':
    main()