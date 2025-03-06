import streamlit as st
import openai

# Streamlit App Configuration
st.set_page_config(
    page_title="📄 AI Resume & Cover Letter Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar: Page Selector
with st.sidebar:
    st.header("📌 Select a Page")
    page = st.radio(
        "Navigate:",
        ["About the App", "AI Resume & Cover Letter Generator"],
        index=0  # Default to "About the App"
    )

# About the App Page
if page == "About the App":
    st.title("📄 About AI Resume & Cover Letter Generator")

    st.markdown("""


## 1️⃣ Name & Role  
**Agent Name:** **ResumeMate**  
**Role:** Your AI-powered assistant for crafting **professional resumes and cover letters** tailored to your job applications.

---

## 2️⃣ Origin Story 🌟  
Every job seeker knows the struggle—creating a **perfect resume and cover letter** can be daunting. Whether you're a **fresh graduate, an experienced professional, or switching careers**, ResumeMate is here to **make the process effortless**.

### 🔹 The Challenge  
Many job seekers:  
- **Struggle with formatting and structuring resumes** professionally.  
- **Fail to highlight their strengths effectively** in a cover letter.  
- **Get rejected by Applicant Tracking Systems (ATS)** due to keyword mismatches.  
- **Spend hours crafting a resume and cover letter** for each job application.  

### 💡 The Solution – ResumeMate!  
ResumeMate was developed as a **smart, AI-powered tool** to **generate optimized, well-structured resumes and cover letters** in **seconds**!  
By leveraging **GPT-4o’s advanced AI capabilities**, it ensures that every document is:  
✅ **Well-Formatted** – Professional, clean, and ATS-friendly.  
✅ **Impactful** – Highlights your **skills, experience, and achievements** effectively.  
✅ **Customizable** – Tailored to any **job title or industry** with **just a few clicks**.  
✅ **Effortless** – Saves you **time and effort** in job applications.  

---

## 3️⃣ How It Works ⚙️  
Using ResumeMate is **super simple**! Just follow these three steps:  

**🔹 Step 1:** **Enter Your Details**  
Fill in your **name, job title, experience, skills, education, and achievements**.  

**🔹 Step 2:** **Generate Resume & Cover Letter**  
Click the **"📄 Generate"** button, and ResumeMate will **instantly create** a professional resume and a personalized cover letter.  

**🔹 Step 3:** **Review & Download**  
Read through the AI-generated documents, make edits if needed, and **use them for job applications**!  

📌 **Bonus:** The AI ensures that **your resume includes job-specific keywords**, increasing your chances of passing ATS scans!  

---

## 4️⃣ Key Features 🚀  
Here’s what makes ResumeMate stand out:  

### 📄 **AI-Generated Resumes**  
- **Professional Layout** – Well-structured and formatted automatically.  
- **Custom Content** – Highlights your **achievements, skills, and experience** in the best way possible.  
- **Optimized for ATS** – Uses **relevant job-related keywords** to improve hiring chances.  

### ✉️ **Personalized Cover Letters**  
- **Industry-Specific** – Tailored to your **job role and field**.  
- **Engaging Opening & Closing** – Makes your application **stand out**.  
- **Highly Customizable** – Modify any section effortlessly.  

### 🔍 **Instant & Smart Generation**  
- **No More Writer’s Block** – AI **writes everything for you** based on best practices.  
- **Time-Saving** – Generate **high-quality documents in seconds**.  

### 🎯 **Keyword Optimization for ATS**  
- Ensures your resume **passes Applicant Tracking Systems (ATS)** by using job-specific keywords.  
- Helps your resume **rank higher in recruiter searches**.  

### 🔄 **Quick & Easy Edits**  
- If you need a **different style or focus**, simply **edit your inputs** and **regenerate**.  

---

## 5️⃣ Why Use ResumeMate? 🎯  
✅ **Save Time & Effort** – No need to manually format and write resumes.  
✅ **Increase Job Application Success** – ATS-friendly and optimized for recruiters.  
✅ **Get Professional Results Instantly** – No writing experience needed!  
✅ **User-Friendly Interface** – Easy to use, even for beginners.  

Start your job search with confidence—**let AI craft the perfect resume & cover letter for you!** 🚀  


    """)

# AI Resume & Cover Letter Generator Page
else:
    st.title("📄 AI Resume & Cover Letter Generator")
    st.markdown("""
        <div style='background-color: #228B22; padding: 1rem; border-radius: 0.5rem; margin-bottom: 2rem; color: white;'>
        Generate professional resumes and cover letters tailored to your job applications using AI.
        </div>
    """, unsafe_allow_html=True)

    # Sidebar: API Configuration
    with st.sidebar:
        st.header("🔑 API Configuration")
        openai_api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")
        if not openai_api_key:
            st.warning("⚠️ Please enter your OpenAI API Key to proceed")
            st.stop()
        st.success("API Key accepted!")

    # User Input Form
    st.header("📝 Enter Your Details")
    col1, col2 = st.columns(2)

    with col1:
        full_name = st.text_input("Full Name")
        job_title = st.text_input("Job Title")
        experience = st.text_area("Work Experience", help="Describe your past job roles and responsibilities.")

    with col2:
        skills = st.text_area("Key Skills", help="List your top skills relevant to the job.")
        education = st.text_area("Education Details", help="Enter your highest degree and institution.")
        achievements = st.text_area("Achievements", help="Highlight any awards, recognitions, or certifications.")

    if st.button("📄 Generate Resume & Cover Letter"):
        with st.spinner("Generating your documents..."):
            user_profile = f"""
            Name: {full_name}
            Job Title: {job_title}
            Experience: {experience}
            Skills: {skills}
            Education: {education}
            Achievements: {achievements}
            """

            def call_gpt4o(api_key, system_prompt, user_message):
                """Calls GPT-4o API using OpenAI's client API."""
                client = openai.Client(api_key=api_key)
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_message},
                        ]
                    )
                    return response.choices[0].message.content
                except Exception as e:
                    return f"❌ Error: {e}"

            resume_prompt = "You are an AI resume writer. Generate a professional resume based on the user's details."
            resume_text = call_gpt4o(openai_api_key, resume_prompt, user_profile)

            cover_letter_prompt = "You are an AI cover letter writer. Generate a personalized cover letter based on the user's details."
            cover_letter_text = call_gpt4o(openai_api_key, cover_letter_prompt, user_profile)

            st.subheader("📄 AI-Generated Resume")
            st.markdown(resume_text)

            st.subheader("✉️ AI-Generated Cover Letter")
            st.markdown(cover_letter_text)

    st.write("---")
    st.caption("🔹 Developed with Streamlit & GPT-4o for AI-powered resume generation.")
