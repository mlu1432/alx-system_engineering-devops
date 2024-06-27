# Web Stack Debugging Tasks

## Task 0: Sky is the limit, let's bring that limit higher

In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure. It turns out it’s not doing well: we are getting a huge amount of failed requests.

### Benchmarking
We are using ApacheBench, a popular tool in the industry, to simulate HTTP requests to a web server. In this case, we will make 2000 requests to our server with 100 requests at a time.

ask 1: User limit
Objective
Change the OS configuration so that it is possible to log in with the holberton user and open a file without any error message.

Issue
The holberton user was encountering "Too many open files" errors