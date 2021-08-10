from src.config.flask_config import app
from src.service import category_service


@app.route("/trainer/<batch_id>")
def batch_individual_averages(batch_id):
    # setup using column-first format
    result = {
        "Associate Name": [],
        "Quiz Score": [],
        "Exam Score": [],
        "Project Score": [],
        "Verbal Score": [],
        "Email": [],
    }
    # get associate scores by week and category
    category_scores = category_service.select_by_batch_averages(batch_id)

    pass
