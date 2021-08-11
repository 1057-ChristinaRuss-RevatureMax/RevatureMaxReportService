from src.dao.dao_helper import cursor_handler
from src.util.fetch import fetch_json
from src.config.db_config import execute_sql

URL_BASE = "https://caliber2-mock.revaturelabs.com:443/mock/"


@cursor_handler
def initialize_trainee_qc(data, cursor):
    cursor.execute(
        """INSERT INTO report_qc_note
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (data['noteId'], data['content'], data['week'], data['batchId'], data['associateId'],
         data['employeeId'], data['type'], data['technicalStatus'], data['createdOn'], data['lastUpdated']),
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


def initialize_tables():
    execute_sql("src/sql/setup.py")
