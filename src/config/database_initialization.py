from src.dao.dao_helper import cursor_handler
from src.util.fetch import fetch_json

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@cursor_handler
def get_batch_ids(cursor):
    cursor.execute('SELECT batch_id FROM report_batch ORDER BY batch_id')
    return cursor.fetchall()


@cursor_handler
def get_emails_by_batch(batch_id, cursor):
    cursor.execute('select email from associate where batch_id = %s', [batch_id])
    return cursor.fetchall()


@cursor_handler
def get_batch_from_email(email, cursor):
    cursor.execute('select batch_id from associate where email = %s', [email])
    return cursor.fetchone()


@cursor_handler
def initialize_trainee_qc(data, cursor):
    cursor.execute(
        """INSERT INTO report_qc_note
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (data['noteId'], data['content'], data['week'], data['batchId'], data['associateId'],
         data['employeeId'], data['type'], data['technicalStatus'], data['createdOn'], data['lastUpdated']),
    )


@cursor_handler
def initialize_category_table(data, cursor):
    cursor.execute(
        """insert into report_on_category values (DEFAULT, %s, %s, %s, %s, %s, %s)""",
        (data['batch_id'], data['email'], data['category'], data['score'], data['week'], data['grade_weight'])
    )


@cursor_handler
def initialize_batch_qc(data, cursor):
    cursor.execute(
        """INSERT INTO report_qc_batch_note
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (data['noteId'], data['content'], data['week'], data['batchId'], data['associateId'],
         data['employeeId'], data['type'], data['technicalStatus'], data['createdOn'], data['lastUpdated']),
    )


def populate_table_entire_batch(batch_id):
    url_ind = f"{URL_BASE}qa/notes/individual/{batch_id}"
    url_batch = f"{URL_BASE}qa/notes/batch/{batch_id}"
    qc_json_ind = fetch_json(url_ind)
    qc_json_batch = fetch_json(url_batch)

    for x in qc_json_ind:
        initialize_trainee_qc(x)

    for x in qc_json_batch:
        initialize_batch_qc(x)


def populate_category_table(email):
    batch_id = get_batch_from_email(email)
    grade_weight = 100
    data = {}

    for i in range(1, 8):
        url = f"{URL_BASE}evaluation/grades/reports/individual/{email}/{i}"
        category_json = fetch_json(url)

        for x in category_json['traineeGrades']:
            data['batch_id'] = batch_id
            data['grade_weight'] = grade_weight
            data['email'] = email
            data['week'] = i
            data['category'] = x
            data['score'] = category_json['traineeGrades'][x]

            initialize_category_table(data)
