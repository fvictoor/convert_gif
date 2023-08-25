from tkinter import Tk, Canvas, PhotoImage, Button, filedialog, messagebox
from moviepy.editor import VideoFileClip
from pkg_resources import resource_filename

def btn_clicked():
    
    filetypes = (('All files', '*.*'), ('Image', '*.png') )
    input_path = filedialog.askopenfilename( title='Open a file', initialdir='/',filetypes=filetypes)
    videoClip = VideoFileClip(input_path)
    videoClip.write_gif(input_path + ".gif", fps=3,fuzz=1)
    messagebox.showinfo(message="Video convertido com sucesso!")

window = Tk()
window.title("Converter video to Gif")
window.geometry("1000x700")
window.configure(bg = "#FFFFFF")
canvas = Canvas(window,bg = "#FFFFFF", height = 800, width = 1000, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

icon_img = resource_filename(__name__,r"img\\icon.ico")
window.iconbitmap(False, icon_img)

background_img_imp = resource_filename(__name__,r"img\\background.png" )
background_img = PhotoImage(file = background_img_imp)
background = canvas.create_image(500.0, 400.0, image=background_img)

img0_imp = resource_filename(__name__,r"img\img0.png" )
img0 = PhotoImage(file = img0_imp)
b0 = Button( image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b0.place( x = 537, y = 312, width = 280, height = 58)

window.resizable(False, False)
window.mainloop()
