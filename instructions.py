#!/usr/bin/python3

class Instructions(object):

	def __init__(self):
    	#If you need to change any of these, do it here I guess. I don't care.
		self.show = 'Please select your show from the drop down list at the start of your program. ' + \
			'Leave your show name selected until you are finished.' 

		self.id = 'At the top of every hour, click the Log ID button. Make sure you also state our ' + \
    		'station tag on air! (KTEQ FM Rapid City)' 

		self.song = 'Enter Song Name, Artist, and Composer (if applicable) for EVERY song you play. ' + \
      		'Try to update this in real time, as this will update the song info metadata for listeners ' + \
        	'on TuneIn, VLC, etc.'

		self.psa = 'Twice per hour, either read or play one of the following Public Service Announcements. ' + \
			'Log the PSA by selecting the correct one from the menu.'
