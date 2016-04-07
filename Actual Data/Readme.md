#Personality Visualization

## PersonalityOperations.py
This python script is responsible for cleaning, processing and crunching the data from the above 4 data sources into customized JSON files for personality visualizations. Many intermediary files are generated in various functions and are saved. Each of the functions, their input & outut formats are listed below. 

 - **readfile()** : Open and read "gfg_users_states.csv", "gfg_personality_survey_responses.csv", "gfg_users_gender_age_state.csv".
 - **writeFile()**: Create and write to files "user_dict.txt", "final.json", "amcharts.json", "openness.json".
 - **readintoList()**: Read the opened files into respective lists.
 - **closeFile()**: Close all the files currently open.
 - **reverse()**: Compute the reverse score. 
 - **combineUserDataAndResponses()**: This is a very crucial and dense function-
     - loops through the "gfg_users_states.csv" file, "gfg_personality_survey_responses.csv" file and merges into a specific format. 
     - computes the O,C,E,A,N values(formulae below) and create *userDict* dictionary
     - checks for inconsistent data & sets the *corrupt* flag if needed
     - loops through ""gfg_users_gender_age_state.csv" and cleans it. Merges it with *userDict*.
     - ```userDict = { gfgid1 :{state: "AB", corrupt: 0, gender: "1/0", age-range: "40", 1:2, 2:2, 3:5 .... 44:1, O:_ , C:_, E:_, A:_, N:_}, gfgid2:{}, gfgid3: {}.... }```
     - *userDict* dictionary is dumped into **user_dict.txt**
 - **cleanDict()**: Returns a list of all gfgid's with *corrupt*=1
 - **relevantDict()**: Returns the *stateDict* which is a condensed version of *userDict*. It is in the following format-
     - ```stateDict = { gfgid1 :{state: "AB", corrupt: 0, gender: "1/0", age-range: "40",O:_ , C:_, E:_, A:_, N:_}, gfgid2:{}, gfgid3: {}.... }```
 - **crunchStateDict()**: This function crunches the *stateDict* data into more JSON-specific format imperative to visualizations. 
    - ```statewiseDict = { 'state':{'O':[3], 'C':[5], 'E':[6], 'A':[7], 'N':[2]'}, 'state2':{}, 'state3:{}.... }```
 - **usJSON()**: Convert *statewiseDict* into JSON format as required by the US Map API. 
    - ```openString = [{"openness": 3.86, "state": "WA", "fillKey": "LOW"}, {"openness": 3.94, "state": "VA", "fillKey": "LOW"}...]```
    - dumped into **openness.json**
 - **amchartJSON()**: Convert *statewiseDict* into JSON format as required by the AmCHarts API. 
    - ```{ "WA": {"A": "3.72", "C": "3.62", "E": "2.94", "O": "3.86", "N": "3.19"}, "VA": {"A": "3.76", "C": "3.74", "E": "2.93", "O": "3.94", "N": "3.16"},..........} ``` 
    - dumped into **final.json**

##Formulae for Personality
Computing simple BFI Scale Scores-
*R* - Reverse Score: Reverse scoring means that the numerical scoring scale runs in the opposite direction. So, in the above example strongly disagree would attract a score of 5, disagree would be 4, neutral still equals 3, agree becomes 2 and strongly agree = 1.

####Compute Reverse Score for-
- Extraversion: 6, 21, 31
- Agreeableness: 2, 12, 27, 37
- Conscientiousness: 8, 18, 23, 43
- Neuroticism: 9, 24, 34
- Openness: 35, 41

####Compute Average of-
- **Extraversion**: 1, 6R, 11, 16, 21R, 26, 31R, 36
- **Agreeableness**: 2R, 7, 12R, 17, 22, 27R, 32, 37R, 42
- **Conscientiousness**: 3, 8R, 13, 18R, 23R, 28, 33, 38, 43R
- **Neuroticism**: 4, 9R, 14, 19, 24R, 29, 34R, 39
- **Openness**: 5, 10, 15, 20, 25, 30, 35R, 40, 41R, 44 

## Data Sources - 
####File 1 - gfg_personality_survey_response.csv
gfgid, question#, "Answer"

#####Scoring
1. Disagree strongly
2. Disagree a little
3. Neither agree, nor disagree
4. Agree a little
5. Agree strongly

####File 2 - gfg_personality_survey_questions.csv
question#, "question"

####File 3 - gfg_users_states.csv
gfgid, state

####File 4 - gfg_users_gender_age_state.csv
gfgid, gender, age_range, state


