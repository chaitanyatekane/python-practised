# Step 01: in terminal run command - pip install requests

import requests
response = requests.get("https://api.github.com/users/chaitanyatekane/repos")
my_repos = response.json()

# print the whole objects list
# print(my_projects)
# print(type(my_projects))  # will return list

# print just the names and urls
for project in my_repos:
    print(
        f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")


# Sample Output :-
# Project Name: 100DaysOfCodeChallenge-Feb-04-2021
# Project Url: https://github.com/chaitanyatekane/100DaysOfCodeChallenge-Feb-04-2021

# Project Name: 30DaysOfCodeChallenge-Jan-04-2021
# Project Url: https://github.com/chaitanyatekane/30DaysOfCodeChallenge-Jan-04-2021

# Project Name: AreYouCricketExpert
# Project Url: https://github.com/chaitanyatekane/AreYouCricketExpert

# Project Name: Auto-Write-Text
# Project Url: https://github.com/chaitanyatekane/Auto-Write-Text

# Project Name: Automotive-Car-Design-Template
# Project Url: https://github.com/chaitanyatekane/Automotive-Car-Design-Template

# Project Name: Background-Changer
# Project Url: https://github.com/chaitanyatekane/Background-Changer

# and so on.........................................................
