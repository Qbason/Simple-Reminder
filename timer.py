from tkinter import *
from pygame import mixer
from time import sleep
from threading import Thread



class Timer():
    
    def __init__(self,play_all_the_time):
        
        #automatic playing var
        self.play_all_the_time =  play_all_the_time
        #roofoftimeview
        self.rootoftimeview = Tk()
        self.rootoftimeview.minsize(height=200,width=200)
        self.rootoftimeview.maxsize(height=200,width=200)
        self.rootoftimeview.resizable(False,False)
        self.rootoftimeview.title("Counting-down-alarm")
        
        self.rootoftimeview.columnconfigure(0,weight=1)
        self.rootoftimeview.rowconfigure(0,weight=1)
        self.rootoftimeview.rowconfigure(1,weight=1)
        self.rootoftimeview.rowconfigure(2,weight=1)
        self.rootoftimeview.rowconfigure(3,weight=1)
        
        #states button 
        self.button = ["START","STOP"]
        
        #for allocating counting down time
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
        
        #default value for e_set_time
        self.e_set_time.insert(0,str(20))
        
        
        #button pod wywolanie funkcji
        self.b_run = Button(self.rootoftimeview,text="START", command=self.start_timer,  font=("Times New Roman",16))
        self.b_run.grid(row=3,column=0, padx=15,sticky="nsew",pady=10)
        
            
        self.rootoftimeview.mainloop()
        
        
        
    def play_sound(self):
        mixer.init()
        mixer.music.load("sound.mp3")
        mixer.music.play()
        #while mixer.music.get_busy():
        self.rootoftimeview.update()
            #time.sleep(1)

    def change_name_button_to_reverse(self):
        """
        If the state was changed from START TO STOP 
        return True \n
        If the state was changed from STOP TO START
        return False
        """
        if self.b_run["text"]=="START":
            self.b_run["text"]="STOP"
            return True
        else:
            self.b_run["text"]="START"
            return False
            
    def start_timer(self):
        nowy_watek = Thread(target=self.counting_down)
        nowy_watek.start()
                
    def counting_down(self):
        
        #checking if we started timer or not
        state = self.change_name_button_to_reverse()
        
        if state:
            try:
                #transform minutes to seconds
                self.counting_down_time =  int(60 * float(self.e_set_time.get()))
            except:
                #based on length 
                self.counting_down_time = len(self.e_set_time.get())*60
            finally:
                #end until the counting ends
                while(self.counting_down_time!=0):
                                        
                    if self.b_run["text"] == "START":
                        return "INTERRUPT"
                    #dec time
                    self.counting_down_time=self.counting_down_time-1
                    #change view
                    self.l_time_counting["text"]=str(self.counting_down_time)
                    #take a nap
                    sleep(1)
                
                
                self.play_sound()
                self.change_name_button_to_reverse()
                
                #if we want to play all the time, execute next timer
                if self.play_all_the_time:
                    self.start_timer()
                #here the thread is going down
                return "END"
        else:
            return "STOPED"


if __name__ == "__main__":

    #define, if we want to play inifty times the alarm with specific time
    play_all_the_time = True

    WindowTime = Timer(play_all_the_time)
    




