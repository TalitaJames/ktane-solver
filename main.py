import interface
import sys

if __name__ == "__main__":
    window = interface.Window()
    window.main_window.show()
    sys.exit(window.app.exec())


