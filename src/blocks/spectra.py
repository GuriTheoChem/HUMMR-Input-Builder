# src/blocks/spectra.py
import streamlit as st
from utils.ui_helpers import bool_kw, int_kw, float_kw

def render_spectra_block():
    st.subheader("Spectra Options")
    opts = {}

    # ---------- Always-visible ----------
    opts["Start"] = st.number_input("Start energy (cm^-1)", value=10000.0, format="%.1f")
    opts["Stop"] = st.number_input("Stop energy (cm^-1)", value=150000.0, format="%.1f")

    # ---------- Checkbox-activated ----------
    float_kw(opts, "FWHM", "FWHM", default=1337.0)
    int_kw(opts, "NPoints", "NPoints", default=14000)
    bool_kw(opts, "Gaussian", "Gaussian", default=True)
    bool_kw(opts, "Lorentzian", "Lorentzian", default=False)

    return opts
