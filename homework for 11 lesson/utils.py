import json

#загружаем кандидатов из файла
def load_candidates_json() -> list[dict]:
#def load_candidates(data):
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id: int) -> dict:
    """Определяем кандидата по номеру"""
    for candidate in load_candidates_json():
        if candidate['id'] == candidate_id:
            return candidate

def get_candidates_by_name(candidate_name: str)->list[dict]:
    """Возвращаем кандидатов по имени"""
    candidates = load_candidates_json()
    result = []
    for candidate in candidates:
        if candidate_name in candidate['name']:
            result.append(candidate)
    return result

def get_candidate_by_skill(skill: str) -> list[dict]:
    """Выбираем кандидатов по навыку"""
    candidates = load_candidates_json()
    result =[]
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(", "):
            result.append(candidate)
    return result
