from src.dao.dao_helper import cursor_handler


@cursor_handler
def create_existing(grade_id, batch_id, email, category, score, week, grade_weight, cursor):
    cursor.execute(
        """INSERT INTO report_on_category
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (grade_id, batch_id, email, category, score, week, grade_weight),
    )


@cursor_handler
def create_new(batch_id, email, category, score, week, grade_weight, cursor):
    cursor.execute(
        """INSERT INTO report_on_category
        VALUES (%s, %s, %s, %s, %s, %s)""",
        (batch_id, email, category, score, week, grade_weight),
    )


@cursor_handler
def select_by_email_assessment_week(email, category, week, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE email LIKE %s AND category LIKE %s AND week = %s""",
        (email, category, week),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_email_assessment(email, category, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE email LIKE %s AND category LIKE %s""",
        (email, category),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_email(email, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE email LIKE %s""",
        (email,),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch(batch_id, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE batch_id LIKE %s""",
        (batch_id,),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch_averages(batch_id, cursor):
    cursor.execute(
        """SELECT batch_id, email, category, AVG(score), week, weight FROM report_on_category
        WHERE batch_id LIKE %s
        GROUP BY email""",
        (batch_id,),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch_assessment(batch_id, category, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE batch_id LIKE %s AND category LIKE %s""",
        (batch_id, category),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch_max_grade(batch_id, max_grade, cursor):
    cursor.execute(
        """SELECT * FROM report_on_category
        WHERE batch_id LIKE %s AND score < %s""",
        (batch_id, max_grade),
    )
    return cursor.fetchall()
