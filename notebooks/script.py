import os  # importing os module

# defining Env variable with 'HOME' as value
key = "LAL"

# invoking getenv() method
value = os.getenv(key, default=None)
print(f"Value of env variable key='LAL': {value}")
