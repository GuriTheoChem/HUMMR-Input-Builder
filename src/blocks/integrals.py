# src/blocks/integrals.py
import streamlit as st
from utils.ui_helpers import bool_kw, int_kw, float_kw, select_kw, str_kw

def render_integrals_block():
    st.subheader("Integrals Block Options")
    integrals_opts = {}

    # ---------- Boolean options ----------
    bool_kw(integrals_opts, "AutoauxThresh1", "AutoauxThresh1", default=True)
    bool_kw(integrals_opts, "AutoauxThresh2", "AutoauxThresh2", default=True)
    bool_kw(integrals_opts, "DoRISOMF", "DoRISOMF", default=True)
    bool_kw(integrals_opts, "OverlapFit", "OverlapFit", default=True)
    bool_kw(integrals_opts, "UseApproximateFock", "UseApproximateFock", default=True)

    # ---------- Float options ----------
    float_kw(integrals_opts, "GridPointThresh", "GridPointThresh", 1e-12)
    float_kw(integrals_opts, "SchwarzThresh", "SchwarzThresh", 1e-12)
    float_kw(integrals_opts, "RadialGridTol", "RadialGridTol", 3e-5)

    # ---------- Integer options ----------
    int_kw(integrals_opts, "LebedevRule", "LebedevRule", 11)

    return integrals_opts
