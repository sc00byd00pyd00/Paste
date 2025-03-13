import socket
import ssl
import base64
import re
import argparse

def create_http_request(url, password):
    # Parse the URL to extract host and path
    host = re.search(r'https?://([^/]+)', url).group(1)
    path = re.sub(r'https?://[^/]+', '', url)
    if not path:
        path = '/'

    # Create HTTP GET request with Basic Auth
    auth_header = f"Authorization: Basic {base64.b64encode(password.encode()).decode()}"
    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"{auth_header}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    return host, request.encode()

def fetch_pastebin_content(url, password):
    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = context.wrap_socket(sock, server_hostname=host)

        # Connect to the server
        sock.connect((host, 443))

        # Send the HTTP request
        sock.sendall(request)

        # Receive the response
        response = b""
        while True:
            data = sock.recv(4096)
            if not data:
                break
            response += data

        # Decode the response
        response = response.decode('utf-8', errors='ignore')

        # Extract the body from the HTTP response
        header, body = response.split('\r\n\r\n', 1)
        return body.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        sock.close()

def save_to_file(content, filename):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content successfully saved to {filename}")
    except IOError as e:
        print(f"An error occurred while saving the file: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Fetch content from a Pastebin link with a password and save it to a file.")
    parser.add_argument("url", help="The Pastebin URL to fetch content from.")
    parser.add_argument("password", help="The password to access the Pastebin content.")
    parser.add_argument("output_filename", help="The filename to save the content to.")
    args = parser.parse_args()

    # Create the HTTP request
    global host, request
    host, request = create_http_request(args.url, args.password)

    # Fetch the content from Pastebin
    content = fetch_pastebin_content(args.url, args.password)

    if content:
        # Save the content to a file
        save_to_file(content, args.output_filename)
    else:
        print("No content to save.")

if __name__ == "__main__":
    main()
