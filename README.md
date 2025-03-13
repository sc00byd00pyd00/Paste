# Pastebin Content Fetcher with Password Protection

This Python script is a **Pastebin Content Fetcher** that securely retrieves content from a Pastebin link protected by a password and saves it to a local file. The script is designed to be flexible, reusable, and user-friendly, allowing you to dynamically specify the Pastebin URL, password, and output filename via command-line arguments.

---

## Key Features

1. **Secure Content Retrieval**:
   - The script uses **Basic Authentication** to access password-protected Pastebin content.
   - The password is encoded in Base64 and included in the HTTP request headers.

2. **Manual HTTP Handling**:
   - Instead of relying on high-level libraries like `requests`, the script manually constructs and sends HTTP requests using Python's `socket` and `ssl` modules.
   - This provides a deeper understanding of how HTTP and HTTPS protocols work under the hood.

3. **Command-Line Arguments**:
   - The script accepts three required arguments:
     - `url`: The Pastebin URL to fetch content from.
     - `password`: The password to access the Pastebin content.
     - `output_filename`: The filename to save the retrieved content to.
   - This makes the script highly flexible and reusable for different tasks.

4. **Error Handling**:
   - The script includes robust error handling for network issues, SSL/TLS errors, and file operations.
   - If any step fails, the script provides clear error messages to help diagnose the issue.

5. **Low-Level Networking**:
   - The script demonstrates low-level networking concepts by manually creating and managing sockets, handling SSL/TLS encryption, and parsing HTTP responses.

6. **User-Friendly**:
   - The script provides a help menu (`-h` or `--help`) that explains how to use it, making it accessible even for users unfamiliar with the code.

---

## How It Works

1. **URL Parsing**:
   - The script extracts the host and path from the provided Pastebin URL.

2. **HTTP Request Construction**:
   - A raw HTTP GET request is constructed, including a `Basic Auth` header with the password encoded in Base64.

3. **Secure Communication**:
   - The script establishes a secure connection to the Pastebin server using SSL/TLS.

4. **Content Retrieval**:
   - The script sends the HTTP request, receives the response, and extracts the content from the response body.

5. **File Saving**:
   - The retrieved content is saved to the specified output file.

---

## Example Usage

To fetch content from a Pastebin link (`https://pastebin.com/raw/abc123`) with the password `mypassword` and save it to `output.txt`, run:

```bash
python script.py https://pastebin.com/raw/abc123 mypassword output.txt
