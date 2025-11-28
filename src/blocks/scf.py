# src/blocks/scf.py
import streamlit as st
from utils.ui_helpers import bool_kw, int_kw, float_kw, select_kw, str_kw

def render_scf_block():
    scf_opts = {}

    # ---------- SCF type ----------
    select_kw(scf_opts, "SCFType", "SCFType", ["RHF", "UHF"], index=0)

    # ---------- Integer options ----------
    int_kw(scf_opts, "MaxIter", "MaxIter", 75)

    # ---------- Float options ----------
    float_kw(scf_opts, "ETol", "ETol", 1e-8)
    float_kw(scf_opts, "DTol", "DTol", 1e-8)
    float_kw(scf_opts, "LevelShiftUp", "LevelShiftUp", 1.0)
    float_kw(scf_opts, "LevelShiftDn", "LevelShiftDn", 1.0)

    # ---------- Guess type ----------
    select_kw(scf_opts, "GuessType", "GuessType", ["Core", "ImprovedCore", "OrcaJSON", "OrcaGBW"], index=0)

    return scf_opts
