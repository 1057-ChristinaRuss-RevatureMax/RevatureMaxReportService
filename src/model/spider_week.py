from dataclasses import dataclass


@dataclass
class SpiderWeek:
    grade_id: str
    trainee_id: str
    associate_id: str
    type: str
    score: str
    week: str
    weight: str

    def __repr__(self):
        return "SpiderWeek(%s, %s, %s, %s, %s, %s, %s)" % (
            self.grade_id,
            self.trainee_id,
            self.associate_id,
            self.type,
            self.score,
            self.week,
            self.weight
        )

    def to_tuple(self):
        return (
            self.grade_id,
            self.trainee_id,
            self.associate_id,
            self.type,
            self.score,
            self.week,
            self.weight
        )