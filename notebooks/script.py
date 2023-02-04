import os  # importing os module

# defining Env variable with 'HOME' as value
key = "LAL"

# invoking getenv() method
value = os.getenv(key, default=None)
with open("output.txt", "w") as f:
    f.write(f"Value of env variable key='HOME': {value}\n")
