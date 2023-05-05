import tkinter as tk
from tkinter import ttk

class LyricLog():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SONG LYRICS")
        self.root.resizable(tk.FALSE,tk.FALSE)
        self.mainFrame  = ttk.Frame(self.root, borderwidth=5, relief="sunken")
        self.lyricFrame = ttk.Frame(self.root, borderwidth=5, relief="sunken")

        self.mainFrame.grid( column=0,  row=0,  columnspan=6,  sticky=(tk.N, tk.W, tk.E, tk.S))
        self.lyricFrame.grid( column=0,  row=1,  columnspan=6,  rowspan=20,  sticky=(tk.N, tk.W, tk.E, tk.S))

        #Create lyrics Section
        self.lyricsText = tk.Text(self.lyricFrame, wrap=tk.WORD )
        self.lyricsText.grid( column=0, row=0)

        # Create Lyrics Scrollbar, bind it to the lyrics
        self.lyricsScrollbar = ttk.Scrollbar(self.lyricFrame)
        self.lyricsScrollbar.grid( column=1, row=0, sticky="NSEW")

        self.lyricsText['yscrollcommand'] = self.lyricsScrollbar.set


        # Button Stuff
        self.buttonGenerate = ttk.Button(self.lyricFrame, text="Generate Lyrics", command=self.generateLyrics)

        self.buttonGenerate.grid(column=0, row=2)

        self.generateDefault()

        self.root.mainloop()

    def postNewMessage(self,msg):
        self.lyricsText.delete("1.0",tk.END)
        self.lyricsText.insert(tk.END, msg)

    def generateDefault(self):
        lyrics =  "This lyrics search program will "
        lyrics += "generate lyrics for the most recent song "
        lyrics += "recorded in the song logger program OR "
        lyrics += "the song currently playing in RadioDJ if that is being used. "
        lyrics += "Please note that lyrics may not be 100 percent accurate "
        lyrics += "and some songs may fail to load lyrics."
        self.postNewMessage(lyrics)

    def generateLyrics(self):
        with open("lyrics.txt") as f:
                lyrics = f.readlines()
        lyrics = "".join(lyrics)
        self.postNewMessage(lyrics)
