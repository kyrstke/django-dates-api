import json

from django.urls import reverse
from django.test import Client

from rest_framework.test import APITestCase
from rest_framework.utils import json

from .models import Date, Month


class GetPostDateTests(APITestCase):
    """
    Tests GET and POST requests to 'get-post-date' route/view
    """

    def setUp(self):
        date = Date(month="January", day=12, fact="Some fact")
        date.save()

        date = Date(month="February", day=6, fact="International Banana day")
        date.save()

        self.client = Client()
        self.url = reverse('get-post-date')

    def test_get_all_dates(self):
        response = self.client.get(self.url)
        json_response = json.loads(response.content.decode('utf8'))

        dates_list = []
        dates_qs = Date.objects.all()
        for date in dates_qs:
            dates_list.append(date.toDict())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(dates_list, json_response)

    def test_post_date_successful(self):
        get1 = self.client.get(self.url)
        response = self.client.post(self.url, data={"month": 3, "day": 10})
        get2 = self.client.get(self.url)

        response_string = response.content.decode('utf-8')
        response_json = json.loads(response_string)
        fetched_fact = response_json["fact"]

        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response_string, '')
        self.assertTrue(fetched_fact)
        self.assertNotEqual(get1.content, get2.content)

    def test_post_date_fail_month(self):
        get1 = self.client.get(self.url)
        response = self.client.post(self.url, data={"month": 13, "day": 10})
        get2 = self.client.get(self.url)

        self.assertEqual(get1.content, get2.content)
        self.assertEqual(response.status_code, 400)

    def test_post_date_fail_day(self):
        get1 = self.client.get(self.url)
        response = self.client.post(self.url, data={"month": 12, "day": 32})
        get2 = self.client.get(self.url)

        self.assertEqual(get1.content, get2.content)
        self.assertEqual(response.status_code, 400)


class GetPopularTests(APITestCase):
    """
    Tests GET requests to 'popular' route/view
    """

    def setUp(self):
        date = Date(month="October", day=1, fact="Some fact")
        date.save()

        date = Date(month="February", day=6, fact="International Banana day")
        date.save()

        date = Date(month="February", day=19, fact="Some other fact")
        date.save()

        month = Month(month="October", days_checked=2)
        month.save()

        month = Month(month="February", days_checked=1)
        month.save()

        self.client = Client()
        self.url = reverse('popular')

    def test_get_popular(self):
        response = self.client.get(self.url)
        json_response = json.loads(response.content.decode('utf8'))

        months_list = []
        months_qs = Month.objects.all()
        for month in months_qs:
            months_list.append(month.toDict())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(months_list, json_response)


class DeleteDateTests(APITestCase):
    """
    Tests DELETE requests to 'delete-date' route/view
    """

    def setUp(self):
        date = Date(month="January", day=12, fact="Some fact")
        date.save()

        date = Date(month="February", day=6, fact="International Banana day")
        date.save()

        self.client = Client()

    def test_delete_date_key(self):
        get1 = self.client.get(reverse('get-post-date'))

        pk = json.loads(get1.content.decode('utf-8'))[0]["id"]
        url = reverse('delete-date', kwargs={"pk": pk})

        response = self.client.delete(url, HTTP_X_API_KEY="SECRET_API_KEY")
        get2 = self.client.get(reverse('get-post-date'))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(get1.content, get2.content)

    def test_delete_date_no_key(self):
        get1 = self.client.get(reverse('get-post-date'))

        pk = json.loads(get1.content.decode('utf-8'))[0]["id"]
        url = reverse('delete-date', kwargs={"pk": pk})

        response = self.client.delete(url)
        get2 = self.client.get(reverse('get-post-date'))

        self.assertEqual(response.status_code, 401)
        self.assertEqual(get1.content, get2.content)

    def test_delete_date_invalid_pk(self):
        get1 = self.client.get(reverse('get-post-date'))

        pk = json.loads(get1.content.decode('utf-8'))[-1]["id"] + 1
        url = reverse('delete-date', kwargs={"pk": pk})

        response = self.client.delete(url, HTTP_X_API_KEY="SECRET_API_KEY")
        get2 = self.client.get(reverse('get-post-date'))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(get1.content, get2.content)
