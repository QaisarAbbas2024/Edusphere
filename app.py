import streamlit as st
from streamlit_extras.colored_header import colored_header

# --- Configuration ---
st.set_page_config(
    page_title="Edusphere",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Color Theme ---
THEME = {
    "primary": "#4B8BBE",
    "secondary": "#306998",
    "accent": "#FFD43B",
    "bg": "#F5F5F5",
    "text": "#333333"
}

# --- Education System Data ---
PRE_UNIVERSITY = {
    "Matric/SSC": {
        "Science": ["Physics", "Chemistry", "Biology", "Mathematics", "Computer Science"],
        "Arts": ["Economics", "Statistics", "Islamic Studies"]
    },
    "O-Level": {
        "Science": ["Physics", "Chemistry", "Biology", "Mathematics", "Computer Science"],
        "Commerce": ["Business Studies", "Accounting", "Economics"]
    },
    "Intermediate/HSSC": {
        "Pre-Medical": {
            "core": ["Biology", "Chemistry", "Physics", "English"],
            "optional": ["Islamic Studies", "Pakistan Studies", "Mathematics"]
        },
        "Pre-Engineering": {
            "core": ["Mathematics", "Physics", "Chemistry", "English"],
            "optional": ["Computer Science", "Islamic Studies"]
        },
        "ICS": {
            "core": ["Computer Science", "Mathematics", "English"],
            "optional": ["Statistics", "Physics", "Economics"]
        },
        "Commerce": {
            "core": ["Principles of Accounting", "Principles of Economics", "Business Mathematics", "English"],
            "optional": ["Commercial Geography", "Computer Studies", "Statistics"]
        }
    },
    "A-Level": {
        "Science": ["Mathematics", "Physics", "Chemistry", "Biology"],
        "Commerce": ["Business", "Accounting", "Economics"]
    }
}

PATHWAYS = {
    # School to College
    "Pre-Medical": {
        "min_marks": 65,
        "description": "Gateway to medical professions",
        "careers": ["MBBS", "BDS", "Pharmacy"],
        "color": "#FF6B6B",
        "icon": "🩺",
        "level": "Intermediate"
    },
    "Pre-Engineering": {
        "min_marks": 60,
        "description": "Pathway to engineering fields",
        "careers": ["Engineering", "Architecture", "Aviation"],
        "color": "#4CC9F0",
        "icon": "⚙️",
        "level": "Intermediate"
    },
    "ICS": {
        "min_marks": 55,
        "description": "Computer science foundation",
        "careers": ["Software Engineering", "IT Degrees"],
        "color": "#F8961E",
        "icon": "💻",
        "level": "Intermediate"
    },
    "Commerce": {
        "min_marks": 50,
        "description": "Business and finance foundation",
        "careers": ["CA", "ACCA", "Business Administration"],
        "color": "#90BE6D",
        "icon": "💰",
        "level": "Intermediate"
    },
    "General Arts": {
        "min_marks": 40,
        "description": "Flexible arts and humanities pathway",
        "careers": ["Journalism", "Education", "Social Sciences"],
        "color": "#B5179E",
        "icon": "🎨",
        "level": "Intermediate"
    },
    
    # College to University
    "Medical Programs": {
        "prerequisites": ["Pre-Medical"],
        "min_marks": 70,
        "description": "Medical degree programs",
        "careers": ["MBBS (5 years)", "BDS (4 years)", "Doctor of Physiotherapy (5 years)"],
        "color": "#EF476F",
        "icon": "🏥",
        "level": "University"
    },
    "Engineering Programs": {
        "prerequisites": ["Pre-Engineering"],
        "min_marks": 65,
        "description": "Engineering degree programs",
        "careers": ["BS Mechanical Engineering", "BS Electrical Engineering"],
        "color": "#118AB2",
        "icon": "🏗️",
        "level": "University"
    },
    "Computer Science Programs": {
        "prerequisites": ["ICS"],
        "min_marks": 55,
        "description": "Technology degree programs",
        "careers": ["BS Computer Science", "BS Software Engineering"],
        "color": "#FFD166",
        "icon": "🤖",
        "level": "University"
    },
    "Business Programs": {
        "prerequisites": ["Commerce"],
        "min_marks": 50,
        "description": "Business degree programs",
        "careers": ["BBA", "BS Accounting & Finance"],
        "color": "#06D6A0",
        "icon": "📈",
        "level": "University"
    },
    "Liberal Arts": {
        "min_marks": 45,
        "description": "General degree programs",
        "careers": ["BA English", "BS Social Sciences", "BFA Arts"],
        "color": "#7209B7",
        "icon": "📚",
        "level": "University"
    }
}

def apply_theme():
    st.markdown(f"""
    <style>
    .pathway-card {{
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        background: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border-left: 5px solid var(--color);
    }}
    .header-text {{
        color: {THEME['primary']};
        font-size: 2.5rem;
    }}
    .subject-pill {{
        display: inline-block;
        padding: 0.2em 0.6em;
        margin: 0.2em;
        border-radius: 15px;
        background-color: {THEME['secondary']};
        color: white;
        font-size: 0.9em;
    }}
    .core-subject {{
        font-weight: bold;
        color: {THEME['primary']};
    }}
    .subject-selector {{
        margin-top: 10px;
        border: 1px solid {THEME['secondary']};
        border-radius: 5px;
        padding: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

def show_recommendations():
    st.title(f"🌟 Your Academic Pathway")
    st.markdown(f"<h4 style='color:{THEME['secondary']}'>Based on {st.session_state.marks}% marks in {st.session_state.education_level}</h4>", 
               unsafe_allow_html=True)
    
    for pathway in st.session_state.recommendations:
        if pathway not in PATHWAYS:
            continue  # Skip invalid pathways
            
        details = PATHWAYS[pathway]
        
        st.markdown(f"""
        <div class="pathway-card" style="--color: {details['color']}">
            <h3>{details['icon']} {pathway}</h3>
            <p><strong>Level:</strong> {details['level']}</p>
            <p><strong>Description:</strong> {details['description']}</p>
            <p><strong>Your Marks:</strong> <span style="color:{THEME['primary']}">
            {st.session_state.marks}%</span> (Minimum required: {details['min_marks']}%)</p>
            <p><strong>Career Options:</strong></p>
            <ul>
                {''.join([f'<li>{career}</li>' for career in details['careers']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.balloons()

def main():
    apply_theme()
    
    # Welcome Page
    if "student_name" not in st.session_state:
        st.markdown('<h1 class="header-text">🎓 Edusphere</h1>', unsafe_allow_html=True)
        st.markdown("### Your Complete Educational Pathway Advisor")
        
        name = st.text_input("Enter your name:")
        if st.button("Begin Journey", type="primary"):
            if name.strip():
                st.session_state.student_name = name.title()
                st.rerun()
            else:
                st.warning("Please enter your name")
        return
    
    # Education Level Selection
    if "education_level" not in st.session_state:
        st.title(f"Welcome, {st.session_state.student_name}!")
        st.markdown("### Select your current education level:")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Matric/SSC/O-Level"):
                st.session_state.education_level = "School"
                st.session_state.next_step = "Intermediate"
                st.rerun()
        with col2:
            if st.button("Intermediate/HSSC/A-Level"):
                st.session_state.education_level = "College"
                st.session_state.next_step = "University"
                st.rerun()
        return
    
    # Main Form
    if "recommendations" not in st.session_state:
        st.title(f"Your {st.session_state.next_step} Pathway")
        
        with st.form("academic_info"):
            # Common fields
            marks = st.number_input("Overall Percentage (%)", 
                                  min_value=0, max_value=100, 
                                  value=70)
            st.session_state.marks = marks
            
            # School-level specific
            if st.session_state.education_level == "School":
                education_type = st.selectbox("Education System", 
                                           ["Matric/SSC", "O-Level"])
                stream = st.selectbox("Stream", 
                                    ["Science", "Arts", "Commerce"] if education_type == "O-Level" 
                                    else ["Science", "Arts"])
                subjects = st.multiselect(
                    "Subjects Studied",
                    PRE_UNIVERSITY[education_type][stream],
                    default=PRE_UNIVERSITY[education_type][stream][:3]
                )
                
            # College-level specific
            else:
                program_type = st.selectbox("Program Type", 
                                          ["Intermediate/HSSC", "A-Level"])
                
                if program_type == "Intermediate/HSSC":
                    program = st.selectbox("Select Program", 
                                         ["Pre-Medical", "Pre-Engineering", "ICS", "Commerce"])
                    
                    # Display core subjects as selectable checkboxes
                    st.markdown("<p class='core-subject'>Core Subjects (Select All):</p>", unsafe_allow_html=True)
                    with st.container(border=True):
                        core_subjects = PRE_UNIVERSITY["Intermediate/HSSC"][program]["core"]
                        selected_core = []
                        cols = st.columns(4)
                        for i, sub in enumerate(core_subjects):
                            with cols[i%4]:
                                if st.checkbox(sub, value=True, key=f"core_{sub}"):
                                    selected_core.append(sub)
                    
                    # Optional subjects
                    if PRE_UNIVERSITY["Intermediate/HSSC"][program]["optional"]:
                        optional = st.multiselect(
                            "Additional Subjects (Optional)",
                            PRE_UNIVERSITY["Intermediate/HSSC"][program]["optional"]
                        )
                        subjects = selected_core + optional
                    else:
                        subjects = selected_core
                else:  # A-Level
                    program = st.selectbox("Select Stream", ["Science", "Commerce"])
                    subjects = st.multiselect(
                        "Select 3-4 Principal Subjects",
                        PRE_UNIVERSITY["A-Level"][program],
                        default=PRE_UNIVERSITY["A-Level"][program][:3]
                    )
            
            career_interest = st.selectbox(
                "Career Interest",
                ["Medical", "Engineering", "Computer Science", "Business", "Undecided"]
            )
            
            if st.form_submit_button("Generate Pathways", type="primary"):
                st.session_state.recommendations = []
                
                # School to Intermediate logic
                if st.session_state.education_level == "School":
                    subjects_set = set(subjects)
                    
                    if {"Biology", "Chemistry", "Physics"}.issubset(subjects_set) and marks >= 65:
                        if career_interest in ["Medical", "Undecided"]:
                            st.session_state.recommendations.append("Pre-Medical")
                    
                    if {"Mathematics", "Physics", "Chemistry"}.issubset(subjects_set) and marks >= 60:
                        if career_interest in ["Engineering", "Undecided"]:
                            st.session_state.recommendations.append("Pre-Engineering")
                    
                    if len(st.session_state.recommendations) == 0:
                        st.session_state.recommendations.append("General Arts")
                
                # Intermediate to University logic
                else:
                    subjects_set = set(subjects)
                    
                    if program_type == "Intermediate/HSSC":
                        if program == "Pre-Medical" and marks >= 70:
                            st.session_state.recommendations.append("Medical Programs")
                        if program == "Pre-Engineering" and marks >= 65:
                            st.session_state.recommendations.append("Engineering Programs")
                        if program == "ICS" and marks >= 55:
                            st.session_state.recommendations.append("Computer Science Programs")
                        if program == "Commerce" and marks >= 50:
                            st.session_state.recommendations.append("Business Programs")
                
                    elif program_type == "A-Level":
                        if {"Biology", "Chemistry", "Physics"}.issubset(subjects_set) and marks >= 70:
                            st.session_state.recommendations.append("Medical Programs")
                        elif {"Mathematics", "Physics", "Chemistry"}.issubset(subjects_set) and marks >= 65:
                            st.session_state.recommendations.append("Engineering Programs")
                        elif {"Mathematics", "Computer Science"}.intersection(subjects_set) and marks >= 55:
                            st.session_state.recommendations.append("Computer Science Programs")
                        elif {"Accounting", "Economics", "Business"}.intersection(subjects_set) and marks >= 50:
                            st.session_state.recommendations.append("Business Programs")
                
                    if len(st.session_state.recommendations) == 0:
                        st.session_state.recommendations.append("Liberal Arts")

                st.rerun()
        return
    
    # Results Page
    show_recommendations()
    
    if st.button("Explore Another Pathway", type="primary"):
        # Clear all session state and return to name entry
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

if __name__ == "__main__":
    main()
