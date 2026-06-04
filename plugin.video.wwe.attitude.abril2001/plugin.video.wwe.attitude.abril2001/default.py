import sys
import xbmcgui
import xbmcplugin

handle = int(sys.argv[1])

videos = [
    ("RAW Is WAR - 16 Abril 2001",
     "https://archive.org/download/WAR-2001/2001-04-16.mp4"),

    ("SmackDown - 19 Abril 2001",
     "https://archive.org/download/2001.03.15/2001.04.19.mp4"),

    ("RAW Is WAR - 23 Abril 2001",
     "https://archive.org/download/WAR-2001/2001-04-23.mp4"),

    ("SmackDown - 26 Abril 2001",
     "https://archive.org/download/2001.03.15/2001.04.26.mp4"),

    ("RAW Is WAR - 30 Abril 2001",
     "https://archive.org/download/WAR-2001/2001-04-30.mp4")
]

for title, url in videos:
    li = xbmcgui.ListItem(label=title)
    li.setProperty('IsPlayable', 'true')

    xbmcplugin.addDirectoryItem(
        handle=handle,
        url=url,
        listitem=li,
        isFolder=False
    )

xbmcplugin.endOfDirectory(handle)
