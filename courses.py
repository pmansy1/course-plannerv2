courses_data = {
    "American Studies": {
        "AMST202": {
            "title": "Early America",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Humanities"],
            "tags": ["History"]  # Cross-listed as HIST 201:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}
        },
        "AMST203": {
            "title": "Conflicts and Cultures in American Society",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "AMST209": {
            "title": "African-American History",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "AMST271": {
            "title": "Decentering and Re-centering History: Anthropology of Museums",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences"],
            "tags": ["Anthropology"]
        },
        "AMST285": {
            "title": "Born in Blood: Violence and the Making of America",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "AMST301": {
            "title": "American Studies Seminar",
            "credits": 1.0,
            "prereqs": ["AMST203"],  # Major core seminar, typically taken after introductory courses
            "offered": ["Spring"],
            "gen_ed": ["Writing Emphasis 2"],
            "tags": []
        }
    },
    "Anthropology": {
        "ANTH101": {
            "title": "Introduction to Cultural Anthropology",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences", "Global Engagement"],
            "tags": []
        },
        "ANTH204": {
            "title": "Religions of the Black Atlantic",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "ANTH205": {
            "title": "Religions of Africa",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Global Engagement"],
            "tags": []
        },
        "ANTH207": {
            "title": "Anthropological Perspectives on Women and Gender",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Global Engagement"],
            "tags": []
        },
        "ANTH215": {
            "title": "Medical Anthropology",
            "credits": 1.0,
            "prereqs": ["ANTH101"],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences", "Global Engagement"],
            "tags": []
        },
        "ANTH228": {
            "title": "Anthropology from the Margins of South Asia",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Global Engagement"],
            "tags": []
        },
        "ANTH245": {
            "title": "Anthropology and Global Health",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Global Engagement"],
            "tags": []
        },
        "ANTH254": {
            "title": "The Meaning of Work",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        }
    },
    "Art History": {
        "AHIS101": {
            "title": "History of Art in the West I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "AHIS102": {
            "title": "History of Art in the West II",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "AHIS226": {
            "title": "Drinking, Dining, and Community in Antiquity",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "AHIS241": {
            "title": "Classical Ideals: The Human Body in Ancient Art",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": ["Classical Civilization", "Women, Gender, and Sexuality"]  # Cross-referenced as CLCV 241 and WMGS:contentReference[oaicite:2]{index=2}
        },
        "AHIS361": {
            "title": "Seminar on Impressionism",
            "credits": 1.0,
            "prereqs": ["AHIS102"],
            "offered": ["Fall"],
            "gen_ed": ["Arts", "Writing Emphasis 2"],
            "tags": ["Drawing"]
        },
        "AHIS364": {
            "title": "Architectural Drawing",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": ["Architecture", "Engineering"]  # Prerequisite for ENGR342 (cross-listed):contentReference[oaicite:3]{index=3}
        },
        "AHIS365": {
            "title": "Elements of Architectural Design",
            "credits": 1.0,
            "prereqs": ["AHIS364"],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": ["Architecture"]
        }
    },
    "Biology": {
        "BIOL183L": {
            "title": "Introductory Biology I (Lab)",
            "credits": 1.25,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "BIOL182L": {
            "title": "Introductory Biology II (Lab)",
            "credits": 1.25,
            "prereqs": ["BIOL183L"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "BIOL215": {
            "title": "Botany",
            "credits": 1.0,
            "prereqs": ["BIOL182L"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "BIOL226": {
            "title": "Foundations in Molecular Biology",
            "credits": 1.0,
            "prereqs": ["BIOL182L"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "BIOL317": {
            "title": "Biochemistry",
            "credits": 1.0,
            "prereqs": ["BIOL182L", "CHEM311"],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        }
    },
    "Chemistry": {
        "CHEM111": {
            "title": "Introductory Chemistry I (w/Lab)",
            "credits": 1.25,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "CHEM112": {
            "title": "Introductory Chemistry II (w/Lab)",
            "credits": 1.25,
            "prereqs": ["CHEM111"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "CHEM211": {
            "title": "Organic Chemistry I (w/Lab)",
            "credits": 1.25,
            "prereqs": ["CHEM112"],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "CHEM212": {
            "title": "Organic Chemistry II (w/Lab)",
            "credits": 1.25,
            "prereqs": ["CHEM211"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "CHEM311": {
            "title": "Analytical Chemistry (w/Lab)",
            "credits": 1.25,
            "prereqs": ["CHEM112"],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],  # Quantitative focus integrated in science context
            "tags": []
        }
    },
    "Computer Science": {
        "CPSC115": {
            "title": "Intro to Computer Science",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "CPSC203": {
            "title": "Mathematical Foundations of Computing",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "CPSC215": {
            "title": "Data Structures and Algorithms",
            "credits": 1.0,
            "prereqs": ["CPSC115"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "CPSC315": {
            "title": "Software Design",
            "credits": 1.0,
            "prereqs": ["CPSC215"],
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        }
    },
    "Economics": {
        "ECON101": {
            "title": "Introduction to Economics (Microeconomics)",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "ECON102": {
            "title": "Introduction to Economics (Macroeconomics)",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "ECON301": {
            "title": "Intermediate Microeconomic Theory",
            "credits": 1.0,
            "prereqs": ["ECON101", "MATH131"],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "ECON302": {
            "title": "Intermediate Macroeconomic Theory",
            "credits": 1.0,
            "prereqs": ["ECON102"],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        }
    },
    "English": {
        "ENGL104": {
            "title": "The American Experiment, Part I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "ENGL105": {
            "title": "The American Experiment, Part II",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "ENGL110": {
            "title": "Inventing English Literature",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "ENGL270": {
            "title": "Creative Writing: Introduction to Writing Fiction and Poetry",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "ENGL334": {
            "title": "Advanced Creative Writing: Fiction",
            "credits": 1.0,
            "prereqs": ["ENGL270"],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        }
    },
    "History": {
        "HIST201": {
            "title": "Early America",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Humanities"],
            "tags": ["American Studies"]  # Cross-listed as AMST 202:contentReference[oaicite:4]{index=4}
        },
        "HIST202": {
            "title": "Modern America",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "HIST221": {
            "title": "Europe in the 20th Century",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "HIST236": {
            "title": "History of the African Diaspora",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities", "Global Engagement"],
            "tags": []
        }
    },
    "Mathematics": {
        "MATH131": {
            "title": "Calculus I",
            "credits": 1.0,
            "prereqs": ["Placement"],  # Requires appropriate math placement
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH132": {
            "title": "Calculus II",
            "credits": 1.0,
            "prereqs": ["MATH131"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH205": {
            "title": "Linear Algebra",
            "credits": 1.0,
            "prereqs": ["MATH132"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH207": {
            "title": "Statistical Data Analysis",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        }
    },
    "Psychology": {
        "PSYC101": {
            "title": "Introduction to Psychology",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],  # Fulfills social science distribution
            "tags": []
        },
        "PSYC261": {
            "title": "Brain and Behavior",
            "credits": 1.0,
            "prereqs": ["PSYC101"],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],  # Neuroscience-oriented psychology course:contentReference[oaicite:5]{index=5}
            "tags": ["Neuroscience"]
        },
        "PSYC221": {
            "title": "Research Design and Analysis",
            "credits": 1.25,
            "prereqs": ["PSYC101"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "PSYC301": {
            "title": "Psychological Neuroscience",
            "credits": 1.0,
            "prereqs": ["PSYC261", "BIOL182L"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": ["Neuroscience"]
        }
    },
    "Public Policy & Law": {
        "PBPL201": {
            "title": "Introduction to Public Policy",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "PBPL202": {
            "title": "Law, Argument, and Public Policy",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "PBPL350": {
            "title": "Senior Seminar in Public Policy",
            "credits": 1.0,
            "prereqs": ["PBPL201"],
            "offered": ["Fall"],
            "gen_ed": ["Writing Emphasis 2"],
            "tags": []
        }
    },
    "Sociology": {
        "SOCL101": {
            "title": "Principles of Sociology",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "SOCL201": {
            "title": "Sociological Theory",
            "credits": 1.0,
            "prereqs": ["SOCL101"],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "SOCL227": {
            "title": "Urban Sociology",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": ["Urban Studies"]
        },
        "SOCL310": {
            "title": "Research Methods in Sociology",
            "credits": 1.0,
            "prereqs": ["SOCL101", "SOCL201"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        }
    },
    "Studio Arts": {
        "STAR121": {
            "title": "Drawing I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "STAR122": {
            "title": "Drawing II",
            "credits": 1.0,
            "prereqs": ["STAR121"],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "STAR141": {
            "title": "Painting I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "STAR231": {
            "title": "Sculpture I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        }
    },
    "Theater & Dance": {
        "THDN103": {
            "title": "Basic Acting",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "THDN123": {
            "title": "Introduction to Ballet",
            "credits": 0.5,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "THDN218": {
            "title": "Principles of Movement",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "THDN304": {
            "title": "Directing",
            "credits": 1.0,
            "prereqs": ["THDN103"],
            "offered": ["Spring"],
            "gen_ed": ["Arts", "Writing Emphasis 2"],
            "tags": []
        }
    },
    "Women, Gender, and Sexuality": {
        "WMGS101": {
            "title": "Introduction to Women, Gender, and Sexuality",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "WMGS206": {
            "title": "Queer Studies: Issues and Controversies",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "WMGS314": {
            "title": "Feminist Theory",
            "credits": 1.0,
            "prereqs": ["WMGS101"],
            "offered": ["Spring"],
            "gen_ed": ["Humanities", "Writing Emphasis 2"],
            "tags": []
        }
    },
    "Writing and Rhetoric": {
        "RHET103": {
            "title": "College Writing",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Writing Emphasis 1"],
            "tags": []
        },
        "RHET125": {
            "title": "Writing Workshop",
            "credits": 0.5,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": [],
            "tags": []
        },
        "RHET202": {
            "title": "Writing in the Disciplines",
            "credits": 1.0,
            "prereqs": ["RHET103"],
            "offered": ["Spring"],
            "gen_ed": [],
            "tags": []
        },
        "RHET225": {
            "title": "Argument and Exposition",
            "credits": 1.0,
            "prereqs": ["RHET103"],
            "offered": ["Fall"],
            "gen_ed": [],
            "tags": []
        }
    },
    "First Year Seminar": {
        "FYSM180": {
            "title": "Imagining Paris",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["First-Year Seminar", "Writing Emphasis 1"],
            "tags": []
        },
        "FYSM189": {
            "title": "The Global City",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["First-Year Seminar", "Writing Emphasis 1", "Global Engagement"],
            "tags": []
        },
        "FYSM193": {
            "title": "Science and Society",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["First-Year Seminar", "Writing Emphasis 1"],
            "tags": []
        }
    },
    "Quantitative Literacy": {
        "QLIT101": {
            "title": "Quantitative Literacy",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        }
    },
    "Mathematics": {
        "MATH 103": {
            "title": "Introduction to Sports Analytics",
            "credits": 1.0,
            "prereqs": ["QLIT 101"],  # Placement exam alternative not listed
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 107": {
            "title": "Elements of Statistics",
            "credits": 1.0,
            "prereqs": ["QLIT 101"], 
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 114": {
            "title": "Judgment and Decision Making",
            "credits": 1.0,
            "prereqs": ["QLIT 101"], 
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 117": {
            "title": "Introduction to Statistics",
            "credits": 1.0,
            "prereqs": ["QLIT 101"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 123": {
            "title": "Mathematical Gems",
            "credits": 1.0,
            "prereqs": ["QLIT 101"],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 127": {
            "title": "Functions, Graphs, and Modeling",
            "credits": 1.0,
            "prereqs": ["QLIT 101"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 131": {
            "title": "Calculus I",
            "credits": 1.25,
            "prereqs": ["MATH 127"],  # or placement exam
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 131L": {
            "title": "Calculus I Workshop",
            "credits": 0.25,
            "prereqs": ["MATH 131"],  # corequisite
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 132": {
            "title": "Calculus II",
            "credits": 1.25,
            "prereqs": ["MATH 131"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 205": {
            "title": "Abstraction and Argument",
            "credits": 1.0,
            "prereqs": [],  # recommended strong background, no formal prereq
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 207": {
            "title": "Statistical Data Analysis",
            "credits": 1.0,
            "prereqs": ["MATH 107", "MATH 127"], 
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 209": {
            "title": "Stochastic Processes",
            "credits": 1.0,
            "prereqs": ["MATH 132"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 228": {
            "title": "Linear Algebra",
            "credits": 1.0,
            "prereqs": ["MATH 132"], 
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 229": {
            "title": "Applied Linear Algebra",
            "credits": 1.0,
            "prereqs": ["MATH 132"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 231": {
            "title": "Calculus III: Multivariable Calculus",
            "credits": 1.25,
            "prereqs": ["MATH 132"],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 234": {
            "title": "Differential Equations",
            "credits": 1.0,
            "prereqs": ["MATH 132"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 253": {
            "title": "Number Theory and Its Application",
            "credits": 1.0,
            "prereqs": ["MATH 132"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 305": {
            "title": "Probability",
            "credits": 1.0,
            "prereqs": ["MATH 231"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 307": {
            "title": "Abstract Algebra I – Theory of Groups",
            "credits": 1.0,
            "prereqs": ["MATH 228", "MATH 205"], 
            "offered": ["Fall"],
            "gen_ed": ["Numerical & Symbolic Reasoning", "Writing Emphasis 2"],
            "tags": []
        },
        "MATH 309": {
            "title": "Numerical Analysis",
            "credits": 1.0,
            "prereqs": ["MATH 132", "CPSC 115"], 
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 334": {
            "title": "Partial Differential Equations",
            "credits": 1.0,
            "prereqs": ["MATH 231", "MATH 234"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        },
        "MATH 341": {
            "title": "Complex Analysis",
            "credits": 1.0,
            "prereqs": ["MATH 231"],
            "offered": ["Spring"],
            "gen_ed": ["Numerical & Symbolic Reasoning"],
            "tags": []
        }
    },

    "Music": {
        "MUSC 101": {
            "title": "Basic Musicianship",
            "credits": 1.25,
            "prereqs": [], 
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 105": {
            "title": "Instrumental Ensemble",
            "credits": 0.5,
            "prereqs": [], 
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Arts", "Wellness"],  # ARTW code
            "tags": []
        },
        "MUSC 107": {
            "title": "Music Lessons (individual instruction)",
            "credits": 0.5,
            "prereqs": ["MUSC 101"],  # may be taken concurrently
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 108": {
            "title": "Steel Pan Ensemble",
            "credits": 0.5,
            "prereqs": [], 
            "offered": ["Fall"],
            "gen_ed": ["Arts", "Wellness"],  # ARTW
            "tags": []
        },
        "MUSC 109": {
            "title": "Jazz Ensemble",
            "credits": 0.5,
            "prereqs": [], 
            "offered": ["Fall"],
            "gen_ed": ["Arts", "Wellness"], 
            "tags": []
        },
        "MUSC 111": {
            "title": "Samba Ensemble",
            "credits": 0.5,
            "prereqs": [], 
            "offered": ["Fall"],
            "gen_ed": ["Arts", "Global Engagement"],  # GLB1 = Arts & Global
            "tags": ["International Studies: Latin American & Caribbean", "Community Learning"]
        },
        "MUSC 113": {
            "title": "Introduction to World Music",
            "credits": 1.0,
            "prereqs": [], 
            "offered": ["Spring"],
            "gen_ed": ["Arts", "Global Engagement"],  # GLB1
            "tags": [
                "International Studies: African Studies", 
                "International Studies: Asian Studies", 
                "International Studies: Latin American & Caribbean"
            ]
        },
        "MUSC 133": {
            "title": "Blues Women to Nicki Minaj",
            "credits": 1.0,
            "prereqs": [], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 150": {
            "title": "Before Lady Gaga and Beyoncé",
            "credits": 1.0,
            "prereqs": [], 
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 175": {
            "title": "Introduction to Recording Arts",
            "credits": 1.0,
            "prereqs": [], 
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 200": {
            "title": "Composition",
            "credits": 1.0,
            "prereqs": ["MUSC 101"], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 209L": {
            "title": "Organists’ Lab",
            "credits": 0.25,
            "prereqs": ["MUSC 107"],  # concurrent enrollment in organ lessons
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 218": {
            "title": "American Popular Music",
            "credits": 1.0,
            "prereqs": [], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 219": {
            "title": "Toca Brasil! (Play Brazil!)",
            "credits": 1.0,
            "prereqs": [], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts", "Global Engagement"],
            "tags": ["International Studies: Latin American & Caribbean"]
        },
        "MUSC 252": {
            "title": "The Beatles and Rock ’n’ Roll",
            "credits": 1.0,
            "prereqs": [], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 260": {
            "title": "Advanced Recording Arts",
            "credits": 1.0,
            "prereqs": ["MUSC 175"], 
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 268": {
            "title": "Mozart and Beethoven",
            "credits": 1.0,
            "prereqs": [], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 274": {
            "title": "Jazz: 1900 to the Present",
            "credits": 1.0,
            "prereqs": [], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 311": {
            "title": "From Plato and Aristotle to Bach and Handel",
            "credits": 1.0,
            "prereqs": ["MUSC 101"],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 312": {
            "title": "18th- and 19th-Century Music: From Mozart to Brahms",
            "credits": 1.0,
            "prereqs": ["MUSC 101"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "MUSC 313": {
            "title": "Inventions and Revolutions in Music",
            "credits": 1.0,
            "prereqs": ["MUSC 201"], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts"],
            "tags": []
        }
    },

    "Neuroscience": {
        "NESC 107": {
            "title": "The Divided Brain",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 120": {
            "title": "Nervous Connections",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 210L": {
            "title": "Neuroendocrinology (with lab)",
            "credits": 1.0,
            "prereqs": ["PSYC 261"], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 248": {
            "title": "Nature and Brain Health: From Urban Places to Wild Spaces",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "NESC 262": {
            "title": "Introduction to Animal Behavior",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 301": {
            "title": "Introduction to Neuroscience Methodology",
            "credits": 1.0,
            "prereqs": ["NESC 120"], 
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 305": {
            "title": "Neurolaw",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 306": {
            "title": "Social Neuroscience",
            "credits": 1.0,
            "prereqs": ["PSYC 261"], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 307": {
            "title": "Clinical Psychobiology",
            "credits": 1.0,
            "prereqs": ["PSYC 261"], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 308": {
            "title": "Cultural Neuroscience",
            "credits": 1.0,
            "prereqs": ["PSYC 261", "ANTH 101"], 
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 312": {
            "title": "Neurobiology of Movement",
            "credits": 1.0,
            "prereqs": ["NESC 201"], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 313": {
            "title": "Emotion and Motivation",
            "credits": 1.0,
            "prereqs": ["PSYC 261"], 
            "offered": ["Alternate Years"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 320": {
            "title": "Developmental Neuroscience",
            "credits": 1.0,
            "prereqs": ["NESC 201"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 345": {
            "title": "Mind, Brain, and Society",
            "credits": 1.0,
            "prereqs": ["PSYC 261"], 
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 362": {
            "title": "Neuroethology",
            "credits": 1.0,
            "prereqs": ["NESC 201", "PSYC 261"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Natural Science", "Writing Emphasis 2"],
            "tags": []
        },
        "NESC 364": {
            "title": "Neuropsychopharmacology",
            "credits": 1.0,
            "prereqs": ["PSYC 261", "NESC 201"], 
            "offered": ["Spring"],
            "gen_ed": ["Natural Science", "Writing Emphasis 2"],
            "tags": []
        },
        "NESC 388": {
            "title": "Current Issues in Neuroscience",
            "credits": 0.5,
            "prereqs": ["NESC 201", "Senior standing"],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "NESC 425": {
            "title": "Research in Neuroscience (Laboratory)",
            "credits": 0.5,
            "prereqs": ["Permission of instructor"], 
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        }
    },

    "Philosophy": {
        "PHIL 101": {
            "title": "Introduction to Philosophy",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "PHIL 103": {
            "title": "Ethics",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "PHIL 205": {
            "title": "Symbolic Logic",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "PHIL 217": {
            "title": "Philosophy and Literature",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities"],
            "tags": ["Literature and Psychology minor"]
        },
        "PHIL 246": {
            "title": "Bioethics",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "PHIL 281": {
            "title": "History of Western Philosophy I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "PHIL 283": {
            "title": "History of Western Philosophy II",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "PHIL 374": {
            "title": "Minds and Brains (Philosophy of Mind)",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "PHIL 378": {
            "title": "Philosophy of Mind",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities"],
            "tags": []
        }
    },

    "Physics": {
        "PHYS 131": {
            "title": "General Physics I (with Lab)",
            "credits": 1.25,
            "prereqs": [],  # high-school physics or placement recommended
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "PHYS 132": {
            "title": "General Physics II (with Lab)",
            "credits": 1.25,
            "prereqs": ["PHYS 131"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "PHYS 141": {
            "title": "Introductory Physics I (Mechanics)",
            "credits": 1.0,
            "prereqs": ["MATH 131"],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "PHYS 231": {
            "title": "Electricity and Magnetism",
            "credits": 1.0,
            "prereqs": ["PHYS 131", "MATH 132"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "PHYS 232": {
            "title": "Waves and Optics",
            "credits": 1.0,
            "prereqs": ["PHYS 231"],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "PHYS 301": {
            "title": "Modern Physics",
            "credits": 1.0,
            "prereqs": ["PHYS 232"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        }
    },

    "Political Science": {
        "POLS 102": {
            "title": "American National Government",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "POLS 103": {
            "title": "Comparative Politics",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "POLS 104": {
            "title": "International Politics",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "POLS 105": {
            "title": "Introduction to Political Theory",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "POLS 239": {
            "title": "Global Politics of Climate Change",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": ["Environmental Studies"]
        },
        "POLS 241": {
            "title": "Classical Political Thought",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "POLS 272": {
            "title": "The American Presidency",
            "credits": 1.0,
            "prereqs": ["POLS 102"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "POLS 273": {
            "title": "Congress and Public Policy",
            "credits": 1.0,
            "prereqs": ["POLS 102"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "POLS 310": {
            "title": "American Foreign Policy",
            "credits": 1.0,
            "prereqs": ["POLS 104"],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "POLS 321": {
            "title": "Civil Rights and Liberties",
            "credits": 1.0,
            "prereqs": ["POLS 102"],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": ["Legal Studies"]
        }
    },

    "Portuguese": {
        "PORT 101": {
            "title": "Elementary Portuguese I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Second Language"],
            "tags": []
        },
        "PORT 102": {
            "title": "Elementary Portuguese II",
            "credits": 1.0,
            "prereqs": ["PORT 101"],
            "offered": ["Spring"],
            "gen_ed": ["Second Language"],
            "tags": []
        },
        "PORT 201": {
            "title": "Intermediate Portuguese I",
            "credits": 1.0,
            "prereqs": ["PORT 102"],
            "offered": ["Fall"],
            "gen_ed": ["Second Language"],
            "tags": []
        },
        "PORT 202": {
            "title": "Intermediate Portuguese II",
            "credits": 1.0,
            "prereqs": ["PORT 201"],
            "offered": ["Spring"],
            "gen_ed": ["Second Language"],
            "tags": []
        }
    },

    "Psychology": {
        "PSYC 101": {
            "title": "Introductory Psychology",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "PSYC 105": {
            "title": "Research Design and Analysis",
            "credits": 1.0,
            "prereqs": ["PSYC 101"],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": ["Quantitative Competency"]
        },
        "PSYC 221": {
            "title": "Abnormal Psychology",
            "credits": 1.0,
            "prereqs": ["PSYC 101"],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "PSYC 255": {
            "title": "Child Development",
            "credits": 1.0,
            "prereqs": ["PSYC 101"],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "PSYC 261": {
            "title": "Brain and Behavior",
            "credits": 1.0,
            "prereqs": ["PSYC 101"],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "PSYC 301": {
            "title": "Behavioral Neuroscience",
            "credits": 1.0,
            "prereqs": ["PSYC 261"],
            "offered": ["Fall"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "PSYC 302": {
            "title": "Behavioral Neuroscience (with Lab)",
            "credits": 1.25,
            "prereqs": ["PSYC 261"],
            "offered": ["Spring"],
            "gen_ed": ["Natural Science"],
            "tags": []
        },
        "PSYC 334": {
            "title": "Current Issues in Cognition",
            "credits": 1.0,
            "prereqs": ["PSYC 101", "PSYC 105"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "PSYC 365": {
            "title": "Cognitive Neuroscience",
            "credits": 1.0,
            "prereqs": ["PSYC 261"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Natural Science"],
            "tags": []
        }
    },

    "Public Policy & Law": {
        "PBPL 201": {
            "title": "Introduction to American Public Policy",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "PBPL 202": {
            "title": "Law, Argument, and Public Policy",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "PBPL 350": {
            "title": "Senior Seminar in Public Policy",
            "credits": 1.0,
            "prereqs": ["PBPL 201", "PBPL 202"],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences", "Writing Emphasis 2"],
            "tags": []
        }
    },

    "Quantitative Literacy": {
        "QLIT 101": {
            "title": "Foundational Techniques for Quantitative Reasoning (Algebraic Reasoning)",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": [],  # QLIT is a foundational skill course (required if placed)
            "tags": []
        }
        # (Quantitative literacy is a foundational requirement; QLIT 101 is the primary course)
    },

    "Religious Studies": {
        "RELG 101": {
            "title": "Introduction to Religion",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "RELG 109": {
            "title": "World Religions",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Humanities", "Global Engagement"],
            "tags": []
        },
        "RELG 211": {
            "title": "Hebrew Bible",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "RELG 212": {
            "title": "New Testament",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "RELG 260": {
            "title": "Meditation, Medicine, and Mind",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Humanities"],
            "tags": []
        }
    },

    "Russian": {
        "RUSS 101": {
            "title": "Elementary Russian I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Second Language"],
            "tags": []
        },
        "RUSS 102": {
            "title": "Elementary Russian II",
            "credits": 1.0,
            "prereqs": ["RUSS 101"],
            "offered": ["Spring"],
            "gen_ed": ["Second Language"],
            "tags": []
        },
        "RUSS 201": {
            "title": "Intermediate Russian I",
            "credits": 1.0,
            "prereqs": ["RUSS 102"],
            "offered": ["Fall"],
            "gen_ed": ["Second Language"],
            "tags": []
        },
        "RUSS 202": {
            "title": "Intermediate Russian II",
            "credits": 1.0,
            "prereqs": ["RUSS 201"],
            "offered": ["Spring"],
            "gen_ed": ["Second Language"],
            "tags": []
        }
    },

    "Sociology": {
        "SOCL 101": {
            "title": "Introduction to Sociology",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": []
        },
        "SOCL 201": {
            "title": "Classical Sociological Theory",
            "credits": 1.0,
            "prereqs": ["SOCL 101"],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences", "Writing Emphasis 2"],
            "tags": []
        },
        "SOCL 202": {
            "title": "Research Methods in Sociology",
            "credits": 1.0,
            "prereqs": ["SOCL 101"],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences"],
            "tags": ["Quantitative Competency"]
        },
        "SOCL 227": {
            "title": "Race, Racism, and Democracy",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences", "Global Engagement", "Identity, Power, and Equity"],
            "tags": []
        },
        "SOCL 272": {
            "title": "Sociology of Health and Illness",
            "credits": 1.0,
            "prereqs": ["SOCL 101"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Social Sciences"],
            "tags": ["Global Health"]
        }
    },

    "Studio Arts": {
        "ARTS 101": {
            "title": "Drawing I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "ARTS 107": {
            "title": "Painting I",
            "credits": 1.0,
            "prereqs": ["ARTS 101"],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "ARTS 111": {
            "title": "Three-Dimensional Design",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "ARTS 151": {
            "title": "Photography I",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "ARTS 225": {
            "title": "Digital Art",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        }
    },

    "Theater & Dance": {
        "THDN 101": {
            "title": "Introduction to Theater",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "THDN 111": {
            "title": "Fundamentals of Acting",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "THDN 123": {
            "title": "Stagecraft",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Arts"],
            "tags": []
        },
        "THDN 235": {
            "title": "History of Theater",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Alternate Years"],
            "gen_ed": ["Humanities"],
            "tags": []
        },
        "THDN 309": {
            "title": "Directing for the Theater",
            "credits": 1.0,
            "prereqs": ["THDN 111"],
            "offered": ["Alternate Years"],
            "gen_ed": ["Arts"],
            "tags": []
        }
    },

    "Women, Gender, and Sexuality": {
        "WMGS 101": {
            "title": "Introduction to Women, Gender, and Sexuality",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Social Sciences", "Global Engagement", "Identity, Power, and Equity"],
            "tags": []
        },
        "WMGS 207": {
            "title": "Gender and Sexuality in a Global World",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Spring"],
            "gen_ed": ["Social Sciences", "Global Engagement"],
            "tags": []
        },
        "WMGS 301": {
            "title": "Feminist Theories",
            "credits": 1.0,
            "prereqs": ["WMGS 101"],
            "offered": ["Fall"],
            "gen_ed": ["Social Sciences", "Writing Emphasis 2"],
            "tags": []
        }
    },

    "Writing and Rhetoric": {
        "RHET 101": {
            "title": "College Writing",
            "credits": 1.0,
            "prereqs": [],
            "offered": ["Fall", "Spring"],
            "gen_ed": ["Writing Emphasis 1"],
            "tags": []
        },
        "RHET 208": {
            "title": "Argument and Exposition",
            "credits": 1.0,
            "prereqs": ["RHET 101"],
            "offered": ["Spring"],
            "gen_ed": ["Writing Emphasis 2"],
            "tags": []
        },
        "RHET 225": {
            "title": "Creative Nonfiction",
            "credits": 1.0,
            "prereqs": ["RHET 101"],
            "offered": ["Fall"],
            "gen_ed": ["Writing Emphasis 2"],
            "tags": []
        },
        "RHET 302": {
            "title": "Writing Theories and Practice",
            "credits": 1.0,
            "prereqs": ["RHET 202"],  # assuming RHET 202 is Writing in the Disciplines
            "offered": ["Alternate Years"],
            "gen_ed": ["Humanities", "Writing Emphasis 2"],
            "tags": []
        }
    }
}

