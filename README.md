backports.html
==============


This is a backport of Python3.4+'s `html` module, original code from [Python's standard library][1]

[1]: https://github.com/python/cpython/blob/master/Lib/html/

Install and use
---------------

```bash
$ pip install backports.html
```
```python
try:
    import html     # use standard library if available
except ImportError:
    import backports.html as html   # fallback to backports
```

Licence
-------

MIT License, see [LICENSE](/LICENSE) for more details.
