# simple-requests

A simple Python library for making HTTP requests with API similar to the popular **requests** library.
It depends only on the Python standard library and uses **urllib.request** module internally.

Supported:
* HTTP methods: GET, POST
* HTTP and HTTPS.
* Disabling SSL certificates validation.
* Request payload as form data, JSON and raw binary data.
* Custom headers.
* Cookies.
* Basic authentication.
* Gzipped response content.

Not supported:
* File upload.
* Persistent Session objects. Since Python's built-in **urllib.request** does not support keep-alive
  connections, persistent sessions do not make much sense in this case.
* Streaming requests and responses. simple-requests is not suitable for sending and receiving
  large volumes of data.

With the limitations listed above it can serve as a drop-in replacement for **requests**.

Example:
```python
import simple_requests as requests

response = requests.get('https://example.com')
if not response.ok:
    response.raise_for_status()
print(response.text)

response = requests.post('https://example.com/login', data={'username': 'foo', 'password': 'bar'})
if not response.ok:
    response.raise_for_status()
print(response.text)
```

This library is packaged as a library addon for [Kodi mediacenter](https://github.com/xbmc/xbmc).
