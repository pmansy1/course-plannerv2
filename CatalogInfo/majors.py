"""
majors.py

This module defines the major requirements for Trinity College undergraduate programs
in the specified 31 subjects. Each major (including both B.A. and B.S. versions when
applicable) has a dictionary containing:
    - required_courses: a list of course codes that are mandatory.
    - required_electives: a dictionary mapping elective categories to either lists of
      specific courses or an integer indicating how many electives in that category
      must be chosen.
    - allied_courses: (optional) a list of required allied or cognate courses.
    - capstone: (optional) a description of the senior capstone requirement.
    - note: (optional) special notes for programs without a formal major.

Course codes and categories are based on Trinity College’s 2024–2025 catalog. Comments
indicate sources or clarifications where relevant.
"""

majors = {
    "American Studies (B.A.)": {
        # Core courses: introductory survey and upper‐division seminar
        "required_courses": ["AMST 203", "AMST 301"],  # source: Trinity Catalog, “American Studies” section
        "required_electives": {
            "200-level American Studies": 2,   # two 200-level AMST courses (including AMST 203)
            "300-level American Studies": 4,   # four 300-level AMST courses (including AMST 301)
            "400-level American Studies": 2,   # two 400-level AMST seminars
            "AMST electives (any level)": 4    # four additional AMST electives (thesis may count as two)
        }
    },

    "Anthropology (B.A.)": {
        # Four core courses: foundational and theory/methods
        "required_courses": ["ANTH 101", "ANTH 301", "ANTH 302", "ANTH 401"],
        "required_electives": {
            "Ethnographic anthropology courses": 2,  # two ethnographic or regional area courses
            "Anthropology electives": 5             # five additional electives (≥1 at 300-level)
        }
    },

    "Art History (B.A.)": {
        # Core surveys and methods
        "required_courses": ["AHIS 101", "AHIS 102", "AHIS 301"],  # source: Trinity Catalog, “Art History” section
        "required_electives": {
            "Non-Western art history": 1,  # at least one course in Asian or other non-Western art
            "Art history electives": 7     # additional art history courses, to total 12 courses
        }
    },

    "Biology (B.A.)": {
        # Foundational sequence
        "required_courses": ["BIOL 182L", "BIOL 183L"],
        "required_electives": {
            "Breadth – Biodiversity": 1,         # one course in biodiversity (e.g., Botany, Invertebrate Zoology)
            "Breadth – Molecular/Cellular": 1,    # one course in cellular/molecular biology
            "Capstone in Biology": 1,             # one senior capstone seminar or research experience
            "Biology electives (200+ level)": 4   # four additional 200-level or higher electives
        },
        "allied_courses": [
            "CHEM 111L",                          # General Chemistry I (with lab)
            "CHEM 112L",                          # General Chemistry II (with lab)
            "one quantitative course (e.g., MATH 107, MATH 126, MATH 131, MATH 132, MATH 142, MATH 207, PSYC 221L)"
        ]
    },

    "Biology (B.S.)": {
        # B.S. includes Genetics in core
        "required_courses": ["BIOL 182L", "BIOL 183L", "BIOL 224L"],  # Genetics with lab
        "required_electives": {
            "Breadth – Biodiversity": 1,
            "Breadth – Molecular/Cellular": 1,
            "Capstone in Biology": 1,
            "Biology electives (200+ level)": 4
        },
        "allied_courses": [
            "CHEM 111L",
            "CHEM 112L",
            "PHYS 101L or CHEM 211L",  # Introductory Physics I or Organic Chemistry I (with lab)
            "one quantitative course (e.g., MATH 107, MATH 126, MATH 131, MATH 132, MATH 142, MATH 207, PSYC 221L)"
        ]
    },

    "Chemistry (B.S.)": {
        # Core chemistry sequence + advanced labs/theory
        "required_courses": [
            "CHEM 211L",  # Organic Chemistry I (with lab)
            "CHEM 212L",  # Organic Chemistry II (with lab)
            "CHEM 309L",  # Physical Chemistry I (with lab)
            "CHEM 310",   # Physical Chemistry II
            "CHEM 311L",  # Analytical Chemistry (with lab)
            "CHEM 312L",  # Physical Clean Lab (lab component for CHEM 310)
            "CHEM 313",   # Advanced Analytical Chemistry
            "CHEM 314L",  # Advanced Organic Chemistry Lab
            "PHYS 231L",  # Electricity & Magnetism (with lab)
            "MATH 132"    # Calculus II
        ],
        "required_electives": {
            "400-level Chemistry elective": 1  # one advanced (400-level) chemistry course
        }
    },

    "Computer Science (B.A.)": {
        # Core computer science courses
        "required_courses": [
            "CPSC 115L",  # Introduction to Computer Science (with lab)
            "CPSC 203",   # Mathematical Foundations of Computing
            "CPSC 215L",  # Data Structures & Algorithms (with lab)
            "CPSC 275L",  # Introduction to Computer Systems (with lab)
            "CPSC 403/404"  # Senior-year seminar sequence
        ],
        "required_electives": {
            "Theory": ["CPSC 219", "CPSC 320"],        # Theory of Computation; Analysis of Algorithms
            "Systems": ["CPSC 315", "CPSC 333"],       # Systems Software; Computer Networks
            "Software": ["CPSC 304", "CPSC 310",       # Software Design; Database Fundamentals
                         "CPSC 316", "CPSC 340",       # Compiler Construction; Engineering Software Design
                         "CPSC 352", "CPSC 372"],      # Artificial Intelligence; High-Performance Computing
            "Additional CS electives": 2               # two more CS electives (≥200-level, at most one outside CS)
        },
        "allied_courses": ["MATH 131"]  # Calculus I required for B.A.
    },

    "Computer Science (B.S.)": {
        # B.S. adds a higher math requirement
        "required_courses": [
            "CPSC 115L",
            "CPSC 203",
            "CPSC 215L",
            "CPSC 275L",
            "CPSC 403/404"
        ],
        "required_electives": {
            "Theory": ["CPSC 219", "CPSC 320"],
            "Systems": ["CPSC 315", "CPSC 333"],
            "Software": ["CPSC 304", "CPSC 310", "CPSC 316", "CPSC 340", "CPSC 352", "CPSC 372"],
            "Additional CS electives": 3  # one extra elective beyond B.A. requirements
        },
        "allied_courses": [
            "MATH 131",  # Calculus I
            "MATH 132"   # Calculus II
        ]
    },

    "Economics (B.A.)": {
        # Core economics sequence and senior capstone
        "required_courses": [
            "ECON 101",  # Principles of Microeconomics
            "ECON 301",  # Intermediate Microeconomic Theory
            "ECON 302",  # Intermediate Macroeconomic Theory
            "ECON 318",  # Introduction to Econometrics
            "ECON 431"   # Senior Seminar in Economics
        ],
        "required_electives": {
            "200-level Economics elective": 1,  # one additional intermediate course
            "300-level Economics elective": 1   # one additional upper-level course
        },
        "allied_courses": ["ECON 218 or MATH 207"]  # Statistical Methods in Economics or equivalent
    },

    "Economics (B.S.)": {
        # B.S. adds Mathematical Economics
        "required_courses": [
            "ECON 101",
            "ECON 301",
            "ECON 302",
            "ECON 312",  # Mathematical Economics
            "ECON 318",
            "ECON 431"
        ],
        "required_electives": {
            "Advanced economics electives": 4  # four additional 300-level or higher economics courses
        },
        "allied_courses": [
            "ECON 218 or MATH 207",  # Statistical Methods
            "MATH 131",              # Calculus I
            "MATH 132"               # Calculus II
        ]
    },

    "Engineering (B.S.)": {
        # Core math, physics, chemistry, engineering courses + yearlong capstone
        "required_courses": [
            "MATH 131",   # Calculus I
            "MATH 132",   # Calculus II
            "MATH 231",   # Calculus III: Multivariable Calculus
            "PHYS 141L",  # Physics I: Mechanics (with lab)
            "PHYS 231L",  # Physics II: Electricity & Magnetism (with lab)
            "CHEM 111L",  # Introductory Chemistry I (with lab)
            "ENGR 212L",  # Linear Circuit Theory (with lab)
            "ENGR 225",   # Mechanics I (Statics)
            "ENGR 483",   # Senior Design I
            "ENGR 484"    # Senior Design II
        ],
        "required_electives": {
            "Engineering electives": 4  # four additional ENGR courses in area of interest
        }
    },

    "Engineering Science (B.A.)": {
        # B.A. track with cognate focus instead of full engineering sequence
        "required_courses": [
            "MATH 131",   # Calculus I
            "MATH 132",   # Calculus II
            "PHYS 141L",  # Physics I: Mechanics
            "PHYS 231L",  # Physics II: Electricity & Magnetism
            "ENGR 212L",  # Linear Circuit Theory (with lab)
            "ENGR 225",   # Mechanics I (Statics)
            "ENGR 483"    # Senior Design I (capstone I)
        ],
        "required_electives": {
            "Cognate focus courses": 4,   # four courses in approved cognate discipline (e.g., Economics, Environmental Science)
            "Engineering electives": 2    # two additional ENGR courses
        }
    },

    "Environmental Science (B.A.)": {
        # Core environmental science methods and senior capstone
        "required_courses": [
            "ENVS 149L",  # Introduction to Environmental Science (with lab)
            "ENVS 275",   # Environmental Science Research Methods
            "ENVS 401"    # Senior Integrative Experience in Environmental Science
        ],
        "required_electives": {
            "Natural science electives": 2,     # two elective courses in biology, chemistry, or geology
            "Social science/humanities electives": 2,  # two policy or humanities-oriented environment courses
            "Environmental science electives": 2       # two additional relevant electives (any department)
        },
        "allied_courses": [
            "CHEM 111L",  # General Chemistry I
            "MATH 107 or MATH 207"  # Introductory Statistics or Statistical Data Analysis
        ]
    },

    "Environmental Science (B.S.)": {
        # B.S. track with stronger science emphasis
        "required_courses": [
            "ENVS 149L",
            "ENVS 275",
            "ENVS 419",  # Advanced Environmental Science (with lab)
            "ENVS 425"   # Senior Seminar in Environmental Science
        ],
        "required_electives": {
            "Natural science electives": 3,     # three science electives (e.g., Ecology, Hydrology, Geology)
            "Social science/humanities electives": 1,  # one policy or humanities-oriented course
            "Environmental science electives": 2       # two additional environmental science electives
        },
        "allied_courses": [
            "CHEM 111L",  # Intro Chem I
            "CHEM 112L",  # Intro Chem II
            "MATH 131",   # Calculus I
            "MATH 132"    # Calculus II
        ]
    },

    "Film Studies (B.A.)": {
        # Core filmmaking and theory courses + electives and capstone
        "required_courses": [
            "FILM 201",  # Production and Cinematic Technique
            "FILM 265",  # Introduction to Film Studies
            "FILM 470"   # Special Topics in Film Theory/Criticism (often taken as a theory capstone)
        ],
        "required_electives": {
            "National Cinemas/Film History": 1,  # one course in film history or a national cinema
            "Film Theory/Criticism": 1,          # one course in film theory or critical approaches
            "Film Production/Arts": 1,           # one course in film production or related art
            "Film Studies electives": 4          # four additional film studies electives (any relevant level)
        },
        "capstone": "Senior Project or Senior Seminar"  # two-semester project or one-semester senior seminar
    },

    "First-Year Seminar": {
        # Not a major—First-Year Seminar is a general curriculum requirement
        "note": "First-Year Seminar courses fulfill the First-Year Seminar and Writing Emphasis 1 distribution. Not an undergraduate major."
    },

    "History (B.A.)": {
        # Core methods course + breadth and senior capstone
        "required_courses": ["HIST 300"],  # History Workshop: Methods and Research Seminar
        "required_electives": {
            "Advanced history seminars (300-level)": 2,      # two research-intensive seminars
            "Non-Western history courses": 2,               # two courses outside U.S. or Europe
            "History electives (any region/period)": 4      # four additional history courses
        },
        "capstone": "Senior Seminar or Thesis"  # senior research seminar or two-semester thesis
    },

    "International Studies (B.A.)": {
        # Flexible core + focus cluster + senior seminar
        "required_courses": [],  # no fixed core—choose from INTS 101, INTS 201, etc.
        "required_electives": {
            "Global core courses": 3,     # three INTS core courses (≥1 at 300-level)
            "Focus cluster courses": 3,   # three courses in chosen thematic/disciplinary focus (≥1 at 300-level)
            "Electives": 3                # three additional courses (any approved area studies or core)
        },
        "allied_courses": ["Foreign language – 4 semesters"],  # proficiency in one language (placement or coursework)
        "capstone": "INTS 401 Senior Seminar"  # interdisciplinary senior seminar
    },

    "Mathematics (B.A.)": {
        # Foundational and proof-based requirements + electives and capstone
        "required_courses": [
            "MATH 231",  # Calculus III
            "MATH 228 or MATH 229",  # Linear Algebra (proof-based) or Applied Linear Algebra
            "MATH 205",  # Abstraction and Argument (intro to proof)
            "MATH 307",  # Abstract Algebra I
            "MATH 331"   # Real Analysis I
        ],
        "required_electives": {
            "200-level math electives": 2,  # two additional courses at 200-level or above (may include one cognate)
            "300-level math electives": 2   # two additional math courses at 300-level or above
        },
        "capstone": "400-level Mathematics seminar"  # one senior-level seminar (e.g., MATH 400)
    },

    "Music (B.A.)": {
        # Flexible requirements—choose theory, history, performance, and electives
        "required_courses": [],  # no single fixed core
        "required_electives": {
            "Music theory courses": 2,           # two music theory courses (e.g., MUSC 101, MUSC 102)
            "Music history courses": 2,          # two music history courses (e.g., MUSC 201, MUSC 202)
            "World music/ethnomusicology": 1,    # one course in world music (e.g., MUSC 105)
            "Performance/ensemble classes": 2,    # two courses in performance (ensembles or individual lessons)
            "Music electives": 3                 # three additional music courses of choice
        },
        "capstone": "Senior Recital or 400-level Music Seminar"  # e.g., MUSC 407 (recital) or MUSC 491 (senior seminar)
    },

    "Neuroscience (B.A.)": {
        # Interdisciplinary foundation in biology, psychology, and chemistry + electives and capstone
        "required_courses": [
            "BIOL 182L",  # Evolution of Life with lab
            "BIOL 183L",  # Cellular Basis of Life with lab
            "PSYC 101",   # Introduction to Psychology
            "PSYC 261",   # Brain and Behavior
            "CHEM 111L",  # Introductory Chemistry I with lab
            "CHEM 112L"   # Introductory Chemistry II with lab
        ],
        "required_electives": {
            "Neuroscience core courses": 2,   # two intermediate neuroscience courses (e.g., NESC 201, NESC 301)
            "Neuroscience electives": 2,      # two additional electives in neuroscience (e.g., NESC 305, NESC 364)
            "Related electives": 1            # one elective in a related field (e.g., PHIL 374, ENGR 346L)
        },
        "allied_courses": ["STAT 107 or PSYC 221L"],  # one statistics course
        "capstone": "Senior Seminar or Research"  # e.g., NESC 402 (seminar) or NESC 425 (research lab)
    },

    "Neuroscience (B.S.)": {
        # B.S. track requires Organic Chemistry I and more math/physics
        "required_courses": [
            "BIOL 182L",
            "BIOL 183L",
            "PSYC 101",
            "PSYC 261",
            "CHEM 111L",
            "CHEM 112L",
            "CHEM 211L"  # Organic Chemistry I with lab
        ],
        "required_electives": {
            "Neuroscience core courses": 3,   # three intermediate neuroscience courses
            "Neuroscience electives": 2,      # two additional neuroscience electives
            "Related electives": 1            # one elective in a related field
        },
        "allied_courses": [
            "MATH 131",   # Calculus I
            "MATH 132",   # Calculus II
            "PHYS 141L"   # Physics I: Mechanics (with lab)
        ],
        "capstone": "Senior Seminar or Research"
    },

    "Philosophy (B.A.)": {
        # Introductory courses, logic, historical sequence + electives and capstone
        "required_courses": [
            "PHIL 101",  # Introduction to Philosophy
            "PHIL 205",  # Symbolic Logic
            "PHIL 281",  # History of Western Philosophy I
            "PHIL 283"   # History of Western Philosophy II
        ],
        "required_electives": {
            "Ethics/Political philosophy": 1,       # one course in ethics or political/social philosophy
            "Metaphysics/Epistemology": 1,          # one course in metaphysics, epistemology, or related
            "Philosophy electives": 4               # four additional philosophy courses (≥2 at 300-level)
        },
        "capstone": "Senior Seminar or Thesis"  # e.g., PHIL 390 (seminar) or a thesis for honors
    },

    "Physics (B.A.)": {
        # Introductory physics sequence + upper-level courses + electives and capstone
        "required_courses": [
            "PHYS 141L",  # Physics I: Mechanics (with lab)
            "PHYS 231L",  # Physics II: Electricity & Magnetism (with lab)
            "PHYS 232L"   # Physics III: Optics & Modern Physics (with lab)
        ],
        "required_electives": {
            "Physics core courses": 4,  # four of the upper-level core physics courses (PHYS 300, 301, 302, 313)
            "Physics elective": 1       # one additional upper-level physics elective (or research)
        },
        "allied_courses": [
            "MATH 131",  # Calculus I
            "MATH 132",  # Calculus II
            "two additional science/math electives"  # e.g., MATH 231, MATH 234, CHEM 111L, BIOL 182L
        ],
        "capstone": "400-level Physics seminar or research"  # e.g., PHYS 315 (advanced lab/Writing Emphasis)
    },

    "Physics (B.S.)": {
        # B.S. track: full core + additional math/chemistry
        "required_courses": [
            "PHYS 141L",
            "PHYS 231L",
            "PHYS 232L"
        ],
        "required_electives": {
            "Physics core courses": 5,  # all five core courses (PHYS 300, 301, 302, 304, 313)
            "Physics elective": 1       # one additional physics elective
        },
        "allied_courses": [
            "MATH 131",  # Calculus I
            "MATH 132",  # Calculus II
            "MATH 231",  # Calculus III
            "MATH 234",  # Differential Equations
            "CHEM 111L"  # Introductory Chemistry I
        ],
        "capstone": "PHYS 315 (Advanced Lab with Writing Emphasis) or equivalent research" 
    },

    "Political Science (B.A.)": {
        # No fixed core; must choose from subfields
        "required_courses": [],  
        "required_electives": {
            "Introductory subfield courses": 3,  # choose 3 from American, Comparative, International, Political Theory
            "Political science electives": 9     # additional POLS courses (total of 12 courses)
        },
        "capstone": "Senior seminar (writing-intensive) or thesis" 
    },

    "Psychology (B.A.)": {
        # Foundational courses + breadth and labs + capstone
        "required_courses": [
            "PSYC 101",    # Introduction to Psychology
            "BIOL 182L",   # Evolution of Life (with lab) – for neuroscience foundation
            "PSYC 221L",   # Research Design and Analysis (with lab)
            "PSYC 261"     # Brain and Behavior
        ],
        "required_electives": {
            "Core content areas": 3,       # one from each of three groups: Social, Cognitive/Perception, Developmental/Clinical
            "Laboratory courses": 2,       # two lab courses (e.g., PSYC 226L, PSYC 255L)
            "Advanced/Specialized courses": 1  # one 300-level or above seminar if not completing a thesis
        },
        "capstone": "PSYC 401/402 Senior Seminar (writing-intensive) or PSYC 498/499 Thesis"
    },

    "Psychology (B.S.)": {
        # B.S. track: stronger science/library emphasis
        "required_courses": [
            "PSYC 101",
            "BIOL 182L",
            "BIOL 183L",   # The Cellular Basis of Life (with lab) for B.S. foundation
            "PSYC 221L",
            "PSYC 261"
        ],
        "required_electives": {
            "Core content areas": 4,      # cover all four content groups
            "Laboratory courses": 3,      # three lab courses (e.g., PSYC 226L, PSYC 255L, PSYC 293L)
            "Advanced/Specialized courses": 2  # two 300-level or above seminars (e.g., PSYC 365, PSYC 392)
        },
        "capstone": "PSYC 401/402 Senior Seminar or PSYC 498/499 Thesis"
    },

    "Public Policy and Law (B.A.)": {
        # Foundational public policy/law/economics + electives and capstone
        "required_courses": [
            "PBPL 201",  # Introduction to American Public Policy
            "PBPL 123",  # Fundamentals of American Law (cross-listed with POLS)
            "ECON 101",  # Principles of Microeconomics
            "MATH 107 or MATH 207"  # Elements of Statistics or Statistical Data Analysis
        ],
        "required_electives": {
            "Law electives": 2,    # two courses in law or jurisprudence (e.g., PBPL 331: Constitutional Law II)
            "Policy electives": 2, # two applied policy courses (e.g., PBPL 414: Segregation & Public Policy)
            "Public policy electives": 2  # two additional electives in public policy or law
        },
        "capstone": "PBPL 403 Senior Seminar in Public Policy (policy analysis project)"
    },

    "Quantitative Literacy": {
        # Not an undergraduate major; foundational skill course only
        "note": "No undergraduate major. QLIT is a foundational general-education requirement."
    },

    "Religious Studies (B.A.)": {
        # Flexible core: courses must cover multiple traditions & methodologies
        "required_courses": [],  
        "required_electives": {
            "Western religious traditions": 2,     # e.g., RELG 111, RELG 112
            "Asian/global religious traditions": 2, # e.g., RELG 109, RELG 260
            "Religious studies electives": 4       # four additional religion courses (any tradition or theme)
        },
        "capstone": "Senior independent project or seminar"
    },

    "Russian (B.A.)": {
        # Advanced language sequence + culture/literature + cognates
        "required_courses": [
            "RUSS 301",  # Advanced Russian I
            "RUSS 302"   # Advanced Russian II
        ],
        "required_electives": {
            "Russian literature/culture": 3,  # three courses in Russian lit/culture (e.g., RUSS 315, RUSS 345)
            "Related electives": 3           # three electives in cognate fields (history, politics, Eurasian studies)
        },
        "allied_courses": ["Study abroad in Russia (strongly encouraged)"]
    },

    "Sociology (B.A.)": {
        # Theory, methods, and senior seminar + electives
        "required_courses": [
            "SOCL 201",  # Classical Sociological Theory
            "SOCL 202",  # Research Methods in Sociology
            "SOCL 210",  # Quantitative Methods for Sociology
            "SOCL 410"   # Senior Seminar in Sociology
        ],
        "required_electives": {
            "300-level Sociology seminars": 3,  # three advanced 300-level courses
            "Sociology electives": 2            # two additional sociology electives (200-level or above)
        }
    }
}
