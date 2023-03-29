import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master= None):
        tk.Frame.__init__(self,master)
        self.pack(expand=1, fill="both")
        self.createWidgets()

    def createWidgets(self):
        #frame of combobox
        frm_1 = tk.Frame(self)
        frm_1.pack(side="top",fill="x",padx=10)
        frm_1.columnconfigure(2, weight=1)
        #1st label of combobox
        lbl_1_1 = tk.Label(frm_1,text="Dictionary size:")
        lbl_1_1.grid(row=0,column=0,sticky="w",rowspan=2)
        #2nd label of combobox
        lbl_1_2 = tk.Label(frm_1, text="Number of CPU threads:")
        lbl_1_2.grid(row=2,column=0,sticky="w")
        #1st combobox
        cb_1_1 = ttk.Combobox(frm_1, values=["32 MB", "16 MB", "8 MB"], width=10)
        cb_1_1.grid(row=0, column=1, sticky="w", rowspan=2, padx=8)
        cb_1_1['state'] = 'readonly'
        cb_1_1.current(0)
        #2nd combobox
        cb_1_2 = ttk.Combobox(frm_1, values=["16", "12", "10"], width=10)
        cb_1_2.grid(row=2, column=1, sticky="w", padx=8)
        cb_1_2['state'] = 'readonly'
        cb_1_2.current(0)
        #the rest labels in frm_1
        lbl_1_3 = tk.Label(frm_1, text="Memory usage:")
        lbl_1_3.grid(row=0, column=2, sticky="w")
        lbl_1_4 = tk.Label(frm_1, text="3530 MB / 65487 MB")
        lbl_1_4.grid(row=1, column=2, sticky="w")
        lbl_1_5 = tk.Label(frm_1, text="/ 16")
        lbl_1_5.grid(row=2, column=2, sticky="w")
        #created buttons in frm_1
        btn_1_1 = tk.Button(frm_1, text="Restart", width=12)
        btn_1_1.grid(row=0, column=3, sticky="w", rowspan=2)
        btn_1_2 = tk.Button(frm_1, text="Stop", width=12, state=tk.DISABLED)
        btn_1_2.grid(row=2, column=3, sticky="w")

        #compressing table
        frm_2 = tk.Frame(self)
        frm_2.columnconfigure(0, weight=1)
        frm_2.pack(side="top", fill="x", expand=0, pady=8,padx=10)
        # 1st row - labels
        lbl_2_1 = tk.Label(frm_2, text="Speed", width=12)
        lbl_2_1.grid(row=0, column=1, sticky="e")
        lbl_2_2 = tk.Label(frm_2, text="CPU Usage", width=12)
        lbl_2_2.grid(row=0, column=2, sticky="e")
        lbl_2_3 = tk.Label(frm_2, text="Rating / Usage", width=12)
        lbl_2_3.grid(row=0, column=3, sticky="e")
        lbl_2_4 = tk.Label(frm_2, text="Rating", width=12)
        lbl_2_4.grid(row=0, column=4, sticky="e")
        # 2nd row - auxiliary inner (labeled) frame
        frm_21 = tk.LabelFrame(frm_2, text="Compressing")
        frm_21.columnconfigure(0, weight=1)
        frm_21.grid(row=1, column=0, sticky="w"+"e", columnspan=5)
        # 1st column - labels in auxiliary frame
        lbl_21_1 = tk.Label(frm_21, text="Current")
        lbl_21_1.grid(row=0, column=0, sticky="w")
        lbl_21_2 = tk.Label(frm_21, text="Resulting")
        lbl_21_2.grid(row=1, column=0, sticky="w")
        # 2nd column - numbers in auxiliary frame
        lbl_21_3 = tk.Label(frm_21, text=" 61125  KB/s", width=12)
        lbl_21_3.grid(row=0, column=1, sticky="e")
        lbl_21_4 = tk.Label(frm_21, text=" 61125  KB/s", width=12)
        lbl_21_4.grid(row=1, column=1, sticky="e")    
        lbl_21_5 = tk.Label(frm_21, text="1506%", width=12)
        lbl_21_5.grid(row=0, column=2, sticky="e")
        lbl_21_6 = tk.Label(frm_21, text="1505%", width=12)
        lbl_21_6.grid(row=1, column=2, sticky="e")
        lbl_21_7 = tk.Label(frm_21, text="4634 MIPS", width=12)
        lbl_21_7.grid(row=0, column=3, sticky="e")
        lbl_21_8 = tk.Label(frm_21, text="4637 MIPS", width=12)
        lbl_21_8.grid(row=1, column=3, sticky="e")
        lbl_21_9 = tk.Label(frm_21, text="69790 MIPS", width=12)
        lbl_21_9.grid(row=0, column=4, sticky="e")
        lbl_21_10 = tk.Label(frm_21, text="69790 MIPS", width=12)
        lbl_21_10.grid(row=1, column=4, sticky="e")
        
        #Decompressing table
        frm_3 = tk.Frame(self)
        frm_3.columnconfigure(0, weight=1)
        frm_3.pack(side="top", fill="x", expand=0, pady=5,padx=10)
        # 2nd row - auxiliary inner (labeled) frame
        frm_31 = tk.LabelFrame(frm_3, text="Decompressing")
        frm_31.columnconfigure(0, weight=1)
        frm_31.grid(row=1, column=0, sticky="w"+"e", columnspan=5)
        # 1st column - labels in auxiliary frame
        lbl_31_1 = tk.Label(frm_31, text="Current")
        lbl_31_1.grid(row=0, column=0, sticky="w")
        lbl_31_2 = tk.Label(frm_31, text="Resulting")
        lbl_31_2.grid(row=1, column=0, sticky="w")
        # 2nd column - numbers in auxiliary frame
        lbl_31_3 = tk.Label(frm_31, text="1017245 KB/s", width=12)
        lbl_31_3.grid(row=0, column=1, sticky="e")
        lbl_31_4 = tk.Label(frm_31, text="1031236 KB/s", width=12)
        lbl_31_4.grid(row=1, column=1, sticky="e")    
        lbl_31_5 = tk.Label(frm_31, text="1585%", width=12)
        lbl_31_5.grid(row=0, column=2, sticky="e")
        lbl_31_6 = tk.Label(frm_31, text="1575%", width=12)
        lbl_31_6.grid(row=1, column=2, sticky="e")
        lbl_31_7 = tk.Label(frm_31, text="5709 MIPS", width=12)
        lbl_31_7.grid(row=0, column=3, sticky="e")
        lbl_31_8 = tk.Label(frm_31, text="5823 MIPS", width=12)
        lbl_31_8.grid(row=1, column=3, sticky="e")
        lbl_31_9 = tk.Label(frm_31, text="90509 MIPS", width=12)
        lbl_31_9.grid(row=0, column=4, sticky="e")
        lbl_31_10 = tk.Label(frm_31, text="91749 MIPS", width=12)
        lbl_31_10.grid(row=1, column=4, sticky="e")
        
        #Frame for data(Elapsed/size/passes) and total Rating table
        frm_4 = tk.Frame(self)
        frm_4.columnconfigure(0, weight=1)
        frm_4.pack(side="top", fill="x", expand=0, pady=5,padx=10)

        #Frame data(Elapsed/size/passes) (left frame)
        frm_41 = tk.Frame(frm_4)
        frm_41.pack(side="left",padx=(0,90))
        #1st row
        lbl_41_1 = tk.Label(frm_41,text="Elapsed time:")
        lbl_41_1.grid(row=0, column=0,sticky="w")
        lbl_41_AP1 = tk.Label(frm_41, width=5)
        lbl_41_AP1.grid(row=0,column=0,sticky="E",pady=5)
        lbl_41_2 = tk.Label(frm_41,text="00:00:41")
        lbl_41_2.grid(row=0,column=4,sticky="E")
        #2nd row
        lbl_41_3 = tk.Label(frm_41, text="Size:")
        lbl_41_3.grid(row=1, column=0,sticky="w")
        lbl_41_AP2 = tk.Label(frm_41, width=5)
        lbl_41_AP2.grid(row=0,column=0,sticky="E",pady=5)
        lbl_41_4 = tk.Label(frm_41,text="256 MB")
        lbl_41_4.grid(row=1,column=4,sticky="E")
        #3rd row
        lbl_41_5 = tk.Label(frm_41, text="Passes")
        lbl_41_5.grid(row=2, column=0,sticky="w")
        lbl_41_AP3 = tk.Label(frm_41, width=5)
        lbl_41_AP3.grid(row=0,column=0,sticky="E",pady=5)
        lbl_41_6 = tk.Label(frm_41,text="5")
        lbl_41_6.grid(row=2,column=4,sticky="E")
        
        #total rating table (right frame)
        frm_42 = tk.LabelFrame(frm_4, text="Total Rating")
        frm_42.pack(side="right")
        lbl_42_AP = tk.Label(frm_42, width=5)
        lbl_42_AP.grid(row=0,column=0,sticky="E",pady=10)
        lbl_42_1 = tk.Label(frm_42,text="1540%", width=12)
        lbl_42_1.grid(row=0,column=1,sticky="E",pady=10)
        lbl_42_2 = tk.Label(frm_42,text="5230 MIPS",width=12)
        lbl_42_2.grid(row=0,column=2,sticky="E",pady=10)
        lbl_42_3 = tk.Label(frm_42,text="80770 MIPS",width=12)
        lbl_42_3.grid(row=0,column=3,sticky="E",pady=10)
        
        #AMD Ryzen lable Frame
        frm_5 = tk.Frame(self)
        frm_5.pack(side="top",anchor="e",padx=10)
        #1st row
        lbl_51 = tk.Label(frm_5, text="AMD Ryzen 7 3700X 8-Core Processor")
        lbl_51.grid(row=0,column=0)
        lbl_52 = tk.Label(frm_5, text="")
        lbl_52.grid(row=0,column=1)
        lbl_53 = tk.Label(frm_5, text="(870F10)")
        lbl_53.grid(row=0,column=2,sticky="E")
        #2nd row
        lbl_54 = tk.Label(frm_5,text="7-Zip 19.00 (x64)")
        lbl_54.grid(row=1,column=2,sticky="E")
        
        #frame for buttons(Help/Cancel) and last lablel
        frm_6 = tk.Frame(self)
        frm_6.pack(side="top", fill="x",expand=0,padx=10,pady=12)
        
        #Frame buttons (tight frame)
        frm_61 = tk.Frame(frm_6)
        frm_61.pack(side="right")
        #button help
        btn_61_1 = tk.Button(frm_61, text="H̲elp",width=12, 
                             bg="gray90", highlightbackground="gray", highlightthickness=2, relief=tk.RIDGE)
        btn_61_1.grid(row=0,column=0,padx=10)
        #button cancel
        btn_61_1 = tk.Button(frm_61, text="Cancel",width=12, 
                             bg="gray90", highlightbackground="gray", highlightthickness=2, relief=tk.RIDGE)
        btn_61_1.grid(row=0,column=1)
        
        #last label's Frame (left frame)
        frm_62 = tk.Frame(frm_6)
        frm_62.pack(side="left",anchor="n")
        lbl_62 = tk.Label(frm_62,text="x64 17.7100 cups: 16 128T")
        lbl_62.grid(row=0,column=0,sticky=("w"+"n"))
        
def main():
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("Benchmark")
    root.mainloop()
        
if __name__ == "__main__":
    main()