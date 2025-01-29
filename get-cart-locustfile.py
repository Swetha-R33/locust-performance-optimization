from locust import task, run_single_user, FastHttpUser
from insert_product import login # type: ignore


class Checkout(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    }

    def __init__(self, environment):
        super().__init__(environment)
        self.username = "test123"
        self.password = "test123"
        # Assuming login function returns a cookies dictionary
        cookies = login(self.username, self.password)
        self.token = cookies.get("token")  # Extract token from cookies

    @task
    def checkout_task(self):
        headers = {
            **self.default_headers,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,/;q=0.8",
            "Cookie": f"token={self.token}",
            "Referer": f"{self.host}/cart",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
        }

        # Perform the GET request for checkout page
        with self.client.get("/checkout", headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()  # Mark as successful if status is 200
            else:
                response.failure(f"Failed with status code: {response.status_code}")

    # Explicitly defining tasks attribute to include the checkout_task
    tasks = [checkout_task]

# This is the correct entry point for running the script
if __name__ == "__main__":
    run_single_user(Checkout)
