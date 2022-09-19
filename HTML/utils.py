from flask import render_template
from flask import request
import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def load_candidates_from_json():
    with open("candidate.json", encoding='utf8') as f:
        my_candidates = json.load(f)
        return render_template('Cat.html', my_candidates=my_candidates)


@app.route("/id/<candidate_id>")
def get_candidate(candidate_id):
    with open('candidate.json', encoding='utf8') as f:
        my_candidates = json.load(f)
        for cand in my_candidates:
            if int(candidate_id) == cand['id']:
                return cand


@app.route("/name/<name_person>")
def find_name(name_person):
    temp = name_person.lower()
    with open('candidate.json', encoding='utf8') as f:
        candidates = json.load(f)
        for candidate in candidates:
            if temp in candidate['name'].lower():
                return render_template('card.html', candidate=candidate)


@app.route("/skills/<name_skills>")
def find_skills(name_skills):
    name_skills.lower()
    with open('candidate.json', encoding='utf8') as f:
        candidates = json.load(f)
        skills_person = []
        for candidate in candidates:
            s = candidate["skills"].replace(',', '')
            x = s.lower().split()
            if name_skills in x:
                skills_person.append(candidate)
        return render_template("list.html",my_candidates=skills_person)


@app.route("/candidate/<name_candidate>")
def candidate_card(name_candidate):
    name_candidate.lower()
    with open('candidate.json', encoding='utf8') as f:
        candidates = json.load(f)
        for cand in candidates:
            if name_candidate in cand["name"]:
                return render_template("card.html", name=name)

@app.route("/search/<name_candidate>")
def search_candidate(name_candidate):
    x = name_candidate.lower()
    candidate = []
    with open('candidate.json', encoding='utf8') as f:
        candidates = json.load(f)
        for cand in candidates:
            b = cand["name"].lower().split()
            if x in b:
                candidate.append(cand)
    return render_template("list.html", my_candidates = candidate )


@app.route("/search_skill/<cand_experience>")
def search_skill(cand_experience):
    x = cand_experience.lower()
    skill_list = []
    with open('candidate.json', encoding='utf8') as f:
        candidates = json.load(f)
        for skill in candidates:
            s = skill["skills"].replace(',', '')
            b = s.lower().split()
            if x in b:
                skill_list.append(skill)
    return render_template("skill.html", candidates = skill_list)

app.run()

