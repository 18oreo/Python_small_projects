import tkinter as t ,time
r = t.Tk()
lbl = t.Label(r,font=('Sans Serrif', 100, 'bold'),bg='blue',fg='white')
lbl.pack(padx=30, pady=30)
def tick(): lbl.config(text=time.strftime("%I:%M:%S %p"))
lbl.after(1000, tick)

tick()
r.mainloop()