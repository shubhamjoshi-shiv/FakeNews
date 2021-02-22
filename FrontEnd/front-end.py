import tkinter as tk
root=tk.Tk()

##################################
main=tk.Frame(root,bg="#e0ffff")
##################################
header_frame=tk.Frame(main,bg="#e0ffff")
head_label=tk.Label(header_frame,text="Fake News Detector",fg="red",bg="#e0ffff",pady=100,font=('Arial','30'))
head_label.pack()
header_frame.place(relx=0.3,rely=0.1,relheight=0.1,relwidth=0.4)
###################################
header=tk.Frame(main,bg="black",padx=2,pady=2,bd=2)
######################################################
text_input=tk.Frame(header)
text=tk.Text(text_input)
text.pack()
text_input.place(relheight=0.4,relwidth=1)
###############################################
button_input=tk.Frame(header,bd=2,bg="#00ffff",padx=2,pady=4)
b=tk.Button(button_input,text="Check",bd=5,bg="teal",pady=2,fg="white",activeforeground="white",activebackground="teal")
b.pack()
button_input.place(relheight=0.1,relwidth=1,rely=0.4)
################################################
result_frame=tk.Frame(header)
result_label=tk.Label(result_frame,text="Result:True",fg="red",bg="#00ffff",pady=100,font=('Arial Black','20'),width=100)
result_label.pack()
result_frame.place(relheight=0.5,relwidth=1,rely=0.5)
header.place(relx=0.3,rely=0.22,relheight=0.6,relwidth=0.4)
#####################################
main.place(relheight=1,relwidth=1)
root.mainloop()
