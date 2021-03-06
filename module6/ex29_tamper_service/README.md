# Tamper service

Last week, we implemented the `/scan` and `/rescan` URLs. When we invoke `/rescan`, we get back a list of the files that have changed. This week, we'll turn our application into a primitive Web service, such that it returns JSON, rather than text.

In other words: `/rescan` should return its results in JSON format to an HTTP client requesting the results.

But wait, what HTTP client should we use?

That's part two of this week's exercise: I want you to create a simple client that can retrieve the JSON results, and then display them locally. You should use the `requests` package (available via PyPI) to retrieve the JSON. Then translate it into something viewable and usable, and print those results on the screen.

In other words, we're taking our little Web app and turning it into a little Web service. And then we're using `requests` to create something that can consume the Web service.
