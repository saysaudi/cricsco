from actions.excel_action import ExcelAction
from actions.ui_action import UIAction
from locators import Locators

class IPLScorecard:
    def __init__(self):
        excel_action = ExcelAction()
        ui_action = UIAction(Locators.url)

        # excel_action.create_sheets()    
        ui_action.open_web_page()

if __name__ == '__main__':
    IPLScorecard()

