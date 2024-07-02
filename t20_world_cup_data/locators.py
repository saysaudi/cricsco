class Locators:
    # url = "https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/kolkata-knight-riders-vs-sunrisers-hyderabad-final-1426312/full-scorecard"
    # url = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/india-vs-south-africa-final-1415755/full-scorecard"
    url = "https://www.espncricinfo.com/series/lanka-premier-league-2024-1421415/kandy-falcons-vs-dambulla-sixers-1st-match-1428459/full-scorecard"

    bowlers_xpath = {
        "first_inns" : {
            "bowling_header" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/thead/tr/th",
            "bowler" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[1]/div/a/span",
            "bowler_over" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[2]",
            "bowler_maiden" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[3]",
            "bowler_run" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[4]",
            "bowler_wicket" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[5]",
            "bowler_econ" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[6]",
            "bowler_0s" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[7]",
            "bowler_4s" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[8]",
            "bowler_6s" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[9]",
            "bowler_wide" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[10]",
            "bowler_nb" : "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[2]/tbody/tr/td[11]"
        },
        "second_inns" : {
            "bowling_header" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/thead/tr/th",
            "bowler" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[1]/div/a/span",
            "bowler_over" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[2]",
            "bowler_maiden" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[3]",
            "bowler_run" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[4]",
            "bowler_wicket" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[5]",
            "bowler_econ" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[6]",
            "bowler_0s" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[7]",
            "bowler_4s" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[8]",
            "bowler_6s" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[9]",
            "bowler_wide" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[10]",
            "bowler_nb" : "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[2]/tbody/tr/td[11]"
        }
    }

    batsmen_xpath = {
        "first_inns": {
            "batting_header": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/thead/tr/th",
            "batsmen": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[1]",
            "status": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[2]",
            "runs": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[3]",
            "played_balls": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[4]",
            "played_mins": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[5]",
            "4s": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[6]",
            "6s": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[7]",
            "sr": "//div[@class='ds-mt-3']/div[1]/div[2]/div/div[2]/table[1]/tbody/tr/td[8]"
        },
        "second_inns": {
            "batting_header": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/thead/tr/th",
            "batsmen": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[1]",
            "status": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[2]",
            "runs": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[3]",
            "played_balls": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[4]",
            "played_mins": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[5]",
            "4s": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[6]",
            "6s": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[7]",
            "sr": "//div[@class='ds-mt-3']/div[1]/div[3]/div/div[2]/table[1]/tbody/tr/td[8]"
        }
    }

    match_details_xpath = {
        "match_details" : "//div[@class='ds-w-full']/div[3]/div[1]/h1",
        "team_a" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a//span",
        "team_a_score" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/strong",
        "team_b" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/a//span",
        "team_b_played_overs_target" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/span",
        "team_b_score" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/strong",
        "match_result" : "//div[@class='ds-w-full']/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div/p/span"
    }

    mvp_xpath = {
        "mvp_header" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/thead/tr/th",
        "mvp_player" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[1]/div/a/span",
        "mvp_team" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[2]",
        "mvp_ti" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[3]",
        "mvp_runs" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[4]",
        "mvp_i_runs" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[5]",
        "mvp_b_impact" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[6]",
        "mvp_bowl" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[7]",
        "mvp_i_wkts" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[8]",
        "mvp_bo_impact" : "//div[@class='ds-w-full']/div[3]/div[1]/div[2]/div/div[2]/div/table/tbody/tr/td[9]"
    }
