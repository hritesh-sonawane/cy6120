# TokenTracker

[⛳️ Github Link](https://github.com/hritesh-sonawane/cy6120/tree/main/assignments/a1-detecting-hardcoded-secrets)

## Overview

This tool detects hardcoded Calendly API tokens in files. Hardcoding sensitive information, such as API tokens, is a common security vulnerability. This program uses regular expressions (regex) to identify such occurrences.

## Features

- **v1:** Basic detection of Calendly API tokens.
- **v2:** Improved detection that filters out obvious invalid tokens.
- **v3:** Validation of detected tokens to identify active and inactive tokens.

## Token Format

Calendly API tokens typically follow the format:
- Starts with `eyJ_`
- Followed by a string of characters (alphanumeric and special characters).

## File Structure

```
project-directory/
│
├── a1/                         # Virtual environment
├── test_files/                 # Sample files for testing
│   ├── sample_config.yaml      # Sample configuration file
│   ├── sample_py_code.py       # Sample Python code for token usage
│   └── sample_tokens.txt       # Sample tokens
│
├── .env                        # Environment variables
├── api_test_script.py          # Script to test API token
├── detector.py                 # Main detection script
└── README.md                   # Project documentation
```

**For ease of grading, this is the content of .env file:**
   ```bash
   CALENDLY_API_TOKEN=eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzI3NzI0MTk5LCJqdGkiOiJiYmMxZTM5MC02NWY4LTRhNTUtODI5MS1mZmM5NDI3MTMwYzgiLCJ1c2VyX3V1aWQiOiJhODk3ZDFjMC00ZjA5LTQ5NTAtOWQyNS1lNGQ1YTBiZjdiODYifQ.s8ormtTmtuPtypOkIK-YDlo-3OcVLEnHepN1lHd7tBdf8F9zoctC_O_1TIcqXFtKg6TlhCUn1h82iHd00Blc0g

# Token 1 - INACTIVE (revoked)
# eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzI3NzI0MDkwLCJqdGkiOiIzZDM3M2JlZS00MDMxLTQwYjYtOWY5Ni1mNDhhZjBjZDcyNTMiLCJ1c2VyX3V1aWQiOiJhODk3ZDFjMC00ZjA5LTQ5NTAtOWQyNS1lNGQ1YTBiZjdiODYifQ.2LMRlAxBq2r7kz5lyoA3G0xBGCp97X_CTW7wRYoHIvmYutHvPeWAMRpwp3VpSAns7MdRGwZbQj6szDAT6r7RWw

# Token 2 - ACTIVE
# eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzI3NzI0MTk5LCJqdGkiOiJiYmMxZTM5MC02NWY4LTRhNTUtODI5MS1mZmM5NDI3MTMwYzgiLCJ1c2VyX3V1aWQiOiJhODk3ZDFjMC00ZjA5LTQ5NTAtOWQyNS1lNGQ1YTBiZjdiODYifQ.s8ormtTmtuPtypOkIK-YDlo-3OcVLEnHepN1lHd7tBdf8F9zoctC_O_1TIcqXFtKg6TlhCUn1h82iHd00Blc0g

# Token 3 - ACTIVE
# eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzI3NzQwMzk4LCJqdGkiOiJkOTNjZjM2My04ZTlhLTQ5NjktYWQ3OC00NTYxZDY4ZjE1MDQiLCJ1c2VyX3V1aWQiOiJhODk3ZDFjMC00ZjA5LTQ5NTAtOWQyNS1lNGQ1YTBiZjdiODYifQ.Iq-ELtZqmUIsMEKFgc0Rt4U3EtKQpatlj-VPB6O_Nm4r71c13FwGU_n6uEWhIP-801rgUuMTgpEe010O0FeqXw
   ```

**Run the detection script:**
   Use the following command to scan a specified directory for hardcoded tokens:
   ```bash
   python detector.py <directory_path>
   ```

