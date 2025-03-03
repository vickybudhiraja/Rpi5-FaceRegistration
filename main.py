import sys
import tkinter as tk
from ui.main_window import MainWindow

def main():
    try:
        app = MainWindow()
        app.mainloop()
        
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
