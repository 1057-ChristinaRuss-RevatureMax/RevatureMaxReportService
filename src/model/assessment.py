from dataclasses import dataclass


@dataclass
class Assessment:
    grade_id: str
    batch_id: str
    associate_id: str
    assessment_type: str
    score: int
    week: str
    grade_weight: int

    def __repr__(self):
        return "Assessment(%s, %s, %s, %s, %s, %s, %s)" % (
            self.grade_id,
            self.batch_id,
            self.associate_id,
            self.assessment_type,
            self.score,
            self.week,
            self.grade_weight,
        )

    def to_tuple(self):
        return (
            self.grade_id,
            self.batch_id,
            self.associate_id,
            self.assessment_type,
            self.score,
            self.week,
            self.grade_weight,
        )
