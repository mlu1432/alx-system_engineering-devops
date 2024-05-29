0x12. Web Stack Debugging 2
Tasks
0. Run software as another user
The root user is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in as the root user, as if you fat finger a command and, for example, run rm -rf /, there is no comeback. 

1. Run Nginx as Nginx
The root user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as root. With this in mind, it’s a good practice not to run your web servers as root (which is the default for most configurations) and instead run the process as the less privileged nginx user instead.

2. 7 lines or less
Using what you did for task #1, make your fix short and sweet.
