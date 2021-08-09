from src.dao import category_dao as dao, associate_dao
from src.model.category import Category


def create_category(category: Category):
    if category.grade_id == -1:  # category has no valid grade id
        dao.create_new(*category.to_tuple()[1:])
    else:  # category refers to something that existed previously
        dao.create_existing(*category.to_tuple())


def select_by_email_category_week(associate_email, category_type, week):
    result = dao.select_by_email_category_week(associate_email, category_type, week)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_email_category(associate_email, category_type):
    result = dao.select_by_email_category(associate_email, category_type)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_email(associate_email):
    result = dao.select_by_email(associate_email)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_batch(batch_id):
    result = dao.select_by_batch(batch_id)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_all_categories():
    return [tpl[0] for tpl in filter(None, dao.select_all_categories())]


def select_by_batch_averages(batch_id):
    categories = select_all_categories()
    associate_scores = {}
    for cat in categories:
        cat = str.lower(cat)
        result_set = select_by_batch_category(batch_id, cat)
        for result in result_set:
            if result.email not in associate_scores.keys():
                associate_scores[result.email] = {}
            if cat not in associate_scores[result.email].keys():
                associate_scores[result.email][cat] = 0
                associate_scores[result.email][f'{cat}_weight'] = 0

            associate_scores[result.email][cat] += result.score * result.grade_weight
            associate_scores[result.email][f'{cat}_weight'] += result.grade_weight

    result = {
        "Associate Name": [],
        "Quiz Score": [],
        "Exam Score": [],
        "Project Score": [],
        "Verbal Score": [],
        "Email": [],
    }
    for associate_email in associate_scores.keys():
        associate_score = associate_scores[associate_email]
        result["Associate Name"].append(associate_dao.select_name_by_email(associate_email))
        result["Quiz Score"].append(associate_score.get("quiz", 0) / associate_score.get("quiz_weight", 1))
        result["Exam Score"].append(associate_score.get("exam", 0) / associate_score.get("exam_weight", 1))
        result["Project Score"].append(associate_score.get("project", 0) / associate_score.get("project_weight", 1))
        result["Verbal Score"].append(associate_score.get("verbal", 0) / associate_score.get("verbal_weight", 1))
        result["Email"].append(associate_email)

    return result


def select_by_batch_category(batch_id, category_type):
    result = dao.select_by_batch_category(batch_id, category_type)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_batch_max_grade(batch_id, max_grade):
    result = dao.select_by_batch_max_grade(batch_id, max_grade)
    return list(map(lambda x: Category(*x), filter(None, result)))
