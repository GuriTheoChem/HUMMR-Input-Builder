import streamlit as st

def render_geom_block():
    """
    Allows user to input geometry manually, specify a file, or upload an .xyz file.
    Numeric formatting is preserved exactly as typed.
    """

    # Default geometry
    default_geom = """H 0.000000 0.000000 0.000000
H 0.000000 0.000000 0.900000"""

    if "geom_mode" not in st.session_state:
        st.session_state.geom_mode = "text"
    if "geom_text" not in st.session_state:
        st.session_state.geom_text = default_geom

    mode = st.radio(
        "Geometry mode",
        ["Enter manually", "Use external file", "Upload XYZ file"],
        index=0
    )

    # --- Manual geometry mode ---
    if mode == "Enter manually":
        st.session_state.geom_mode = "text"
        geom_text = st.text_area("Geometry", value=st.session_state.geom_text, height=150)
        st.session_state.geom_text = geom_text

        geom_list = []
        for line in geom_text.splitlines():
            if not line.strip():
                continue
            parts = line.split()
            if len(parts) != 4:
                st.error(f"Invalid geometry line: '{line}' (expected 4 columns)")
                continue
            atom, x, y, z = parts[0], parts[1], parts[2], parts[3]
            geom_list.append((atom, x, y, z))

        return {"type": "text", "geom_list": geom_list}

    # --- File mode (external reference) ---
    elif mode == "Use external file":
        st.session_state.geom_mode = "file"
        filename = st.text_input("Geometry filename (.xyz)")
        return {"type": "file", "filename": filename}

    # --- Upload XYZ file ---
    else:
        st.session_state.geom_mode = "upload"
        uploaded_file = st.file_uploader("Upload XYZ file", type=["xyz"], key="xyz_upload")
        geom_list = []

        if uploaded_file is not None:
            content = uploaded_file.read().decode("utf-8")
            lines = content.splitlines()

            if len(lines) < 3:
                st.error("XYZ file must have at least 3 lines (number of atoms, comment, coordinates).")
            else:
                for line in lines[2:]:
                    if not line.strip():
                        continue
                    parts = line.split()
                    if len(parts) != 4:
                        st.error(f"Invalid geometry line in uploaded file: '{line}'")
                        continue
                    atom, x, y, z = parts[0], parts[1], parts[2], parts[3]
                    geom_list.append((atom, x, y, z))

                # Paste into text area for preview/edit
                st.session_state.geom_text = "\n".join([f"{a} {x} {y} {z}" for a, x, y, z in geom_list])
                st.text_area("Geometry (from uploaded XYZ file)", value=st.session_state.geom_text, height=150)

            return {"type": "text", "geom_list": geom_list}

        # If upload removed or None, revert to default geometry
        st.session_state.geom_text = default_geom
        geom_list = []
        for line in default_geom.splitlines():
            atom, x, y, z = line.split()
            geom_list.append((atom, x, y, z))
        return {"type": "text", "geom_list": geom_list}
