# videogrep.py
## Grep for specific words in srt files and create EDL list

Will generate an EDL list based on a searchword. This EDL list can later be used with mplayer.

Usage: 
``` 
python video.py SEARCHWORD PATH_TO_VIDEOFILE
```
Example:
```
python video.py SEARCHWORD PATH_TO_VIDEOFILE > shortcut.edl
mplayer -edl shortcut.edl PATH_TO_VIDEOFILE
```
(it only properly works if srt file is in the same path and has exactly the same filename with srt ending!

## Notes
Project initially inspired by Michael Murtaugh's [videogrep](http://activearchives.org/wiki/Videogrep).
Similar ideas and thoughts had been floating around at the same time and evolved into much better and polished projects like [Supercut](http://www.supercut.org) and Julian Palacz's [Algorithmic search for love](http://julian.palacz.at/film/algorithmic-search-for-love)

