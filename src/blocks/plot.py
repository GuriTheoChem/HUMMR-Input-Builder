# src/blocks/plots.py
import streamlit as st
from utils.ui_helpers import bool_kw, int_kw, str_kw

def render_plots_block():
    st.subheader("Orbital and Density Plots Options")
    opts = {}

    # ---------- Always-visible ----------
    # ORBS: user enters list manually
    orbs_input = st.text_input("Orbitals to plot (ORBS, comma-separated indices)", value="")
    if orbs_input.strip():
        try:
            opts["ORBS"] = [int(x.strip()) for x in orbs_input.split(",")]
        except:
            st.warning("Invalid ORBS input: please enter comma-separated integers.")

    # GRIDPOINTS: default 40 40 40
    grid_input = st.text_input("Grid points (x y z) for plot (GRIDPOINTS)", value="40 40 40")
    try:
        opts["GRIDPOINTS"] = [int(x) for x in grid_input.strip().split()]
        if len(opts["GRIDPOINTS"]) != 3:
            st.warning("GRIDPOINTS must have three integer values.")
    except:
        st.warning("Invalid GRIDPOINTS input. Enter three integers separated by spaces.")

    # ---------- Checkbox-activated ----------
    # RANGE: 6 floats, entered as text
    range_input = st.text_input(
        "Plot range (xmin xmax ymin ymax zmin zmax) for RANGE",
        value="-7.0 7.0 -7.0 7.0 -7.0 7.0"
    )
    try:
        opts["RANGE"] = [float(x) for x in range_input.strip().split()]
        if len(opts["RANGE"]) != 6:
            st.warning("RANGE must have six numeric values.")
    except:
        st.warning("Invalid RANGE input. Enter six numbers separated by spaces.")

    # Boolean options
    bool_kw(opts, "PLOTDENSITY", "PLOTDENSITY", default=False)
    bool_kw(opts, "PLOTSPINDENSITY", "PLOTSPINDENSITY", default=False)

    # String options
    str_kw(opts, "DENSITYFILENAME", "DENSITYFILENAME", default="Density.tmp")
    str_kw(opts, "SPINDENSITYFILENAME", "SPINDENSITYFILENAME", default="Spindensity.tmp")

    return opts
