from tkinter import *
from pygame import mixer
from time import time,sleep




class Timer():
    
    def __init__(self):
        #roofoftimeview
        self.rootoftimeview = Tk()
        self.rootoftimeview.minsize(height=200,width=200)
        self.rootoftimeview.maxsize(height=200,width=200)
        self.rootoftimeview.resizable(False,False)
        self.rootoftimeview.title("Odliczator-dzwiekowy")
        
        self.rootoftimeview.columnconfigure(0,weight=1)
        self.rootoftimeview.rowconfigure(0,weight=1)
        self.rootoftimeview.rowconfigure(1,weight=1)
        self.rootoftimeview.rowconfigure(2,weight=1)
        self.rootoftimeview.rowconfigure(3,weight=1)
        
        self.button = ["START","STOP"]
        self.counting_down_time = 0
        
        #label pod wyswietlanie uplynietego czasu
        self.l_time_counting = Label(self.rootoftimeview, text="", font=("Times New Roman",16))
        self.l_time_counting.grid(row=0,column=0,columnspan=1,padx=15,sticky="nsew",pady=10)
        
        #label pod opisowke entry
        self.l_set_time = Label(self.rootoftimeview,text="Wpisz ilość minut: ", font=("Times New Roman",16))
        self.l_set_time.grid(row=1,column=0,columnspan=1,padx=15,sticky="nsew")
        
        #entry pod ustawienie czasu
        self.e_set_time = Entry(self.rootoftimeview,justify="center")
        self.e_set_time.grid(row=2,column=0,columnspan=1, padx=15,sticky="nsew",pady=10)
        #default value
        self.e_set_time.insert(0,str(20))
        
        
        #button pod wywolanie funkcji
        self.b_run = Button(self.rootoftimeview,text="START", command=self.start_timer,  font=("Times New Roman",16))
        self.b_run.grid(row=3,column=0, padx=15,sticky="nsew",pady=10)

        self.start_timer()
        self.rootoftimeview.mainloop()
        
        
    def play_sound(self):
        mixer.init()
        mixer.music.load("sound.mp3")
        mixer.music.play()
        #while mixer.music.get_busy():
        self.rootoftimeview.update()
            #time.sleep(1)

    def change_name_button(self):
        if self.b_run["text"]=="START":
            self.b_run["text"]="STOP"
            return True
        else:
            self.b_run["text"]="START"
            return False
            
    def start_timer(self):
        state = self.change_name_button()
        
        if state:
            try:
                self.counting_down_time =  int(60 * float(self.e_set_time.get()))
            except:
                self.counting_down_time = len(self.e_set_time.get())*60
            start_time = time()
            while(True):

                if time()-start_time>=1:
                    start_time = time()
                    self.counting_down_time=self.counting_down_time-1
                    self.l_time_counting["text"]=str(self.counting_down_time)
                
                if self.counting_down_time==0:
                    self.change_name_button()
                    break
                
                if self.b_run["text"] == "START":
                    return
                
                self.rootoftimeview.update()
                sleep(0.25)
            self.play_sound()
            return self.start_timer()

            
            



OkiekoTajmera = Timer()




