import tkinter as tk
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import string

root = tk.Tk()
root.geometry("600x600+400+2")
class MainWindow:
    def __init__(self, master):
        self.Student_label = tk.Label(master, text="Select Student's Answer File", font = ('Comic Sans MS',11))
        self.Student_label.place(relx = 0.2, rely = 0.1)

        self.file1_entry = tk.Entry(master, width=20)
        self.file1_entry.place(relx = 0.4, rely=0.2)

        self.file1_button = tk.Button(master, text="Select File", command=lambda: self.select1stfile())
        self.file1_button.place(relx=0.7, rely=0.2)

        self.Teacher_label = tk.Label(master, text="Select Teacher's Answer Files", font = ('Comic Sans MS',11))
        self.Teacher_label.place(relx = 0.2, rely = 0.4)

        self.file2_label = tk.Label(master, text="1st Answer File")
        self.file2_label.place(relx=0.2, rely=0.5)

        self.file2_entry = tk.Entry(master, width=20)
        self.file2_entry.place(relx = 0.4, rely=0.5)

        self.file2_button = tk.Button(master, text="Select File", command=lambda: self.select2ndfile())
        self.file2_button.place(relx=0.7, rely=0.5)

        self.file3_label = tk.Label(master, text="2nd Answer File")
        self.file3_label.place(relx=0.2, rely=0.55)

        self.file3_entry = tk.Entry(master, width=20)
        self.file3_entry.place(relx = 0.4, rely=0.55)

        self.file3_button = tk.Button(master, text="Select File", command=lambda: self.select3rdfile())
        self.file3_button.place(relx=0.7, rely=0.55)

        self.file4_label = tk.Label(master, text="3rd Answer File")
        self.file4_label.place(relx=0.2, rely=0.6)

        self.file4_entry = tk.Entry(master, width=20)
        self.file4_entry.place(relx = 0.4, rely=0.6)

        self.file4_button = tk.Button(master, text="Select File", command=lambda: self.select4thfile())
        self.file4_button.place(relx=0.7, rely=0.6)

        self.match_button = tk.Button(master, text="Match Answers", command=lambda: self.match_answer(master))
        self.match_button.place(relx=0.4, rely = 0.75)




    def select1stfile(self):
        self.file1 = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
        if self.file1=="":
            self.file1=None
        else:
            lst = [ele for ele in self.file1.split("/")]
            print(lst[-1])
            self.file1_entry.delete(0,END)
            self.file1_entry.insert(END, lst[-1])

    def select2ndfile(self):
        self.file2 = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
        if self.file2=="":
            self.file2=None
        else:
            lst = [ele for ele in self.file2.split("/")]
            print(lst[-1])
            self.file2_entry.delete(0,END)
            self.file2_entry.insert(END, lst[-1])

    def select3rdfile(self):
        self.file3 = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
        if self.file3=="":
            self.file3=None
        else:
            lst = [ele for ele in self.file3.split("/")]
            print(lst[-1])
            self.file3_entry.delete(0,END)
            self.file3_entry.insert(END, lst[-1])

    def select4thfile(self):
        self.file4 = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
        if self.file4=="":
            self.file4=None
        else:
            lst = [ele for ele in self.file4.split("/")]
            print(lst[-1])
            self.file4_entry.delete(0,END)
            self.file4_entry.insert(END, lst[-1])

    def match_answer(self, master):
        def jaccard(a, b):
            c = a.intersection(b)
            return float(len(c)) / (len(a) + len(b) - len(c))

        def resultCalculation(fname):
            tans1 = open(self.file2_entry.get())
            tans2 = open(self.file3_entry.get())
            tans3 = open(self.file4_entry.get())
            removeFile=open("removeFile.txt")
            resultsFile=open("ResultFile.txt","a+")
            answer = open(fname)

            list1 = tans1.read().split()
            list2 = tans2.read().split()
            list3 = tans3.read().split()
            list4 = answer.read().split()
            rem   = removeFile.read().split()
            
            list1 = [word.lower() for word in list1]
            for i in list1:
                if i in string.punctuation or i in rem:
                    list1.remove(i)
            
            list2 = [word.lower() for word in list2]
            for i in list2:
                if i in string.punctuation or i in rem:
                    list2.remove(i)
            
            list3 = [word.lower() for word in list3]
            for i in list3:
                if i in string.punctuation or i in rem:
                    list3.remove(i)
            
            list4 = [word.lower() for word in list4]
            for i in list4:
                if i in string.punctuation or i in rem:
                    list4.remove(i)

            words1 = set(list1)
            words2 = set(list2)
            words3 = set(list3)
            words4 = set(list4)
            result=list()
            result.append(jaccard(words1, words4))
            result.append(jaccard(words2, words4))
            result.append(jaccard(words2, words4))
            marks=0
            for i in result:
                if i > marks:
                    marks=i
            r=str(fname[:len(fname)-4])+" "+str(int(marks*100))+"\n"
            resultsFile.write(r)
            return (marks*100)
        self.std_res = int(resultCalculation(self.file1_entry.get()))
        print(self.std_res)

        self.result_print = tk.Label(master, text="Score = " + str(self.std_res),  font = ('Comic Sans MS',11))
        self.result_print.place(relx= 0.4, rely=0.85)

MW = MainWindow(root)
root.mainloop()