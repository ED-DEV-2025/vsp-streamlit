# Adaptive Virtual Simulated Patient Builder

This repository contains a simple browser‑based prototype for building and running virtual simulated patient (VSP) cases. Everything runs client side so it can be hosted with GitHub Pages or embedded in an LMS via an iframe.

## Features
* **Case Builder** – enter patient demographics, background information and a correct diagnosis. Optionally provide sample question/answer pairs in JSON form.
* **Chat Simulation** – chat with the patient. Responses are generated using the OpenAI Chat API (supply your API key in the page).
* **Consultation Scoring** – basic scoring rewards the use of open‑ended questions. The score updates after each learner message.
* **Diagnostic Checks** – every five exchanges the learner is asked for a working diagnosis. A simple text similarity check compares it to the case diagnosis and reveals the answer when 70% similarity is reached.

## Usage
Open `docs/index.html` in a browser or enable GitHub Pages for the `docs` folder. Enter your OpenAI API key, fill in the case details and start chatting.

This is a lightweight proof of concept and does not include a backend. Contributions are welcome!
