from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from own_models.problem_models import Problem
from own_models.manual_review_models import ManualReviewRequest
from django.urls import reverse

User = get_user_model()

class ManualReviewTestCase(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(username='student1', password='pass', role=1)
        self.teacher = User.objects.create_user(username='teacher1', password='pass', role=2, is_staff=True)
        self.problem = Problem.objects.create(title='Test Problem', description='desc', created_by=self.teacher)
        self.client = Client()

    def login_with_session(self, user):
        self.client.login(username=user.username, password='pass')
        session = self.client.session
        session['user_id'] = user.id
        session['user_role'] = user.role
        session.save()

    def test_student_request_manual_review(self):
        self.login_with_session(self.student)
        response = self.client.post(reverse('manual_review:request_manual_review', args=[self.problem.id]), {'code': 'print(1)'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ManualReviewRequest.objects.count(), 1)
        req = ManualReviewRequest.objects.first()
        self.assertEqual(req.student, self.student)
        self.assertEqual(req.problem, self.problem)
        self.assertEqual(req.code, 'print(1)')
        self.assertEqual(req.status, 'pending')

    def test_teacher_can_see_pending_reviews(self):
        req = ManualReviewRequest.objects.create(student=self.student, problem=self.problem, code='print(2)')
        self.login_with_session(self.teacher)
        response = self.client.get(reverse('manual_review:teacher_review_list'))
        self.assertContains(response, 'print(2)')

    def test_teacher_review_and_comment(self):
        req = ManualReviewRequest.objects.create(student=self.student, problem=self.problem, code='print(3)')
        self.login_with_session(self.teacher)
        response = self.client.post(reverse('manual_review:review_detail', args=[req.id]), {
            'annotated_code': 'print(3) # good',
            'review_comment': 'Well done!'
        })
        req.refresh_from_db()
        self.assertEqual(req.status, 'reviewed')
        self.assertEqual(req.annotated_code, 'print(3) # good')
        self.assertEqual(req.review_comment, 'Well done!')

    def test_student_can_view_review_result(self):
        req = ManualReviewRequest.objects.create(student=self.student, problem=self.problem, code='print(4)', status='reviewed', annotated_code='print(4) # fix', review_comment='Fix this line')
        self.login_with_session(self.student)
        response = self.client.get(reverse('manual_review:student_review_result', args=[req.id]))
        self.assertContains(response, 'Fix this line')
        self.assertContains(response, 'print(4) # fix')