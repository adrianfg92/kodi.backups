import xbmcaddon
import xbmcgui

from lib.mega import Mega

addon = xbmcaddon.Addon()
addonName = addon.getAddonInfo('id')
mega = Mega()

selfAddon = xbmcaddon.Addon(id=addonName)
password = selfAddon.getSetting('username')
username = selfAddon.getSetting('password')

m = mega.login(username, password)
quota = m.get_quota()

line1 = "Hello Adrian! " + quota

xbmcgui.Dialog().ok(addonName, line1)
