#!/usr/bin/python3

import json

import tkinter as tk
from tkinter import ttk

from collections import OrderedDict

MONDAY    = 0
TUESDAY   = 1
WEDNESDAY = 2
THURSDAY  = 3
FRIDAY    = 4
SATURDAY  = 5
SUNDAY    = 6

class ShowFrame(object):
    def __init__(self,rt,row):
        self.root = rt

        self.frame = ttk.Frame(self.root, borderwidth=5, relief="sunken")
        self.frame.grid( column=0,  row=row, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.descriptionFrame = ttk.Frame(self.root, borderwidth=5, relief="sunken")
        self.descriptionFrame.grid( column=0,  row=row+10, sticky=(tk.N, tk.E, tk.S))

        # Create Labels
        self.labelDate         = ttk.Label(self.frame, text="Show Date")
        self.labelStart        = ttk.Label(self.frame, text="Show Start Time (Military Time)")
        self.labelEnd          = ttk.Label(self.frame, text="Show End   Time (Military Time)")
        self.labelShowLength   = ttk.Label(self.frame, text="Show Length (In Hours)")
        self.labelShowName     = ttk.Label(self.frame, text="Show Name")
        self.labelShowShort    = ttk.Label(self.frame, text="Short Description")

        self.labelDescription    = ttk.Label(self.descriptionFrame, text="Show Description")

        # Create a Tkinter variable
        self.varDate = tk.StringVar(self.root)

        # Create A Button
        # Button Stuff
        self.buttonSubmit = ttk.Button(self.frame, text="Add New Show", command=self.newShow)

        # Dictionary with options
        choices = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday', 'Sunday']
        self.varDate.set('Monday') # set the default option

        self.menuDate = ttk.OptionMenu(self.frame, self.varDate, *choices)

        # Create Entry Fields
        #self.entryDate = ttk.Entry(self.frame, width=50, textvariable=None)
        self.entryStart = ttk.Entry(self.frame, textvariable=None)
        self.entryEnd = ttk.Entry(self.frame,  textvariable=None)
        self.entryShowLength = ttk.Entry(self.frame, textvariable=None)
        self.entryShowName = ttk.Entry(self.frame, textvariable=None)
        self.entryShowShort = ttk.Entry(self.frame, textvariable=None)

        # Create DJ Label Fields
        self.labelDJname  = [None,None,None,None]
        self.labelDJemail = [None,None,None,None]
        self.labelDJtype  = [None,None,None,None]
        for i in range(len(self.labelDJname)):
            strInfo = "DJ #" + str(i+1) + " "
            self.labelDJname[i]  = ttk.Label(self.frame, text=strInfo+"Name")
            self.labelDJemail[i] = ttk.Label(self.frame, text=strInfo+"Email")
            self.labelDJtype[i]  = ttk.Label(self.frame, text=strInfo+"Type")

        # Create DJ Entry Fields
        self.entryDJname = [None,None,None,None]
        self.entryDJemail = [None,None,None,None]
        self.entryDJtype = [None,None,None,None]
        for i in range(len(self.entryDJname)):
            self.entryDJname[i] = ttk.Entry(self.frame, textvariable=None)
            self.entryDJemail[i] = ttk.Entry(self.frame, textvariable=None)
            self.entryDJtype[i] = ttk.Entry(self.frame, textvariable=None)

        #Create Description Section
        self.textDescription = tk.Text(self.descriptionFrame, wrap=tk.WORD)

        #Pack Labels
        self.labelDate.grid(        column=0, row=1, sticky=(tk.N, tk.W, tk.S))
        self.labelStart.grid(       column=0, row=2, sticky=(tk.N, tk.W, tk.S))
        self.labelEnd.grid(         column=0, row=3, sticky=(tk.N, tk.W, tk.S))
        self.labelShowLength.grid(  column=0, row=4, sticky=(tk.N, tk.W, tk.S))
        self.labelShowName.grid(    column=0, row=5, sticky=(tk.N, tk.W, tk.S))
        self.labelShowShort.grid(   column=0, row=6, sticky=(tk.N, tk.W, tk.S))

        self.labelDescription.grid(column=0, row=0, sticky=(tk.N, tk.W))

        #Pack Entry Fields
        self.menuDate.grid(         column=1, row=1, sticky=(tk.N, tk.E, tk.S))
        self.entryStart.grid(       column=1, row=2, sticky=(tk.N, tk.E, tk.S))
        self.entryEnd.grid(         column=1, row=3, sticky=(tk.N, tk.E, tk.S))
        self.entryShowLength.grid(  column=1, row=4, sticky=(tk.N, tk.E, tk.S))
        self.entryShowName.grid(    column=1, row=5, sticky=(tk.N, tk.E, tk.S))
        self.entryShowShort.grid(   column=1, row=6, sticky=(tk.N, tk.E, tk.S))

        self.buttonSubmit.grid(   column=1, row=7, sticky=(tk.N, tk.E, tk.S))

        # Pack Description
        self.textDescription.grid( column=1, row=0, sticky=(tk.N, tk.E,tk.S,tk.W))

        j = 1
        # Pack DJ Info
        for i in range(len(self.entryDJname)):
            self.labelDJname[i].grid(  column=2, row=j+0, sticky=(tk.N, tk.W, tk.S))
            self.entryDJname[i].grid(  column=3, row=j+0, sticky=(tk.N, tk.E, tk.S))
            self.labelDJemail[i].grid( column=2, row=j+1, sticky=(tk.N, tk.W, tk.S))
            self.entryDJemail[i].grid( column=3, row=j+1, sticky=(tk.N, tk.E, tk.S))
            self.labelDJtype[i].grid(  column=2, row=j+2, sticky=(tk.N, tk.W, tk.S))
            self.entryDJtype[i].grid(  column=3, row=j+2, sticky=(tk.N, tk.E, tk.S))
            j +=3

    def loadJSON(self):
        with open('shows.json') as data_file:
            return json.load(data_file)

    def sortJSON(self):
        # Dumb script just to reorganize stuff
        id = 0
        x = self.loadJSON()
        newJSON = OrderedDict()
        newJSON['shows'] = []
        for show in x['shows']:
            newEntry = OrderedDict()
            newEntry['id']          = "{:0>6}".format(id)
            newEntry['show name']   = show['show name']
            newEntry['status']      = show['status']
            newEntry['show date']   = show['show date']
            newEntry['start']       = show['start']
            newEntry['end']         = show['end']
            newEntry['length']      = show['length']
            newEntry['short']       = show['short']
            newEntry['description'] = show['description']

            djList = []
            for dj in show['djs']:
                newDJ = OrderedDict()
                newDJ['dj name']  = dj['dj name']
                newDJ['dj email'] = dj['dj email']
                newDJ['dj type']  = dj['dj type']
                djList.append(newDJ)
            newEntry['djs'] = djList

            # add to json
            newJSON['shows'].append(newEntry)
            id+=1
        with open('shows.json', 'w') as outfile:
            json.dump(newJSON, outfile,sort_keys=False,indent=4, separators=(',', ': '))


    def newShow(self):
        # Get entries
        j = self.loadJSON()

        total = len(j['shows'])
        id = "{:0>6}".format(total + 1)
        print(id)

        show = OrderedDict()
        show['id'] = id
        show['show name']   = self.entryShowName.get()
        show['status']      = "Active"
        show['show date']   = self.varDate.get()
        show['start']       = self.entryStart.get()
        show['end']         = self.entryEnd.get()
        show['length']      = self.entryShowLength.get()
        show['short']       = self.entryShowShort.get()
        show['description'] = self.textDescription.get("1.0","end-1c")

        djs = []
        for i in range(4):
            check = self.entryDJname[i].get().replace(" ","")
            if len(check) > 0:
                dj = {}
                dj['dj name']  = self.entryDJname[i].get()
                dj['dj email'] = self.entryDJemail[i].get()
                dj['dj type']  = self.entryDJtype[i].get()
                djs.append(dj)
        show['djs'] = djs

        #print(show)
        # add the new show
        j['shows'].append(show)
        with open('shows.json', 'w') as outfile:
            json.dump(j, outfile,sort_keys=False,indent=4, separators=(',', ': '))

        self.sortJSON()
        # Close window
        self.root.destroy()

class ShowNew(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Show Log - New Show")
        self.root.resizable(tk.FALSE,tk.FALSE)
        self.mainFrame  = ttk.Frame(self.root, borderwidth=5, relief="sunken")

        self.mainFrame.grid( column=0,  row=0,  columnspan=6,  sticky=(tk.N, tk.W, tk.E, tk.S))
        self.sf = ShowFrame(self.root,1)
        self.root.mainloop()

if __name__ == '__main__':
    s = ShowNew()
