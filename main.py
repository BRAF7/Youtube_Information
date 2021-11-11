#Imports
import search

#Front
from tkinter import font,Label,Button,Entry, Tk

#Back
from concurrent.futures import ThreadPoolExecutor





def run(title_video, range_videos):
    search_module : search = search
    search_module.start(title_video, range_videos)




executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix='facilitos')
def thread_video():
    
    title_video = entry_search.get()
    range_video = int(entry_range.get())
    executor.submit(run, title_video, range_video)





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