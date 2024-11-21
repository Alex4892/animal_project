# from django.test import TestCase, RequestFactory
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from animals_app.models import Animal, Kind
# from animals_app.forms import AnimalForm
# from animals_app.views import (view_animals, view_detail_animal,
#                                add_animal_view, edit_animal_view,
#                                delete_animal_view)

# User = get_user_model()

# class AnimalViewTests(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(username='testuser',
#                                              password='password')
#         self.kind = Kind.objects.create(name='Test Kind')
#         self.animal = Animal.objects.create(
#             title='Test Animal',
#             nickname='Test Nickname',
#             description='Test Description',
#             phone_number=123,
#             signs='Test Signs',
#             submit=self.user
#         )
#         self.animal.kinds.add(self.kind)

#     def test_view_animals(self):
#         url = reverse('animals:index')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'animals/index.html')
#         self.assertIn('animals', response.context)
#         self.assertEqual(len(response.context['animals']), 1)

#     def test_view_detail_animal(self):
#         url = reverse('animals:detail_animal', args=[self.animal.id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'animals/detail_animal.html')
#         self.assertIn('animal', response.context)
#         self.assertEqual(response.context['animal'].name, 'Test Animal')

#     def test_add_animal_view_get(self):
#         url = reverse('animals:add_animal')
#         self.client.login(username='testuser', password='password')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'animals/add_animal.html')
#         self.assertIsInstance(response.context['form'], AnimalForm)

#     def test_add_animal_view_post(self):
#         url = reverse('animals:add_animal')
#         data = {
#             'title': 'Test Animal',
#             'nickname' : 'Test Nickname',
#             'description' : 'Test Description',
#             'phone_number' : 123,
#             'signs' : 'Test Signs',
#             'kinds': [self.kind.id]
#         }
#         self.client.login(username='testuser', password='password')
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Book.objects.filter(name='New Animal').count(), 1)

#     def test_edit_animal_view_get(self):
#         url = reverse('animals:edit_animal', args=[self.animal.id])
#         self.client.login(username='testuser', password='password')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'animals/add_animal.html')
#         self.assertIsInstance(response.context['form'], AnimalForm)
#         self.assertEqual(response.context['form'].instance, self.animal)

#     def test_edit_animal_view_post(self):
#         url = reverse('animals:edit_animal', args=[self.animal.id])
#         data = {
#             'title': 'Updated Animal Title',
#             'nickname' : 'Test Nickname',
#             'description' : 'Test Description',
#             'phone_number' : 123,
#             'signs' : 'Test Signs',
#             'kinds': [self.kind.id]
#         }
#         self.client.login(username='testuser', password='password')
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 302)
#         self.animal.refresh_from_db()
#         self.assertEqual(self.animal.name, 'Updated Animal Title')

#     def test_delete_animal_view(self):
#         url = reverse('animals:delete_animal', args=[self.animal.id])
#         self.client.login(username='testuser', password='password')
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, 302)
#         self.assertFalse(Animal.objects.filter(id=self.animal.id).exists())

# python manage.py test animals_app.tests.unit_tests.tests

# Create your tests here.
