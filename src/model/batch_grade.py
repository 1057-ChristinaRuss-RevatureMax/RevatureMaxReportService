from dataclasses import dataclass


@dataclass
class BatchGrade():
    name: str
    average: int
    batch_id: str

    def __repr__(self):
        return "BatchGrade(%s, %s, %s)" % (
            self.name,
            self.average,
            self.batch_id
        )

    def to_tuple(self):
        return (
            self.name,
            self.average,
            self.batch_id
        )
