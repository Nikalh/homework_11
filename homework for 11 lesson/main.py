from flask import Flask, render_template

from utils import get_candidate, get_candidate_by_skill, \
    get_candidates_by_name, load_candidates_json

app = Flask(__name__)


@app.route("/")
def page_main():
    candidates: list[dict] = load_candidates_json()

    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def candidate_page(idx):
    """Поиск кандидата по номеру"""
    candidate: dict = get_candidate(idx)
    if not candidate:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search_candidates(candidate_name):
    """Поиск навыков"""
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route("/skill/<candidate_skill>")
def page_search_candidates_skills(candidate_skill):
    """Поиск навыков"""
    candidates: list[dict] = get_candidate_by_skill(candidate_skill)
    return render_template('skill.html', skill=candidate_skill, candidates=candidates)

app.run()
