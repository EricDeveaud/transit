# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import sys

try:
    import wx
    import wx.xrc
    from wx.lib.buttons import GenBitmapTextButton

    hasWx = True
    
    #Check if wx is the newest 3.0+ version:
    try:
        from wx.lib.pubsub import pub
        pub.subscribe
        newWx = True
    except AttributeError as e:
        from wx.lib.pubsub import Publisher as pub
        newWx = False
except Exception as e:
    hasWx = False
    newWx = False

import os
import time
import datetime
import threading
import numpy
import matplotlib.pyplot as plt
import multiprocessing as mp
import math
import subprocess

from functools import partial

import traceback

import pytransit
import pytransit.analysis
import pytransit.trash as trash
import pytransit.transit_tools as transit_tools
import pytransit.tnseq_tools as tnseq_tools
import pytransit.norm_tools as norm_tools
import pytransit.fileDisplay as fileDisplay
import pytransit.qcDisplay as qcDisplay
import pytransit.images as images



method_wrap_width = 250
methods = pytransit.analysis.methods


wildcard = "Python source (*.py)|*.py|" \
            "All files (*.*)|*.*"
transit_prefix = "[TRANSIT]"







###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"TRANSIT", pos = wx.DefaultPosition, size = wx.Size( 1300,975 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        

        #Define variables

        #Define Text
        self.instructions_text = """
1. Choose the annotation file ("prot table") that corresponds to the datasets to be analyzed.
2. Add the desired Control and Experimental datasets.
3. (Optional) If you wish to visualize their read counts, select the desired datasets and click on the "View" button.
4. Select the desired analysis method from the dropdown menu on the top-right of the window, and follow its instructions.
"""


        # Define ART
        bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, (16, 16))



        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.mainWindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.VSCROLL )
        self.mainWindow.SetScrollRate( 5, 5 )
        self.mainWindow.SetMinSize( wx.Size( 700,-1 ) )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        # Organism
        orgSizer = wx.StaticBoxSizer( wx.StaticBox( self.mainWindow, wx.ID_ANY, u"Organism" ), wx.VERTICAL )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.mainWindow, wx.ID_ANY, u"Annotation File:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer10.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        

        self.annotationFilePicker = GenBitmapTextButton(self.mainWindow, 1, bmp, '[Click to add Annotation File (.prot_table)]', size= wx.Size(400, 30))


        bSizer10.Add( self.annotationFilePicker, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_panel2 = wx.Panel( self.mainWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetMinSize( wx.Size( 100,-1 ) )
        self.m_panel2.SetMaxSize( wx.Size( 150,-1 ) )
        
        bSizer10.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        orgSizer.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        
        bSizer4.Add( orgSizer, 0, wx.EXPAND, 5 )
        
        ctrlSizer = wx.StaticBoxSizer( wx.StaticBox( self.mainWindow, wx.ID_ANY, u"Control Samples" ), wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.ctrlRemoveButton = wx.Button( self.mainWindow, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.ctrlRemoveButton, 0, wx.ALL, 5 )
        
        self.ctrlView = wx.Button( self.mainWindow, wx.ID_ANY, u"Track View", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ctrlView.Hide()
        
        bSizer2.Add( self.ctrlView, 0, wx.ALL, 5 )
        
        self.ctrlScatter = wx.Button( self.mainWindow, wx.ID_ANY, u"Scatter", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ctrlScatter.Hide()
        
        bSizer2.Add( self.ctrlScatter, 0, wx.ALL, 5 )
        
        self.ctrlFilePicker = GenBitmapTextButton(self.mainWindow, 1, bmp, '[Click to add Control Dataset(s)]', size= wx.Size(400, 30))
        bSizer2.Add( self.ctrlFilePicker, 1, wx.ALL, 5 )
        
        self.m_panel21 = wx.Panel( self.mainWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel21.SetMinSize( wx.Size( 100,-1 ) )
        self.m_panel21.SetMaxSize( wx.Size( 150,-1 ) )
        
        bSizer2.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        ctrlSizer.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        self.list_ctrl = wx.ListCtrl( self.mainWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SUNKEN_BORDER )

        self.list_ctrl.SetMaxSize(wx.Size(940,200))
        ctrlSizer.Add( self.list_ctrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer4.Add( ctrlSizer, 1, wx.EXPAND, 5 )
        
        expSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.mainWindow, wx.ID_ANY, u"Experimental Samples" ), wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.expSizer = wx.Button( self.mainWindow, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.expSizer, 0, wx.ALL, 5 )
        
        self.expView = wx.Button( self.mainWindow, wx.ID_ANY, u"Track View", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.expView.Hide()
        
        bSizer3.Add( self.expView, 0, wx.ALL, 5 )
        
        self.expScatter = wx.Button( self.mainWindow, wx.ID_ANY, u"Scatter", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.expScatter.Hide()
        
        bSizer3.Add( self.expScatter, 0, wx.ALL, 5 )
       

        self.expFilePicker = GenBitmapTextButton(self.mainWindow, 1, bmp, '[Click to add Experimental Dataset(s)]', size= wx.Size(400, 30))
        bSizer3.Add( self.expFilePicker, 1, wx.ALL, 5 )
        
        self.m_panel22 = wx.Panel( self.mainWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel22.SetMinSize( wx.Size( 100,-1 ) )
        self.m_panel22.SetMaxSize( wx.Size( 150,-1 ) )
        
        bSizer3.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        expSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
        
        self.list_exp = wx.ListCtrl( self.mainWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SUNKEN_BORDER )
        self.list_exp.SetMaxSize(wx.Size(940, 200))
        expSizer1.Add( self.list_exp, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer4.Add( expSizer1, 1, wx.EXPAND, 5 )
        
        filesSizer = wx.StaticBoxSizer( wx.StaticBox( self.mainWindow, wx.ID_ANY, u"Results Files" ), wx.VERTICAL )
        
        bSizer141 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.displayButton = wx.Button( self.mainWindow, wx.ID_ANY, u"Display Table", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer141.Add( self.displayButton, 0, wx.ALL, 5 )
        
        self.fileActionButton = wx.Button( self.mainWindow, wx.ID_ANY, u"Display Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.fileActionButton.Hide()
        
        bSizer141.Add( self.fileActionButton, 0, wx.ALL, 5 )
        
        self.addFileButton = GenBitmapTextButton(self.mainWindow, 1 , bmp, 'Add Results File', size= wx.Size(150, 30))


        bSizer141.Add( self.addFileButton, 0, wx.ALL, 5 )
        
        fileActionChoiceChoices = [ u"[Choose Action]"]
        self.fileActionChoice = wx.Choice( self.mainWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, fileActionChoiceChoices, 0 )
        self.fileActionChoice.SetSelection( 0 )
        bSizer141.Add( self.fileActionChoice, 0, wx.ALL, 5 )
        
        
        filesSizer.Add( bSizer141, 0, 0, 5 )
        
        self.list_files = wx.ListCtrl( self.mainWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SUNKEN_BORDER )
        self.list_files.SetMaxSize(wx.Size(940,200))
        filesSizer.Add( self.list_files, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer4.Add( filesSizer, 1, wx.EXPAND, 5 )
        
        
        self.mainWindow.SetSizer( bSizer4 )
        self.mainWindow.Layout()
        bSizer4.Fit( self.mainWindow )
        bSizer1.Add( self.mainWindow, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.DOUBLE_BORDER|wx.TAB_TRAVERSAL )
        self.m_panel5.SetMaxSize( wx.Size( 2,-1 ) )
        
        bSizer1.Add( self.m_panel5, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.optionsWindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.VSCROLL |wx.EXPAND)
        self.optionsWindow.SetScrollRate( 5, 5 )
        self.optionsWindow.SetMinSize( wx.Size( 310,1000 ) )
        #self.optionsWindow.SetMaxSize( wx.Size( 310,1000 ) )
        #self.optionsWindow.BackgroundColour = (200, 0, 20) 
        

        self.optionsSizer = wx.BoxSizer( wx.VERTICAL )

        # Logo Section
        self.logoImg = wx.StaticBitmap( self.optionsWindow, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.optionsSizer.Add( self.logoImg, 0, wx.ALL|wx.ALIGN_CENTER, 5 )

        self.versionLabel = wx.StaticText( self.optionsWindow, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.versionLabel.Wrap( -1 )
        self.versionLabel.SetFont( wx.Font( 10, 74, 90, 92, False, "Sans" ) )

        self.optionsSizer.Add( self.versionLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        # Method Information 
        self.methodInfoText = wx.StaticBox( self.optionsWindow, wx.ID_ANY, u"Instructions" )
        self.methodInfoSizer = wx.StaticBoxSizer( self.methodInfoText, wx.VERTICAL )

        self.methodShortText = wx.StaticText( self.optionsWindow, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.methodShortText.Wrap(250)
        self.methodShortText.Hide()
        self.methodInfoSizer.Add( self.methodShortText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.methodLongText = wx.StaticText( self.optionsWindow, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.methodLongText.Wrap(250)
        self.methodLongText.Hide()
        self.methodInfoSizer.Add( self.methodLongText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.methodDescText = wx.StaticText( self.optionsWindow, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.methodDescText.Wrap(250)
        self.methodDescText.Hide()
        self.methodInfoSizer.Add( self.methodDescText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.methodTnText = wx.StaticText( self.optionsWindow, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.methodTnText.Wrap(250)

        font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.methodTnText.SetFont(font)
        self.methodTnText.Hide()

        self.methodInfoSizer.Add( self.methodTnText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.methodInstructions = wx.StaticText( self.optionsWindow, wx.ID_ANY, self.instructions_text, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.methodInstructions.Wrap( 250 )
        self.methodInfoSizer.Add( self.methodInstructions, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        self.optionsSizer.Add( self.methodInfoSizer, 0, wx.ALL|wx.EXPAND, 5 )




        # Method Options 
        self.methodSizerText = wx.StaticBox( self.optionsWindow, wx.ID_ANY, u"Method Options" )
        self.methodSizer = wx.StaticBoxSizer( self.methodSizerText, wx.VERTICAL )

        #self.methodSizerText.Hide()
        #self.methodSizer.SetMinSize( wx.Size( 250,-1 ) ) 
        
        self.m_panel1 = wx.Panel( self.optionsWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel1.SetMinSize( wx.Size( 50,1 ) )
        
        self.methodSizer.Add( self.m_panel1, 0, wx.ALL, 5 )
        
        self.globalLabel = wx.StaticText( self.optionsWindow, wx.ID_ANY, u"Global Options", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.globalLabel.Wrap( -1 )
        self.methodSizer.Add( self.globalLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.globalPanel = wx.Panel( self.optionsWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.globalPanel.SetMinSize( wx.Size( 50,90 ) )
        self.globalPanel.SetMaxSize( wx.Size( 250,-1) )
       
        #self.globalPanel.BackgroundColour = (200, 230, 250) 
        bSizer1431 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer1521 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer1621 = wx.BoxSizer( wx.VERTICAL )
        
        self.globalNTerminusLabel = wx.StaticText( self.globalPanel, wx.ID_ANY, u"Ignore N-Terminus %:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.globalNTerminusLabel.Wrap( -1 )
        bSizer1621.Add( self.globalNTerminusLabel, 0, wx.ALL, 5 )
        
        self.globalCTerminusLabel = wx.StaticText( self.globalPanel, wx.ID_ANY, u"Ignore C-Terminus %:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.globalCTerminusLabel.Wrap( -1 )
        bSizer1621.Add( self.globalCTerminusLabel, 0, wx.ALL, 5 )
        
        
        bSizer1521.Add( bSizer1621, 1, wx.EXPAND, 5 )
        
        bSizer1721 = wx.BoxSizer( wx.VERTICAL )
        
        self.globalNTerminusText = wx.TextCtrl( self.globalPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1721.Add( self.globalNTerminusText, 0, wx.ALL, 5 )
        
        self.globalCTerminusText = wx.TextCtrl( self.globalPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1721.Add( self.globalCTerminusText, 0, wx.ALL, 5 )
        
        
        bSizer1521.Add( bSizer1721, 1, wx.EXPAND, 5 )
        
        
        bSizer1431.Add( bSizer1521, 1, wx.EXPAND, 5 )
        
        
        self.globalPanel.SetSizer( bSizer1431 )
        self.globalPanel.Layout()
        bSizer1431.Fit( self.globalPanel )
        self.methodSizer.Add( self.globalPanel, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        #--------------------#

        self.optionsSizer.Add( self.methodSizer, 0, wx.EXPAND, 5 )

        self.optionsWindow.SetSizer( self.optionsSizer )
        self.optionsWindow.Layout()

        self.optionsWindow.Fit()
        
        #self.optionsSizer.Fit( self.optionsWindow )
        bSizer1.Add( self.optionsWindow, 0, wx.ALL, 5 )
        
        #--------------------#        

        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.fileMenuItem = wx.Menu()
        self.exportMenuItem = wx.Menu()
        self.selectedExportMenuItem = wx.Menu()
        self.selectedExportIGVMenuItem = wx.MenuItem( self.selectedExportMenuItem, wx.ID_ANY, u"to IGV", wx.EmptyString, wx.ITEM_NORMAL )
        self.selectedExportMenuItem.AppendItem( self.selectedExportIGVMenuItem )
        

        self.selectedExportCombinedWigMenuItem = wx.MenuItem( self.selectedExportMenuItem, wx.ID_ANY, u"to Combined Wig", wx.EmptyString, wx.ITEM_NORMAL )
        self.selectedExportMenuItem.AppendItem( self.selectedExportCombinedWigMenuItem )


        self.exportMenuItem.AppendSubMenu( self.selectedExportMenuItem, u"Selected Datasets" )
        
        self.fileMenuItem.AppendSubMenu( self.exportMenuItem, u"Export" )
        
        self.convertMenuItem = wx.Menu()
        self.annotationConvertPTToPTTMenu = wx.MenuItem( self.convertMenuItem, wx.ID_ANY, u"prot_table to PTT", wx.EmptyString, wx.ITEM_NORMAL )
        self.convertMenuItem.AppendItem( self.annotationConvertPTToPTTMenu )
        
        self.annotationConvertPTToGFF3Menu = wx.MenuItem( self.convertMenuItem, wx.ID_ANY, u"prot_table to GFF3", wx.EmptyString, wx.ITEM_NORMAL )
        self.convertMenuItem.AppendItem( self.annotationConvertPTToGFF3Menu )
        
        self.annotationConvertPTTToPT = wx.MenuItem( self.convertMenuItem, wx.ID_ANY, u"PTT to prot_table", wx.EmptyString, wx.ITEM_NORMAL )
        self.convertMenuItem.AppendItem( self.annotationConvertPTTToPT )
        
        self.annotationConvertGFF3ToPT = wx.MenuItem( self.convertMenuItem, wx.ID_ANY, u"GFF3 to prot_table", wx.EmptyString, wx.ITEM_NORMAL )
        self.convertMenuItem.AppendItem( self.annotationConvertGFF3ToPT )
        
        self.fileMenuItem.AppendSubMenu( self.convertMenuItem, u"Convert" )
        
        self.fileExitMenuItem = wx.MenuItem( self.fileMenuItem, wx.ID_ANY, u"&Exit", wx.EmptyString, wx.ITEM_NORMAL )
        self.fileMenuItem.AppendItem( self.fileExitMenuItem )
        
        self.m_menubar1.Append( self.fileMenuItem, u"&File" ) 
        
        self.viewMenuItem = wx.Menu()
        self.scatterMenuItem = wx.MenuItem( self.viewMenuItem, wx.ID_ANY, u"&Scatter Plot", wx.EmptyString, wx.ITEM_NORMAL )
        self.viewMenuItem.AppendItem( self.scatterMenuItem )
        
        self.trackMenuItem = wx.MenuItem( self.viewMenuItem, wx.ID_ANY, u"&Track View", wx.EmptyString, wx.ITEM_NORMAL )
        self.viewMenuItem.AppendItem( self.trackMenuItem )
        
        self.qcMenuItem = wx.MenuItem( self.viewMenuItem, wx.ID_ANY, u"&Quality Control", wx.EmptyString, wx.ITEM_NORMAL )
        self.viewMenuItem.AppendItem( self.qcMenuItem )
        
        self.m_menubar1.Append( self.viewMenuItem, u"&View" ) 
       

        # 
        self.methodsMenuItem = wx.Menu()
        self.himar1MenuItem = wx.Menu()
        self.tn5MenuItem = wx.Menu()
        
        
        self.methodsMenuItem.AppendSubMenu(self.himar1MenuItem, "&Himar1 Methods")
        self.methodsMenuItem.AppendSubMenu(self.tn5MenuItem, "&Tn5 Methods")
        self.m_menubar1.Append( self.methodsMenuItem, u"&Analysis" )
        
 
        self.SetMenuBar( self.m_menubar1 )

        
        self.helpMenuItem = wx.Menu()
        self.documentationMenuItem = wx.MenuItem(self.helpMenuItem, wx.ID_ANY, u"&Documentation", wx.EmptyString, wx.ITEM_NORMAL)
        self.helpMenuItem.AppendItem(self.documentationMenuItem)
        self.aboutMenuItem = wx.MenuItem(self.helpMenuItem, wx.ID_ANY, u"&About", wx.EmptyString, wx.ITEM_NORMAL)
        self.helpMenuItem.AppendItem(self.aboutMenuItem)
        self.m_menubar1.Append( self.helpMenuItem, u"&Help" )
        
        
        self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        



        self.Centre( wx.BOTH )
        
        # Connect Events

        self.annotationFilePicker.Bind( wx.EVT_BUTTON, self.annotationFileFunc )
        self.ctrlRemoveButton.Bind( wx.EVT_BUTTON, self.ctrlRemoveFunc )
        self.ctrlView.Bind( wx.EVT_BUTTON, self.allViewFunc )
        self.ctrlScatter.Bind( wx.EVT_BUTTON, self.scatterFunc )
        self.ctrlFilePicker.Bind( wx.EVT_BUTTON, self.loadCtrlFileFunc )
        self.expSizer.Bind( wx.EVT_BUTTON, self.expRemoveFunc )
        self.expView.Bind( wx.EVT_BUTTON, self.allViewFunc )
        self.expScatter.Bind( wx.EVT_BUTTON, self.scatterFunc )
        self.expFilePicker.Bind( wx.EVT_BUTTON, self.loadExpFileFunc )
        self.displayButton.Bind( wx.EVT_BUTTON, self.displayFileFunc )
        self.fileActionButton.Bind( wx.EVT_BUTTON, self.fileActionFunc )
        self.addFileButton.Bind( wx.EVT_BUTTON, self.addFileFunc )
        self.fileActionChoice.Bind( wx.EVT_CHOICE, self.fileActionFunc )
        self.list_files.Bind( wx.EVT_LIST_ITEM_SELECTED, self.fileSelected )
        self.Bind( wx.EVT_MENU, self.selectedToIGV, id = self.selectedExportIGVMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.selectedToCombinedWig, id = self.selectedExportCombinedWigMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.annotationPT_to_PTT, id = self.annotationConvertPTToPTTMenu.GetId() )
        self.Bind( wx.EVT_MENU, self.annotationPT_to_GFF3, id = self.annotationConvertPTToGFF3Menu.GetId() )
        self.Bind( wx.EVT_MENU, self.annotationPTT_to_PT, id = self.annotationConvertPTTToPT.GetId() )
        self.Bind( wx.EVT_MENU, self.annotationGFF3_to_PT, id = self.annotationConvertGFF3ToPT.GetId() )
        self.Bind( wx.EVT_MENU, self.Exit, id = self.fileExitMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.scatterFunc, id = self.scatterMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.allViewFunc, id = self.trackMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.qcFunc, id = self.qcMenuItem.GetId() )

        self.Bind( wx.EVT_MENU, self.aboutFunc, id = self.aboutMenuItem.GetId() )
        self.Bind( wx.EVT_MENU, self.documentationFunc, id = self.documentationMenuItem.GetId() )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class

    def onHimar1Checked(self, event):
        event.Skip()

    def onTn5Checked(self, event):
        event.Skip()

    def annotationFileFunc( self, event ):
        event.Skip()
    
    def ctrlRemoveFunc( self, event ):
        event.Skip()
    
    def allViewFunc( self, event ):
        event.Skip()
    
    def scatterFunc( self, event ):
        event.Skip()
    
    def loadCtrlFileFunc( self, event ):
        event.Skip()
    
    def expRemoveFunc( self, event ):
        event.Skip()
    
    def loadExpFileFunc( self, event ):
        event.Skip()
    
    def displayFileFunc( self, event ):
        event.Skip()
    
    def fileActionFunc( self, event ):
        event.Skip()
    
    def addFileFunc( self, event ):
        event.Skip()
    
    
    def MethodSelectFunc( self, event ):
        event.Skip()
    
#    def RunGumbelFunc( self, event ):
#        event.Skip()
    
    def RunBinomialFunc( self, event ):
        event.Skip()
    
    def LoessPrevFunc( self, event ):
        event.Skip()
    
    def RunHMMFunc( self, event ):
        event.Skip()
    
    
    def RunResamplingFunc( self, event ):
        event.Skip()
    
    
    def RunDEHMMFunc( self, event ):
        event.Skip()
    
    def ctrlToIGV( self, event ):
        event.Skip()
    
    def expToIGV( self, event ):
        event.Skip()
    
    def selectedToIGV( self, event ):
        event.Skip()

    def selectedToCombinedWig( self, event ):
        event.Skip()
    
    def annotationPT_to_PTT( self, event ):
        event.Skip()
    
    def annotationPT_to_GFF3( self, event ):
        event.Skip()
    
    def annotationPTT_to_PT( self, event ):
        event.Skip()
    
    def annotationGFF3_to_PT( self, event ):
        event.Skip()
    
    def Exit( self, event ):
        event.Skip()
    
    
    def qcFunc( self, event ):
        event.Skip()
    
    def aboutFunc( self, event ):
        event.Skip()

    def documentationFunc( self, event ):
        event.Skip()
    

#!/usr/bin/env python

# Copyright 2015.
#   Michael A. DeJesus, Chaitra Ambadipudi, and  Thomas R. Ioerger.
#
#
#    This file is part of TRANSIT.
#
#    TRANSIT is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#
#    TRANSIT is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with TRANSIT.  If not, see <http://www.gnu.org/licenses/>.


#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class TnSeekFrame(MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        MainFrame.__init__(self,parent)

        self.SetIcon(images.transit_icon.GetIcon())

        self.workdir = os.getcwd()
        self.annotation = ""
        self.transposons = ["himar1", "tn5"]
        #import pkgutil
        #print [x for x in pkgutil.iter_modules(['transit/analysis'])]
        #print gumbel.Gumbel.__bases__

        self.logoImg.SetBitmap(images.transit_logo2.GetImage().ConvertToBitmap())
        self.versionLabel.SetLabel(pytransit.__version__)
        self.methodSizerText.Hide()        

        self.index_ctrl = 0
        self.list_ctrl.InsertColumn(0, 'File', width=210)
        self.list_ctrl.InsertColumn(1, 'Total Reads', width=85)
        self.list_ctrl.InsertColumn(2, 'Density', width=85)
        self.list_ctrl.InsertColumn(3, 'Mean Count', width=90)
        self.list_ctrl.InsertColumn(4, 'Max Count', width=85)
        self.list_ctrl.InsertColumn(5, 'Full Path', width=403)


        self.index_exp = 0
        self.list_exp.InsertColumn(0, 'File', width=210)
        self.list_exp.InsertColumn(1, 'Total Reads', width=85)
        self.list_exp.InsertColumn(2, 'Density', width=85)
        self.list_exp.InsertColumn(3, 'Mean Count', width=90)
        self.list_exp.InsertColumn(4, 'Max Count', width=85)
        self.list_exp.InsertColumn(5, 'Full Path',width=403)


        self.index_file = 0
        self.list_files.InsertColumn(0, 'Name', width=350)
        self.list_files.InsertColumn(1, 'Type', width=100)
        self.list_files.InsertColumn(2, 'Date', width=230)
        self.list_files.InsertColumn(3, 'Full Path',width=403)


        self.verbose = True


        self.statusBar.SetStatusText("Welcome to TRANSIT")
        self.progress_count = 0
        pub.subscribe(self.setProgressRange, "progressrange")
        pub.subscribe(self.updateProgress, "progress")
        pub.subscribe(self.updateStatus, "status")
        pub.subscribe(self.addFile, "file")
        pub.subscribe(self.finishRun, "finish")
        pub.subscribe(self.saveHistogram, "histogram")   
 
        #self.outputDirPicker.SetPath(os.path.dirname(os.path.realpath(__file__)))

        methodChoiceChoices = [ "[Choose Method]"]
        for name in methods:
            methods[name].gui.definePanel(self)
            #methods[name].gui.panel.BackgroundColour = (0, 200, 20)
            self.methodSizer.Add(methods[name].gui.panel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
            methods[name].gui.Hide()

            if "himar1" in methods[name].transposons:
                tempMenuItem = wx.MenuItem( self.himar1MenuItem, wx.ID_ANY, methods[name].fullname(), wx.EmptyString, wx.ITEM_NORMAL )
                self.Bind( wx.EVT_MENU, partial(self.MethodSelectFunc,  methods[name].fullname()), tempMenuItem )
                self.himar1MenuItem.AppendItem( tempMenuItem )
            if "tn5" in methods[name].transposons:
                tempMenuItem = wx.MenuItem( self.tn5MenuItem, wx.ID_ANY, methods[name].fullname(), wx.EmptyString, wx.ITEM_NORMAL )
                self.Bind( wx.EVT_MENU, partial(self.MethodSelectFunc, methods[name].fullname()), tempMenuItem )
                self.tn5MenuItem.AppendItem( tempMenuItem )

        #progress
        self.progressPanel = wx.Panel( self.optionsWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        progressSizer = wx.BoxSizer( wx.VERTICAL )

        self.progressLabel = wx.StaticText( self.progressPanel, wx.ID_ANY, u"Progress", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.progressLabel.Wrap( -1 )
        progressSizer.Add( self.progressLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.progress = wx.Gauge( self.progressPanel, wx.ID_ANY, 20, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
        progressSizer.Add( self.progress, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        #self.progressPanel.BackgroundColour = (0, 0, 250)
        self.progressPanel.SetSizer( progressSizer )
        self.progressPanel.SetMaxSize(wx.Size(100, 100))
        self.progressPanel.Layout()

        #progressSizer.Fit( self.progressPanel )
        self.methodSizer.Add( self.progressPanel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        #self.methodSizer.Add( self.globalLabel, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        #self.methodSizer.Hide()
        self.progress.SetRange(50)
        #########
        
        self.optionsWindow.Fit()

        self.HideProgressSection()
        self.HideGlobalOptions()

    


    def Exit(self, event):
        """Exit Menu Item"""
        if self.verbose:
            transit_tools.transit_message("Exiting Transit")
        self.Close()


    def updateProgress(self, msg):
        """"""
        if newWx:
            method, count = msg
        else:
            method, count = msg.data
        self.progress_count = count
        try:
            self.progress.SetValue(self.progress_count)
        except:
            pass

    def setProgressRange(self, msg):
        """"""
        if newWx:
            count = msg
        else:
            count = msg.data
        try:
            self.progress.SetRange(count)
        except:
            pass

    

    def updateStatus(self, msg):
        """"""
        if newWx:
            method, text = msg 
        else:
            method, text = msg.data
        self.statusBar.SetStatusText(text)

    
    def saveHistogram(self, msg):
        if newWx:
            data, orf, path, delta = msg
        else:
            data, orf, path, delta = msg.data

        n, bins, patches = plt.hist(data, normed=1, facecolor='c', alpha=0.75, bins=100)
        plt.xlabel('Delta Sum')
        plt.ylabel('Probability')
        plt.title('%s - Histogram of Delta Sum' % orf)
        plt.axvline(delta, color='r', linestyle='dashed', linewidth=3)
        plt.grid(True)
        genePath = os.path.join(path, orf +".png")
        plt.savefig(genePath)
        plt.clf()



    def addFile(self, data):
        if not newWx:
            data = data.data
        fullpath = data["path"]
        name = transit_tools.basename(fullpath)
        type = data["type"]
        date = data["date"]
        self.list_files.InsertStringItem(self.index_file, name)
        self.list_files.SetStringItem(self.index_file, 1, "%s" % type)
        self.list_files.SetStringItem(self.index_file, 2, "%s" % (date))
        self.list_files.SetStringItem(self.index_file, 3, "%s" % (fullpath))
        self.index_file+=1
        

    def finishRun(self,msg):
        if not newWx: msg = msg.data
        try:
            #methods[msg].gui.Enable()
            pass
        except Exception as e:
            transit_tools.transit_message("Error: %s" % e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)


    def ResetProgress(self):
        self.progress_count = 0



    def HideAllOptions(self):
        self.HideGlobalOptions()
        self.HideProgressSection()
        for name in methods:
            methods[name].gui.Hide()


    def HideGlobalOptions(self):
        self.globalLabel.Hide()
        self.globalNTerminusLabel.Hide()
        self.globalCTerminusLabel.Hide()
        self.globalNTerminusText.Hide()
        self.globalCTerminusText.Hide()


    def ShowGlobalOptions(self):
        self.globalLabel.Show()
        self.globalNTerminusLabel.Show()
        self.globalCTerminusLabel.Show()
        self.globalNTerminusText.Show()
        self.globalCTerminusText.Show()

    def HideProgressSection(self):
        self.progressLabel.Hide()
        self.progress.Hide()


    def ShowProgressSection(self):
        self.progressLabel.Show()
        self.progress.Show()

    def onHimar1Checked(self, event):
        if self.methodCheckBoxHimar1.GetValue():
            self.transposons.append("himar1")
        else:
            self.transposons.remove("himar1")
        self.filterMethodsByTransposon()

    def onTn5Checked(self, event):
        if self.methodCheckBoxTn5.GetValue():
            self.transposons.append("tn5")
        else:
            self.transposons.remove("tn5")
        self.filterMethodsByTransposon()

    def filterMethodsByTransposon(self):
        newmethods = {}
        fullmethods = pytransit.analysis.methods
        goodTn = False
        for method in fullmethods:
            goodTn = False
            for tn in self.transposons:
                if tn in fullmethods[method].transposons:
                    goodTn = True
            if goodTn:
                newmethods[method] = fullmethods[method]
        
        methodChoiceChoices = [ "[Choose Method]"]
        for name in newmethods:
            methodChoiceChoices.append(methods[name].fullname())
        self.methodChoice.SetItems(methodChoiceChoices)
        self.methodChoice.SetSelection( 0 )



    def SaveFile(self, DIR=None, FILE="", WC=""):
        """
        Create and show the Save FileDialog
        """
        path = ""

        if not DIR:
            DIR = os.getcwd()

        dlg = wx.FileDialog(
            self, message="Save file as ...",
            defaultDir=DIR,
            defaultFile=FILE, wildcard=WC, style=wx.SAVE|wx.OVERWRITE_PROMPT
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if self.verbose:
                transit_tools.transit_message("You chose the following output filename: %s" % path)
        dlg.Destroy()
        return path

    def OpenFile(self, DIR=".", FILE="", WC=""):
        """
        Create and show the Open FileDialog
        """
        path = ""
        dlg = wx.FileDialog(
            self, message="Save file as ...",
            defaultDir=DIR,
            defaultFile=FILE, wildcard=WC, style=wx.OPEN
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if self.verbose:
                transit_tools.transit_message("You chose the following file: %s" % path)
        dlg.Destroy()
        return path


    def ctrlSelected(self, col=5):
        selected_ctrl = []
        current = -1
        while True:
            next = self.list_ctrl.GetNextSelected(current)
            if next == -1:
                break
            path = self.list_ctrl.GetItem(next, col).GetText()
            selected_ctrl.append(path)
            current = next
        return selected_ctrl


    def expSelected(self, col=5):
        selected_exp = []
        current = -1
        while True:
            next = self.list_exp.GetNextSelected(current)
            if next == -1:
                break
            path = self.list_exp.GetItem(next, col).GetText()
            selected_exp.append(path)
            current = next
        return selected_exp


    def allSelected(self, col=5):
        selected_all = self.ctrlSelected(col) + self.expSelected(col)
        return selected_all


    def ctrlAll(self, col=5):
        all_ctrl = []
        for i in range(self.list_ctrl.GetItemCount()):
            all_ctrl.append(self.list_ctrl.GetItem(i, col).GetText())
        return all_ctrl


    def expAll(self, col=5):
        all_exp = []
        for i in range(self.list_exp.GetItemCount()):
            all_exp.append(self.list_exp.GetItem(i, col).GetText())
        return all_exp


    def loadCtrlFileFunc(self, event):
        self.statusBar.SetStatusText("Loading Control Dataset(s)...")
        try:
        
            dlg = wx.FileDialog(
                self, message="Choose a file",
                defaultDir=self.workdir,
                defaultFile="",
                wildcard=u"Read Files (*.wig)|*.wig;|\nRead Files (*.txt)|*.txt;|\nRead Files (*.dat)|*.dat;|\nAll files (*.*)|*.*",
                style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
                )
            if dlg.ShowModal() == wx.ID_OK:
                paths = dlg.GetPaths()
                print "You chose the following Control file(s):"
                for fullpath in paths:
                    print "\t%s" % fullpath
                    name = transit_tools.basename(fullpath)
                    (density, meanrd, nzmeanrd, nzmedianrd, maxrd, totalrd, skew, kurtosis) = tnseq_tools.get_wig_stats(fullpath)
                    self.list_ctrl.InsertStringItem(self.index_ctrl, name)
                    self.list_ctrl.SetStringItem(self.index_ctrl, 1, "%1.1f" % (totalrd))
                    self.list_ctrl.SetStringItem(self.index_ctrl, 2, "%2.1f" % (density*100))
                    self.list_ctrl.SetStringItem(self.index_ctrl, 3, "%1.1f" % (meanrd))
                    self.list_ctrl.SetStringItem(self.index_ctrl, 4, "%d" % (maxrd))
                    self.list_ctrl.SetStringItem(self.index_ctrl, 5, "%s" % (fullpath))
                    self.index_ctrl+=1
            dlg.Destroy()
        except Exception as e:
            transit_tools.transit_message("Error: %s" % e)
            print "PATH", fullpath
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
        self.statusBar.SetStatusText("")


    def loadExpFileFunc(self, event):
        self.statusBar.SetStatusText("Loading Experimental Dataset(s)...")
        try:

            dlg = wx.FileDialog(
                self, message="Choose a file",
                defaultDir=self.workdir,
                defaultFile="",
                wildcard=u"Read Files (*.wig)|*.wig;|\nRead Files (*.txt)|*.txt;|\nRead Files (*.dat)|*.dat;|\nAll files (*.*)|*.*",
                style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
                )
            if dlg.ShowModal() == wx.ID_OK:
                paths = dlg.GetPaths()
                print "You chose the following Experimental file(s):"
                for fullpath in paths:
                    print "\t%s" % fullpath
                    name = transit_tools.basename(fullpath)
                    (density, meanrd, nzmeanrd, nzmedianrd, maxrd, totalrd, skew, kurtosis) = tnseq_tools.get_wig_stats(fullpath)
                    self.list_exp.InsertStringItem(self.index_exp, name)
                    self.list_exp.SetStringItem(self.index_exp, 1, "%1.1f" % (totalrd))
                    self.list_exp.SetStringItem(self.index_exp, 2, "%2.1f" % (density*100))
                    self.list_exp.SetStringItem(self.index_exp, 3, "%1.1f" % (meanrd))
                    self.list_exp.SetStringItem(self.index_exp, 4, "%d" % (maxrd))
                    self.list_exp.SetStringItem(self.index_exp, 5, "%s" % (fullpath))
                    self.index_exp+=1
            dlg.Destroy()
        except Exception as e:
            transit_tools.transit_message("Error: %s" % e)
            print "PATH", fullpath
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

        self.statusBar.SetStatusText("")

    def ctrlRemoveFunc(self, event):
        next = self.list_ctrl.GetNextSelected(-1)
        while next != -1:
            if self.verbose:
                transit_tools.transit_message("Removing control item (%d): %s" % (next, self.list_ctrl.GetItem(next, 0).GetText()))
            self.list_ctrl.DeleteItem(next)
            next = self.list_ctrl.GetNextSelected(-1)
            self.index_ctrl-=1 

     


    def expRemoveFunc(self, event):
        next = self.list_exp.GetNextSelected(-1)
        while next != -1:
            if self.verbose:
                transit_tools.transit_message("Removing experimental item (%d): %s" % (next, self.list_exp.GetItem(next, 0).GetText()))
            self.list_exp.DeleteItem(next)
            next = self.list_exp.GetNextSelected(-1)
            self.index_exp-=1


    def allViewFunc(self, event, gene=""):
        
        annotationpath = self.annotation
        datasets = self.ctrlSelected() + self.expSelected()

        if datasets and annotationpath:
            if self.verbose:
                transit_tools.transit_message("Visualizing counts for: %s" % ", ".join([transit_tools.fetch_name(d) for d in datasets]))
            viewWindow = trash.TrashFrame(self, datasets, annotationpath, gene)
            viewWindow.Show()
        elif not datasets:
            transit_tools.ShowError("Error: No datasets selected.")
            return
        else:
            transit_tools.ShowError("Error: No annotation file selected.")
            return





    def ctrlViewFunc(self, event, gene=""):
        annotationpath = self.annotation
        datasets = self.ctrlSelected()
        if datasets and annotationpath:
            if self.verbose:
                transit_tools.transit_message("Visualizing counts for: %s" % ", ".join([transit_tools.fetch_name(d) for d in datasets]))
            viewWindow = trash.TrashFrame(self, datasets, annotationpath, gene)
            viewWindow.Show()
        elif not datasets:
            if self.verbose:
                transit_tools.transit_message("No datasets selected to visualize!")
        else:
            if self.verbose:
                transit_tools.transit_message("No annotation file selected")



    def expViewFunc(self, event, gene=""):
        annotationpath = self.annotation
        datasets = self.expSelected()
        if datasets and annotationpath:
            if self.verbose:
                transit_tools.transit_message("Visualizing counts for: %s" % ", ".join([transit_tools.fetch_name(d) for d in datasets]))
            viewWindow = trash.TrashFrame(self, datasets, annotationpath, gene)
            viewWindow.Show()
        elif not datasets:
            if self.verbose:
                transit_tools.transit_message("No datasets selected to visualize!")
        else:
            if self.verbose:
                transit_tools.transit_message("No annotation file selected")



    def scatterFunc(self, event):
        """ """
        #annotationpath = self.annotation
        datasets = self.ctrlSelected() + self.expSelected()
        if len(datasets) == 2:
            if self.verbose:
                transit_tools.transit_message("Showing scatter plot for: %s" % ", ".join([transit_tools.fetch_name(d) for d in datasets]))
            (data, position) = tnseq_tools.get_data(datasets)
            X = data[0,:]
            Y = data[1,:]

            plt.plot(X,Y, "bo")
            plt.title('Scatter plot - Reads at TA sites')
            plt.xlabel(transit_tools.fetch_name(datasets[0]))
            plt.ylabel(transit_tools.fetch_name(datasets[1])) 
            plt.show()
        else:
            transit_tools.ShowError(MSG="Please make sure only two datasets are selected (across control and experimental datasets).")


    def qcFunc(self, event):
        datasets = self.allSelected()
        nfiles = len(datasets)

        if nfiles == 0:
            transit_tools.transit_message("You must select atleast one dataset control or experimental dataset.")
            transit_tools.ShowError(MSG="You must select atleast one dataset control or experimental dataset.")
            
        elif nfiles >= 1:
            transit_tools.transit_message("Displaying results: %s" % datasets[0])
            try:
                qcWindow = qcDisplay.qcFrame(self, datasets)
                qcWindow.Show()
            except Exception as e:
                transit_tools.transit_message("Error occured displaying file: %s" % str(e))
                traceback.print_exc()


    def aboutFunc(self, event):
        description = """TRANSIT is a tool for analysing TnSeq data. It provides an easy to use graphical interface and access to several different analysis methods that allow the user to determine essentiality within a single condition as well as between two conditions.


If you need to cite this tool, please use the following reference:

DeJesus, M.A., Ambadipudi, C., Baker, R., Sassetti, C., and Ioerger, T.R. (2015). TRANSIT - a Software Tool for Himar1 TnSeq Analysis. PLOS Computational Biology, 11(10):e1004401


"""


        licence = """
TRANSIT is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.


TRANSIT is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with TRANSIT.  If not, see <http://www.gnu.org/licenses/>.
        """



        info = wx.AboutDialogInfo()
        #info.SetIcon(wx.Icon('hunter.png', wx.BITMAP_TYPE_PNG))
        info.SetName('TRANSIT')
        info.SetVersion(pytransit.__version__)
        info.SetDescription(description)
        info.SetCopyright('(C) 2015 - 2016\n Michael A. DeJesus\nThomas R. Ioerger')
        info.SetWebSite('http://saclab.tamu.edu/essentiality/transit/')
        info.SetLicence(licence)
        info.AddDeveloper('Michael A. DeJesus')
        info.AddDeveloper('Thomas R. Ioerger')
        info.AddDeveloper('Chaitra Ambadipudi')
        info.AddDeveloper('Richard Baker')
        info.AddDeveloper('Christopher Sassetti')
        info.AddDeveloper('Eric Nelson')
        #info.AddDocWriter('Jan Bodnar')
        #info.AddArtist('The Tango crew')
        #info.AddTranslator('Jan Bodnar')
        wx.AboutBox(info)





    def documentationFunc(self, event):

        filepath = "http://saclab.tamu.edu/essentiality/transit/transit.html"
        output = ""
        error = ""
        try:
            if sys.platform.startswith('darwin'):
                OS = "OSX"
                #subprocess.call(('open', filepath))
                args = ["open", filepath]
                output,error = subprocess.Popen(args,stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
            elif os.name == 'nt':
                OS = "Windows"
                os.startfile(filepath)
            elif os.name == 'posix':
                OS = "Linux"
                args = ["xdg-open", filepath]
                output,error = subprocess.Popen(args,stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
                if "not found" in error:
                    args = ["exo-open", filepath]
                    output,error = subprocess.Popen(args,stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()

        except Exception as e:
            error_text = """Error occurred opening documentation URL.\nYour browser or OS may not be configured correctly."""
            transit_tools.ShowError(MSG=error_text)
            traceback.print_exc()



    def annotationFileFunc(self, event):

        wc = u"Prot Table (*.prot_table)|*.prot_table;|\nProt Table (*.txt)|*.txt;|\nProt Table (*.dat)|*.dat;|\nAll files (*.*)|*.*" 
        self.annotation = self.OpenFile(DIR=self.workdir, FILE="", WC=wc)
        if self.annotation:
            self.annotationFilePicker.SetLabel(transit_tools.basename(self.annotation))
            if self.verbose:
                transit_tools.transit_message("Annotation File Selected: %s" % self.annotation)
        else:
            self.annotationFilePicker.SetLabel("[Click to add Annotation File (.prot_table)]")
        
    def MethodSelectFunc(self, selected_name, test=""):
        #X = self.methodChoice.GetCurrentSelection()
        #selected_name = self.methodChoice.GetString(X)
    
        #If empty is selected
        if selected_name == "[Choose Method]":
            self.HideAllOptions()
            self.methodInfoText.SetLabel(u"Instructions")
            self.methodInstructions.Show()
            self.methodInstructions.SetLabel(self.instructions_text)
            self.methodInstructions.Wrap(method_wrap_width)
            self.methodShortText.Hide()
            self.methodLongText.Hide()
            self.methodTnText.Hide()
            self.methodDescText.Hide()

            self.method_choice = ""
        else:
            self.ShowGlobalOptions()
            self.methodSizerText.Show()
            #Show Selected Method and hide Others
            for name in methods:
                methods[name].gui.Hide()
                if methods[name].fullname() == selected_name:
                    self.methodInfoText.SetLabel("%s" % methods[name].short_name)
                    
                    #self.methodShortText.SetLabel("[%s]" % methods[name].short_name)
                    #self.methodShortText.Wrap(250)
                    #self.methodLongText.SetLabel(methods[name].long_name)
                    #self.methodLongText.Wrap(250)

                    self.methodTnText.SetLabel(methods[name].getTransposonsText())
                    self.methodTnText.Wrap(250)
                    self.methodTnText.Show()

                    self.methodDescText.SetLabel(methods[name].getDescriptionText())
                    self.methodDescText.Wrap(250)
                    self.methodDescText.Show()
                    self.methodInstructions.SetLabel("")
                    methods[name].gui.Show()
                    self.statusBar.SetStatusText("[%s]" % methods[name].short_name)
                else:
                    methods[name].gui.Hide()
            self.ShowProgressSection()
            self.method_choice = selected_name

        self.Layout()
        if self.verbose:
            transit_tools.transit_message("Selected Method: %s" % (selected_name))




    def displayFileFunc(self, event):
        next = self.list_files.GetNextSelected(-1)
        if next > -1:
            dataset = self.list_files.GetItem(next, 3).GetText()
            if self.verbose:
                transit_tools.transit_message("Displaying results: %s" % self.list_files.GetItem(next, 0).GetText())

            try:
                #fileWindow = fileDisplay.FileFrame(self, dataset, self.list_files.GetItem(next, 1).GetText())
                fileWindow = fileDisplay.TransitGridFrame(self, dataset)
                fileWindow.Show()
            except Exception as e:
                transit_tools.transit_message("Error occurred displaying file: %s" % str(e))
                traceback.print_exc()

        else:
            if self.verbose:
                transit_tools.transit_message("No results selected to display!")
        

    def fileSelected(self,event):
        next = self.list_files.GetNextSelected(-1)
        if next > -1:
            dataset_path = self.list_files.GetItem(next, 3).GetText()
            dataset_name = self.list_files.GetItem(next, 0).GetText()
            dataset_type = self.list_files.GetItem(next, 1).GetText()
            self.updateGraphChoices(dataset_type)
        else:
            pass
        


    def updateGraphChoices(self, dataset_type):

        empty_action = "[Choose Action]"
        if dataset_type == "Gumbel":
            choices = [empty_action, "Plot Ranked Probability of Essentiality"]
        elif dataset_type == "Binomial":
            choices = [empty_action, "Plot Ranked Probability of Essentiality"]
        elif dataset_type == "HMM - Sites":
            choices = [empty_action]
        elif dataset_type == "HMM - Genes":
            choices = [empty_action]
        elif dataset_type == "Resampling":
            choices = [empty_action, "Create a Volcano Plot", "Plot Histogram of logFC of Gene Counts"]
        elif dataset_type == "DE-HMM - Sites":
            choices = [empty_action, "Recreate Sites File"]
        elif dataset_type == "DE-HMM - Segments":
            choices = [empty_action]
        else:
           choices = [empty_action] 

        self.fileActionChoice.SetItems(choices)
        self.fileActionChoice.SetSelection(0)


    def fileActionFunc(self, event):
        # 0 - nothing
        # 1 - Volcano
        # 2 - Hist gene counts ratio
        
        plot_choice  = self.fileActionChoice.GetCurrentSelection()
        plot_name = self.fileActionChoice.GetString(plot_choice)
        if plot_name == "[Choose Action]":
                return
        next = self.list_files.GetNextSelected(-1)
        if next > -1:
            dataset_path = self.list_files.GetItem(next, 3).GetText()
            dataset_name = self.list_files.GetItem(next, 0).GetText()
            dataset_type = self.list_files.GetItem(next, 1).GetText()
            
            if self.verbose:
                transit_tools.transit_message("Performing the '%s' action on dataset '%s'" % (plot_name, dataset_name))

            if plot_name == "Create a Volcano Plot":
                self.graphVolcanoPlot(dataset_name, dataset_type, dataset_path)
            elif plot_name == "Plot Histogram of logFC of Gene Counts":
                self.graphGeneCounts(dataset_name, dataset_type, dataset_path)
            elif plot_name == "Plot Ranked Probability of Essentiality":
                self.graphRankedZbar(dataset_name, dataset_type, dataset_path)
            else:
                return

            self.fileActionChoice.SetSelection(0)
            
        else:
            transit_tools.ShowError(MSG="Please select a results file to plot!")
    
       

 


    def graphGeneCounts(self, dataset_name, dataset_type, dataset_path):
        try:
            if dataset_type == "Resampling":
                X = []
                for line in open(dataset_path):
                    if line.startswith("#"): continue
                    tmp = line.strip().split("\t")
                    try:
                        log2FC = float(tmp[7])
                    except:
                        log2FC = 0
                    X.append(log2FC)

                n, bins, patches = plt.hist(X, normed=1, facecolor='c', alpha=0.75, bins=100)
                plt.xlabel('log2 FC - Total Gene Counts')
                plt.ylabel('Probability')
                plt.title('Histogram of log2 Fold Change for Total Normalized Counts within Genes')
                plt.axvline(0, color='r', linestyle='dashed', linewidth=3)
                plt.grid(True)
                plt.show()
                plt.close()
            else:
               transit_tools.ShowError(MSG="Need to select a 'Resampling' results file for this type of plot.")

        except Exception as e:
            transit_tools.transit_message("Error occurred creating plot: %s" % str(e))
            traceback.print_exc()





    def graphVolcanoPlot(self, dataset_name, dataset_type, dataset_path):
        try:
            if dataset_type == "Resampling":
                X = []; Y = [];
                for line in open(dataset_path):
                    if line.startswith("#"): continue
                    tmp = line.strip().split("\t")
                    try:
                        #log2FC = math.log(float(tmp[6])/float(tmp[5]),2)
                        log2FC = float(tmp[7])
                        log10qval = -math.log(float(tmp[-1].strip()), 10)
                    except:
                        log2FC = 0
                        log10qval = 0
                        #log2FC = 1
                        #log10qval = 1
                    X.append(log2FC)
                    Y.append(log10qval)

                plt.plot(X,Y, "bo")
                plt.xlabel("Log Fold Change (base 2)")
                plt.ylabel("-Log q-value (base 10)")
                plt.title("Resampling - Volcano plot")
                plt.show()
                plt.close()
            else:
               transit_tools.ShowError(MSG="Need to select a 'Resampling' results file for this type of plot.")
            
        except Exception as e:
            print "Error occurred creating plot:", str(e)
        

    def graphRankedZbar(self, dataset_name, dataset_type, dataset_path):
        try:
            X = []; Y = [];
            for line in open(dataset_path):
                if line.startswith("#"): continue
                tmp = line.strip().split("\t")
                try:
                    #log2FC = math.log(float(tmp[6])/float(tmp[5]),2)
                    zbar = float(tmp[-2])
                except:
                    zbar = 0
                if zbar >= 0:
                    Y.append(zbar)

            Y.sort()
            index=range(1,len(Y)+1)
            plt.plot(index,Y, "bo")
            plt.xlabel("Rank of Gene According to Probability of Essentiality")
            plt.ylabel("Probability of Essentiality")
            plt.title("Ranked Probability of Essentiality")
            plt.show()
            plt.close()

        except Exception as e:
            print "Error occurred creating plot:", str(e)




    def LoessPrevFunc(self,event):
        datasets_selected = self.ctrlSelected() + self.expSelected()
        if not datasets_selected:
            transit_tools.ShowError(MSG="Need to select at least one control or experimental dataset.")
            return

        data, position = tnseq_tools.get_data(datasets_selected)
        (K,N) = data.shape
        window = 100
        for j in range(K):

            size = len(position)/window + 1
            x_w = numpy.zeros(size)
            y_w = numpy.zeros(size)
            for i in range(size):
                x_w[i] = window*i
                y_w[i] = sum(data[j][window*i:window*(i+1)])

            y_smooth = stat_tools.loess(x_w, y_w, h=10000)
            plt.plot(x_w, y_w, "g+")
            plt.plot(x_w, y_smooth, "b-")
            plt.xlabel("Genomic Position")
            plt.ylabel("Reads per 100 insertion sites")

            plt.title("LOESS Fit - %s" % transit_tools.basename(datasets_selected[j]) )
            plt.show()
            plt.close()
    

    def addFileFunc(self, event):

        try:
            dlg = wx.FileDialog(
                self, message="Choose a file",
                defaultDir=self.workdir,
                defaultFile="",
                wildcard=u"Results Files (*.dat)|*.dat;|\nResults Files (*.txt)|*.txt;|\nAll files (*.*)|*.*",
                style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
                )
            if dlg.ShowModal() == wx.ID_OK:
                paths = dlg.GetPaths()
                print "You chose the following Results file(s):"
                for fullpath in paths:
                    print "\t%s" % fullpath
                    name = transit_tools.basename(fullpath)
                    line = open(fullpath).readline()
                    if line.startswith("#Gumbel"):
                        type = "Gumbel"
                    elif line.startswith("#Binomial"):
                        type = "Binomial"
                    elif line.startswith("#HMM - Sites"):
                        type = "HMM - Sites"
                    elif line.startswith("#HMM - Genes"):
                        type = "HMM - Genes"
                    elif line.startswith("#Resampling"):
                        type = "Resampling"
                    elif line.startswith("#DE-HMM - Sites"):
                        type = "DE-HMM - Sites"
                    elif line.startswith("#DE-HMM - Segments"):
                        type = "DE-HMM - Segments"
                    else:
                        type = "Unknown"
                    data = {"path":fullpath, "type":type, "date": datetime.datetime.today().strftime("%B %d, %Y %I:%M%p")}
                    if newWx:
                        wx.CallAfter(pub.sendMessage, "file", data=data)
                    else:
                        wx.CallAfter(pub.sendMessage, "file", data)
            dlg.Destroy()
        except Exception as e:
            transit_tools.transit_message("Error: %s" %  e)
            print "PATH", fullpath
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)



    def choseMethodsMenu(self, selected_name, event):
        if self.verbose:
            transit_tools.transit_message("Selected Method: %s" % (selected_name))
        self.MethodSelectFunc(selected_name) 


    def convertToIGVGUI(self, datasets):
        annotationPath = self.annotation
        if datasets and annotationPath:
            defaultFile = "read_counts.igv"
            defaultDir = os.getcwd()
            outputPath = self.SaveFile(defaultDir, defaultFile)
            if not outputPath:
                return
            if self.verbose:
        
                transit_tools.transit_message("Converting the following datasets to IGV format: %s" % ", ".join([transit_tools.fetch_name(d) for d in datasets]))
            self.convertToIGV(datasets, annotationPath, outputPath)
            if self.verbose:
                transit_tools.transit_message("Finished conversion")
        elif not datasets:
            transit_tools.ShowError("Error: No datasets selected to convert!")
        elif not annotationPath:
            transit_tools.ShowError("Error: No annotation file selected.")
        else:
            pass


    def convertToIGV(self, dataset_list, annotationPath, path):

        normchoice = self.chooseNormalization()

        if not normchoice:
            normchoice = "nonorm"

        (fulldata, position) = tnseq_tools.get_data(dataset_list)
        (fulldata, factors) = norm_tools.normalize_data(fulldata, normchoice, dataset_list, annotationPath)
        position = position.astype(int)

        output = open(path, "w")
        output.write("#Converted to IGV with TRANSIT.\n")
        if normchoice != "nonorm":
            output.write("#Reads normalized using '%s'\n" % normchoice)
    
        output.write("#Files:\n#%s\n" % "\n#".join(dataset_list))
        output.write("#Chromosome\tStart\tEnd\tFeature\t%s\tTAs\n" % ("\t".join([transit_tools.fetch_name(D) for D in dataset_list])))
        chrom = transit_tools.fetch_name(annotationPath)

        for i,pos in enumerate(position):
            output.write("%s\t%s\t%s\tTA%s\t%s\t1\n" % (chrom, position[i], position[i]+1, position[i], "\t".join(["%1.1f" % fulldata[j][i] for j in range(len(fulldata))])))
        output.close()



    def convertToCombinedWigGUI(self, datasets):
        annotationPath = self.annotation
        if datasets and annotationPath:
            defaultFile = "combined_read_counts.txt"
            defaultDir = os.getcwd()
            outputPath = self.SaveFile(defaultDir, defaultFile)
            if not outputPath:
                return
            if self.verbose:
                transit_tools.transit_message("Converting the following datasets to Combined Wig format: %s" % ", ".join([transit_tools.fetch_name(d) for d in datasets]))
            self.convertToCombinedWig(datasets, annotationPath, outputPath)
            if self.verbose:
                transit_tools.transit_message("Finished conversion")
        elif not datasets:
            transit_tools.ShowError("Error: No datasets selected to convert!")
        elif not annotationPath:
            transit_tools.ShowError("Error: No annotation file selected.")
        else:
            pass

    

    def convertToCombinedWig(self, dataset_list, annotationPath, path):
        normchoice = self.chooseNormalization()

        if not normchoice:
            normchoice = "nonorm"

        (fulldata, position) = tnseq_tools.get_data(dataset_list)
        (fulldata, factors) = norm_tools.normalize_data(fulldata, normchoice, dataset_list, annotationPath)
        position = position.astype(int)


        hash = tnseq_tools.get_pos_hash(annotationPath)
        rv2info = tnseq_tools.get_gene_info(annotationPath)

        output = open(path, "w")
        output.write("#Converted to CombinedWig with TRANSIT.\n")
        if normchoice != "nonorm":
            output.write("#Reads normalized using '%s'\n" % normchoice)

        (K,N) = fulldata.shape
        output.write("#Files:\n")
        for f in dataset_list:
            output.write("#%s\n" % f)

        for i,pos in enumerate(position):
            #output.write("%s\t%s\t%s\n" % (position[i], "\t".join(["%1.1f" % fulldata[j][i] for j in range(K)]), ",".join(["%s (%s)" % (orf,rv2info.get(orf,["-"])[0]) for orf in hash.get(position[i], [])]) )  )

            output.write("%-10d %s  %s\n" % (position[i], "".join(["%7.1f" % c for c in fulldata[:,i]]),",".join(["%s (%s)" % (orf,rv2info.get(orf,["-"])[0]) for orf in hash.get(position[i], [])])   ))


        output.close()
    


    def chooseNormalization(self):

        dlg = wx.SingleChoiceDialog(
                self, "Choose how to normalize read-counts accross datasets.", 'Normalization Choice',
                ["nonorm", "nzmean", "totreads", "TTR", "zinfnb", "quantile", "betageom", "aBGC", "emphist"], 
                wx.CHOICEDLG_STYLE
                )
 
        if dlg.ShowModal() == wx.ID_OK:
            transit_tools.transit_message("Selected the '%s' normalization method" % dlg.GetStringSelection())
 
        dlg.Destroy()
        return dlg.GetStringSelection()


    def selectedToIGV(self, event):
        datasets = self.ctrlSelected() + self.expSelected()
        self.convertToIGVGUI(datasets)


    def selectedToCombinedWig(self, event):
        datasets = self.ctrlSelected() + self.expSelected()
        self.convertToCombinedWigGUI(datasets)

        
    def annotationPT_to_GFF3(self, event):
        annotationpath = self.annotation
        defaultFile = transit_tools.fetch_name(annotationpath) + ".gff3"
        #defaultDir = os.path.dirname(os.path.realpath(__file__))
        defaultDir = os.getcwd()
        outputPath = self.SaveFile(defaultDir, defaultFile)

        ORGANISM = transit_tools.fetch_name(annotationpath)
        if not annotationpath:
            transit_tools.ShowError("Error: No annotation file selected.")

        elif outputPath:
            if self.verbose:
                transit_tools.transit_message("Converting annotation file from prot_table format to GFF3 format")
            year = time.localtime().tm_year
            month = time.localtime().tm_mon
            day = time.localtime().tm_mday
            
            output = open(outputPath, "w")
            output.write("##gff-version 3\n")
            output.write("##converted to IGV with TRANSIT.\n")
            output.write("##date %d-%d-%d\n" % (year, month, day))
            output.write("##Type DNA %s\n" % ORGANISM)
            
            for line in open(annotationpath):
                if line.startswith("#"): continue
                tmp = line.strip().split("\t")
                desc = tmp[0]; start = int(tmp[1]); end = int(tmp[2]); strand = tmp[3];
                length = tmp[4]; name = tmp[7]; orf = tmp[8];
                ID = name
                desc.replace("%", "%25").replace(";", "%3B").replace("=","%3D").replace(",","%2C")
                output.write("%s\tRefSeq\tgene\t%d\t%d\t.\t%s\t.\tID=%s;Name=%s;Alias=%s;locus_tag=%s;desc=%s\n" % (ORGANISM, start, end, strand, orf,ID, orf, orf,desc))
                
            output.close()
            if self.verbose:
                transit_tools.transit_message("Finished conversion")
       



    def annotationPT_to_PTT(self, event):
 
        annotationpath = self.annotation
        defaultFile = transit_tools.fetch_name(annotationpath) + ".ptt.table"
        #defaultDir = os.path.dirname(os.path.realpath(__file__))
        defaultDir = os.getcwd()

        datasets = self.ctrlSelected() + self.expSelected()
        if not annotationpath:
            transit_tools.ShowError("Error: No annotation file selected.")
        elif not datasets:
            transit_tools.ShowError("Error: Please add a .wig dataset, to determine TA sites.")            
        else:
            
            outputPath = self.SaveFile(defaultDir, defaultFile)
            if not outputPath: return
            if self.verbose:
                transit_tools.transit_message("Converting annotation file from prot_table format to PTT format")
            (data, position) = tnseq_tools.get_data(datasets)
            orf2info = tnseq_tools.get_gene_info(annotationpath)
            hash = tnseq_tools.get_pos_hash(annotationpath)
            (orf2reads, orf2pos) = tnseq_tools.get_gene_reads(hash, data, position, orf2info)

            output = open(outputPath, "w")
            output.write("geneID\tstart\tend\tstrand\tTA coordinates\n")
            for line in open(annotationpath):
                if line.startswith("#"): continue
                tmp = line.strip().split("\t")
                orf = tmp[8]
                name = tmp[7]
                desc = tmp[0]
                start = int(tmp[1])
                end = int(tmp[2])
                strand = tmp[3]
                ta_str = "no TAs"
                if orf in orf2pos: ta_str = "\t".join([str(int(ta)) for ta in orf2pos[orf]])
                output.write("%s\t%s\t%s\t%s\t%s\n" % (orf, start, end, strand, ta_str))
            output.close()
            if self.verbose:
                transit_tools.transit_message("Finished conversion")
                


    def annotationPTT_to_PT(self, event):

        annotationpath = self.annotation
        defaultFile = transit_tools.fetch_name(annotationpath) + ".prot_table"
        #defaultDir = os.path.dirname(os.path.realpath(__file__))
        defaultDir = os.getcwd()
        
        datasets = self.ctrlSelected() + self.expSelected()
        if not annotationpath:
            transit_tools.ShowError("Error: No annotation file selected.")
        #elif not datasets:
        #    transit_tools.ShowError("Error: Please add a .wig dataset, to determine TA sites.")
        else:

            outputPath = self.SaveFile(defaultDir, defaultFile)
            if not outputPath: return
            if self.verbose:
                transit_tools.transit_message("Converting annotation file from PTT format to prot_table format")
            #(data, position) = tnseq_tools.get_data(datasets)
            #orf2info = tnseq_tools.get_gene_info(annotationpath)
            #hash = tnseq_tools.get_pos_hash(annotationpath)
            #(orf2reads, orf2pos) = tnseq_tools.get_gene_reads(hash, data, position, orf2info)
            
            
            output = open(outputPath, "w")
            #output.write("geneID\tstart\tend\tstrand\tTA coordinates\n")
            for line in open(annotationpath):
                if line.startswith("#"): continue
                if line.startswith("geneID"): continue
                tmp = line.strip().split("\t")
                orf = tmp[0]
                if orf == "intergenic": continue
                name = "-"
                desc = "-"
                start = int(tmp[1])
                end = int(tmp[2])
                length = ((end-start+1)/3)-1
                strand = tmp[3]
                someID = "-"
                someID2 = "-"
                COG = "-"
                output.write("%s\t%d\t%d\t%s\t%d\t%s\t%s\t%s\t%s\t%s\n" % (desc, start, end, strand, length, someID, someID2, name, orf, COG))
            output.close()
            if self.verbose:
                transit_tools.transit_message("Finished conversion")

        #geneID  start   end strand  TA coordinates
        


    def annotationGFF3_to_PT(self, event):

        annotationpath = self.annotation
        defaultFile = transit_tools.fetch_name(annotationpath) + ".prot_table"
        #defaultDir = os.path.dirname(os.path.realpath(__file__))
        defaultDir = os.getcwd()

        datasets = self.ctrlSelected() + self.expSelected()
        if not annotationpath:
            transit_tools.ShowError("Error: No annotation file selected.")
        else:
            outputPath = self.SaveFile(defaultDir, defaultFile)
            if not outputPath: return
            if self.verbose:
                transit_tools.transit_message("Converting annotation file from GFF3 format to prot_table format")

            output = open(outputPath, "w")
            for line in open(annotationpath):
                if line.startswith("#"): continue
                tmp = line.strip().split("\t")
                chr = tmp[0]
                type = tmp[2]
                start = int(tmp[3])
                end = int(tmp[4])
                length = ((end-start+1)/3)-1
                strand = tmp[6]
                features = dict([tuple(f.split("=")) for f in tmp[8].split(";")])
                if "ID" not in features: continue
                orf = features["ID"]
                name = features.get("Name", "-")
                if name == "-": name = features.get("name", "-")
                
                desc = features.get("Description", "-")
                if desc == "-": desc = features.get("description", "-")
                if desc == "-": desc = features.get("Desc", "-")
                if desc == "-": desc = features.get("desc", "-")

                someID = "-"
                someID2 = "-"
                COG = "-"
                output.write("%s\t%d\t%d\t%s\t%d\t%s\t%s\t%s\t%s\t%s\n" % (desc, start, end, strand, length, someID, someID2, name, orf, COG))
            output.close()
            if self.verbose:
                transit_tools.transit_message("Finished conversion")

                 

    def RunMethod(self, event):
        #FLORF
        #X = self.methodChoice.GetCurrentSelection()
        #selected_name = self.methodChoice.GetString(X)
        selected_name = self.method_choice
        for name in methods:
            if  methods[name].fullname() == selected_name:
                methodobj = methods[name].method
        try:
            M = methodobj.fromGUI(self)
            if M: 
                thread = threading.Thread(target=M.Run())
                thread.setDaemon(True)
                thread.start()
        except Exception as e:
            transit_tools.transit_message("Error: %s" % str(e))
            traceback.print_exc()


