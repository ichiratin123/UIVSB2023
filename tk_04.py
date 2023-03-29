import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master= None):
        tk.Frame.__init__(self,master)
        self.pack(expand=1, fill="both")
        self.createWidgets()

    def createWidgets(self):
        # create Frame--------------------------------------------------
        frm_left = tk.Frame(self)
        frm_right = tk.Frame(self)
        
        frm_left.pack(side="left",fill="y")
        frm_right.pack(side="right",fill="both", expand=1)
        # --------------------------------------------------------------
        
        # create ListBox------------------------------------------------
        lb = tk.Listbox(frm_left, activestyle=None,
                        height=15,width=26,
                        highlightbackground="black", highlightthickness=1)
        lb.insert(1,"Start / Exit options")
        lb.insert(2,"JPG / PCD / GIF")
        lb.insert(3,"Extentions")
        lb.insert(4,"Viewing")
        lb.insert(5,"Zoom / Color management")
        lb.insert(6,"Browsing / Editing")
        lb.insert(7,"Full Screen/ Slideshow")
        lb.insert(8,"Video / Sound")
        lb.insert(9,"File Handling")
        lb.insert(10,"Language")
        lb.insert(11,"Toolbar")
        lb.insert(12,"PlugIns")
        lb.insert(13,"Miscellaneous")
        lb.pack(side=tk.TOP,padx = 5)
        
        lb.select_set(6)
        
        # create buttons------------------------------------------------
        frm_btn = tk.LabelFrame(frm_left)
        frm_btn.pack(side="top",fill="both",pady= 10,padx = 5)
        buttonborder =tk.Frame(frm_btn,
                             highlightbackground="#0078D7",
                             highlightcolor="#0078D7",
                             highlightthickness=2,
                             bd=0)
        buttonborder.pack(pady = 10)
        btn_ok = tk.Button(buttonborder, text="OK",width=10, bg="gray90", relief=tk.RIDGE)
        btn_ok.pack(side="top")
        btn_cancel = tk.Button(frm_btn,text="Cancel",width=10, 
                               bg="gray90", highlightbackground="gray", highlightthickness=2, relief=tk.RIDGE)
        btn_cancel.pack(pady = 10,side="top")
        # --------------------------------------------------------------
        
        # create browsing/editing---------------------------------------
        frm_1 = tk.LabelFrame(frm_right)
        lbl_BE = tk.Label(frm_1, text="Browsing/Editing")
        lbl_BE.pack(pady = 3)
        frm_1.pack(side="top", fill= "x", padx=5)
        # --------------------------------------------------------------
        
        # create browsing-----------------------------------------------
        frm_2 = tk.LabelFrame(frm_right,text="Browsing:")
        self.chVarT1 = tk.BooleanVar()
        self.chVarT1.set("True")
        # # checkbox 1--------------------------------------------------
        chb_21 = tk.Checkbutton(frm_2, variable=self.chVarT1,
                               text="View other files in folder (moving/browsing through folder; thumbnails window)")
        chb_21.grid(row=0, column=0, columnspan=3, sticky=tk.W)
        # # checkbox 2--------------------------------------------------
        self.chVarT2 = tk.BooleanVar()
        self.chVarT2.set("True")
        chb_22 = tk.Checkbutton(frm_2, variable=self.chVarT2, 
                               text="Show hidden files/folders while moving/browsing through folder")
        chb_22.grid(row=1, column=0, columnspan=3, sticky=tk.W)
        # # label in brwosing-------------------------------------------
        lbl = tk.Label(frm_2, 
                       text="If the end/begin of the folder is reached (during browsing):")
        lbl.grid(row=2, column=0,columnspan=3, sticky=tk.W)
        # # radiobuttons------------------------------------------------
        self.s = tk.IntVar()
        self.s.set(1)
        rdo_21 = tk.Radiobutton(frm_2,
                               text="Show Browse dialog", 
                               variable=self.s,value=1)
        rdo_21.grid(row=3, column=0, sticky=tk.W,columnspan=3,padx= 10)
        rdo_22 = tk.Radiobutton(frm_2,
                               text="Loop current folder", 
                               variable=self.s, value=2)
        rdo_22.grid(row=3, column=1, sticky=tk.W,columnspan=3,padx=10)
        rdo_23 = tk.Radiobutton(frm_2,
                               text="Do nothing (stop)", 
                               variable=self.s, value=3)
        rdo_23.grid(row=3, column=2, sticky=tk.W,columnspan=3,padx=10)
        # # checkbox 3--------------------------------------------------
        self.chVarT3 = tk.BooleanVar()
        self.chVarT3.set("True")
        chb_23 = tk.Checkbutton(frm_2, variable=self.chVarT3, 
                               text="Beep on folder loop, stop or screenshot save")
        chb_23.grid(row=4, column=0, columnspan=3, sticky=tk.W)
        # # checkbox 4--------------------------------------------------
        chb_24 = tk.Checkbutton(frm_2, 
                               text="Jump to next image if Page keys or Mouse wheel used (if vertical scrollbar visible)")
        chb_24.grid(row=5, column=0, columnspan=3, sticky=tk.W)
        # # checkbox 5--------------------------------------------------
        self.chVarT4 = tk.BooleanVar()
        self.chVarT4.set("True")
        chb_25 = tk.Checkbutton(frm_2, variable=self.chVarT4, 
                               text="Multipage images: Change pages using Page Up/Down keys")
        chb_25.grid(row=6, column=0, columnspan=3, sticky=tk.W)
        
        frm_2.pack(side="top",fill="both",expand=1,padx=5)
        # --------------------------------------------------------------
        
        # create editing------------------------------------------------
        frm_3 = tk.LabelFrame(frm_right,text="Editing:")
        lbl_31 = tk.Label(frm_3, text="Set the number of Undo/Redo steps:")
        lbl_31.grid(row=0, column=0, sticky=tk.W)
        
        
        frmAP = tk.Label(frm_3, width=1) # auxiliary padding 
        frmAP.grid(row=0, column=1)
        
        frm_31 = tk.Frame(frm_3)
        frm_31.grid(row=0, column=2, sticky=tk.W)
        entVar = tk.StringVar()
        entVar.set("5")
        ent1 = tk.Entry(frm_31,width=5,textvariable=entVar)
        ent1.pack(side="left")
        
        lbl_32 = tk.Label(frm_31, text="(0 - 20; 0 = disable Undo/Redo)")
        lbl_32.pack(side="left")
        
        frm_32 = tk.Frame(frm_3)
        frm_32.grid(row=1, column=0, sticky=tk.W)
        
        chb_31 = tk.Checkbutton(frm_32, text="Select selection/grid color")
        chb_31.pack(side="left")
        
        lblColor_31 = tk.Label(frm_32, width=8, bg="gray", relief=tk.SUNKEN)
        lblColor_31.pack(side="left")
        
        frm_322 = tk.Frame(frm_3)
        frm_322.grid(row=1, column=2,sticky=tk.W)
        btn_31 = tk.Button(frm_322,text="Choose", width=10, bg="gray90", highlightbackground="gray", highlightthickness=2, relief=tk.RIDGE)
        btn_31.pack(side="left")
        
        lbl_33 = tk.Label(frm_322, text="(selection color is inverted)")
        lbl_33.pack(side="left",padx=5)
        
        self.chVarT5 = tk.BooleanVar()
        self.chVarT5.set("True")
        chb_32 = tk.Checkbutton(frm_3, variable=self.chVarT5, 
                                text="Import palette: Use nearest color")
        chb_32.grid(row=2, column=0, columnspan=3, sticky=tk.W)
        
        chb_33 = tk.Checkbutton(frm_3, 
                                text="Paste into selection: Fit to selection (default: stretch to selection)")
        chb_33.grid(row=3, column=0, columnspan=3, sticky=tk.W)
        
        self.chVarT6 = tk.BooleanVar()
        self.chVarT6.set("True")
        chb_34 = tk.Checkbutton(frm_3, variable=self.chVarT6, 
                                text="Paste Special: Fit clipboard image to displayed image")
        chb_34.grid(row=4, column=0, columnspan=3, sticky=tk.W)
        
        lbl_34 = tk.Label(frm_3, text="Selection border size:")
        lbl_34.grid(row=5, column=0, sticky=tk.W)
        
        frmAP2 = tk.Label(frm_3, width=1) # auxiliary padding 
        frmAP2.grid(row=5, column=1)
        
        frm_33 = tk.Frame(frm_3)
        frm_33.grid(row=5, column=2, sticky=tk.W, pady=5)
        entVar = tk.StringVar()
        entVar.set("1")
        ent2 = tk.Entry(frm_33,width=5,textvariable=entVar)
        ent2.pack(side="left")
        
        lbl_35 = tk.Label(frm_33, text="(1-10 pixels)")
        lbl_35.pack(side="left", padx=5)
        
        lbl_36 = tk.Label(frm_3, text="Set grid cell size (edit menu)")
        lbl_36.grid(row=6, column=0, sticky=tk.W)
        
        frmAP3 = tk.Label(frm_3, width=1) # auxiliary padding 
        frmAP3.grid(row=6, column=1)
        
        frm_34 = tk.Frame(frm_3)
        frm_34.grid(row=6, column=2, sticky=tk.W, pady=5)
        entVar = tk.StringVar()
        entVar.set("64")
        ent3 = tk.Entry(frm_34,width=5,textvariable=entVar)
        ent3.pack(side="left")
        
        lbl_37 = tk.Label(frm_34, text="pixels")
        lbl_37.pack(side="left", padx=5)
        
        lbl_38 = tk.Label(frm_3, text="Tolerance value for 'Auto crop borders':")
        lbl_38.grid(row=7, column=0, sticky=tk.W)
        
        frmAP4 = tk.Label(frm_3, width=1) # auxiliary padding 
        frmAP4.grid(row=7, column=1)
        
        frm_35 = tk.Frame(frm_3)
        frm_35.grid(row=7, column=2, sticky=tk.W,pady=5)
        entVar = tk.StringVar()
        entVar.set("0")
        ent4 = tk.Entry(frm_35,width=5,textvariable=entVar)
        ent4.pack(side="left")
        
        lbl_38 = tk.Label(frm_35, text="(0 - 128)")
        lbl_38.pack(side="left", padx=5)
        
        frm_3.pack(side="top",fill="both",expand=1,padx=5)
        # --------------------------------------------------------------
        
        # create cut----------------------------------------------------
        frm_4 = tk.LabelFrame(frm_right,text="Cut:")
        lbl_BG = tk.Label(frm_4, text="Background color for")
        lbl_BG.grid(row=0, column=0, sticky=tk.W)
        
        frmAP5 = tk.Label(frm_4, width=5) # auxiliary padding 
        frmAP5.grid(row=0, column=1)
        
        frm_41 = tk.Frame(frm_4)
        frm_41.grid(row=0, column=2, sticky=tk.W)
        
        lbl_42 = tk.Label(frm_41, width=8, bg="black", relief=tk.SUNKEN)
        lbl_42.pack(side="left", padx=5)
        
        frm_412 = tk.Frame(frm_4)
        frm_412.grid(row=0, column=3,sticky=tk.W)
        btn_41 = tk.Button(frm_412,text="Choose", width=10, bg="gray90", highlightbackground="gray", highlightthickness=2, relief=tk.RIDGE)
        btn_41.pack(side="left", pady=5)
        
        lbl_43 = tk.Label(frm_412, text="(or click in the loaded image)")
        lbl_43.pack(side="left",padx=5)
        
        frm_4.pack(side="top",fill="both",expand=1,padx=5)
        # -------------------------------------------------------------
        
        # create Option------------------------------------------------
        frm_5 = tk.LabelFrame(frm_right,text="Options for TXT -files/Text-paste")
        
        frm_51 = tk.Frame(frm_5)
        frm_51.pack(side="left",anchor="nw")
        self.s1 = tk.IntVar()
        rdo_51 = tk.Radiobutton(frm_51,
                               text="Custom font (True Type):", 
                               variable=self.s1,value=1)
        rdo_51.grid(row=0, column=0, sticky=tk.W)
        rdo_52 = tk.Radiobutton(frm_51,
                               text="ANSI font", 
                               variable=self.s1,value=0)
        rdo_52.grid(row=1, column=0, sticky=tk.W)
        rdo_53 = tk.Radiobutton(frm_51,
                               text="ASCII font", 
                               variable=self.s1, value=3)
        rdo_53.grid(row=2, column=0, sticky=tk.W)
        rdo_54 = tk.Radiobutton(frm_51,
                               text="ANSI thin  font", 
                               variable=self.s1, value=4)
        rdo_54.grid(row=3, column=0, sticky=tk.W)
        
        frm_52 = tk.Frame(frm_5)
        frm_52.pack(side="left", anchor="nw")
        
        frm_521 = tk.Frame(frm_52)
        frm_521.grid(row=0,column=0)
        lbl_51 = tk.Label(frm_521,relief=tk.SUNKEN,width=34, text="Courier New, size: 10")
        lbl_51.grid(row=0,column=0)
        btn_51 = tk.Button(frm_521, text="Choose", width=10, bg="gray90", highlightbackground="gray", highlightthickness=2, relief=tk.RIDGE)
        btn_51.grid(row=0, column=1, padx=5)
        
        frm_522 = tk.Frame(frm_52)
        frm_522.grid(row=1, column=0,sticky="w",pady=(8,0))
        lbl_52 = tk.Label(frm_522,text="Font color:")
        lbl_52.grid(row=0,column=0)
        
        frmAP6 = tk.Label(frm_522, width=15) # auxiliary padding 
        frmAP6.grid(row=0, column=1)
        lbl_53 = tk.Label(frm_522,text="Background color:")
        lbl_53.grid(row=0,column=2)
        
        frm_523 = tk.Frame(frm_52)
        frm_523.grid(row=3, column=0,sticky="w")
        lbl_54 = tk.Label(frm_523, width=8, bg="#00FF00", relief=tk.SUNKEN)
        lbl_54.pack(side="left", padx=5)
        btn_52 = tk.Button(frm_523,text="Choose", width=10, bg="gray90", highlightbackground="gray", highlightthickness=2, relief=tk.RIDGE)
        btn_52.pack(side="left", pady=5)
        
        frmAP7 = tk.Label(frm_523, width=2) # auxiliary padding 
        frmAP7.pack(side="left")
        
        lbl_54 = tk.Label(frm_523, width=8, bg="white", relief=tk.SUNKEN)
        lbl_54.pack(side="left", padx=5)
        btn_52 = tk.Button(frm_523,text="Choose", width=10, bg="gray90", highlightbackground="gray", highlightthickness=2, relief=tk.RIDGE)
        btn_52.pack(side="left", pady=5)
        
        frm_5.pack(side="top",fill="both",expand=1,padx=5,pady=(0,5))

        # --------------------------------------------------------------

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("Propertires/Setting")
    root.mainloop()
        
if __name__ == "__main__":
    main()