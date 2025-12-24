import streamlit as st
from pathlib import Path

from backend import (
    save_uploaded_file,
    extract_text,
    needs_ocr,
    clean_text,
)
from backend import evaluate_resume

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Resume Checker & Summarizer",
    layout="wide",
)

st.title("📄 Resume Checker & Summarizer")
st.caption("Upload a job description and resumes to evaluate candidate fit")

# -------------------------
# Sidebar – Inputs
# -------------------------
st.sidebar.header("Inputs")

jd_file = st.sidebar.file_uploader(
    "Upload Job Description (PDF or DOCX)",
    type=["pdf", "docx"],
)

resume_files = st.sidebar.file_uploader(
    "Upload Resumes (PDF or DOCX)",
    type=["pdf", "docx"],
    accept_multiple_files=True,
)

run_button = st.sidebar.button("Run Screening")

# -------------------------
# Main Logic
# -------------------------
if run_button:
    if not jd_file:
        st.error("Please upload a Job Description file.")
        st.stop()

    if not resume_files:
        st.error("Please upload at least one resume.")
        st.stop()

    # ---- Process Job Description ----
    with st.spinner("Processing job description..."):
        jd_path = save_uploaded_file(jd_file)
        jd_text_raw = extract_text(jd_path)

        if needs_ocr(jd_text_raw):
            st.warning("Job Description appears to be scanned. OCR not implemented yet.")
            st.stop()

        jd_text = clean_text(jd_text_raw)

    results = []

    # ---- Process Resumes ----
    for resume_file in resume_files:
        with st.spinner(f"Evaluating {resume_file.name}..."):
            try:
                resume_path = save_uploaded_file(resume_file)
                resume_text_raw = extract_text(resume_path)

                if needs_ocr(resume_text_raw):
                    st.warning(
                        f"{resume_file.name} appears to be scanned. OCR not implemented yet."
                    )
                    continue

                resume_text = clean_text(resume_text_raw)

                evaluation = evaluate_resume(
                    resume_text=resume_text,
                    jd_text=jd_text,
                )

                evaluation["file_name"] = resume_file.name
                results.append(evaluation)

            except Exception as e:
                st.error(f"Failed to process {resume_file.name}: {e}")

    # -------------------------
    # Display Results
    # -------------------------
    if not results:
        st.warning("No resumes could be evaluated.")
        st.stop()

    # Sort by match score
    results.sort(key=lambda x: x.get("match_score", 0), reverse=True)

    st.subheader("📊 Screening Results")

    for idx, res in enumerate(results, start=1):
        with st.expander(
            f"{idx}. {res.get('candidate_name','Unknown')} "
            f"({res.get('match_score',0)}%) – {res.get('final_verdict','')}"
        ):
            st.markdown(f"**Resume File:** {res.get('file_name')}")
            st.markdown("**Matched Skills:**")
            st.write(res.get("matched_skills", []))

            st.markdown("**Missing Skills:**")
            st.write(res.get("missing_skills", []))

            st.markdown("**Experience Summary:**")
            st.write(res.get("experience_summary", ""))

            st.markdown("**Explanation:**")
            st.write(res.get("explanation", ""))

else:
    st.info("Upload a Job Description and resumes from the sidebar to begin.")
