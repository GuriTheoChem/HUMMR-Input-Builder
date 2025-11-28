# src/blocks/ci.py
import streamlit as st
from utils.ui_helpers import bool_kw, int_kw, float_kw, select_kw, str_kw

def render_ci_block():
    st.subheader("CI Block Options")

    opts = {}

    # ---------- Boolean options ----------
    bool_kw(opts, "BatchHCINEVPT2", "BatchHCINEVPT2", default=True)
    bool_kw(opts, "DoCIPSIOnHCI", "DoCIPSIOnHCI", default=True)
    bool_kw(opts, "DoHCIPT2", "DoHCIPT2", default=True)

    # ---------- Integer options ----------
    int_kw(opts, "DavidsonGuessDim", "DavidsonGuessDim", 1024)
    int_kw(opts, "DavidsonMaxIter", "DavidsonMaxIter", 50)
    int_kw(opts, "DavidsonMaxSize", "DavidsonMaxSize", 500)
    int_kw(opts, "DavidsonPCDim0", "DavidsonPCDim0", 512)
    int_kw(opts, "DavidsonPCDim1", "DavidsonPCDim1", 0)
    int_kw(opts, "HCIMaxIter", "HCIMaxIter", 20)
    int_kw(opts, "MaxPrefixBatchSize", "MaxPrefixBatchSize", 1000)

    # ---------- Float options ----------
    float_kw(opts, "DavidsonRTol", "DavidsonRTol", 1e-6)
    float_kw(opts, "EpsilonGen", "EpsilonGen", 1e-2)
    float_kw(opts, "EpsilonHCI", "EpsilonHCI", 1e-5)
    float_kw(opts, "EpsilonHCIPT2", "EpsilonHCIPT2", 1e-6)
    float_kw(opts, "EpsilonHCINEVPT2", "EpsilonHCINEVPT2", 1e-7)
    float_kw(opts, "EpsilonHCIENEVPT2", "EpsilonHCIENEVPT2", 1e-7)
    float_kw(opts, "HCIETol", "HCIETol", 1e-5)

    # ---------- String options ----------
    str_kw(opts, "HCICFGsFName", "HCICFGsFName", default="")

    return opts
