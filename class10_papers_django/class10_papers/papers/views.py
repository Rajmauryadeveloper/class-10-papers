from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Query

# ---------------------------------------------------------------------------
# Static content for each Class 10 subject.
# Edit / expand this dictionary to add real syllabus content, chapter-wise
# notes, sample papers, etc.
# ---------------------------------------------------------------------------
SUBJECTS = {
    'maths': {
        'name': 'Mathematics',
        'icon': '📐',
        'summary': 'Algebra, Geometry, Trigonometry, Statistics & Probability for Class 10.',
        'topics': [
            'Real Numbers',
            'Polynomials',
            'Pair of Linear Equations in Two Variables',
            'Quadratic Equations',
            'Arithmetic Progressions',
            'Triangles & Coordinate Geometry',
            'Trigonometry & its Applications',
            'Circles and Constructions',
            'Areas Related to Circles',
            'Surface Areas and Volumes',
            'Statistics and Probability',
        ],
        'sample_papers': [
            {'title': 'Maths Sample Paper 1 (Standard)', 'link': '#'},
            {'title': 'Maths Sample Paper 2 (Basic)', 'link': '#'},
        ],
    },
    'science': {
        'name': 'Science',
        'icon': '🔬',
        'summary': 'Physics, Chemistry and Biology concepts covered in the Class 10 syllabus.',
        'topics': [
            'Chemical Reactions and Equations',
            'Acids, Bases and Salts',
            'Metals and Non-metals',
            'Carbon and its Compounds',
            'Life Processes',
            'Control and Coordination',
            'Heredity and Evolution',
            'Light – Reflection and Refraction',
            'The Human Eye and the Colourful World',
            'Electricity & Magnetic Effects of Current',
            'Our Environment',
        ],
        'sample_papers': [
            {'title': 'Science Sample Paper 1', 'link': '#'},
            {'title': 'Science Sample Paper 2', 'link': '#'},
        ],
    },
    'social-science': {
        'name': 'Social Science',
        'icon': '🌍',
        'summary': 'History, Geography, Political Science and Economics for Class 10.',
        'topics': [
            'The Rise of Nationalism in Europe',
            'Nationalism in India',
            'The Making of a Global World',
            'Resources and Development',
            'Water Resources',
            'Agriculture & Manufacturing Industries',
            'Power Sharing and Federalism',
            'Political Parties & Democracy',
            'Development and Sectors of the Economy',
            'Money and Credit',
            'Globalisation and the Indian Economy',
        ],
        'sample_papers': [
            {'title': 'Social Science Sample Paper 1', 'link': '#'},
            {'title': 'Social Science Sample Paper 2', 'link': '#'},
        ],
    },
    'english': {
        'name': 'English',
        'icon': '📖',
        'summary': 'First Flight & Footprints without Feet — prose, poetry, grammar and writing skills.',
        'topics': [
            'A Letter to God / Nelson Mandela: Long Walk to Freedom',
            'Two Stories about Flying / From the Diary of Anne Frank',
            'Glimpses of India / Madam Rides the Bus',
            'The Hundred Dress I & II',
            'Poetry: Dust of Snow, Fire and Ice, A Tiger in the Zoo',
            'Grammar: Tenses, Modals, Reported Speech, Determiners',
            'Writing Skills: Letter Writing, Analytical Paragraph',
            'Footprints without Feet (Supplementary Reader)',
        ],
        'sample_papers': [
            {'title': 'English Sample Paper 1', 'link': '#'},
            {'title': 'English Sample Paper 2', 'link': '#'},
        ],
    },
    'hindi': {
        'name': 'Hindi',
        'icon': '✒️',
        'summary': 'क्षितिज एवं कृतिका पाठ्यक्रम — गद्य, पद्य, व्याकरण और लेखन कौशल।',
        'topics': [
            'सूरदास, तुलसीदास, देव (पद्य खंड)',
            'नेताजी का चश्मा, बालगोबिन भगत (गद्य खंड)',
            'माता का अँचल, साना-साना हाथ जोड़ि',
            'व्याकरण: पद परिचय, रचना के आधार पर वाक्य भेद',
            'पत्र लेखन एवं अनुच्छेद लेखन',
            'कृतिका: माता का अँचल, तताँरा वामीरो कथा',
        ],
        'sample_papers': [
            {'title': 'हिंदी सैंपल पेपर 1', 'link': '#'},
            {'title': 'हिंदी सैंपल पेपर 2', 'link': '#'},
        ],
    },
}


def home(request):
    """Landing / intro page with a button for each subject."""
    context = {
        'subjects': [
            {'slug': slug, **data} for slug, data in SUBJECTS.items()
        ]
    }
    return render(request, 'papers/home.html', context)


def subject_detail(request, subject_slug):
    """Subject page: content + a query form for that subject."""
    subject = SUBJECTS.get(subject_slug)
    if subject is None:
        return render(request, 'papers/404_subject.html', status=404)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        question = request.POST.get('question', '').strip()

        if name and question:
            Query.objects.create(
                subject=subject_slug.replace('-', '_'),
                name=name,
                email=email,
                question=question,
            )
            messages.success(
                request,
                "Thanks! Your question has been submitted. We'll get back to you soon."
            )
            return redirect(reverse('subject_detail', args=[subject_slug]) + '#query')
        else:
            messages.error(request, "Please fill in your name and question before submitting.")

    context = {
        'slug': subject_slug,
        'subject': subject,
    }
    return render(request, 'papers/subject_detail.html', context)
