def block_to_text(name, data_dict):
    lines = [name]
    for key, value in data_dict.items():
        if value is None or value == "":
            continue
        if isinstance(value, list):
            v = " ".join(str(x) for x in value)
        else:
            v = str(value)
        lines.append(f"  {key} {v}")
    lines.append("End\n\n")
    return "\n".join(lines)


def geom_to_text(geom_data):
    lines = ["Geom"]
    if geom_data["type"] == "text":
        for atom, x, y, z in geom_data["geom_list"]:
            lines.append(f"  {atom} {x} {y} {z}")
    elif geom_data["type"] in ["file", "upload"]:
        lines.append(f"  {geom_data['filename']}")
    lines.append("End\n")
    return "\n".join(lines)


def assemble_input(general_dict, blocks_dict, geom_data):
    txt = block_to_text("General", general_dict)

    for bname, bdata in blocks_dict.items():
        txt += block_to_text(bname, bdata)

    txt += geom_to_text(geom_data)
    return txt
