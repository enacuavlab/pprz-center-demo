###############################################################################
# [Imports]

import PyQt5.QtWidgets as Widgets

import ui.set_manager as manager
import ui.main_window as ui


###############################################################################
# [Constants]

MODULE = '[HMI]'


###############################################################################
# [Hmi class]

class Hmi(Widgets.QMainWindow):
    """Class to manage the main window HMI."""
    def __init__(self):
        super(Hmi, self).__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = SettingsManager(self)

        self.ui.actionSetManager.triggered.connect(self.settings.show)


class SettingsManager(Widgets.QDialog):
    """Class to manage the settings manager HMI."""
    def __init__(self, parent):
        super(SettingsManager, self).__init__(parent)
        self.ui = manager.Ui_Dialog()
        self.ui.setupUi(self)
