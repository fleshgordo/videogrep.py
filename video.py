"""

Will generate an EDL list based on a searchword. This EDL list can later be used with mplayer

Usage: python video.py SEARCHWORD PATH_TO_VIDEOFILE

Example:
python video.py SEARCHWORD PATH_TO_VIDEOFILE > shortcut.edl
mplayer -edl shortcut.edl PATH_TO_VIDEOFILE

(it only properly works if srt file is in the same path and has exactly the same filename with srt ending!

"""

import re,sys,os
import time,fileinput

def timecode2seconds (timecode) :
	time_sep = timecode.split(":")
	start_timechunk = time_sep[2].split(",")
	start_timechunk_millsec = start_timechunk[1].split(" ")
	start_millsec = int(start_timechunk_millsec[0])
	end_timechunk = time_sep[4].split(",")
	end_millsec = int(end_timechunk[1])

	start_hour = int(time_sep[0])
	start_minutes = int(time_sep[1])
	start_seconds = int(start_timechunk[0])


	end_minutes = time_sep[3]
	end_hour = start_timechunk[1]
	end_seconds = end_timechunk[0]
	end_hour = end_hour[9:]
	
	end_hour = int(end_hour) * 3600
	end_minutes = int(end_minutes) * 60

	start_hour = start_hour * 3600
	start_minutes = start_minutes * 60
	start_all = start_hour + start_minutes + start_seconds
	end_all = end_hour + end_minutes + int(end_seconds)
	difference = end_all - start_all
	return start_all, end_all

#f=open('/home/gordo/media/videos/thenet1995/thenet1995.srt','r')


searchstring = '(\d\d:\d\d:\d\d.\d\d\d --> \d\d:\d\d:\d\d.\d\d\d)\r(.*[^\d]*)'
searchfor = sys.argv[1]
filename = sys.argv[2]

f=open(filename[:-4]+'.srt','r')
lines = f.read()

m = re.findall(searchstring,lines)
arraylength = len(m)
i = 0
#total = os.popen("mplayer -vo dummy -ao dummy -identify /home/gordo/media/videos/thenet1995/*  2>&1 | grep ID_LENGTH")
total = os.popen("mplayer -vo dummy -ao dummy -identify " + filename+ "  2>&1 | grep ID_LENGTH")
totallength =  total.read()
total = totallength.split("=")
total = total[1].strip("\n")
total = total.split(".")
total = total[0]
new_start = ""

for result in m:
	if searchfor in result[1]:
		timecode = result[0]
		start_time, end_time = timecode2seconds(timecode)
		if i==0:
			print 0, start_time, '0'
			new_start = end_time
		else:
			print new_start, start_time, '0'
			new_start = end_time
		i+=1

print new_start, int(total), '0'
