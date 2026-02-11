import json
import subprocess
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]

st.set_page_config(page_title="Paper Orchestrator", layout="wide")
st.title("Paper Workflow Orchestrator (Demo)")

paper_id = st.text_input("paper_id", value="anti_bayesian_2015")
intro_file = st.text_input("Intro file", value=str(ROOT / "demo_v2_anti_bayesian" / "parsed.md"))
index_file = st.text_input("RAG index", value=str(ROOT / "rag" / "background_index.json"))
out_file = st.text_input("Output pre-results file", value=str(ROOT / "demo_v2_anti_bayesian" / "pre_results_hypothesis.md"))

col1, col2 = st.columns(2)
with col1:
    if st.button("1) Build RAG index"):
        cmd = ["python3", str(ROOT / "scripts" / "build_background_index.py"), "--input", str(ROOT / "rag" / "background_corpus.jsonl"), "--output", str(ROOT / "rag" / "background_index.json")]
        r = subprocess.run(cmd, capture_output=True, text=True)
        st.code((r.stdout or "") + ("\n" + r.stderr if r.stderr else ""))

with col2:
    if st.button("2) Generate Pre-Results Hypothesis"):
        cmd = ["python3", str(ROOT / "scripts" / "generate_hypothesis_stage.py"), "--paper-id", paper_id, "--intro", intro_file, "--rag-index", index_file, "--out", out_file]
        r = subprocess.run(cmd, capture_output=True, text=True)
        st.code((r.stdout or "") + ("\n" + r.stderr if r.stderr else ""))

st.subheader("Quick RAG query")
q = st.text_input("query", value="efficient coding anti-bayesian repulsive bias")
if st.button("3) Query RAG"):
    cmd = ["python3", str(ROOT / "scripts" / "query_background_rag.py"), "--index", index_file, "--query", q, "--topk", "3"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    st.code((r.stdout or "") + ("\n" + r.stderr if r.stderr else ""))

st.subheader("Preview outputs")
for p in [Path(out_file), ROOT / "demo_v2_anti_bayesian" / "figure_map.md", ROOT / "demo_v2_anti_bayesian" / "post_expert.md"]:
    if p.exists():
        with st.expander(str(p.relative_to(ROOT))):
            st.text(p.read_text()[:8000])
