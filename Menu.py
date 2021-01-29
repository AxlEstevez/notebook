#!/usr/bin/python3
#-*- coding: utf-8 -*

import sys
from Notebook import Notebook
from Note import Note

class Menu(object):
    """ Display a command Line Interface (CLI) """
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }
    
    def display_menu(self):
        print("""
        [ Notebook Menu ]
        1. Show All Aotes 
        2. Search Notes
        3. Add Note
        4. Modify Notes
        5. Quit
        """)
    
    def run(self):
        """ Display the menu and respond to choise. """
        choice = ""
        while True:
            self.display_menu()
            choice = input("Enter option >> ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not valid choice")
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id}: {note.id}\n{note.memo}")
    
    def search_notes(self):
        filter_input = input("Search for >> ")
        notes = self.notebook.search(filter_input)
        self.show_notes(notes)
    
    def add_note(self):
        memo = input("Enter memo >> ")
        self.notebook.new_note(memo)
        print("Your note has been addend")
    
    def modify_note(self):
        id_note = input("Enter a note id >> ")
        memo = input("Enter a memo >> ")
        tags = input("Enter tags >>")
        if memo:
            self.notebook.modify_memo(id_note, memo)
        if tags:
            self.notebook.modify_tags(id_note, tags)
    
    def quit(self):
        print("Thank you for using you notebook today")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
