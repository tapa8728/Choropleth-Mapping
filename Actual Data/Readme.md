
##Formulae for Personality
Computing simple BFI Scale Scores-
R - Reverse Score: Reverse scoring means that the numerical scoring scale runs in the opposite direction. So, in the above example strongly disagree would attract a score of 5, disagree would be 4, neutral still equals 3, agree becomes 2 and strongly agree = 1.

####Compute Reverse Score for-
- Extraversion: 6, 21, 31
- Agreeableness: 2, 12, 27, 37
- Conscientiousness: 8, 18, 23, 43
- Neuroticism: 9, 24, 34
- Openness: 35, 41

####Compute Average of-
#####Extraversion: 1, 6R, 11, 16, 21R, 26, 31R, 36
#####Agreeableness: 2R, 7, 12R, 17, 22, 27R, 32, 37R, 42
#####Conscientiousness: 3, 8R, 13, 18R, 23R, 28, 33, 38, 43R
#####Neuroticism: 4, 9R, 14, 19, 24R, 29, 34R, 39
#####Openness: 5, 10, 15, 20, 25, 30, 35R, 40, 41R, 44 

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

## PersonalityOperations.py
This python script is responsible for generating
