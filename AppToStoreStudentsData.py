import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.geometry("600x600+299+2")
root.configure(background="#68829E")
root.title("Students Data")

#root1=''
#root2=''
#root3=''
f_insert = open('Std_data_insert.txt', 'a+')


class Insert_Window:
    def __init__(self, master):

        self.name=tk.Label(master, text="Name", background="#4CB5F5")
        self.name.place(relx=0.250, rely=0.235)

        self.insrt_name=tk.Entry(master, width=30)
        self.insrt_name.place(relx=0.350, rely=0.235)

        self.roll_no=tk.Label(master, text="Roll Number", background="#4CB5F5")
        self.roll_no.place(relx=0.160, rely=0.300)

        self.insrt_roll_no=tk.Entry(master, width=30)
        self.insrt_roll_no.place(relx=0.350, rely=0.300)

        self.dept=tk.Label(master, text="Department", background="#4CB5F5")
        self.dept.place(relx=0.170, rely=0.365)

        self.insrt_dept=tk.Entry(master, width=30)
        self.insrt_dept.place(relx=0.350, rely=0.365)

        self.cgpa=tk.Label(master, text="CGPA", background="#4CB5F5")
        self.cgpa.place(relx=0.250, rely=0.430)

        self.insrt_cgpa=tk.Entry(master, width=8)
        self.insrt_cgpa.place(relx=0.350, rely=0.430)

        self.insrt = tk.Button(master,background="#BCBABE", text="Insert", command= lambda: self.dstr_insrt_wind(self.insrt_name, self.insrt_roll_no, self.insrt_dept, self.insrt_cgpa, master))
        self.insrt.place(relx = 0.350, rely = 0.550)

    def dstr_insrt_wind(self, insrt_name, insrt_roll_no, insrt_dept, insrt_cgpa, master):
        f_insert.write('{}   {}   {}   {}\n'.format(insrt_name.get(), insrt_roll_no.get(), insrt_dept.get(), insrt_cgpa.get()))
        master.destroy()


class Fetch_Window:
    def __init__(self, master):
        roll_num1=[]
        f_insert.seek(0)
        for line in f_insert:
            roll_data = [ele for ele in line.split("   ")] 
            print(roll_data)   
            roll_num1.append(int(roll_data[1]))
        print(roll_num1)        
        self.variable = tk.IntVar(master)
        self.variable.set(roll_num1[0])
        self.roll_val = roll_num1[0]
        self.drop_roll = tk.OptionMenu(master, self.variable, *roll_num1, command= self.callback)
        self.drop_roll.place(relx=0.350, rely=0.150) 

        self.fetch_but = tk.Button(master,background="#FFCCAC",  text="Fetch", command=lambda: self.fetch_fun(master))
        self.fetch_but.place(relx=0.350, rely=0.250)

    def callback(self, selection):
        self.roll_val = selection
    
    def fetch_fun(self, master):
        f_insert.seek(0)
        for line in f_insert:
            roll_data = [ele for ele in line.split("   ")]
            print(roll_data)
            if int(roll_data[1])==self.roll_val:
                label_name = roll_data[0]
                label_roll = roll_data[1]
                label_dept = roll_data[2]
                label_cgpa = roll_data[3]
                break 

        self.l_name = tk.Label(master, text="Name: {}".format(label_name), background="#4CB5F5")
        self.l_name.place(relx=0.350, rely=0.400)

        self.l_roll = tk.Label(master, text="Roll Number: {}".format(label_roll), background="#4CB5F5")
        self.l_roll.place(relx=0.350, rely=0.500)

        self.l_dept = tk.Label(master, text="Department: {}".format(label_dept), background="#4CB5F5")
        self.l_dept.place(relx=0.350, rely=0.600)

        self.l_cgpa = tk.Label(master, text="CGPA: {}".format(label_cgpa), background="#4CB5F5")
        self.l_cgpa.place(relx=0.350, rely=0.700) 
                     



class Delete_Window:
    def __init__(self, master):
        roll_num1=[]
        f_insert.seek(0)
        for line in f_insert:
            roll_data = [ele for ele in line.split("   ")]    
            roll_num1.append(int(roll_data[1]))
        self.variable1 = tk.IntVar(master)
        self.variable1.set(roll_num1[0])
        self.drop_roll = tk.OptionMenu(master, self.variable1, *roll_num1, command=self.callback)
        self.drop_roll.place(relx=0.350, rely=0.350) 

        self.delet = tk.Button(master,background="#FFCCAC", text="Delete", command= lambda: self.confirmation_box(master))
        self.delet.place(relx = 0.350, rely = 0.550)
    

    def callback(self, selection):
        self.roll_val = selection

    
    def confirmation_box(self, master):
        self.MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to delete the data',icon = 'warning')
        if self.MsgBox == 'yes':
            f_del = open('Std_data_insert.txt', 'r')
            lines = f_del.readlines()
            f_del.close()
            f_del = open('Std_data_insert.txt', 'w')
            for line in lines:
                roll_data = [ele for ele in line.split("   ")]
                if int(roll_data[1])!=self.roll_val:
                    f_del.write(line)
            master.destroy()

        else:
            messagebox.showinfo('Return','You will now return to the application screen')

class Main_Window:
    def __init__(self, parent):
        self.Insert=tk.Button(parent, text="Insert", width="27", command=lambda: self.insert_wind(), background="#505160")
        self.Insert.grid(row=0,column=0)

        self.Fetch=tk.Button(parent, text="Fetch", width="27", command=lambda: self.fetch_wind(), background="#505160")
        self.Fetch.grid(row=0,column=1)

        self.Delete=tk.Button(parent, text="Delete", width="28", command=lambda: self.delete_data(), background="#505160")
        self.Delete.grid(row=0, column=2)

    def insert_wind(self):
        root1=tk.Tk()
        root1.geometry("400x400+400+2")
        root1.configure(background="#4CB5F5")
        root1.title("Insert Student's Details")       
        ins_win = Insert_Window(root1)

    def fetch_wind(self):
        root2=tk.Tk()
        root2.geometry("400x400+400+2")
        root2.configure(background="#4CB5F5")
        root2.title("Fetch Student's Data")
        fet_win = Fetch_Window(root2)

    def delete_data(self):
        root3=tk.Tk()
        root3.geometry("400x400+400+2")
        root3.configure(background="#4CB5F5")
        root3.title("Delete Student's Data")
        del_win = Delete_Window(root3)

main_wind = Main_Window(root)
root.mainloop()
f_insert.close()
