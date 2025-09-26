# Rowlett Group of AA - Website

This repository contains the source code for the official website of the Rowlett Group of Alcoholics Anonymous. It is a single-page application (SPA) designed to be a comprehensive resource for new and existing members.

## Project Purpose

The primary purpose of this website is to carry the message of Alcoholics Anonymous to the alcoholic who still suffers. It serves as a central point of information for the Rowlett Group, providing meeting schedules, contact information, literature, and resources for recovery. The site is designed to be welcoming, informative, and easily accessible to anyone seeking help with a drinking problem.

## Features

- **Single-Page Application (SPA):** Fast, responsive navigation without full page reloads.
- **Dynamic Meeting Schedule:** Displays the full weekly meeting schedule, highlighting the current day's meetings and special events.
- **Meeting Filters:** Allows users to filter the schedule to show "Open" or "Closed" meetings.
- **Interactive Literature Library:** Provides access to the A.A. Big Book and Twelve Steps and Twelve Traditions. Users can read PDF versions or watch American Sign Language (ASL) video interpretations.
- **Service Information:** Details opportunities for members to get involved in service work.
- **Group History:** A detailed timeline of the Rowlett Group's history.
- **Big Book Study Guide:** An interactive guide with a color-coding system and a dictionary lookup tool to assist with studying A.A. literature.
- **Contact and Location Info:** Includes an embedded Google Map and a contact form.
- **Contribution Information:** Provides clear instructions for making 7th Tradition contributions via Zelle or mail.
- **PWA-Enabled:** A service worker provides basic offline caching for improved reliability.
- **SEO Optimized:** Uses JSON-LD structured data to improve search engine visibility.

## Technology Stack

- **HTML5:** The core structure of the website.
- **CSS3:** Custom styles for layout, theming, and animations.
    - **Tailwind CSS:** A utility-first CSS framework used for most of the styling.
- **JavaScript (ES6+):** Powers all the dynamic functionality, SPA routing, and interactivity.
- **No external build tools or frameworks:** The site is built with vanilla HTML, CSS, and JavaScript for simplicity and ease of maintenance.

## File Structure & Core Concepts

- **`index.html`:** The single file that contains the entire application.
    - **`<head>`:** Contains metadata, links to external resources (Tailwind CSS, Font Awesome, Google Fonts), custom styles, and JSON-LD for SEO.
    - **`<body>`:**
        - **`<header>`:** The sticky navigation bar.
        - **`<main>`:** Contains a series of `<section>` elements, each acting as a separate "page". All sections except the active one are hidden using the `hidden` class.
        - **`<script>`:** The main JavaScript block at the end of the file. It controls the entire application's logic.
- **`README.md`:** This file.

### Core Concepts

1.  **SPA Routing:** The application uses the URL hash (`#`) to determine which page (i.e., which `<section>`) to display. A `hashchange` event listener calls a `showPage(pageId)` function to manage visibility.
2.  **Dynamic Content:** Sections like the schedule, literature library, and group history are generated dynamically by JavaScript functions (e.g., `initializeSchedule()`). This keeps the HTML clean and makes content updates easier. These initialization functions are designed to run only once per page load to avoid redundant work.
3.  **Event Delegation:** A single `click` event listener on the `document.body` handles most UI interactions (navigation, accordions, tabs) for efficiency.

## Local Development & Setup

Since this project uses no build tools, setup is straightforward.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```
2.  **Serve the file locally:**
    You cannot simply open `index.html` directly in your browser from the file system (`file:///...`) because the service worker and some APIs may not function correctly. You need to serve it from a local web server.

    If you have Python installed, you can easily start a server:

    ```bash
    # For Python 3
    python -m http.server 8000
    ```

    If you have Node.js installed, you can use `http-server`:
    ```bash
    # Install it globally if you haven't already
    npm install -g http-server

    # Run the server
    http-server -p 8000
    ```

3.  **Access the site:**
    Open your web browser and navigate to `http://localhost:8000`.

## Contribution Guidelines

We welcome contributions to improve the website. Please follow these guidelines:

1.  **Create an Issue:** Before starting work on a new feature or bug fix, please open an issue to discuss the proposed changes.
2.  **Fork the Repository:** Create a fork of the project to your own GitHub account.
3.  **Create a Branch:** Create a descriptive branch name for your feature or fix (e.g., `feature/add-new-event` or `fix/mobile-menu-bug`).
4.  **Write Clean Code:**
    - Follow the existing coding style.
    - Add comments to new or complex JavaScript logic.
    - Ensure the site remains accessible and responsive.
5.  **Test Your Changes:** Thoroughly test your changes on different devices and browsers to ensure there are no regressions.
6.  **Submit a Pull Request:** Push your changes to your fork and submit a pull request to the main repository. Provide a clear description of the changes you have made.