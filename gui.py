#!/usr/bin/python
# -*- coding: utf-8 -*-

# size.py

import wx
from resources.python.schedule import *
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin

Tuesday = [
          [1, "04:30", "05:30"],
          [2, "07:00", "08:30"],
          [3, " ", " "],
          [4, "10:00", "11:00"],
          [5, "12:00", "14:00"],
          [6, "15:30", "16:30"],
          [7, "18:00", "20:30"],
          [8, " ", " "],
          [9, "22:00", "23:00"],
          [0, " ", " "]
]

class AutoWidthListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        ListCtrlAutoWidthMixin.__init__(self)

class PageOne(wx.Panel):
    def __init__(self, parent):
        panel = wx.Panel.__init__(self, parent)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.list = AutoWidthListCtrl(panel)
        self.list.InsertColumn(0, 'Program', width=140)
        self.list.InsertColumn(1, 'Time On', width=130)
        self.list.InsertColumn(2, 'Time Off', wx.LIST_FORMAT_RIGHT, 90)

        for i in Tuesday:
            index = self.list.InsertStringItem(sys.maxint, i[0])
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageTwo object", (40,40))

class PageThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageThree object", (60,60))

class MainFrame(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    

        menubar = wx.MenuBar()
        viewMenu = wx.Menu()
        fileMenu = wx.Menu()

        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')
        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statubar', 
            'Show Statusbar', kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 
            'Show Toolbar', kind=wx.ITEM_CHECK)
        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)
        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        menubar.Append(fileMenu, '&File')
        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddLabelTool(1, '', wx.Bitmap('resources/images/application-exit.png'))
        self.toolbar.Realize()

        p = wx.Panel(self)
        nb = wx.Notebook(p)
        page1 = PageOne(nb)
        page2 = PageTwo(nb)
        page3 = PageThree(nb)
        nb.AddPage(page1, "Central Heating Overview")
        nb.AddPage(page2, "Schedule Control")
        nb.AddPage(page3, "Settings")
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')
        self.SetSize((900, 600))
        self.SetTitle('Network Menu')
        self.Centre()
        self.Show(True)

    def ToggleStatusBar(self, e):
        
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):
        
        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()        
        
    def OnQuit(self, e):
        self.Close()

def main():
    
    ex = wx.App()
    MainFrame(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()
