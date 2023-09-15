import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonName = addon.getAddonInfo('id')
selfAddon = xbmcaddon.Addon(id=addonName)

APIKEY = selfAddon.getSetting('apikey')

line1 = "Hello Adrian 0.0.11!" + APIKEY

xbmcgui.Dialog().ok(addonName, line1)
