from tkinter import font,Label,Button,Entry, Tk
from search import start
import threading



def run(title_video, range_videos):
    start(title_video, range_videos)




def thread_video():
    title_video = entry_search.get()
    range_video = int(entry_range.get())
    thread1 = threading.Thread(target=run, args= (title_video, range_video))
    thread1.start()




if __name__ == '__main__':
    root = Tk()
    root.title('Obtener videos')
    root.geometry('700x500')

    entry_search = Entry(root,width=20)
    entry_search['font'] = font.Font(size=12)
    entry_search.place(x=220,y=100)

    btn_search = Button(root,width=16,height=1,text='Buscar',font=font.Font(size=12),command=thread_video).place(x=0,y=400)

    label_titulo = Label(root,width=40,height=1,text='Ingresa un tema a buscar',font=font.Font(size=15)).place(x=20,y=10)

    label_rango = Label(root,width=20,height=2,text='¿Cuantos videos quiere?\n(Valor de 1 al 30)',font=font.Font(size=12)).place(x=220,y=170)

    entry_range = Entry(root,width=20)
    entry_range['font'] = font.Font(size=12)
    entry_range.place(x=220,y=250)

    root.mainloop()