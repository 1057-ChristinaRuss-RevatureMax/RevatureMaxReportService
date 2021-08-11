from src.config.compare_batch_initialization import (
    populate_associate_table,
    populate_batch_table,
    populate_category_table,
    populate_assessment_table,
)
from src.config.database_initialization import initialize_tables


if __name__ == "__main__":
    initialize_tables()
    populate_associate_table()
    populate_batch_table()
    populate_category_table()
    populate_assessment_table()
