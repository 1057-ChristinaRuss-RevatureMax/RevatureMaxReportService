class Batch:
    rb_id: str
    batch_id: str
    rb_name: str
    skill: str
    rb_location: str
    rb_type: str
    good_grade: int
    passing_grade: int
    current_week: int
    rb_start_date: str
    rb_end_date: str

    def __repr__(self):
        return "Batch(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (
            self.rb_id,
            self.batch_id,
            self.rb_name,
            self.skill,
            self.rb_location,
            self.rb_type,
            self.good_grade,
            self.passing_grade,
            self.current_week,
            self.rb_start_date,
            self.rb_end_date,
        )

    def to_tuple(self):
        return (
            self.rb_id,
            self.batch_id,
            self.rb_name,
            self.skill,
            self.rb_location,
            self.rb_type,
            self.good_grade,
            self.passing_grade,
            self.current_week,
            self.rb_start_date,
            self.rb_end_date,
        )
