from test.data.test_compare_batch_data import batches, batch_grades, spider_weeks
from unittest import TestCase, mock
from src.model.batch import Batch
from src.model.batch_grade import BatchGrade
from src.model.spider_week import SpiderWeek
from src.service import compare_batch_services as service


class TestCompareBatchService(TestCase):
    @mock.patch("src.dao.compare_batch_dao.get_batch_by_id")
    def test_get_batch_by_id(self, m_select):
        batch = Batch(69, "TR-1140", "Mock Batch 69", "PEGA", "Savannah", "Type", 90, 100, -13, "2021-05-14",
                      "2021-07-23")
        batch_tuple = (batch.rb_id, batch.batch_id, batch.rb_name, batch.rb_start_date, batch.rb_end_date, batch.skill,
                       batch.rb_location, batch.rb_type, batch.good_grade, batch.passing_grade, batch.current_week)
        m_select.return_value = batch_tuple
        test_result = service.get_batch_by_id(batch.batch_id, productionDB=False)
        self.assertTrue(m_select.called)
        self.assertEqual(test_result, batch_tuple)

    @mock.patch("src.dao.compare_batch_dao.get_batches_with_same_skill")
    def test_get_batches_same_skill(self, m_select):
        batch_one = Batch(69, "TR-1140", "Mock Batch 69", "PEGA", "Savannah", "Type", 90, 100, -13, "2021-05-14",
                          "2021-07-23")
        batch_two = Batch(70, "TR-1145", "Mock Batch 70", "PEGA", "Savannah", "Type", 90, 100, -13, "2021-05-28",
                          "2021-08-06")
        batch_three = Batch(71, "TR-1072", "Mock Batch 71", "PEGA", "Savannah", "Type", 90, 100, -13, "2020-05-14",
                            "2020-07-23")
        batch_four = Batch(72, "TR-1021", "Mock Batch 72", "PEGA", "Savannah", "Type", 90, 100, -13, "2021-04-14",
                           "2021-06-23")
        batches_list_of_tuples = [(batch_one.rb_id, batch_one.batch_id, batch_one.rb_name, batch_one.rb_start_date,
                                   batch_one.rb_end_date, batch_one.skill,
                                   batch_one.rb_location, batch_one.rb_type, batch_one.good_grade,
                                   batch_one.passing_grade, batch_one.current_week),
                                  (batch_three.rb_id, batch_three.batch_id, batch_three.rb_name,
                                   batch_three.rb_start_date, batch_three.rb_end_date, batch_three.skill,
                                   batch_three.rb_location, batch_three.rb_type, batch_three.good_grade,
                                   batch_three.passing_grade, batch_three.current_week),
                                  (batch_four.rb_id, batch_four.batch_id, batch_four.rb_name, batch_four.rb_start_date,
                                   batch_four.rb_end_date, batch_four.skill,
                                   batch_four.rb_location, batch_four.rb_type, batch_four.good_grade,
                                   batch_four.passing_grade, batch_four.current_week)]
        m_select.return_value = batches_list_of_tuples
        test_result = service.get_batches_with_same_skill(batch_two.batch_id, batch_two.rb_start_date,
                                                          productionDB=False)
        self.assertTrue(m_select.called)
        self.assertEqual(batches_list_of_tuples, test_result)

    @mock.patch("src.dao.compare_batch_dao.batch_total_avg")
    def test_batch_total_avg(self, m_select):
        grade_one = BatchGrade("name", 60, "TR-1140").to_tuple()
        grade_two = BatchGrade("name", 50, "TR-1140").to_tuple()
        expected_result = ((grade_two[1] + grade_one[1]) / 2,)
        m_select.return_value = expected_result
        test_result = service.batch_total_avg("TR-1140", productionDB=False)
        self.assertTrue(m_select.called)
        self.assertEqual(expected_result[0], test_result)

    @mock.patch("src.dao.compare_batch_dao.batch_weekly_avg")
    def test_batch_weekly_avg(self, m_select):
        spider_one = SpiderWeek(0, "TR-1140", None, "type", 60, 1, 100).to_tuple()
        spider_two = SpiderWeek(1, "TR-1140", None, "type", 50, 1, 100).to_tuple()
        expected_result = ((spider_two[4] + spider_one[4]) / 2,)
        m_select.return_value = expected_result
        test_result = service.batch_weekly_avg('TR-1140', 100, productionDB=False)
        self.assertTrue(m_select.called)
        self.assertEqual(expected_result[0], test_result)