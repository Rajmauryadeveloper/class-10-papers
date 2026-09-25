# Class 10 Subject Papers — Django Website

A simple Django site with:
- **Home page** — intro + 5 buttons (Maths, Science, Social Science, English, Hindi)
- **Subject pages** — syllabus topics, sample papers, and a **query/question form**
  for each subject (saved to the database, viewable in Django admin)

## Folder structure

```
class10_papers/
├── manage.py
├── requirements.txt
├── db.sqlite3                # created after migrate
├── class10_papers/           # project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── papers/                   # app
    ├── __init__.py
    ├── admin.py
    ├── models.py              # Query model
    ├── views.py                # SUBJECTS content + views
    ├── urls.py
    ├── migrations/
    ├── static/papers/css/style.css
    └── templates/papers/
        ├── base.html
        ├── home.html
        ├── subject_detail.html
        └── 404_subject.html
```

## Setup

```bash
# 1. Create & activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations (creates the Query table)
python manage.py makemigrations
python manage.py migrate

# 4. (Optional) create an admin user to view submitted questions
python manage.py createsuperuser

# 5. Run the dev server
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** — you'll see the home page with 5 subject
buttons. Each subject page shows its topics/sample papers and has a form at
the bottom to submit a question. Submitted questions are stored in the
`Query` model and visible at **http://127.0.0.1:8000/admin/**.

## Customizing content

All subject text (topics, summaries, sample-paper links) lives in the
`SUBJECTS` dictionary at the top of `papers/views.py` — edit it to add real
notes, PDFs, or links to sample papers per subject.

## Adding a 6th subject

1. Add an entry to `SUBJECTS` in `papers/views.py` with a unique slug key.
2. It will automatically get a button on the home page and its own page at
   `/subject/<slug>/` — no template or URL changes needed.
