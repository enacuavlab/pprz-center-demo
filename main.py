###############################################################################
# [Imports]

import sys
import PyQt5.QtWidgets as Widgets

import hmi


###############################################################################
# [Main function]
def main():
    """Main program : creates the main window and starts the main loop."""
    app = Widgets.QApplication(sys.argv)
    main_window = hmi.Hmi()
    main_window.show()
    exec_return_code = app.exec_()
    sys.exit(exec_return_code)


if __name__ == "__main__":
    main()

