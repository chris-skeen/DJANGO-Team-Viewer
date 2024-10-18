from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass
from typing import List
# Create your views here.

@dataclass
class Team:
  name: str
  desc: str
  members: List

manTeam = Team('Management', """
      As the Management team we are required to manage all of the chores for each day and who does them.
      This includes:
      1. Cleaning the kitchen, and taking out the trash.

      2. Sweeping the main lobby and also sweeping the backhallway/classrooms
               
      3. Wiping all the tables, including the kitchen tables.

               """, ['Chris', 'Aidan', 'Kilan', 'Tanner'])

proTeam = Team('Procurement', """
  Description - We buy food to cook so that we can feed you guys at lunch time and we buy supplies like soap, trash, bags etc
               """, ['Arthur', 'Aaron', 'Markel', 'Jacob'])


docTeam = Team('Documentation', """
  Description - We buy food to cook so that we can feed you guys at lunch time and we buy supplies like soap, trash, bags etc
               """, ['Patrick', 'Jason'])

comTeam = Team('Community', """
Our job is to plan events that bring people together, build lasting relationships, and promote engagement.
               """, ['Arianna', 'Peyton'])

teams = {
  "Management": manTeam,
  "Procurement": proTeam,
  "Documentation": docTeam,
  "Community": comTeam,
}

man_name = teams['Management'].name
pro_name = teams['Procurement'].name
doc_name = teams['Documentation'].name
com_name = teams['Community'].name

man_desc = teams['Management'].desc
pro_desc = teams['Procurement'].desc
doc_desc = teams['Documentation'].desc
com_desc = teams['Community'].desc

man_members = teams['Management'].members
pro_members = teams['Procurement'].members
doc_members = teams['Documentation'].members
com_members = teams['Community'].members

# teams['Management'].desc

def root_view(request: HttpRequest):
    
  context = {
    "name": ["Management", "Documentation", "Community", "Procurement"]

  }

  return render(request, "home.html", context)

def teams_view(request: HttpRequest, team: str):
  if team == "Management":
    team_context = {
      "name": man_name,
      "desc": man_desc,
      "members": man_members,
    }
  elif team == "Procurement":
    team_context = {
      "name": pro_name,
      "desc": pro_desc,
      "members": pro_members,
    }

  elif team == "Documentation":
    team_context = {
      "name": doc_name,
      "desc": doc_desc,
      "members": doc_members,
    }

  elif team == "Community":
    team_context = {
      "name": com_name,
      "desc": com_desc,
      "members": com_members,
    }

  return render(request, "teams.html", team_context)