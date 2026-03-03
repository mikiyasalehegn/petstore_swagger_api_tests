import time
from functools import wraps
import random
import string


def poll(timeout=40, interval=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()

            while time.time() - start_time < timeout:
                result = func(*args, **kwargs)

                if result:  # if function returns something truthy
                    return result

                time.sleep(interval)

            raise TimeoutError(f"Function {func.__name__} timed out after {timeout} seconds")

        return wrapper
    return decorator

def update_keys(data, **kwargs):
    for key in kwargs:
        data[key] = kwargs[key]
    return data

def random_string(length):
    # Generate random word (nonsense)
    random_word = ''.join(random.choices(string.ascii_letters, k=length))
    return random_word

@poll(timeout=40, interval=1)
def get_random_existing_id(api_client, max_id):
    random_id = random.randint(1, max_id)

    response = api_client(random_id)

    if response.status_code == 200:
        return response.json()["id"]

    return None  # tells decorator to retry