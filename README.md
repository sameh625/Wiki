# Wiki Encyclopedia

A Django-based encyclopedia web app that allows users to view, search, create, edit, and browse random Markdown-based entries.

---

## Features

- **Entry Page:**  
  Visit `/wiki/TITLE` to view an encyclopedia entry. If the entry exists, its Markdown content is converted to HTML and displayed. If not, an error page is shown.

- **Index Page:**  
  The home page lists all entries. Each entry name is a clickable link to its page.

- **Search:**  
  - Use the sidebar search box to find entries.
  - If your query matches an entry title exactly, you are redirected to that entry.
  - If not, you see a results page listing all entries containing the query as a substring (case-insensitive). Each result is a clickable link.

- **New Page:**  
  - Click “Create New Page” in the sidebar to add a new entry.
  - Enter a title and Markdown content.
  - If the title already exists, you’ll see an error message.
  - Otherwise, the entry is saved and you’re redirected to its page.

- **Edit Page:**  
  - On any entry page, click “Edit Page” to modify its Markdown content.
  - The textarea is pre-filled with the current content.
  - Save changes to update the entry and return to its page.

- **Random Page:**  
  - Click “Random Page” in the sidebar to be taken to a random entry.

- **Markdown to HTML:**  
  - All entry content is stored in Markdown and rendered as HTML using the [`markdown2`](https://github.com/trentm/python-markdown2) library.

---

## Setup

1. **Clone the repository and install dependencies:**
    ```sh
    pip install django markdown2
    ```

2. **Run migrations:**
    ```sh
    python manage.py migrate
    ```

3. **Start the development server:**
    ```sh
    python manage.py runserver
    ```

4. **Access the app:**  
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## File Structure

- `encyclopedia/views.py` — All main view logic (index, entry, search, create, edit, random).
- `encyclopedia/util.py` — Utility functions for reading/writing entries.
- `encyclopedia/templates/encyclopedia/` — All HTML templates.
- `encyclopedia/static/encyclopedia/styles.css` — CSS styles.

---

## Notes

- Entries are stored as Markdown files in the `entries/` directory.
- The app uses Django’s default file storage for reading/writing entries.
- Error handling is provided for non-existent entries and duplicate titles.
- All Markdown is converted to HTML before display.

---
