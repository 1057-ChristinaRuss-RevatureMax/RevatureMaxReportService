from dataclasses import dataclass


@dataclass
class Associate:
    email: str
    salesforceId: str
    firstname: str
    lastname: str
    batch_id: str

    def __repr__(self):
        return "Associate(%s, %s, %s, %s, %s)" % (
            self.email,
            self.salesforceId,
            self.firstname,
            self.lastname,
            self.batch_id
        )

    def to_tuple(self):
        return (
            self.email,
            self.salesforceId,
            self.firstname,
            self.lastname,
            self.batch_id
        )
