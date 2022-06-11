#!/usr/bin/env python3
import sys
import json
import csv
from outscraper import ApiClient
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QInputDialog

API_KEY = 'Z29vZ2xlLW9hdXRoMnwxMTc0MDk1OTAxOTcxMjgxNjQ1ODN8NjJhMGFhMWJkMg'

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        
        self.setWindowTitle('CLASSPLUS Scrapper')
        width = 500
          
        # setting  the fixed width of window
        self.setFixedWidth(width)
        self.setCentralWidget(QLabel("FILE DOWNLOADED SUCCESSFULLY !!"))
        
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        self.take_input()
        
    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Please Check Current Directory")
        self.setStatusBar(status)

    def search(self,q, n):
        api_client = ApiClient(api_key=API_KEY)


        result = api_client.google_maps_search_v2(q, limit=n, language='en')


        jtopy = json.dumps(result)


        dict_json=json.loads(jtopy)[0]

        return dict_json


    def save_to_file(self,dict_json, file_name):

        header = ['name', 'full_address', 'phone', 'site', 'rating']

        data = []

        for dict in dict_json:
            data.append([dict['name'], dict['full_address'], dict['phone'], dict['site'], dict['rating']])

    
        with open(file_name, 'w', encoding='UTF8', newline='') as f:
           writer = csv.writer(f)

        # write the header
           writer.writerow(header)

        # write multiple rows
           writer.writerows(data)

        print("csv file created") 
           
    def scriptCall(self,searchText,record,output):
        data = self.search(searchText,record)
        output=output+'.csv'
        self.save_to_file(data, output)
        print("succefully completed")    

    def take_input(self):
        searchText, done1=QInputDialog.getText(self,'SCRAPPER CLASSPLUS', 'Enter your searchText:')
        record, done2=QInputDialog.getText(self,'SCRAPPER CLASSPLUS', 'Enter the numbe of record:')
        outputFile, done3=QInputDialog.getText(self,'SCRAPPER CLASSPLUS', 'Enter Output file name(without .cvs):')
        
        if done1 and done2 and done3:
            self.scriptCall(str(searchText),record,outputFile)   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())