import re

import os.path as osp
import pickle
import subprocess
import tempfile
from typing import Dict, Optional, Union


from mathics import __version__, settings, version_info, version_string
from mathics import settings
from mathics.doc.utils import load_doctest_data
from doc2rst import DOCTEST_RST_DATA_PCL

ASY_LATEX_BLOCK = re.compile(r'\\begin{asy}([\s\S]+?)\\end{asy}')
IMAGE_LATEX_ENTRY = re.compile(r'\\includegraphics\[(.*?)\]{(.*?)}')

DOC_DIR = settings.DOC_DIR


SKIP_ASY = False

def get_tmp_filename(suffix=""):
    # This produces a random name, where the png file is going to be stored.
    # LaTeX does not have a native way to store an figure embedded in
    # the source.
    fp = tempfile.NamedTemporaryFile(delete=True, suffix=suffix)
    path = fp.name
    fp.close()
    return path



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


def convert_test_data_to_rst(latex_test_data):
    """
    Process all the entries in the LaTeX test data dict
    and produce a new dict with test data formatted for
    RsT.
    """
    rst_tex_data = {}
    for key, test in latex_test_data.items():
        rst_tex_data[key] = convert_output_to_rst(test)
    return rst_tex_data


def compile_latex_to_png(content):
    return "/tmp/generate_me.png %"+content+"\n"
    
def process_asy(content:str):
    """Convert asy code into a png picture.
    Return a LaTeX includegraphics instruction"""
    tmp_filename = get_tmp_filename(".asy")
    # print(content)
    if not SKIP_ASY:
        with open(tmp_filename, "w") as asy_file:
            asy_file.write(content)

    tmp_path, _ =osp.split(tmp_filename)
    result = tmp_filename[:-4]+".png"
    if not SKIP_ASY:
        subprocess.run(["asy", "-f", "png", tmp_filename], cwd=tmp_path)
    result = osp.abspath(result)
    return r"\includegraphics[]{"+result+"}"
        

def mathics_latex_to_RsT(
        out_latex:Optional[Union[str, dict]])->Optional[Union[str, dict]]:
    if out_latex is None:
        return None
    # If out_latex is a dict, returns without changes.
    if isinstance(out_latex, dict):
        return out_latex
    assert isinstance(out_latex, (str,dict))
    # out_latex is a string
    out_latex = str(out_latex).strip()
    out_latex = ASY_LATEX_BLOCK.sub(lambda m: process_asy(m.group(1)), out_latex)
    out_latex = out_latex.strip()
    img_match = IMAGE_LATEX_ENTRY.fullmatch(out_latex)
    if img_match:
        parms = img_match.group(1)
        filename = img_match.group(2)
        return f".. image:: {filename}\n    :align: center\n\n"
    if IMAGE_LATEX_ENTRY.match(out_latex):
        # Compile LaTeX a produce a png picture.
        filename = compile_latex_to_png(out_latex)
        return f".. image:: {filename}\n    :align: center\n\n"
    out_latex = out_latex.replace("`", r"\`{}")
    
    lines = out_latex.split("\n")
    if len(lines)>1:
        return "\n.. math::\n    " + "\n    ".join(lines)+"\n\n"

    return f":math:`{out_latex}`\n"

def convert_result_to_rst(result_dict):

    converted_result = {
        "line":result_dict["line"],
        "form":"RsT",
        "out":[mathics_latex_to_RsT(out_line)  for  out_line in result_dict["out"]],
        "result": mathics_latex_to_RsT(result_dict["result"]),
    }
    for key in result_dict:
        assert key in converted_result
    return converted_result

    
def convert_output_to_rst(test_data):
    """
    Convert the output data from a doctest
    to RsT format.
    """
    # print(test_data["query"])
    converted_data = {"query":test_data["query"],
                      "results": [
                          convert_result_to_rst(item) for item in
                          test_data["results"]
                      ]}
    return converted_data
    

def main():
    """Generate a pickle file with outputs compatible with RsT"""
    latex_test_data = read_doctest_data()
    rst_test_data = convert_test_data_to_rst(latex_test_data)
    with open(DOCTEST_RST_DATA_PCL, "wb") as output_file:
        pickle.dump(rst_test_data, output_file, 4)
    print("done.")


if __name__ == "__main__":
    main()
