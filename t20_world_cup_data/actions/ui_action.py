from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from locators import Locators
from actions.excel_action import ExcelAction


class UIAction:
    def __init__(self, url):
        self.url = url
        chromedriver_path = 'C:/Users/SAUDI/Documents/seleniumdrivers/chromedriver.exe'   
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.excel_action = ExcelAction()

    def open_web_page(self):   
        # Open the webpage
        self.driver.get(self.url)
        time.sleep(1)
        self.get_match_details()
        self.driver.quit()


    def get_match_details(self):
        match_details = self.driver.find_element(By.XPATH, Locators.match_details_xpath["match_details"]).text
        team_a = self.driver.find_element(By.XPATH, Locators.match_details_xpath["team_a"]).text
        team_a_score = self.driver.find_element(By.XPATH, Locators.match_details_xpath["team_a_score"]).text
        team_b = self.driver.find_element(By.XPATH, Locators.match_details_xpath["team_b"]).text
        team_b_played_overs_target = self.driver.find_element(By.XPATH, Locators.match_details_xpath["team_b_played_overs_target"]).text
        team_b_score = self.driver.find_element(By.XPATH, Locators.match_details_xpath["team_b_score"]).text
        match_result = self.driver.find_element(By.XPATH, Locators.match_details_xpath["match_result"]).text

        match_details_list = [match_details, team_a, team_a_score, team_b, team_b_played_overs_target, team_b_score, match_result]

        self.excel_action.write_match_details(match_details_list)
        self.get_inns_details() 
        return True

    def get_inns_details(self):
        inns_list = ['first_inns', 'second_inns']
        for inns in inns_list:
            self.inns_details(inns)

    def inns_details(self, inns):
        avoid_char = ['', ' ']
        self.inns = inns
        batting_header = self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['batting_header'])
        batsmen = self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['batsmen'])
        batsmen_status = self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['status'])
        batsmen_runs = self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['runs'])
        batsmen_played_balls = self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['played_balls'])
        batsmen_played_mins = self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['played_mins'])
        batsmen_4s = self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['4s'])
        batsmen_6s = self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['6s'])
        batsmen_sr = self.driver.find_elements(By.XPATH, Locators.batsmen_xpath[inns]['sr'])
        # Initialize lists to hold the data
        batting_header_list = [bat_header.text for bat_header in batting_header if bat_header.text not in avoid_char]
        batsmen_list = [batsman.text for batsman in batsmen if batsman.text not in avoid_char]
        batsmen_status_list = [status.text for status in batsmen_status if status.text not in avoid_char]
        batsmen_runs_list = [runs.text for runs in batsmen_runs if runs.text not in avoid_char]
        batsmen_played_balls_list = [balls.text for balls in batsmen_played_balls if balls.text not in avoid_char]
        batsmen_played_mins_list = [mins.text for mins in batsmen_played_mins if mins.text not in avoid_char]
        batsmen_4s_list = [fours.text for fours in batsmen_4s if fours.text not in avoid_char]
        batsmen_6s_list = [sixes.text for sixes in batsmen_6s if sixes.text not in avoid_char]
        batsmen_sr_list = [sr.text for sr in batsmen_sr if sr.text not in avoid_char]

        bat_stat_list = [batting_header_list, batsmen_list, batsmen_status_list, batsmen_runs_list, batsmen_played_balls_list, batsmen_played_mins_list, batsmen_4s_list, batsmen_6s_list, batsmen_sr_list]

        self.excel_action.write_batting_stats(bat_stat_list)

        bowling_header = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowling_header'])
        bowler = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler'])
        bowler_over = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_over'])
        bowler_maiden = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_maiden'])
        bowler_run = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_run'])
        bowler_wicket = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_wicket'])
        bowler_econ = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_econ'])
        bowler_0s = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_0s'])
        bowler_4s = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_4s'])
        bowler_6s = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_6s'])
        bowler_wide = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_wide'])
        bowler_nb = self.driver.find_elements(By.XPATH, Locators.bowlers_xpath[inns]['bowler_nb'])
        # Initialize lists to hold the data
        bowling_header_list = [bowl_header.text for bowl_header in bowling_header if bowl_header.text!= '']
        bowler_list = [bowl.text for bowl in bowler if bowl.text != '']
        bowler_over_list = [bowl_over.text for bowl_over in bowler_over if bowl_over.text != '']
        bowler_maiden_list = [bowl_maiden.text for bowl_maiden in bowler_maiden if bowl_maiden.text != '']
        bowler_run_list = [bowl_run.text for bowl_run in bowler_run if bowl_run.text != '']
        bowler_wicket_list = [bowl_wicket.text for bowl_wicket in bowler_wicket if bowl_wicket.text != '']
        bowler_econ_list = [bowl_econ.text for bowl_econ in bowler_econ if bowl_econ.text != '']
        bowler_0s_list = [bowl_0s.text for bowl_0s in bowler_0s if bowl_0s.text != '']
        bowler_4s_list = [bowl_4s.text for bowl_4s in bowler_4s if bowl_4s.text != '']
        bowler_6s_list = [bowl_6s.text for bowl_6s in bowler_6s if bowl_6s.text != '']
        bowler_wide_list = [bowl_wide.text for bowl_wide in bowler_wide if bowl_wide.text != '']
        bowler_nb_list = [bowl_nb.text for bowl_nb in bowler_nb if bowl_nb.text != '']

        bowl_stat_list = [bowling_header_list, bowler_list, bowler_over_list, bowler_maiden_list, bowler_run_list, bowler_wicket_list, bowler_econ_list, bowler_0s_list, bowler_4s_list, bowler_6s_list, bowler_wide_list, bowler_nb_list]

        self.excel_action.write_batting_stats(bowl_stat_list)
    