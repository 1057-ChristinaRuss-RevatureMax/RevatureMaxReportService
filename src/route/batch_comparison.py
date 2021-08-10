from src.config.flask_config import app
from src.service import category_service


@app.route("/trainer/<batch_id>")
def batch_individual_averages(batch_id):
    # get associate scores by week and category
    return category_service.select_by_batch_averages(batch_id)
