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


def select_by_batch_averages(batch_id):
    result = dao.select_by_batch_averages(batch_id)
    return list(map(lambda x: Category(-1, *x), filter(None, result)))


def select_by_batch_category(batch_id, category_type):
    result = dao.select_by_batch_category(batch_id, category_type)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_by_batch_max_grade(batch_id, max_grade):
    result = dao.select_by_batch_max_grade(batch_id, max_grade)
    return list(map(lambda x: Category(*x), filter(None, result)))


def select_all_batch_averages(batch_id):
    # emails = list(map(lambda x: Category(*x), filter(None, dao.select_by_batch(batch_id))))
    # self.batch_id
    # self.email
    # self.category
    # self.score
    # self.week
    pass
