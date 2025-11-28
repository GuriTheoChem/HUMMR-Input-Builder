# src/blocks/implicit_solvation.py
import streamlit as st
from utils.ui_helpers import bool_kw, int_kw, float_kw, select_kw, str_kw

def render_implicit_solvation_block():
    st.subheader("Implicit Solvation Options")
    opts = {}

    # ---------- Always-visible dropdowns ----------
    solvent_list = [
        "AceticAcid","Acetone","Acetonitrile","Anisole","Benzene","Bromobenzene",
        "Carbondisulfide","Carbontetrachloride","Chlorobenzene","Chloroform","CHCL3",
        "Cyclohexane","Dibutylether","ODichlorobenzene","Dichloroethane","Diethylamine",
        "Diethylether","Dimethoxyethane","Dimethylacetamide","Dimethylformamide",
        "Dimetgylsulfoxide","Dioxane","Ethanol","Ethylacetate","Ethylbenzoate","Formamide",
        "HFIP","Isopropanol","Methanol","Nitrobenzene","Nitromethane","Pyridine","THF",
        "Toluene","Trichloroethylene","Triethylamine","TrifluoroaceticAcid","Trufluoroethanol",
        "Water","Oxylene"
    ]

    opts["Solvent"] = st.selectbox("Solvent", solvent_list)
    opts["Solver"] = st.selectbox("Solver", ["PCG", "Inverse"], index=0)
    opts["Model"] = st.selectbox("Model", ["CPCM", "COSMO"], index=0)

    # ---------- Checkbox-activated options ----------
    str_kw(opts, "ChargeRepresentation", "ChargeRepresentation", default="Gaussian")
    float_kw(opts, "Epsilon", "Epsilon", 1.0)
    float_kw(opts, "IntegralThreshold", "IntegralThreshold", 1e-12)
    int_kw(opts, "LebedevOrder", "LebedevOrder", 8)
    bool_kw(opts, "DoRISOMF", "DoRISOMF", default=False)
    bool_kw(opts, "OverlapFit", "OverlapFit", default=True)
    float_kw(opts, "GridPointThresh", "GridPointThresh", 1e-12)
    float_kw(opts, "SchwarzThresh", "SchwarzThresh", 1e-12)
    float_kw(opts, "RadialGridTol", "RadialGridTol", 3e-5)
    bool_kw(opts, "UseApproximateFock", "UseApproximateFock", default=False)
    int_kw(opts, "PCGMaxIter", "PCGMaxIter", 100)
    float_kw(opts, "PCGThreshold", "PCGThreshold", 1e-10)
    float_kw(opts, "RadialScaling", "RadialScaling", 1.2)

    if st.checkbox("NewRadius"):
        radii_text = st.text_area("NewRadius entries (format: AtomType value, one per line)")
        new_radii = []
        for line in radii_text.splitlines():
            try:
                atom, val = line.split()
                new_radii.append((atom.strip(), float(val)))
            except:
                pass
        if new_radii:
            opts["NewRadius"] = new_radii

    if st.checkbox("ReadSolvFile"):
        filename = st.text_input("Solv file name")
        properties = st.selectbox("Properties to read", ["OverwriteAll", "NoRead"])
        opts["ReadSolvFile"] = (filename, properties)

    select_kw(opts, "UpdatingScheme", "UpdatingScheme", ["Direct", "Gradient"], index=0)

    return opts
