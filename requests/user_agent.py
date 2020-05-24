# Creating fake User Agent
# User agent is a software that sends requests to browser in behalf of user.
# Browsers like Google chrome, Mozilla firefox are  user agents.

from fake_useragent import UserAgent

ua = UserAgent()
header = {"user_agent": ua.chrome}
print(ua.chrome)
