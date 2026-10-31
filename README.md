
# CA Havran Jiří - Web Presentation

A modern, responsive business website built for a local travel agency (CA Havran Jiří) to establish their online presence, showcase services, and allow clients to easily send inquiries.

## Features & What It Does
- **Interactive Homepage & Sections:** Clear presentation of agency services, contact details, and business hours.
- **Working Inquiry Form:** Fully functional contact form where users can submit their name, email, phone number, and message.
- **Backend Email Integration:** Connected to a Python (FastAPI) backend deployed on Vercel that processes form submissions and sends emails via SMTP with proper `Reply-To` functionality.
- **GDPR Compliance:** Integrated data privacy notice informing users about personal data processing for inquiry handling.
- **Responsive Design:** Optimized layout that works seamlessly on both mobile devices and desktop computers.

## Live Demo
Check out the live website here: [https://ca-jiri-havran.vercel.app/](https://ca-jiri-havran.vercel.app/)

## Tech Stack
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Backend:** Python, FastAPI, fastapi-mail
- **Hosting & Deployment:** Vercel


## also a word from me
Its a website i build for my friend because he just started getting into these tech stuff. i wanted to help him so i made him a website that contains a form and his contact info.

This site is custom build by me (and a bit from claude) but this website looks like a postcard. Do you remember licking those poststamps or how you call them in english

## How to run locally

1. **Clone this repo**
```bash
git clone https://github.com/citunek22/CA-Jiri-Havran
cd CA-Jiri-Havran
```

2. **Setup the backend (Python)**
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

3. **Open the file**
Simply open the `index.html` file in your browser or use a Live Server extension in VS Code.

## Preview
This is how it looks like I think it looks like a postcard:
<img width="1080" height="2243" alt="1000043611" src="https://github.com/user-attachments/assets/4cb2c9f9-3a58-41b2-8ced-cf268ba849cf" />
