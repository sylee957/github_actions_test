import os

print("Hello world")
print(os.environ["TEST_SECRET"])
print(os.environ["TEST_SECRET"][0] == 'A')
