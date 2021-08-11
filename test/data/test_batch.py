# CREATE TABLE report_batch (
#   rb_id BIGSERIAL PRIMARY KEY,
#   batch_id VARCHAR UNIQUE,       -- batchId
#   rb_name VARCHAR,               -- name
#   skill VARCHAR,                 -- skill
#   rb_location VARCHAR,           -- location
#   rb_type VARCHAR,               -- type
#   good_grade SERIAL,             -- goodGrade
#   passing_grade SERIAL,          -- passingGrade
#   -- for some reason, I've seen test data with negative week numbers
#   current_week INTEGER,          -- currentWeek
#   rb_start_date VARCHAR,         -- startDate
#   rb_end_date VARCHAR            -- endDate
# );
from src.model.batch import Batch
batches = [
    Batch(3000, "EX-B01", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3001, "EX-B02", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3002, "EX-B03", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3003, "EX-B04", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3004, "EX-B05", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3005, "EX-B06", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3006, "EX-B07", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3007, "EX-B08", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3008, "EX-B09", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(3009, "EX-B10", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
    Batch(30010, "EX-B11", "RB", "SKILL-1", "Detroit", "Type", 90, 100, -13, "", ""),
]
