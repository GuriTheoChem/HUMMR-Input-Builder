# utils/ui_helpers.py
import streamlit as st

# ---------- Helper for bool keywords ----------
def bool_kw(opts_dict, label, keyname, default=True):
    if st.checkbox(label, key=f"{keyname}_chk"):
        opts_dict[keyname] = st.selectbox(f"{label} (True / False)", [True, False],
                                         index=0 if default else 1, key=f"{keyname}_val")

# ---------- Helper for float-in-scientific-notation ----------
def float_kw(opts_dict, label, keyname, default, fmt="%.1e"):
    if st.checkbox(label, key=f"{keyname}_chk"):
        opts_dict[keyname] = st.number_input(label, value=default, format=fmt, key=f"{keyname}_val")

# ---------- Helper for integer keywords ----------
def int_kw(opts_dict, label, keyname, default):
    if st.checkbox(label, key=f"{keyname}_chk"):
        opts_dict[keyname] = st.number_input(label, min_value=0, value=default, step=1, key=f"{keyname}_val")

# ---------- Helper for selectbox keywords ----------
def select_kw(opts_dict, label, keyname, options, index=0):
    if st.checkbox(label, key=f"{keyname}_chk"):
        opts_dict[keyname] = st.selectbox(label, options, index=index, key=f"{keyname}_val")

# ---------- Helper for string keywords ----------
def str_kw(opts_dict, label, keyname, default=""):
    if st.checkbox(label, key=f"{keyname}_chk"):
        opts_dict[keyname] = st.text_input(label, value=default, key=f"{keyname}_val")
