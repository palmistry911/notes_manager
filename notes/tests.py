from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Note

User = get_user_model()


class NoteTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.note = Note.objects.create(title="Тестовая заметка", content="Тестовый контент", user=self.user)

    def test_note_list(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_note(self):
        note = Note.objects.create(
            title='Second Note',
            description='Another Description',
            user=self.user,
        )
        self.assertEqual(Note.objects.count(), 2)
        self.assertEqual(note.title, 'Second Note')

    def test_update_note(self):
        self.note.title = 'Updated Note'
        self.note.save()
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_delete_note(self):
        self.note.delete()
        self.assertEqual(Note.objects.count(), 0)

    def test_retrieve_note(self):
        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, 'Test Note')
