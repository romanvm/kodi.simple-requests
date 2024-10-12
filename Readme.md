# simple-requests

A simple Python library for making HTTP requests with API similar to the popular **requests** library.
It depends only on the Python standard library.

Supported:
* HTTP methods: GET, POST
* HTTP and HTTPS.
* Disabling SSL certificates validation.
* Request payload as form data, JSON and raw binary data.
* Custom headers.
* Basic authentication.
* Gzipped response content.

Not supported:
* Cookies.
* File upload.

With the limitation listed above it can serve as a drop-in replacement for **requests**.

This library is bundled as a library addon for [Kodi mediacenter](https://github.com/xbmc/xbmc).
