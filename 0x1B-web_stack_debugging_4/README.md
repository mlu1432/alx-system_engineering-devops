## 0x1B-web_stack_debugging_4
# Web Stack Debugging 4

In this web stack debugging task, we encountered a high number of failed requests on our web server setup featuring Nginx. To address this issue, we used ApacheBench to simulate HTTP requests and identified that 943 requests failed out of 2000 requests made.

To fix the stack and reduce the number of failed requests to 0, we performed the following steps:

1. Analyzed the logs: We reviewed the logs to gain insights into the root cause of the failed requests. Logs are valuable resources when troubleshooting web server issues.

2. Applied necessary fixes: Based on the analysis, we made the required changes to the stack configuration to resolve the issues causing the failed requests.

3. Verified the fix: After applying the fixes, we re-ran the ApacheBench test with 2000 requests and observed that all requests were successfully completed without any failures.
