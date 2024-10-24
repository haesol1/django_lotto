from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):


    def test_generate(self):


        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate() # GuessNumbers 클래스의 generate 함수를 실행


        print(g.update_date)
        print(g.lottos)

        self.assertTrue(len(g.lottos) > 20)

### TDD(Test-driven development)
