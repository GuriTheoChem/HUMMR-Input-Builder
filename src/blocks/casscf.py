# src/blocks/casscf.py
import streamlit as st
from utils.ui_helpers import bool_kw, int_kw, float_kw, select_kw, str_kw

def render_casscf_block():
    casscf_opts = {}

    # =====================================================
    # Basic CASSCF Options (always visible)
    # =====================================================
    with st.expander("Basic CASSCF Options", expanded=False):
        casscf_opts["NEl"] = st.number_input("Number of active electrons (NEl)", min_value=0, value=4, step=1)
        casscf_opts["NOrb"] = st.number_input("Number of active orbitals (NOrb)", min_value=0, value=4, step=1)
        casscf_opts["NRoots"] = st.number_input("Number of roots (NRoots)", min_value=1, value=1, step=1)
        casscf_opts["CISolver"] = st.selectbox("Active-space solver (CISolver)", ["FCI", "HCI", "GCI"], index=0)
        casscf_opts["MaxIter"] = st.number_input("Max orbital optimization iterations", min_value=1, value=35, step=1)
        casscf_opts["OrbStep"] = st.selectbox("Orbital optimization technique (OrbStep)", ["NR", "DIIS", "FNR", "SuperCIPTDIIS"], index=3)
        casscf_opts["SwitchOrbStep"] = st.selectbox("Orbital optimization step near convergence (SwitchOrbStep)", ["NR", "DIIS", "FNR", "SuperCIPTDIIS"], index=1)

    # =====================================================
    # Advanced CASSCF Options (checkbox-controlled)
    # =====================================================
    with st.expander("Advanced CASSCF Options"):
        # ---------- Float options ----------
        float_kw(casscf_opts, "ConfImportanceThrs", "ConfImportanceThrs", 5e-2, "%.2e")
        float_kw(casscf_opts, "DIISFac", "DIISFac", 1.05, "%.2f")
        float_kw(casscf_opts, "ETol", "ETol", 1e-7)
        float_kw(casscf_opts, "GTol", "GTol", 1e-4)
        float_kw(casscf_opts, "IPEAShiftValue", "IPEAShiftValue", 0.25, "%.2f")
        float_kw(casscf_opts, "PrintWeightThresh", "PrintWeightThresh", 0.01, "%.2f")
        float_kw(casscf_opts, "LevelShiftDn", "LevelShiftDn", 1.0, "%.2f")
        float_kw(casscf_opts, "LevelShiftUp", "LevelShiftUp", 1.0, "%.2f")
        float_kw(casscf_opts, "NRTol", "NRTol", 1e-5)
        float_kw(casscf_opts, "SwitchOrbStepThresh", "SwitchOrbStepThresh", 0.03, "%.2f")
        float_kw(casscf_opts, "TrustRadius", "TrustRadius", 0.5)
        float_kw(casscf_opts, "TrustRadiusScaling", "TrustRadiusScaling", 0.7)
        float_kw(casscf_opts, "UsePrevCFGsThrs", "UsePrevCFGsThrs", 5e-4)
        float_kw(casscf_opts, "NRRTol", "NRRTol", 1e-5)
        float_kw(casscf_opts, "PCGThresh", "PCGThresh", 1e-5)

        # ---------- Integer options ----------
        int_kw(casscf_opts, "DavidsonAHPCDim", "DavidsonAHPCDim", 256)
        int_kw(casscf_opts, "DIISDim", "DIISDim", 5)
        int_kw(casscf_opts, "MaxNTrialVecs", "MaxNTrialVecs", 500)
        int_kw(casscf_opts, "OutputLevel", "OutputLevel", 0)
        int_kw(casscf_opts, "NRMaxIter", "NRMaxIter", 50)
        int_kw(casscf_opts, "NRGuessMatDim", "NRGuessMatDim", 256)
        int_kw(casscf_opts, "PCGMaxIter", "PCGMaxIter", 100)

        # ---------- Boolean options ----------
        bool_kw(casscf_opts, "DoASSIST", "DoASSIST")
        bool_kw(casscf_opts, "DoNEVPT2", "DoNEVPT2")
        bool_kw(casscf_opts, "DoSOC", "DoSOC")
        bool_kw(casscf_opts, "StoreSOCMatrices", "StoreSOCMatrices")
        bool_kw(casscf_opts, "DoQDNEVPT2", "DoQDNEVPT2")
        bool_kw(casscf_opts, "FullConvergence", "FullConvergence")
        bool_kw(casscf_opts, "GTensor", "GTensor")
        bool_kw(casscf_opts, "IPEAShift", "IPEAShift")
        bool_kw(casscf_opts, "ReadMatricesOnly", "ReadMatricesOnly")
        bool_kw(casscf_opts, "WriteMatricesOnly", "WriteMatricesOnly")
        bool_kw(casscf_opts, "ReadExtHOrcaJSON", "ReadExtHOrcaJSON")
        bool_kw(casscf_opts, "CalcSSGrad", "CalcSSGrad")
        bool_kw(casscf_opts, "CalcSAGrad", "CalcSAGrad")
        bool_kw(casscf_opts, "CalcNAC", "CalcNAC")
        bool_kw(casscf_opts, "CalcCIOptGrad", "CalcCIOptGrad")
        bool_kw(casscf_opts, "DoENEVPT2", "DoENEVPT2")
        bool_kw(casscf_opts, "DoNEVPT2Residuals", "DoNEVPT2Residuals")
        bool_kw(casscf_opts, "DoAC0", "DoAC0")

        # ---------- Selectbox options ----------
        select_kw(casscf_opts, "FinalActOrbs", "FinalActOrbs", ["unchanged", "natural", "canonical"], index=2)
        select_kw(casscf_opts, "OrbOrderType", "OrbOrderType", ["none", "Fiedler", "Generic"], index=2)
        select_kw(casscf_opts, "PTCanonStep", "PTCanonStep", ["SA", "SS", 0, 1], index=0)
        select_kw(casscf_opts, "QDNEVPT2Type", "QDNEVPT2Type", ["VanVleck", "Cloizeaux", "Bloch"])

        # ---------- Weights (multi-value doubles) ----------
        if st.checkbox("Weights"):
            weights_input = st.text_input(
                "Weights (comma-separated doubles)",
                value="1.0",
                help="Specify one or more weights, comma-separated."
            )
            weights = []
            for x in weights_input.split(","):
                try:
                    val = float(x.strip())
                    weights.append(val)
                except ValueError:
                    st.warning(f"Invalid float value: {x.strip()}. Ignoring.")
            if not weights:
                weights = [1.0]

            casscf_opts["Weights"] = weights

    return casscf_opts
