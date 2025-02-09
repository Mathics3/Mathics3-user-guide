import re

import os.path as osp
import pickle
import subprocess
import tempfile
from typing import Dict, Optional, Union

import matplotlib
import matplotlib.pyplot as plt

from mathics import __version__, settings, version_info, version_string
from mathics import settings
from mathics.doc.utils import load_doctest_data
from doc2rst import DOCTEST_RST_DATA_PCL

ASY_LATEX_BLOCK = re.compile(r"\\begin{asy}([\s\S]+?)\\end{asy}")
IMAGE_LATEX_ENTRY = re.compile(r"(?m)\\includegraphics\[(.*?)\]{(.*?)}")

DOC_DIR = settings.DOC_DIR


SKIP_ASY = False



def convert_asy_code(content: str, key=""):
    """Convert asy code into a png picture.
    Return a LaTeX includegraphics instruction"""
    tmp_filename = get_tmp_filename(prefix="asy_" + key, suffix=".asy")
    # print(content)
    if not SKIP_ASY:
        with open(tmp_filename, "w") as asy_file:
            asy_file.write(content)

    tmp_path, _ = osp.split(tmp_filename)
    result = tmp_filename[:-4] + ".png"
    if not SKIP_ASY:
        subprocess.run(["asy", "-f", "png", "-render", "70", tmp_filename], cwd=tmp_path)
    result = osp.abspath(result)
    return r"\includegraphics[]{" + result + "}"


def convert_latex_to_png(content, key=""):
    """
    Generate a png image from LaTeX
    code.
    """
    tmp_filename = get_tmp_filename(prefix="eq_"+key, suffix=".png")
    try:
        latex_to_img(f"${content}$", tmp_filename)
    except ValueError as e:
        print(f"${content}$", "could not be processed as LaTeX")
        print(e)
        raise
    return tmp_filename


def convert_mathics_latex_to_RsT(
        out_latex: Optional[Union[str, dict]], key=""
) -> Optional[Union[str, dict]]:
    """
    Convert a LaTeX block into a RsT compatible
    block.
    """
    if out_latex is None:
        return None
    # If out_latex is a dict, return without changes.
    # By now, it only contains plane-text prints and
    # messages.
    if isinstance(out_latex, dict):
        return out_latex

    assert isinstance(out_latex, str)
    # out_latex is a string
    out_latex = str(out_latex).strip()
    out_latex = ASY_LATEX_BLOCK.sub(lambda m: convert_asy_code(m.group(1), key), out_latex)
    out_latex = out_latex.strip()
    img_match = IMAGE_LATEX_ENTRY.fullmatch(out_latex)
    if img_match:
        parms = img_match.group(1)
        filename = img_match.group(2)
        return f".. image:: {filename}\n    :align: center\n\n"
    if "multicol" in out_latex or IMAGE_LATEX_ENTRY.findall(out_latex):
        # Compile LaTeX a produce a png picture.
        filename = convert_latex_to_png(out_latex, key)
        return f".. image:: {filename}\n    :align: center\n\n"
    out_latex = out_latex.replace("`", r"\`{}")

    lines = out_latex.split("\n")
    if len(lines) > 1:
        return "\n.. math::\n    " + "\n    ".join(lines) + "\n\n"

    return f":math:`{out_latex}`\n"



def convert_output_to_rst(test_data, key=""):
    """
    Convert the output data from a doctest
    to RsT format.
    """
    # print(test_data["query"])
    try:
        converted_data = {
            "query": test_data["query"],
            "results": [convert_result_to_rst(item, key) for item in test_data["results"]],
        }
    except ValueError, RuntimeError:
        print("Result from ", test_data["query"], "could not be converted.")
        return None
    return converted_data


def convert_result_to_rst(result_dict, key=""):
    """
    Convert the content of the result dict
    to a RsT compatible form.
    """
    converted_result = {
        "line": result_dict["line"],
        "form": "RsT",
        "out": [convert_mathics_latex_to_RsT(out_line, key) for out_line in result_dict["out"]],
        "result": convert_mathics_latex_to_RsT(result_dict["result"], key),
    }
    for key in result_dict:
        assert key in converted_result
    return converted_result


def convert_test_data_to_rst(latex_test_data):
    """
    Process all the entries in the LaTeX test data dict
    and produce a new dict with test data formatted for
    RsT.
    """
    rst_tex_data = {}
    for key, test in latex_test_data.items():
        rst_tex_data[key] = convert_output_to_rst(test, ("_".join(key[:-1])).replace(" ", "_")+"_")
    return rst_tex_data



def get_tmp_filename(prefix="", suffix=""):
    # This produces a random name, where the png file is going to be stored.
    # LaTeX does not have a native way to store an figure embedded in
    # the source.
    fp = tempfile.NamedTemporaryFile(delete=True, prefix=prefix, suffix=suffix)
    path = fp.name
    fp.close()
    return path


def latex_to_img(tex, fn):
    """
    produce a picture from LaTeX code.
    Borrowed from
    https://stackoverflow.com/questions/1381741/converting-latex-code-to-images-or-other-displayble-format-with-python
    """
    matplotlib.rcParams["text.latex.preamble"] = (
        "\\usepackage{multicol}\n" "\\usepackage{amsmath}\n" "\\usepackage{amssymb}\n" "\\usepackage{graphicx}\n"
    )
    # LaTeX from matplotlib does not accept linebreaks or
    # the \text command. Use \mbox instead.
    tex = tex.replace(r'\text{',r'\mbox{')
    tex = tex.replace("\n", " ")
    # TODO: adjust the size of the figure.
    plt.figure(figsize=(3,1))
    plt.rc("text", usetex=True)
    plt.rc("font", family="serif")
    plt.axis("off")
    plt.text(0.05, 0.5, f"{tex}", size=12)
    plt.savefig(fn, format="png", bbox_inches='tight', backend="pgf", dpi=250,)
    plt.close()



def read_doctest_data(quiet=False) -> Optional[Dict[tuple, dict]]:
    """
    Read doctest information from PCL file and return this.
    This is a wrapper around laod_doctest_data().
    """
    if not quiet:
        print(f"Extracting internal doctest data for {version_string}")
    try:
        return load_doctest_data(
            settings.get_doctest_latex_data_path(should_be_readable=True)
        )
    except KeyboardInterrupt:
        print("\nAborted.\n")
        return None
    except Exception:
        return {}



def main():
    """Generate a pickle file with outputs compatible with RsT"""
    latex_test_data = read_doctest_data()
    rst_test_data = convert_test_data_to_rst(latex_test_data)
    with open(DOCTEST_RST_DATA_PCL, "wb") as output_file:
        pickle.dump(rst_test_data, output_file, 4)
    print("done.")



    
if __name__ == "__main__":    
    main()
