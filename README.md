# SisPeC Website Documentation

This document provides an overview of the SisPeC accounting website implementation.

## Project Structure
```
C:\Users\ericssonlc\dev\sispec\website\
├── app.py
├── requirements.txt
├── SisPeC.png
├── start_server.bat
├── sispec_env\
│   ├── Scripts\
│   └── ...
├── static\
│   └── SisPeC.png
└── templates\
    └── index.html
```

## Features Implemented

### 1. Color Scheme
The website uses the following color palette:
- Primary: #049b8c (teal)
- Secondary: #246cc3 (blue)
- Accent: #1484a6 (dark teal)
- Light Accent: #0c8c9c (light teal)
- Dark Accent: #1c7cb1 (dark blue)

### 2. Navigation
- Fixed header with centered navigation menu
- Smooth scrolling to sections
- Active state highlighting for current section
- Improved hover effects with subtle animations

### 3. Sections
- **Home**: Hero section with company description and call-to-action buttons
- **Notícias**: Latest news and updates section
- **Serviços**: Services offered section with service cards
- **Simuladores**: Tax calculation tools section
- **Quem Somos**: About us section with team information
- **Contato**: Contact form section

### 4. UI/UX Improvements
- Enhanced color usage throughout the site
- Improved visual hierarchy with shadows and borders
- Better interactive elements with hover effects
- Responsive design for all devices
- Improved form elements with focus states
- Decorative elements for section titles

### 5. Logo Implementation
- SisPeC logo positioned on the left side of the header
- Logo size increased for better visibility
- Proper alignment with the navigation menu

## Technical Details

### Dependencies
- Flask (web framework)
- Flask-Bootstrap (for styling)
- Requests (for HTTP requests)
- BeautifulSoup4 (for web scraping)

### Setup Instructions
1. Create virtual environment: `python -m venv sispec_env`
2. Activate virtual environment: `sispec_env\Scripts\activate.bat`
3. Install dependencies: `pip install -r requirements.txt`
4. Start the server: `python app.py` or use `start_server.bat`

## Running the Application
The application can be started using the batch file:
```
start_server.bat
```

The website will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Recent Changes
- Increased the size of the top bar and logo
- Properly aligned the menu with the center of the page (ignoring the SisPeC logo)
- Positioned the SisPeC logo more to the left, separated from the menu
- Improved UX/UI with better color usage throughout the site
- Updated the image next to "Nossa História" to something more appropriate for the accounting context