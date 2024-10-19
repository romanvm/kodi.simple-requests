# simple-requests

## Description

**simple-requests** is a simple Python library for making HTTP requests with API similar to the 
popular **requests** library.
It depends only on the Python standard library and uses **urllib.request** module internally.

### Supported:

* HTTP methods: GET, POST
* HTTP and HTTPS.
* Disabling SSL certificates validation.
* Request payload as form data, JSON and raw binary data.
* Custom headers.
* Cookies.
* Basic authentication.
* Gzipped response content.

### Not supported:

* File upload.
* Persistent Session objects. Since Python's built-in **urllib.request** does not support keep-alive
  connections, persistent sessions do not make much sense in this case.
* Streaming requests and responses. simple-requests is not suitable for sending and receiving
  large volumes of data.

With the limitations listed above it can serve as a drop-in replacement for **requests**.

## Motivation

The **simple-requests** library is designed to be used as a library addon for [Kodi mediacenter](https://github.com/xbmc/xbmc).
While **requests** library is available for Kodi Python addons, it is quite heavy and has several dependencies,
that is why it can slow down addon start-up, especially on low-performance systems like single-board computers.
It is also overkill for simple scenarios like interacting with various information APIs or web page loading
that require only GET or POST requests.
On the other side, Python's built-in **urllib.request** module is quite verbose and not very intuitive to use. That is why
**simple-requests** was created as a wrapper for **urllib.request** with a familiar API of **requests** library.

## Examples:

```python
from pprint import pprint

import simple_requests as requests

response = requests.get('https://httpbin.org/html')
if not response.ok:
    response.raise_for_status()
print(response.text)

response = requests.post('https://httpbin.org/post', data={'username': 'foo', 'password': 'bar'})
if not response.ok:
    response.raise_for_status()
pprint(response.json())
```

License: [MIT](https://opensource.org/license/mit)
