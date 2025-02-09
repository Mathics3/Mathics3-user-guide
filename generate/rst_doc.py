
import re
import os.path as osp
from typing import Callable, Optional, Sequence

from mathics.doc.doc_entries import (
    CONSOLE_RE,
    DL_ITEM_RE,
    DL_RE,
    HYPERTEXT_RE,
    IMG_RE,
    LATEX_DISPLAY_EQUATION_RE,
    LATEX_HREF_RE,
    LATEX_INLINE_EQUATION_RE,
    LATEX_RE,
    LATEX_URL_RE,
    LIST_ITEM_RE,
    LIST_RE,
    MATHICS_RE,
    PYTHON_RE,
    QUOTATIONS_RE,
    REF_RE,
    SPECIAL_COMMANDS,
    DocTest,
    DocTests,
    DocText,
    DocumentationEntry,
    get_results_by_test,
    post_sub,
    pre_sub,
)
from mathics.doc.structure import (
    DocChapter,
    DocGuideSection,
    DocPart,
    DocSection,
    DocSubsection,
    Documentation,
    MathicsMainDocumentation,
    SUBSECTION_RE,
    SUBSECTION_END_RE,
)
from mathics.settings import DOC_DIR


ITALIC_RE = re.compile(r"(?s)<(?P<tag>i)>(?P<content>.*?)</(?P=tag)>")


class RstDocTests(DocTests):

    def __init__(self, index, testcase, key_prefix=None):
        super().__init__(index, testcase, key_prefix)

    def rst(self, test_data=None) -> str:
        return "\n" + "\n".join(test.rst(test_data) for test in self.get_tests()) + "\n"


class RsTDocumentationEntry(DocumentationEntry):
    """A class to hold our custom XML-like format.
    The `rst()` method can turn this into RsT.

    Mathics core also uses this in getting usage strings (`??`).
    """

    items: Sequence["RsTDocumentationEntry"]

    def __init__(self, doc_str: str, title: str, section: Optional[DocSection]):
        super().__init__(doc_str, title, section)

    def rst(self, test_data=None) -> str:
        return "\n".join([item.rst(test_data) for item in self.items])

    def _set_classes(self):
        """
        Tells to the initializator of DocumentationEntry
        the classes to be used to build the items.
        """
        self.docTest_collection_class = RsTDocTests
        self.docTest_class = RsTDocTest
        self.docText_class = RsTDocText


class RsTMathicsMainDocumentation(MathicsMainDocumentation):
    """
    Subclass of MathicsMainDocumentation which is able to
    produce a the documentation in RsT format.
    """

    parts: Sequence["RsTDocPart"]

    def __init__(self):
        super().__init__()
        self.load_documentation_sources()

    def _set_classes(self):
        """
        This function tells to the initializator of
        MathicsMainDocumentation which classes must be used to
        create the different elements in the hierarchy.
        """
        self.chapter_class = RsTDocChapter
        self.doc_class = RsTDocumentationEntry
        self.guide_section_class = RsTDocGuideSection
        self.part_class = RsTDocPart
        self.section_class = RsTDocSection
        self.subsection_class = RsTDocSubsection


class RsTDocChapter(DocChapter):
    doc: RsTDocumentationEntry
    guide_sections: Sequence["RsTDocGuideSection"]

    def rst(self, data):
        pass


class RsTDocPart(DocPart):
    def __init__(self, doc: "Documentation", title: str, is_reference: bool = False):
        self.chapter_class = RsTDocChapter
        super().__init__(doc, title, is_reference)


class RsTDocSection(DocSection):
    subsections: Sequence["RsTDocSubsection"]

    def __init__(
        self,
        chapter,
        title: str,
        text: str,
        operator,
        installed=True,
        in_guide=False,
        summary_text="",
    ):
        super().__init__(
            chapter, title, text, operator, installed, in_guide, summary_text
        )


class RsTDocGuideSection(DocGuideSection):
    """An object for a Documented Guide Section.
    A Guide Section is part of a Chapter. "Colors" or "Special Functions"
    are examples of Guide Sections, and each contains a number of Sections.
    like NamedColors or Orthogonal Polynomials.
    """

    subsections: Sequence["RsTDocSubsection"]

    def __init__(
        self,
        chapter: RsTDocChapter,
        title: str,
        text: str,
        submodule,
        installed: bool = True,
    ):
        super().__init__(chapter, title, text, submodule, installed)

    def get_tests(self):
        # FIXME: The below is a little weird for Guide Sections.
        # Figure out how to make this clearer.
        # A guide section's subsection are Sections without the Guide.
        # it is *their* subsections where we generally find tests.
        for section in self.subsections:
            if not section.installed:
                continue
            for subsection in section.subsections:
                # FIXME we are omitting the section title here...
                if not subsection.installed:
                    continue
                for doctests in subsection.items:
                    yield doctests.get_tests()

    def rst(self, data):
        pass


class RsTDocSubsection(DocSubsection):
    """An object for a Documented Subsection.
    A Subsection is part of a Section.
    """

    subsections: Sequence["RsTDocSubsection"]

    def __init__(
        self,
        chapter,
        section,
        title,
        text,
        operator=None,
        installed=True,
        in_guide=False,
        summary_text="",
    ):
        super().__init__(
            chapter, section, title, text, operator, installed, in_guide, summary_text
        )


class RsTDocTest(DocTest):
    def rst(self, test_data=None) -> str:
        """
        Return a RsT representation of the test
        """
        formatted_test = ">>> " + self.test + "\n"
        test_result = self.result
        output_for_key = test_data.get(self.key, None) if self.key else None
#        output_for_key = None
        if output_for_key:                             
            result_content_list = output_for_key["results"]
            
            if len(result_content_list)==0:
                return formatted_test
            
            assert len(result_content_list)==1
            for out_msg in result_content_list[0]["out"]:
                if isinstance(out_msg, dict):
                    if "prefix" in out_msg:
                        formatted_test += f"\n    %s %s" % (out_msg["prefix"], out_msg["text"])+"\n"
                    else:
                        formatted_test += f"\n    %s" % (out_msg["text"])+"\n"
                    continue
                formatted_test += "    " + "\n    ".join(out_msg)+"\n"

            result_content = result_content_list[0]["result"]
            if result_content is None:
                return formatted_test + "\n"
            test_result = '\n    =\n' + result_content + "\n"
        else:
            # We are using OutputForm results. Process as text.
            lines = test_result.split("\n")
            if len(lines)>1:
                test_result = '    = ' + "\n    ".join(lines) + "\n"
            else:
                test_result = '    = ' + test_result + "`\n"
        if test_result == "":
            return result

        formatted_test += test_result

        return formatted_test


class RsTDocTests(DocTests):

    def rst(self, test_data=None) -> str:
        return "\n" + "\n".join(test.rst(test_data) for test in self.get_tests()) + "\n"


class RsTDocText(DocText):
    """
    Class to hold some (non-test) RsT text.
    """

    def rst(self, test_data=None) -> str:
        """ReStructuredText version of the documentation entry text"""
        text = str(self.text)
        text = "\n".join(line.strip() for line in text.split("\n"))

        text = text.replace(r"\'", "_SIMPLEQUOTE_")
        text = text.replace(r"\$", "_DOLARSYMBOL_")


        def repl_subsection(match):
            title=match.group(1)
            title = "\n" + title + "\n" + len(title)*"-"+"\n"
            return title

        text = SUBSECTION_RE.sub(repl_subsection, text)
        text = SUBSECTION_END_RE.sub("", text)
        
        # We start by replacing Python code
        def repl_python(match):
            return "``python\n%s\n``\n" % match.group(1).strip()

        text, post_substitutions = pre_sub(PYTHON_RE, text, repl_python)

        # Process included images
        def repl_img(match):
            # TODO: consider to implement this using
            # substitutions
            src = match.group("src")
            result = """.. image:: %s\n""" % (osp.join(DOC_DIR,"..","latex","images", src.strip()),)
            return result

        text, post_substitutions = pre_sub(
            IMG_RE, text, repl_img, tuple(post_substitutions)
        )

        # Process LaTeX equations.
        def repl_display_eq(match) -> str:
            eq = match.group(1)
            return f"\n.. :math:`{eq}`\n"

        def repl_inline_eq(match) -> str:
            eq = match.group(1)
            return f":math:`{eq}`"

        text, post_substitutions = pre_sub(
            LATEX_DISPLAY_EQUATION_RE, text, repl_display_eq, tuple(post_substitutions)
        )
        text, post_substitutions = pre_sub(
            LATEX_INLINE_EQUATION_RE, text, repl_inline_eq, tuple(post_substitutions)
        )

        # Process quotations. In Mathics, `"..."` represents strings
        def repl_quotation(match):
            return r'"%s"' % match.group(1)

        text, post_substitutions = pre_sub(
            QUOTATIONS_RE, text, repl_quotation, tuple(post_substitutions)
        )

        def repl_hypertext(match) -> str:
            tag = match.group("tag")
            content = match.group("content")
            content = content.replace("\n", "")
            if tag == "em":
                return f"`<{content}>`_"

            text = match.group("text")
            if text is None:
                return f"`{content} <{content}>`_"
            return f"`{text} <{content}>`_"

        text = HYPERTEXT_RE.sub(repl_hypertext, text)

        def mathics_repl(match):
            code = match.group(1)
            lines = code.split("\n")
            if len(lines)>1:
                code = 4*" "+"\n    ".join(lines)
                return ".. code-block:\n"+code
            return f":code:`{code}` "

        text = MATHICS_RE.sub(mathics_repl, text)

        def repl_dl(match):
            dl_text = match.group(1)
            last_tag = "dl"

            def repl_dd_dt(match):
                nonlocal last_tag
                match_dict = match.groupdict()
                if last_tag == "dt" == match_dict["tag"]:
                    return 4 * " " + "same as\n\n" + match_dict["content"].strip() + "\n"
                last_tag = match_dict["tag"]
                if last_tag == "dt":
                    return match_dict["content"].strip() + "\n"

                dd_content = match_dict["content"].strip()
                lines = dd_content.split("\n")
                if len(lines)>1:
                    dd_content = f'\n{4*" "}'.join(line.strip() for line in lines)
                return 4 * " " + dd_content + "\n\n"

            dl_text = DL_ITEM_RE.sub(repl_dd_dt, dl_text)
            return dl_text + "\n\n"

        text = DL_RE.sub(repl_dl, text)

        def repl_list(match):
            idx = 0
            tag = match.group("tag")
            content = match.group("content")
            env = "itemize" if tag == "ul" else "enumerate"

            def repl_list_item(m):
                nonlocal tag
                nonlocal idx
                if tag == "ul":
                    return "- %s\n" % m.group(1)
                idx += 1
                return "%d. %s\n" % (idx, m.group(1))

            content = LIST_ITEM_RE.sub(repl_list_item, content)
            return "\n%s\n" % (content,)

        text = LIST_RE.sub(repl_list, text)

        def repl_ref(match):
            return r"_{%s}" % match.group("label")

        text = REF_RE.sub(repl_ref, text)

        def repl_console(match):
            content = match.group("content")
            content = content.strip()
            content = content.replace(r"\$", "$")
            lines = content.split("\n")
            if len(lines)>1:
                content = f"\n{4*' '}"+f"\n{4*' '}".join(lines)
                return ".. code-block: console%s\n\n" % content
            return " :code:`%s` " % content

        text = CONSOLE_RE.sub(repl_console, text)

        def repl_italic(match):
            content = match.group("content")
            return "*%s*" % content

        text = ITALIC_RE.sub(repl_italic, text)

        
        text = post_sub(text, post_substitutions)
        text = text.replace("_SIMPLEQUOTE_", "'")
        text = text.replace("_DOLARSYMBOL_", "$")
        return text
