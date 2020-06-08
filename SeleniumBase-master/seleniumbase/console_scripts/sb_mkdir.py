"""
Creates a new folder for running SeleniumBase scripts.

Usage:
seleniumbase mkdir [DIRECTORY_NAME]
Output:
Creates a new folder for running SeleniumBase scripts.
The new folder contains default config files,
sample tests for helping new users get started, and
Python boilerplates for setting up customized
test frameworks.
"""

import codecs
import os
import sys


def invalid_run_command():
    exp = ("  ** mkdir **\n\n")
    exp += "  Usage:\n"
    exp += "          seleniumbase mkdir [DIRECTORY_NAME]\n"
    exp += "  Example:\n"
    exp += "          seleniumbase mkdir browser_tests\n"
    exp += "  Output:\n"
    exp += "          Creates a new folder for running SeleniumBase scripts.\n"
    exp += "          The new folder contains default config files,\n"
    exp += "          sample tests for helping new users get started, and\n"
    exp += "          Python boilerplates for setting up customized\n"
    exp += "          test frameworks.\n"
    print("")
    raise Exception('INVALID RUN COMMAND!\n\n%s' % exp)


def main():
    num_args = len(sys.argv)
    if sys.argv[0].split('/')[-1].lower() == "seleniumbase" or (
            sys.argv[0].split('\\')[-1].lower() == "seleniumbase") or (
            sys.argv[0].split('/')[-1].lower() == "sbase") or (
            sys.argv[0].split('\\')[-1].lower() == "sbase"):
        if num_args < 3 or num_args > 3:
            invalid_run_command()
    else:
        invalid_run_command()
    dir_name = sys.argv[num_args - 1]
    if len(str(dir_name)) < 2:
        raise Exception('Directory name length must be at least 2 '
                        'characters long!')
    if os.path.exists(os.getcwd() + '/' + dir_name):
        raise Exception('Directory "%s" already exists '
                        'in the current path!\n' % dir_name)
    else:
        os.mkdir(dir_name)

        data = []
        data.append("[pytest]")
        data.append("addopts = --capture=no --ignore conftest.py "
                    "-p no:cacheprovider")
        data.append("filterwarnings =")
        data.append("    ignore::pytest.PytestWarning")
        data.append("    ignore:.*U.*mode is deprecated:DeprecationWarning")
        data.append("junit_family = legacy")
        data.append("python_files = test_*.py *_test.py *_tests.py *_suite.py")
        data.append("python_classes = Test* *Test* *Test *Tests *Suite")
        data.append("python_functions = test_*")
        data.append("markers =")
        data.append("    marker1: custom marker")
        data.append("    marker2: custom marker")
        data.append("    marker3: custom marker")
        data.append("    marker_test_suite: custom marker")
        data.append("    expected_failure: custom marker")
        data.append("    local: custom marker")
        data.append("    remote: custom marker")
        data.append("    offline: custom marker")
        data.append("    develop: custom marker")
        data.append("    qa: custom marker")
        data.append("    ready: custom marker")
        data.append("    master: custom marker")
        data.append("    release: custom marker")
        data.append("    staging: custom marker")
        data.append("    production: custom marker")
        data.append("")
        file_path = "%s/%s" % (dir_name, "pytest.ini")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        data = []
        data.append("[nosetests]")
        data.append("nocapture=1")
        data.append("logging-level=INFO")
        data.append("")
        data.append("[bdist_wheel]")
        data.append("universal=1")
        file_path = "%s/%s" % (dir_name, "setup.cfg")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        data = []
        data.append("from seleniumbase import BaseCase")
        data.append("")
        data.append("")
        data.append("class MyTestClass(BaseCase):")
        data.append("")
        data.append("    def test_basic(self):")
        data.append('        self.open("https://xkcd.com/353/")')
        data.append('        self.assert_title("xkcd: Python")')
        data.append("        self.assert_element('img[alt=\"Python\"]')")
        data.append("        self.click('a[rel=\"license\"]')")
        data.append('        self.assert_text("free to copy and reuse")')
        data.append('        self.go_back()')
        data.append('        self.click("link=About")')
        data.append('        self.assert_text("xkcd.com", "h2")')
        data.append('        self.open('
                    '"://store.xkcd.com/collections/everything")')
        data.append(
            '        self.update_text("input.search-input", "xkcd book\\n")')
        data.append('        self.assert_text("xkcd: volume 0", "h3")')
        data.append("")
        file_path = "%s/%s" % (dir_name, "my_first_test.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        data = []
        data.append("from seleniumbase import BaseCase")
        data.append("")
        data.append("")
        data.append("class MyTestClass(BaseCase):")
        data.append("")
        data.append("    def test_demo_site(self):")
        data.append('        self.open('
                    '"https://seleniumbase.io/demo_page.html")')
        data.append('        self.assert_title("Web Testing Page")')
        data.append('        self.assert_element("tbody#tbodyId")')
        data.append('        self.assert_text("Demo Page", "h1")')
        data.append('        self.update_text("#myTextInput", '
                    '"This is Automated")')
        data.append('        self.update_text("textarea.area1", '
                    '"Testing Time!\\n")')
        data.append("        self.update_text('[name=\"preText2\"]', "
                    "\"Typing Text!\")")
        data.append('        self.assert_text("Automation Practice", "h3")')
        data.append('        self.hover_and_click("#myDropdown", '
                    '"#dropOption2")')
        data.append('        self.assert_text("Link Two Selected", "h3")')
        data.append('        self.assert_text("This Text is Green", "#pText")')
        data.append('        self.click("#myButton")')
        data.append('        self.assert_text("This Text is Purple", '
                    '"#pText")')
        data.append("        self.assert_element('svg[name=\"svgName\"]')")
        data.append("        self.assert_element('progress[value=\"50\"]')")
        data.append('        self.press_right_arrow("#myslider", times=5)')
        data.append("        self.assert_element('progress[value=\"100\"]')")
        data.append("        self.assert_element('meter[value=\"0.25\"]')")
        data.append('        self.select_option_by_text("#mySelect", '
                    '"Set to 75%")')
        data.append("        self.assert_element('meter[value=\"0.75\"]')")
        data.append('        self.assert_false(self.is_element_visible('
                    '"img"))')
        data.append('        self.switch_to_frame("#myFrame1")')
        data.append('        self.assert_true(self.is_element_visible("img"))')
        data.append('        self.switch_to_default_content()')
        data.append('        self.assert_false(self.is_text_visible('
                    '"iFrame Text"))')
        data.append('        self.switch_to_frame("#myFrame2")')
        data.append('        self.assert_true(self.is_text_visible('
                    '"iFrame Text"))')
        data.append('        self.switch_to_default_content()')
        data.append('        self.assert_false(self.is_selected('
                    '"#radioButton2"))')
        data.append('        self.click("#radioButton2")')
        data.append('        self.assert_true(self.is_selected('
                    '"#radioButton2"))')
        data.append('        self.assert_false(self.is_selected('
                    '"#checkBox1"))')
        data.append('        self.click("#checkBox1")')
        data.append('        self.assert_true(self.is_selected("#checkBox1"))')
        data.append('        self.assert_false(self.is_selected('
                    '"#checkBox2"))')
        data.append('        self.assert_false(self.is_selected('
                    '"#checkBox3"))')
        data.append('        self.assert_false(self.is_selected('
                    '"#checkBox4"))')
        data.append('        self.click_visible_elements('
                    '"input.checkBoxClassB")')
        data.append('        self.assert_true(self.is_selected("#checkBox2"))')
        data.append('        self.assert_true(self.is_selected("#checkBox3"))')
        data.append('        self.assert_true(self.is_selected("#checkBox4"))')
        data.append('        self.assert_false(self.is_element_visible('
                    '".fBox"))')
        data.append('        self.switch_to_frame("#myFrame3")')
        data.append('        self.assert_true(self.is_element_visible('
                    '".fBox"))')
        data.append('        self.assert_false(self.is_selected(".fBox"))')
        data.append('        self.click(".fBox")')
        data.append('        self.assert_true(self.is_selected(".fBox"))')
        data.append('        self.switch_to_default_content()')
        data.append('        self.assert_link_text("seleniumbase.com")')
        data.append('        self.assert_link_text("SeleniumBase on GitHub")')
        data.append('        self.assert_link_text("seleniumbase.io")')
        data.append('        self.click_link_text("SeleniumBase Demo Page")')
        data.append('        self.assert_exact_text("Demo Page", "h1")')
        data.append("")
        file_path = "%s/%s" % (dir_name, "test_demo_site.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        data = []
        data.append("from seleniumbase import BaseCase")
        data.append("from parameterized import parameterized")
        data.append("")
        data.append("")
        data.append("class GoogleTestClass(BaseCase):")
        data.append("")
        data.append("    @parameterized.expand([")
        data.append('        ["pypi", "pypi.org"],')
        data.append('        ["wikipedia", "wikipedia.org"],')
        data.append('        ["seleniumbase", "seleniumbase/SeleniumBase"],')
        data.append("    ])")
        data.append("    def test_parameterized_google_search("
                    "self, search_term, expected_text):")
        data.append("        self.open('https://google.com/ncr')")
        data.append("        self.update_text('input[title=\"Search\"]', "
                    "search_term + '\\n')")
        data.append("        self.assert_element('#result-stats')")
        data.append("        self.assert_text(expected_text, '#search')")
        data.append("")
        file_path = "%s/%s" % (dir_name, "parameterized_test.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        dir_name_2 = dir_name + "/" + "boilerplates"
        os.mkdir(dir_name_2)

        data = []
        data.append("")
        file_path = "%s/%s" % (dir_name_2, "__init__.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        data = []
        data.append("from seleniumbase import BaseCase")
        data.append("")
        data.append("")
        data.append("class BaseTestCase(BaseCase):")
        data.append("")
        data.append("    def setUp(self):")
        data.append("        super(BaseTestCase, self).setUp()")
        data.append("        # << Add custom code AFTER the super() line >>")
        data.append("")
        data.append("    def tearDown(self):")
        data.append("        self.save_teardown_screenshot()")
        data.append("        # << Add custom code BEFORE the super() line >>")
        data.append("        super(BaseTestCase, self).tearDown()")
        data.append("")
        data.append("    def login(self):")
        data.append("        # <<< Placeholder. Add your code here. >>>")
        data.append("        pass")
        data.append("")
        data.append("    def example_method(self):")
        data.append("        # <<< Placeholder. Add your code here. >>>")
        data.append("        pass")
        data.append("")
        file_path = "%s/%s" % (dir_name_2, "base_test_case.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        data = []
        data.append("class Page(object):")
        data.append('    html = "html"')
        data.append("")
        file_path = "%s/%s" % (dir_name_2, "page_objects.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        data = []
        data.append("from .base_test_case import BaseTestCase")
        data.append("from .page_objects import Page")
        data.append("")
        data.append("")
        data.append("class MyTestClass(BaseTestCase):")
        data.append("")
        data.append("    def test_boilerplate(self):")
        data.append("        self.login()")
        data.append("        self.example_method()")
        data.append("        self.assert_element(Page.html)")
        data.append("")
        file_path = "%s/%s" % (dir_name_2, "boilerplate_test.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        dir_name_3 = dir_name_2 + "/" + "samples"
        os.mkdir(dir_name_3)

        data = []
        data.append("")
        file_path = "%s/%s" % (dir_name_3, "__init__.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        data = []
        data.append("from seleniumbase import BaseCase")
        data.append("from .google_objects import HomePage, ResultsPage")
        data.append("")
        data.append("")
        data.append("class GoogleTests(BaseCase):")
        data.append("")
        data.append("    def test_google_dot_com(self):")
        data.append("        self.open('https://google.com/ncr')")
        data.append(
            "        self.update_text(HomePage.search_box, 'github')")
        data.append("        self.assert_element(HomePage.list_box)")
        data.append("        self.assert_element(HomePage.search_button)")
        data.append(
            "        self.assert_element(HomePage.feeling_lucky_button)")
        data.append("        self.click(HomePage.search_button)")
        data.append(
            "        self.assert_text('github.com', "
            "ResultsPage.search_results)")
        data.append("        self.assert_element(ResultsPage.images_link)")
        data.append("")
        file_path = "%s/%s" % (dir_name_3, "google_test.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()

        data = []
        data.append("class HomePage(object):")
        data.append("    dialog_box = '[role=\"dialog\"] div'")
        data.append("    search_box = 'input[title=\"Search\"]'")
        data.append("    list_box = '[role=\"listbox\"]'")
        data.append("    search_button = 'input[value=\"Google Search\"]'")
        data.append(
            "    feeling_lucky_button = "
            "'''input[value=\"I'm Feeling Lucky\"]'''")
        data.append("")
        data.append("")
        data.append("class ResultsPage(object):")
        data.append("    google_logo = 'img[alt=\"Google\"]'")
        data.append("    images_link = 'link=Images'")
        data.append("    search_results = 'div#center_col'")
        data.append("")
        file_path = "%s/%s" % (dir_name_3, "google_objects.py")
        file = codecs.open(file_path, "w+", "utf-8")
        file.writelines("\r\n".join(data))
        file.close()
        print('''\n* Directory "%s" was created with config files '''
              '''and sample tests! *\n''' % dir_name)


if __name__ == "__main__":
    main()
