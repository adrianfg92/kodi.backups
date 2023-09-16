import xbmcaddon
import xbmcgui

FOLDERNAME = 'Kodi'
# FAVOURITES = 'favourites.xml'

addon = xbmcaddon.Addon()
addonName = addon.getAddonInfo('id')

selfAddon = xbmcaddon.Addon(id=addonName)
password = selfAddon.getSetting('password')
username = selfAddon.getSetting('username')

line1 = "Folder id: "
xbmcgui.Dialog().ok(addonName, line1)
