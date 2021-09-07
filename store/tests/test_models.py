from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product

class TestCategoriewModel(TestCase):

    def setUp(self):
        self.data1=Category.objects.create(name='django',slug='django')

    def test_category_model_entry(self):
        #this test category insertion /type validation / attribute
        data=self.data1
        self.assertTrue(isinstance(data,Category))
        self.assertEqual(str(data),'django')



class TestProductsModel(TestCase):
  
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        #we add id to category_id, created_by_id beecause it added automatically by django
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')
        # self.data2 = Product.products.create(category_id=1, title='django advanced', created_by_id=1,
        #                                      slug='django-advanced', price='20.00', image='django', is_active=False)

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')


    # def test_category_url(self):
    #     """
    #     Test category model slug and URL reverse
    #     """
    #     data = self.data1
    #     response = self.client.post(
    #         reverse('store:category_list', args=[data.slug]))
    #     self.assertEqual(response.status_code, 200)

    # def test_products_url(self):
    #     """
    #     Test product model slug and URL reverse
    #     """
    #     data = self.data1
    #     url = reverse('store:product_detail', args=[data.slug])
    #     self.assertEqual(url, '/item/django-beginners/')
    #     response = self.client.post(
    #         reverse('store:product_detail', args=[data.slug]))
    #     self.assertEqual(response.status_code, 200)

    # def test_products_custom_manager_basic(self):
    #     """
    #     Test product model custom manager returns only active products
    #     """
    #     data = Product.products.all()
    #     self.assertEqual(data.count(), 1)
