#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import csv
import datetime

#imports
import shows
import psa

def logSong(*args):
	song     = songName.get()
	artist   = songArtist.get()
	composer = songComposer.get()
	show     = showName.get()
	now      = datetime.datetime.now()

	filename = 'bmi_' + str(now.month).zfill(2) + '_' + str(now.year) + '.csv'
	date = str(now.month).zfill(2) + '/' + str(now.day).zfill(2) + '/' + str(now.year)
	time = str(now.hour).zfill(2) + ':' + str(now.minute).zfill(2)

	with open(filename, 'a', newline='') as songlog:
		songwriter = csv.writer(songlog, delimiter=',')
		songwriter.writerow([date, time, song, artist, composer, show])

	songName_entry.delete(0, 'end')
	songArtist_entry.delete(0, 'end')
	songComposer_entry.delete(0, 'end')

def logID():
	show = showName.get()
	now = datetime.datetime.now()
	
	filename = 'bmi_' + str(now.month).zfill(2) + '_' + str(now.year) + '.csv'
	date = str(now.month).zfill(2) + '/' + str(now.day).zfill(2) + '/' + str(now.year)
	time = str(now.hour).zfill(2) + ':' + str(now.minute).zfill(2)

	with open(filename, 'a', newline='') as idlog:
		idwriter = csv.writer(idlog, delimiter=',')
		idwriter.writerow([date, time, 'STATION TAG', 'KTEQ', '', show])

def logPSA(*args):
	show = showName.get()
	psa  = psaName.get()
	now = datetime.datetime.now()
	
	filename  = 'bmi_' + str(now.month).zfill(2) + '_' + str(now.year) + '.csv'
	filename2 = 'psa_' + str(now.month).zfill(2) + '_' + str(now.year) + '.csv'
	date = str(now.month).zfill(2) + '/' + str(now.day).zfill(2) + '/' + str(now.year)
	time = str(now.hour).zfill(2) + ':' + str(now.minute).zfill(2)

	with open(filename, 'a', newline='') as psalog:
		psawriter = csv.writer(psalog, delimiter=',')
		psawriter.writerow([date, time, psa, 'PSA', '', show])

	with open(filename2, 'a', newline='') as psalog:
		psawriter = csv.writer(psalog, delimiter=',')
		psawriter.writerow([date, time, psa])


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


#CREATE NEW INSTANCE OF SHOWS AND PSAS
shows = shows.Shows()
psas = psa.PSA()

#Create the variables
showName = StringVar()
showName.set(shows.list[0])

psaName = StringVar()
psaName.set(psas.list[0])

songName = StringVar()
songArtist = StringVar()
songComposer = StringVar()


#Create text boxes
songName_entry     = ttk.Entry(songFrame, width=7, textvariable=songName)
songArtist_entry   = ttk.Entry(songFrame, width=7, textvariable=songArtist)
songComposer_entry = ttk.Entry(songFrame, width=7, textvariable=songComposer)


#Place Text Boxes
songComposer_entry.grid(column=3, row=3, columnspan=3, sticky=(W, E))
songArtist_entry.grid(column=3, row=2, columnspan=3, sticky=(W, E))
songName_entry.grid(column=3, row=1, columnspan=3, sticky=(W, E))


#Create drop downs
showNameList = OptionMenu(infoFrame, showName, *shows.list)
psaNameList = OptionMenu(psaFrame, psaName, *psas.list)

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
