from django.utils.timezone import now
import requests

from core import logger


class CatFact:
    def __init__(self, *args, **kwargs):
        self.fact = "Could not fetch cat fact, but, hey! cats are fun!"
        
    def fetch_cat_fact(self):
        url = "https://catfact.ninja/fact/"
        try:
            res = requests.get(url, timeout=10)
            data = res.json()
            if res.status_code != 200:
                raise Exception(data.get('message', 'Error Occurred'))
            self.fact = data['fact']
        except Exception as e:
            logger.error(f"FETCHING CAT FACT ERROR: {str(e)}")
            pass
        
    def get_response(self):
        return {
            'status': 'success',
            'user': {
                'email': 'adegbiranayinoluwa.paul@yahoo.com',
                'name': 'Paul Adegbiran-Ayinoluwa',
                'stack': 'Python/Django'
            },
            'timestamp': now(),
            'fact': self.fact
        }
