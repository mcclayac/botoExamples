__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/24/17'
__revision__ = '$'
__revision_date__ = '$'


import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()



# >>> import urllib.request
# >>> import urllib.parse
# >>> data = {}
# >>> data['name'] = 'Somebody Here'
# >>> data['location'] = 'Northampton'
# >>> data['language'] = 'Python'
# >>> url_values = urllib.parse.urlencode(data)
# >>> print(url_values)  # The order may differ from below.
# name=Somebody+Here&language=Python&location=Northampton
# >>> url = 'http://www.example.com/example.cgi'
# >>> full_url = url + '?' + url_values
# >>> data = urllib.request.urlopen(full_url)