import xbmcaddon
import xbmcgui
from mega import Mega

FOLDERNAME = 'Kodi'
# FAVOURITES = 'favourites.xml'

addon = xbmcaddon.Addon()
addonName = addon.getAddonInfo('id')

selfAddon = xbmcaddon.Addon(id=addonName)
password = selfAddon.getSetting('password')
username = selfAddon.getSetting('username')

mega = Mega()
m = mega.login(username, password)

# Get folder andcreate folder if not exist
folder = m.find(FOLDERNAME)
if not folder:
    m.create_folder(FOLDERNAME)
    folder = m.find(FOLDERNAME)

line1 = "Folder id: " + folder[0]
xbmcgui.Dialog().ok(addonName, line1)
# print(folder)

# # Deleting old backup
# file = m.find(FAVOURITES)
# if file:
#     m.destroy(file[0])
#
# # Upload new backup
# m.upload(FAVOURITES, folder[0])
