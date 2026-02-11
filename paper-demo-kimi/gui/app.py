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

st.subheader("Aggressive context compaction")
compact_only = st.checkbox("Compact packet only mode", value=True)
per_file = st.number_input("Per-file char cap", min_value=300, max_value=5000, value=1800, step=100)
if st.button("4) Build compact context packet"):
    cmd = ["python3", str(ROOT / "scripts" / "context_compact.py"), "--root", str(ROOT), "--out", "context/context_packet.json", "--per-file", str(per_file)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    st.code((r.stdout or "") + ("\n" + r.stderr if r.stderr else ""))

st.subheader("OpenRouter pre-parse")
pre_task = st.selectbox("Pre-parse task", options=["parse_text", "parse_equation", "parse_figure"], index=0)
pre_input_default = str(ROOT / "context" / "context_packet.json") if compact_only else str(ROOT / "demo_v2_anti_bayesian" / "parsed.md")
pre_input = st.text_input("Pre-parse input", value=pre_input_default)
pre_model = st.text_input("Model override (optional)", value="")
pre_ttl = st.number_input("Cache TTL hours", min_value=1, max_value=24*30, value=168, step=24)
if st.button("5) Run OpenRouter pre-parse"):
    cmd = ["python3", str(ROOT / "scripts" / "openrouter_preparse.py"), "--task", pre_task, "--input", pre_input, "--cache-ttl-hours", str(pre_ttl)]
    if pre_model.strip():
        cmd += ["--model", pre_model.strip()]
    r = subprocess.run(cmd, capture_output=True, text=True)
    st.code((r.stdout or "") + ("\n" + r.stderr if r.stderr else ""))

if st.button("6) Cleanup expired OpenRouter cache"):
    cmd = ["python3", str(ROOT / "scripts" / "openrouter_preparse.py"), "--cleanup-only", "--input", str(ROOT / "README.md"), "--cache-ttl-hours", str(pre_ttl)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    st.code((r.stdout or "") + ("\n" + r.stderr if r.stderr else ""))

st.subheader("Kimi Stage B/C (compact packet only)")
stage_model = st.text_input("Kimi model", value="moonshotai/kimi-k2.5")
if st.button("7) Run Stage B reconcile"):
    cmd = ["python3", str(ROOT / "scripts" / "stage_b_reconcile.py"), "--packet", str(ROOT / "context" / "context_packet.json"), "--model", stage_model, "--out", str(ROOT / "demo_v2_anti_bayesian" / "stage_b_reconcile.md")]
    r = subprocess.run(cmd, capture_output=True, text=True)
    st.code((r.stdout or "") + ("\n" + r.stderr if r.stderr else ""))
if st.button("8) Run Stage C final post"):
    cmd = ["python3", str(ROOT / "scripts" / "stage_c_finalize.py"), "--packet", str(ROOT / "context" / "context_packet.json"), "--stage-b", str(ROOT / "demo_v2_anti_bayesian" / "stage_b_reconcile.md"), "--model", stage_model, "--out", str(ROOT / "demo_v2_anti_bayesian" / "post_expert_compact.md")]
    r = subprocess.run(cmd, capture_output=True, text=True)
    st.code((r.stdout or "") + ("\n" + r.stderr if r.stderr else ""))

st.subheader("Local delegation (Ollama)")
local_input = st.text_input("Local task input", value=str(ROOT / "demo_v2_anti_bayesian" / "parsed.md"))
local_model = st.text_input("Local model", value="qwen2.5:7b-instruct")
local_task = st.selectbox("Task", options=["summarize", "normalize", "checklist"], index=0)
if st.button("9) Run local delegation"):
    cmd = ["python3", str(ROOT / "local" / "delegate_basic.py"), "--task", local_task, "--input", local_input, "--model", local_model]
    r = subprocess.run(cmd, capture_output=True, text=True)
    st.code((r.stdout or "") + ("\n" + r.stderr if r.stderr else ""))

st.subheader("Preview outputs")
for p in [Path(out_file), ROOT / "demo_v2_anti_bayesian" / "figure_map.md", ROOT / "demo_v2_anti_bayesian" / "post_expert.md"]:
    if p.exists():
        with st.expander(str(p.relative_to(ROOT))):
            st.text(p.read_text()[:8000])
