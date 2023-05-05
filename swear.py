import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import csv
import json

class SwearLog():
    def __init__(self, date="", time="", song="", artist="",composer="",show=""):
        self.root = tk.Tk()
        self.root.title("SWEAR LOG UH OH")
        self.root.resizable(tk.FALSE,tk.FALSE)
        self.mainFrame  = ttk.Frame(self.root, borderwidth=5, relief="sunken")
        self.swearFrame = ttk.Frame(self.root, borderwidth=5, relief="sunken")

        self.mainFrame.grid( column=0,  row=0,  columnspan=6,  sticky=(tk.N, tk.W, tk.E, tk.S))
        self.swearFrame.grid( column=0,  row=1,  columnspan=6,  rowspan=20,  sticky=(tk.N, tk.W, tk.E, tk.S))

        # Values read in when creating class
        default = []
        self.swearDate     = date
        self.swearTime     = time
        self.swearSong     = song
        self.swearArtist   = artist
        self.swearComposer = composer
        self.swearShow     = show
        self.swearReport   = ""

        default.append(self.swearDate    )
        default.append(self.swearTime    )
        default.append(self.swearSong    )
        default.append(self.swearArtist  )
        default.append(self.swearComposer)
        default.append(self.swearShow    )

        # StringVars
        self.varDate     = tk.StringVar()
        self.varTime     = tk.StringVar()
        self.varSong     = tk.StringVar()
        self.varArtist   = tk.StringVar()
        self.varComposer = tk.StringVar()
        self.varShow     = tk.StringVar()

        self.varSwear     = tk.StringVar()

        lList = []
        self.labelExplanation = ttk.Label(self.mainFrame, text="Log Swears for a song\n(This form assumes the song with swears was the most recently played track. Change if necessary.)")
        self.labelDate     = ttk.Label(self.mainFrame, text="Date: ")
        self.labelTime     = ttk.Label(self.mainFrame, text="Time: ")
        self.labelSong     = ttk.Label(self.mainFrame, text="Song Name : ")
        self.labelArtist   = ttk.Label(self.mainFrame, text="Song Artist: ")
        self.labelComposer = ttk.Label(self.mainFrame, text="Song Composer: ")
        self.labelShow     = ttk.Label(self.mainFrame, text="Radio Show: ")

        self.labelSwear = ttk.Label(self.swearFrame, text="Description of incident (What swear words were in the song, if the swears were said by a DJ, etc.)")

        lList.append(self.labelExplanation)
        lList.append(self.labelDate       )
        lList.append(self.labelTime       )
        lList.append(self.labelSong       )
        lList.append(self.labelArtist     )
        lList.append(self.labelComposer   )
        lList.append(self.labelShow       )

        # Button Stuff
        self.buttonSubmit = ttk.Button(self.swearFrame, text="Submit Swear Log", command=self.submit)

        # Text Entry stuff
        eList = []
        self.entryDate = ttk.Entry(self.mainFrame, width=7, textvariable=self.varDate)
        self.entryTime = ttk.Entry(self.mainFrame, width=7, textvariable=self.varTime)
        self.entrySong = ttk.Entry(self.mainFrame, width=7, textvariable=self.varSong)
        self.entryArtist = ttk.Entry(self.mainFrame, width=7, textvariable=self.varArtist)
        self.entryComposer = ttk.Entry(self.mainFrame, width=7, textvariable=self.varComposer)
        self.entryShow = ttk.Entry(self.mainFrame, width=7, textvariable=self.varShow)

        self.entrySwear = tk.Text(self.swearFrame, wrap=tk.WORD )

        eList.append(self.entryDate)
        eList.append(self.entryTime)
        eList.append(self.entrySong)
        eList.append(self.entryArtist)
        eList.append(self.entryComposer)
        eList.append(self.entryShow)

        # Set variable defaults
        self.varDate.set(self.swearDate)
        self.varTime.set(self.swearTime)
        self.varSong.set(self.swearSong)
        self.varArtist.set(self.swearArtist)
        self.varComposer.set(self.swearComposer)
        self.varShow.set(self.swearShow)

        rIndex = 1
        cIndex = 1
        for entry in eList:
            entry.grid(column=cIndex, row=rIndex, columnspan=6, sticky=(tk.W, tk.E))
            entry.delete(0,tk.END)
            entry.insert(0, default[rIndex-1])
            rIndex += 1
        rIndex = 0

        rIndex = 0
        cIndex = 0
        for label in lList:
            label.grid(column=cIndex, row=rIndex, columnspan=6, sticky=(tk.W, tk.E))
            rIndex += 1
        rIndex = 0

        #Pack entry stuff
        self.labelSwear.grid(  column=0, row=0)
        self.entrySwear.grid(  column=0, row=1)
        self.buttonSubmit.grid(column=0, row=2)

        self.root.mainloop()

    def submit(self):
        self.prepData()
        self.postCSV()

        # Inform user
        messagebox.showwarning(
            "SWEARS SUBMITTED",
            "Submitted Swear Log. :)"
        )

        # Close window
        self.root.destroy()

    def prepData(self):
        # Get all data ready to send
        self.swearDate     = self.cleanData(self.entryDate.get()    )
        self.swearTime     = self.cleanData(self.entryTime.get()    )
        self.swearSong     = self.cleanData(self.entrySong.get()    )
        self.swearArtist   = self.cleanData(self.entryArtist.get()  )
        self.swearComposer = self.cleanData(self.entryComposer.get())
        self.swearShow     = self.cleanData(self.entryShow.get()    )
        self.swearReport   = self.cleanData(self.entrySwear.get("1.0",tk.END) )

    def cleanData(self,entry):
        if not entry.strip():
            # Entry is empty, so set as "None"
            return "None"
        return entry

    def postCSV(self):
        dt = self.swearDate
        ti = self.swearTime
        so = self.swearSong
        ar = self.swearArtist
        co = self.swearComposer
        sh = self.swearShow
        re = self.swearReport

        post = [dt,ti,so,ar,co,sh,re]
        with open("swear_log.csv", 'a', newline='') as swearlog:
            swearwriter = csv.writer(swearlog, delimiter=',')
            swearwriter.writerow(post)
