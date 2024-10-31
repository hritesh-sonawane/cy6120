import pickle
import base64

original_session_data = {
    'username': 'hritesh',
    'role': 'user'
}

original_session_data['role'] = 'admin'
pickled_data = pickle.dumps(original_session_data)
encoded_data = base64.b64encode(pickled_data).decode('utf-8')

print(encoded_data)

#####