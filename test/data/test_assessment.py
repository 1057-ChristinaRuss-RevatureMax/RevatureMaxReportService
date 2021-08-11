# CREATE TABLE report_on_assessment (
#   grade_id        BIGSERIAL,    --
#   batch_id        VARCHAR
#     REFERENCES report_batch(batch_id),
#   associate_id    VARCHAR(40)
#     REFERENCES associate(email),
#   assessment_type  VARCHAR(10), -- assessmentType
#   score           INTEGER
#     CHECK (score >= 0),           -- score
#   week            INTEGER
#     CHECK (week > 0),             -- week
#   grade_weight    INTEGER
#     CHECK (grade_weight >= 0)     -- weight
# );
from src.model.assessment import Assessment
assessments = [
    Assessment(3000, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
    Assessment(3001, "EX-B01", "ex0003@example.com", "Score", 60, 1, 100),
    Assessment(3002, "EX-B01", "ex0005@example.com", "Score", 60, 1, 100),
    Assessment(3003, "EX-B01", "ex0007@example.com", "Score", 60, 1, 100),
    Assessment(3004, "EX-B01", "ex0009@example.com", "Score", 60, 1, 100),
    Assessment(3005, "EX-B02", "ex0002@example.com", "Score", 60, 1, 100),
    Assessment(3006, "EX-B02", "ex0004@example.com", "Score", 60, 1, 100),
    Assessment(3007, "EX-B02", "ex0006@example.com", "Score", 60, 1, 100),
    Assessment(3008, "EX-B02", "ex0008@example.com", "Score", 60, 1, 100),
    Assessment(3009, "EX-B01", "ex0001@example.com", "Score", 60, 1, 100),
    Assessment(30010, "EX-B01", "ex0003@example.com", "Score", 70, 2, 100),
    Assessment(30011, "EX-B01", "ex0005@example.com", "Score", 70, 2, 100),
    Assessment(30012, "EX-B01", "ex0007@example.com", "Score", 70, 2, 100),
    Assessment(30013, "EX-B01", "ex0009@example.com", "Score", 70, 2, 100),
    Assessment(30014, "EX-B02", "ex0002@example.com", "Score", 70, 2, 100),
    Assessment(30015, "EX-B02", "ex0004@example.com", "Score", 70, 2, 100),
    Assessment(30016, "EX-B02", "ex0006@example.com", "Score", 70, 2, 100),
    Assessment(30017, "EX-B02", "ex0008@example.com", "Score", 70, 2, 100),
    Assessment(30020, "EX-B01", "ex0001@example.com", "Score", 60, 3, 100),
    Assessment(30021, "EX-B01", "ex0003@example.com", "Score", 60, 3, 100),
    Assessment(30022, "EX-B01", "ex0005@example.com", "Score", 60, 3, 100),
    Assessment(30023, "EX-B01", "ex0007@example.com", "Score", 60, 3, 100),
    Assessment(30024, "EX-B01", "ex0009@example.com", "Score", 60, 3, 100),
    Assessment(30025, "EX-B02", "ex0002@example.com", "Score", 60, 3, 100),
    Assessment(30026, "EX-B02", "ex0004@example.com", "Score", 60, 3, 100),
    Assessment(30027, "EX-B02", "ex0006@example.com", "Score", 60, 3, 100),
    Assessment(30028, "EX-B02", "ex0008@example.com", "Score", 60, 3, 100),
    Assessment(30029, "EX-B01", "ex0001@example.com", "Score", 60, 3, 100),
    Assessment(300210, "EX-B01", "ex0003@example.com", "Score", 70, 4, 100),
    Assessment(300211, "EX-B01", "ex0005@example.com", "Score", 70, 4, 100),
    Assessment(300212, "EX-B01", "ex0007@example.com", "Score", 70, 4, 100),
    Assessment(300213, "EX-B01", "ex0009@example.com", "Score", 70, 4, 100),
    Assessment(300214, "EX-B02", "ex0002@example.com", "Score", 70, 4, 100),
    Assessment(300215, "EX-B02", "ex0004@example.com", "Score", 70, 4, 100),
    Assessment(300216, "EX-B02", "ex0006@example.com", "Score", 70, 4, 100),
    Assessment(300217, "EX-B02", "ex0008@example.com", "Score", 70, 4, 100),
]
