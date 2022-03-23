from django.test import TestCase

# Create your tests here.

import numpy
import pandas

d = {'Tom': 1, 'Mary': 2, 'Mark': '3'}
r = d['Tom'] + d['Mark']
df = pd.DataFrame([d])
