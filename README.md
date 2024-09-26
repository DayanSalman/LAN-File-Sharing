---
# LAN File Sharing & Code Snippet Manager

A lightweight web application that facilitates **file sharing** over a Local Area Network (LAN) and allows users to **save, manage, and share code snippets** securely. The app uses Flask as the backend framework with basic authentication for security, and a responsive frontend built using HTML, Bootstrap, and JavaScript.

## Features

- **File Upload & Download**: Upload and download files securely within your LAN.
- **Code Snippet Manager**: Save, manage, and retrieve code snippets.
- **Basic Authentication**: Secure the web interface using HTTP Basic Authentication.
- **Responsive UI**: The frontend is built with Bootstrap for mobile-friendly views.
- **File & Code Management**: Clear all uploaded files or saved code snippets with one click.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Key Features](#key-features)
4. [File Structure](#file-structure)
5. [Tech Stack](#tech-stack)
6. [Future Enhancements](#future-enhancements)
7. [Contributing](#contributing)
8. [License](#license)

---

## Installation

### Prerequisites

- Python 3.x
- Flask
- Bootstrap (for frontend UI)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/DayanSalman/LAN-File-Sharing.git
    cd LAN-File-Sharing
    ```
    
2. Run the Flask application:
    ```bash
    python app.py
    ```

3. Access the application at `http://localhost:80` or via your LAN's local IP address.

## Usage

1. **Upload Files**:
   - Navigate to the file upload section, select a file, and hit "Upload". The uploaded file will be stored on the server and listed for download.
   
2. **Download Files**:
   - Click on any listed file to download it to your local machine.

3. **Save Code Snippets**:
   - Enter your code in the text area provided and click "Save Code". Saved code snippets will appear in the list below, where they can be copied or cleared.

4. **Clear Files and Code Snippets**:
   - Use the provided buttons to clear all uploaded files or code snippets from the server.

### Security

The application requires basic authentication for all endpoints. You can modify the `users` dictionary in the `app.py` file to set your own username and password for secure access.

```python
users = {
    "admin": "password"  # Change this for security purposes
}
```

## Key Features

- **File Sharing**: Easily upload and download files within a LAN environment.
- **Code Snippet Management**: Store and retrieve code snippets.
- **Authentication**: Uses HTTP Basic Authentication to secure file uploads/downloads and code management.
- **Responsive Design**: A mobile-friendly UI built with Bootstrap 4.
- **File Management**: Option to clear all uploaded files and code snippets with one click.

## File Structure
```bash
LAN-File-Sharing/
│
├── LAN_Sharing/               
│   ├── auth.py                 # Authentication handling
│   └── templates/
│       └── index.html          # Main HTML file for the web interface
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, Bootstrap, JavaScript
- **Authentication**: HTTP Basic Authentication (Flask-HTTPAuth)
- **File Handling**: Python `os` module and Flask's `send_from_directory`

## Future Enhancements

- **Production Deployment**: Migrate the app from a development server to a production server (e.g., using **Gunicorn**).
- **HTTPS Support**: Implement HTTPS for secure data transmission.
- **Enhanced Authentication**: Add OAuth or token-based authentication for enhanced security.
- **Cloud Deployment**: Deploy the application to cloud services like **Heroku**, **AWS**, or **Google Cloud** for easy access over the internet.
- **Database Integration**: Use a database (e.g., SQLite, PostgreSQL) to store file and code metadata.
- **User Management**: Add support for multiple users with different roles and permissions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

To contribute:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/NewFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to modify this README to fit your project specifics and add any additional sections as needed!

