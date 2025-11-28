import streamlit as st
from blocks.general import render_general_block
from blocks.geom import render_geom_block
from blocks.scf import render_scf_block
from blocks.casscf import render_casscf_block
from blocks.ci import render_ci_block
from blocks.integrals import render_integrals_block
from blocks.implicitsolvation import render_implicit_solvation_block
from blocks.plot import render_plots_block
from blocks.spectra import render_spectra_block
from utils.generator import assemble_input

st.set_page_config(
    page_title="HUMMR Input Builder",
    page_icon="⚛️",
    layout="wide"
)

# --- Layout ---
left, right = st.columns([1, 1])  # Split screen

# Track choices
if "general" not in st.session_state:
    st.session_state.general = {}
if "geom" not in st.session_state:
    st.session_state.geom = []
if "blocks" not in st.session_state:
    st.session_state.blocks = {}

AVAILABLE_BLOCKS = [
    "SCF",
    "CASSCF",
    "CI",
    "ImplicitSolvation",
    "Spectra",
    "OrbPlot",
    "Integrals",
]

# --- LEFT PANEL ---
with left:
    st.header("⚙️ HUMMR Input Builder")

    # --- General Block ---
    with st.expander("General Block", expanded=False):
        st.session_state.general = render_general_block()

    st.divider()
    st.subheader("Include Blocks")
    chosen = st.multiselect("Select additional blocks", AVAILABLE_BLOCKS)

    st.session_state.blocks.clear()
    for blk in chosen:
        with st.expander(f"{blk} Block", expanded=False):  # Each optional block as dropdown
            if blk == "SCF":
                st.session_state.blocks["SCF"] = render_scf_block()
            elif blk == "CASSCF":
                st.session_state.blocks["CASSCF"] = render_casscf_block()
            elif blk == "CI":
                st.session_state.blocks["CI"] = render_ci_block()
            elif blk == "Integrals":
                st.session_state.blocks["Integrals"] = render_integrals_block()
            elif blk == "ImplicitSolvation":
                st.session_state.blocks["ImplicitSolvation"] = render_implicit_solvation_block()
            elif blk == "OrbPlot":
                st.session_state.blocks["OrbPlot"] = render_plots_block()
            elif blk == "Spectra":
                st.session_state.blocks["Spectra"] = render_spectra_block()
            # Add more blocks here as needed

    st.divider()
    # --- Geometry Block ---
    with st.expander("Geometry", expanded=False):
        st.session_state.geom = render_geom_block()

# --- RIGHT PANEL ---
with right:
    st.header("📄 Input Preview")
    final_input = assemble_input(
        st.session_state.general,
        st.session_state.blocks,
        st.session_state.geom,
    )
    st.text_area("Generated Input", final_input, height=800, label_visibility="collapsed")

    # --- Download button ---
    st.download_button(
        label="💾 Download Input File",
        data=final_input,
        file_name="hummr_input.inp",
        mime="text/plain"
    )