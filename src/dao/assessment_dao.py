from src.dao.dao_helper import cursor_handler


@cursor_handler
def create_existing(grade_id, batch_id, email, assessment_type, score, week, grade_weight, cursor):
    cursor.execute(
        """INSERT INTO report_on_assessment
        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (grade_id, batch_id, email, assessment_type, score, week, grade_weight),
    )


@cursor_handler
def create_new(batch_id, email, assessment_type, score, week, grade_weight, cursor):
    cursor.execute(
        """INSERT INTO report_on_assessment
        VALUES (%s, %s, %s, %s, %s, %s)""",
        (batch_id, email, assessment_type, score, week, grade_weight),
    )


@cursor_handler
def select_by_email_assessment_week(email, assessment_type, week, cursor):
    cursor.execute(
        """SELECT * FROM report_on_assessment
        WHERE associate_id LIKE %s AND assessment_type LIKE %s AND week = %s""",
        (email, assessment_type, week),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_email_assessment(email, assessment_type, cursor):
    cursor.execute(
        """SELECT * FROM report_on_assessment
        WHERE associate_id LIKE %s AND assessment_type LIKE %s""",
        (email, assessment_type),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_email(email, cursor):
    cursor.execute(
        """SELECT * FROM report_on_assessment
        WHERE associate_id LIKE %s""",
        (email,),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch(batch_id, cursor):
    cursor.execute(
        """SELECT * FROM report_on_assessment
        WHERE batch_id LIKE %s""",
        (batch_id,),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch_assessment(batch_id, assessment_type, cursor):
    cursor.execute(
        """SELECT * FROM report_on_assessment
        WHERE batch_id LIKE %s AND assessment_type LIKE %s""",
        (batch_id, assessment_type),
    )
    return cursor.fetchall()


@cursor_handler
def select_by_batch_max_grade(batch_id, max_grade, cursor):
    cursor.execute(
        """SELECT * FROM report_on_assessment
        WHERE batch_id LIKE %s AND score < %s""",
        (batch_id, max_grade),
    )
    return cursor.fetchall()
