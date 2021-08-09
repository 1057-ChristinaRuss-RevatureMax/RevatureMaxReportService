from src.dao import category_dao as dao
from src.model.category import Category


def create_category(category: Category):
    if category.grade_id == -1:  # category has no valid grade id
        dao.create_new(*category.to_tuple()[1:])
    else:  # category refers to something that existed previously
        dao.create_existing(*category)


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
        result_set = map(lambda x: Category(*x), filter(None, select_by_batch_category(batch_id, cat)))
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
        result["Associate Name"].append("")  # TODO: join email on name
        result["Quiz Score"].append(associate_score["quiz"] / associate_score["quiz_weight"])
        result["Exam Score"].append(associate_score["exam"] / associate_score["exam_weight"])
        result["Project Score"].append(associate_score["project"] / associate_score["project_weight"])
        result["Verbal Score"].append(associate_score["verbal"] / associate_score["verbal_weight"])
        result["Email"].append(associate_email)

    return result


def select_by_batch_category(batch_id, category_type):
    result = dao.select_by_batch_category(batch_id, category_type)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_batch_max_grade(batch_id, max_grade):
    result = dao.select_by_batch_max_grade(batch_id, max_grade)
    return list(map(lambda x: Category(*x), filter(None, result)))
