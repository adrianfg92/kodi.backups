# import xbmcaddon
# import xbmcgui
#
# addon = xbmcaddon.Addon()
# addonname = addon.getAddonInfo('name')
#
# line1 = "Hello Adrian 021!"
#
# xbmcgui.Dialog().ok(addonname, line1)

import xbmc
import xbmcaddon
import xbmcgui

ADDON = xbmcaddon.Addon()
CWD = ADDON.getAddonInfo('path').decode('utf-8')


class GUI(xbmcgui.WindowXML):
    def __init__(self, *args, **kwargs):
        self.data = kwargs['optional1']

    def onInit(self):
        xbmc.executebuiltin('Container.SetViewMode(50)')
        listitems = []
        listitem1 = xbmcgui.ListItem('my first item')
        listitems.append(listitem1)
        listitem2 = xbmcgui.ListItem('my second item')
        listitems.append(listitem2)
        self.clearList()
        self.addItems(listitems)
        xbmc.sleep(100)
        self.setFocusId(self.getCurrentContainerId())


if __name__ == '__main__':
    ui = GUI('script-testwindow.xml', CWD, 'default', '1080i', True, optional1='some data')
    ui.doModal()
    del ui
