# Blog Website using Flask

A simple blog website built using Python and Flask. It fetches blog posts from an external API and displays them dynamically. It also includes a contact form that sends messages directly to an email address using SMTP.

## About the Project

I built this project to practise Python web development and understand how Flask works.

While building it, I worked with Flask routes, HTML templates, API requests and email integration.

## Features

- Homepage displaying blog posts.
- Individual pages for each blog post.
- About page.
- Contact page with a working contact form.
- Fetching blog content from an external API.
- Sending contact form messages through Gmail SMTP.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Requests
- SMTP

## Project Structure

```text
BLOG-WEBSITE/
│
├── static/
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── post.html
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

**1. Clone this repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Open the project folder**

```bash
cd BLOG-WEBSITE
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the environment**

Windows:

```bash
.venv\Scripts\activate
```

**5. Install the required packages**

```bash
pip install -r requirements.txt
```

**6. Configure environment variables**

Create a `.env` file in the project folder and add your Gmail credentials:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
FLASK_DEBUG=1
```

Use a Gmail App Password instead of your regular Gmail password.

**7. Run the application**

```bash
python main.py
```

Open your browser and visit:

`http://127.0.0.1:5001`

## What I Learned

- Creating web applications using Flask.
- Working with Flask routing.
- Fetching data from external APIs.
- Passing data into HTML templates.
- Handling HTML form submissions.
- Sending emails using Python SMTP.

## Future Improvements

- Add a database to store blog posts.
- Add an admin panel.
- Improve form validation.
- Deploy the website online.

## Author

**Your Name**

GitHub: YOUR_GITHUB_PROFILE_LINK
