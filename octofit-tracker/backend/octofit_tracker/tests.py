from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout, User

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        activity = Activity.objects.create(user=user, activity_type='run', duration=10, team=team)
        self.assertEqual(activity.activity_type, 'run')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.points, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')
