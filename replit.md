# AV Post

A single-page digital corporate newspaper/newsletter for "Best Brands". It is a self-contained multilingual (Ukrainian/Russian) interactive web page mimicking the layout of a physical newspaper.

## Tech Stack

- **Frontend:** Pure static HTML/CSS/JavaScript (no framework, no build step)
- **Languages:** Ukrainian and Russian (toggled via JS)
- **Server (dev):** Python's built-in `http.server` on port 5000

## Project Structure

```
/
├── index.html       # The entire app (HTML, CSS, JS, and base64 images all-in-one)
└── replit.md        # This file
```

## Running the App

The workflow starts a Python HTTP server:

```
python3 -m http.server 5000 --bind 0.0.0.0
```

## Deployment

Configured as a **static** site deployment — the root directory (`.`) is the public directory.

## Features

- Multilingual toggle (UA/RU)
- Interactive personality quiz with confetti
- Horoscope section with wine pairings
- Accordion-style zodiac navigation
- Responsive design (mobile, tablet, desktop)
