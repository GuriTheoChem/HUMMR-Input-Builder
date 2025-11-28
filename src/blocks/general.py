# src/blocks/general.py
import streamlit as st
from utils.ui_helpers import bool_kw, int_kw, float_kw, select_kw, str_kw

# Predefined basis sets
BASIS_SETS = [
    "SV", "SVP", "def2-SVP", "def2-SVPD", "def2-SV(P)", "def2-TZVP", "def2-TZVPP",
    "def2-TZVPD", "def2-TZVPPD", "def2-QZVP", "def2-QZVPP", "def2-QZVPD", "def2-QZVPPD",
    "cc-pVDZ", "cc-pVTZ", "cc-pVQZ", "cc-pV5Z",
    "aug-cc-pVDZ", "aug-cc-pVTZ", "aug-cc-pVQZ", "aug-cc-pV5Z",
    "ANO-RCC-MB", "ANO-RCC-VDZP", "ANO-RCC-VTZP", "ANO-RCC",
    "STO-3G", "3-21G", "6-31G",
    "USER-DEFINED", "USER-DEFINED-ORCA"
]

AUX_BASIS_SETS = [
    "def2-JK", "def2-SVP-C", "def2-SVPD-C", "def2-TZVP-C",
    "def2-TZVPD-C", "def2-QZVP-C", "def2-QZVPP-C", "def2-QZVPPD-C",
    "USER-DEFINED", "USER-DEFINED-ORCA"
]

def render_general_block():
    general = {}

    # =====================================================
    # Essential Options (always visible)
    # =====================================================
    with st.expander("Essential Options", expanded=False):
        # Calculation type
        general["CalcType"] = st.selectbox(
            "Calculation Type (CalcType)",
            ["NONE", "SCF", "CASSCF", "PLOT"],
            index=2   # default CASSCF
        )

        # Charge
        general["Charge"] = st.number_input("Total Charge (Charge)", value=0, step=1)

        # ----------------- Multiplicity -----------------
        mult_input = st.text_input(
            "Spin multiplicity / multiplicities (Mult)",
            value="1",
            help="For CASSCF you may specify multiple multiplicities, comma-separated. Minimum value = 1."
        )
        multiplicities = []
        for x in mult_input.split(","):
            try:
                val = int(x.strip())
                if val < 1:
                    st.warning(f"Multiplicity must be ≥ 1. Ignoring value {val}.")
                    continue
                multiplicities.append(val)
            except ValueError:
                st.warning(f"Invalid integer value: {x.strip()}. Ignoring.")
        if not multiplicities:
            multiplicities = [1]

        general["Mult"] = multiplicities

        # ----------------- Basis -----------------
        basis_choice = st.selectbox("Basis Set", BASIS_SETS, index=BASIS_SETS.index("def2-SVP"))

        if basis_choice in ["USER-DEFINED", "USER-DEFINED-ORCA"]:
            basis_file = st.text_input("Basis file name")
            # Combine keyword + file name into one string
            general["Basis"] = f"{basis_choice} {basis_file}".strip()
        else:
            general["Basis"] = basis_choice

        # ----------------- Auxiliary Basis -----------------
        aux_choice = st.selectbox("Auxiliary Basis Set", AUX_BASIS_SETS, index=AUX_BASIS_SETS.index("def2-JK"))

        if aux_choice in ["USER-DEFINED", "USER-DEFINED-ORCA"]:
            aux_file = st.text_input("Auxiliary basis file name")
            # Combine keyword + file name into one string
            general["AuxBasis"] = f"{aux_choice} {aux_file}".strip()
        else:
            general["AuxBasis"] = aux_choice

        # Other essential options
        general["OrcaJSONName"] = st.text_input("ORCA JSON filename (OrcaJSONName)", value="orca.json")
        general["Ints"] = st.selectbox("Integral Approximation (Ints)", ["NoRI", "RI"], index=1)
        general["Name"] = st.text_input("Calculation name (Name)", value="")

    # =====================================================
    # Advanced General Options (checkbox-controlled)
    # =====================================================
    with st.expander("Advanced Options"):
        bool_kw(general, "PrintBasis", "PrintBasis")
        bool_kw(general, "PrintOrbComp", "PrintOrbComp")

        str_kw(general, "InputBasis", "InputBasis")

        # ReadExternalH has two string arguments
        if st.checkbox("ReadExternalH"):
            method = st.selectbox("External Hamiltonian format", ["HUMMR", "ORCA", "READABLE"])
            fname = st.text_input("External Hamiltonian filename")
            # Combine method and filename into a single string
            general["ReadExternalH"] = f"{method} {fname}".strip()


        str_kw(general, "OrbGuessName", "OrbGuessName")
        bool_kw(general, "DoGeomOpt", "DoGeomOpt")

        # Orbital rotation (multi-value)
        if st.checkbox("OrbGuessRotation (GuessOrbRotation)"):
            i = st.number_input("First orbital index", min_value=0, value=0)
            j = st.number_input("Second orbital index", min_value=0, value=1)
            ang = st.number_input("Rotation angle (deg)", value=90.0)
            # Combine into single string
            general["OrbGuessRotation"] = f"{i} {j} {ang}"


        int_kw(general, "NThreads (OMP_NUM_THREADS)", "NThreads", default=1)
        str_kw(general, "PointChargeFilename", "PointChargeFilename")

    return general
