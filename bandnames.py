import wx
import bandnamefunctions

class Frame(wx.Frame):
    def __init__(self, title):
        # create window
        wx.Frame.__init__(self, None, title=title, size = (320,250))
        panel = wx.Panel(self)

        # create menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)

        # create static elements
        wx.StaticBox(panel, pos=(10,20), size=(300, 120))
        self.desc = wx.StaticText(panel, label='At a loss to come up with a name for your newly-formed super-underground indie band?  Try our Band Name Generator!', pos=(20,30))
        self.desc.Wrap(290)

        self.genbutton = wx.Button(panel, label='Generate', pos=(210,100))
        self.genbutton.Bind(wx.EVT_BUTTON, self.generate)

        # create return elements

        wx.StaticBox(panel, pos=(10,150), size=(300, 60))
        wx.StaticText(panel, label='Your new band name is:', pos=(20, 160))
        self.bandname = wx.TextCtrl(panel, size=(250,-1), pos=(20,180))

    def generate(self, event):
        name = bandnamefunctions.generatename()
        self.bandname.SetValue(value = name)


    def exitProgram(self, event):
        self.Destroy()



def main():
    app = wx.App()
    frame = Frame("Indie Band Name Generator")
    frame.Show()
    app.MainLoop()

if __name__ == "__main__": main()
