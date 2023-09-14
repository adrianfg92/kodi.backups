import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "Hello Adrian 023!"

xbmcgui.Dialog().ok(addonname, line1)
