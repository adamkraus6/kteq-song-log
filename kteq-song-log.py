from tkinter import *
from tkinter import ttk


def logSong(*args):
	pass

def logID():
	pass

def logPSA(*args):
	pass


#create the window and title it
root = Tk()
root.title("KTEQ 91.3FM SONG AND PSA LOG")

#create the info frame
infoFrame = ttk.Frame(root, borderwidth=5, relief="sunken", width=300, height=250)
infoFrame.grid(column=0, row=0, columnspan=6, rowspan=5, sticky=(N, W, E, S))

#create the song frame
songFrame = ttk.Frame(root, borderwidth=5, relief="sunken", width=300, height=250)
songFrame.grid(column=6, row=0, columnspan=6, rowspan=5, sticky=(N, W, E, S))

#create the PSA frame
psaFrame = ttk.Frame(root, borderwidth=5, relief="sunken", width=300, height=250)
psaFrame.grid(column=0, row=5, columnspan=6, rowspan=5, sticky=(N, W, E, S))

#create the ID frame
idFrame = ttk.Frame(root, borderwidth=5, relief="sunken", width=400, height=250)
idFrame.grid(column=6, row=5, columnspan=6, rowspan=5, sticky=(N, W, E, S))


#Create the variables
showName = StringVar()
showName.set("Select Show Name")

psaName = StringVar()
psaName.set("PSA 1")

songName = StringVar()
songArtist = StringVar()
songComposer = StringVar()


#Create text boxes
songName_entry = ttk.Entry(songFrame, width=7, textvariable=songName)
songArtist_entry = ttk.Entry(songFrame, width=7, textvariable=songArtist)
songComposer_entry = ttk.Entry(songFrame, width=7, textvariable=songComposer)


#Place Text Boxes
songComposer_entry.grid(column=3, row=3, columnspan=3, sticky=(W, E))
songArtist_entry.grid(column=3, row=2, columnspan=3, sticky=(W, E))
songName_entry.grid(column=3, row=1, columnspan=3, sticky=(W, E))


#Create drop downs
showNameList = OptionMenu(infoFrame, showName, "Select Show Name", "The Jambulance", "Bear Bacon")
psaNameList = OptionMenu(psaFrame, psaName, "PSA 1", "PSA 2", "PSA 3", "PSA 4")

#Place Drop Downs
showNameList.grid(column=3, row=1, columnspan=3, sticky=(W, E))
psaNameList.grid(column=3, row=1, columnspan=3, sticky=(W, E))


#Create buttons
logSong = ttk.Button(songFrame, text="Log Song", command=logSong)
logPSA = ttk.Button(psaFrame, text="Log PSA", command=logPSA)
logID = ttk.Button(idFrame, text="Log ID", command=logID)


#place buttons
logSong.grid(column=2, row=4, sticky=(W, E))
logPSA.grid(column=2, row=3, sticky=(W, E))
logID.grid(column=2, row=3, sticky=(N, W, E, S))


#Create labels
songName_lbl     = ttk.Label(songFrame, text="Song Name:")
songArtist_lbl   = ttk.Label(songFrame, text="Song Artist:")
songComposer_lbl = ttk.Label(songFrame, text="Song Composer:")
psa_lbl          = ttk.Label(psaFrame,  text="PSA Title:")

#Place labels
songName_lbl.grid(column=0, row=1, columnspan=3, sticky=W)
songArtist_lbl.grid(column=0, row=2, columnspan=3, sticky=W)
songComposer_lbl.grid(column=0, row=3, columnspan=3, sticky=W)
psa_lbl.grid(column=0, row=1, columnspan=3, sticky=W)

root.mainloop()
