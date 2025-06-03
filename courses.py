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
    # ... (Additional departments and courses would continue similarly)
}
