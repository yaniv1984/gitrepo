<h3 align="left"><a href="https://github.com/seleniumbase/SeleniumBase/"><img src="https://cdn2.hubspot.net/hubfs/100006/images/super_logo_m.png" title="SeleniumBase" width="290" /></a></h3>

<a id="language_tests"></a>
<h3><img src="https://seleniumbase.io/img/sb_icon.png" title="SeleniumBase" width="30" /> Language Tests (Python 3+)</h3>

<b>SeleniumBase</b> supports the following 10 languages:
<ul>
<li>English</li>
<li><a href="https://seleniumbase.io/help_docs/chinese/">Chinese / 中文</a></li>
<li>Dutch / Nederlands</li>
<li>French / Français</li>
<li>Italian / Italiano</li>
<li>Japanese / 日本語</li>
<li>Korean / 한국어</li>
<li>Portuguese / Português</li>
<li>Russian / Русский</li>
<li>Spanish / Español</li>
</ul>

Examples can be found in [<a href="https://github.com/seleniumbase/SeleniumBase/tree/master/examples/translations">SeleniumBase/examples/translations</a>].

Multi-language tests are run with **pytest** like any other test. Every test method has a one-to-one mapping to every other supported language.<br /><i>Examples:</i>
```
self.开启网址(URL) = self.open(URL)
self.нажмите(CSS) = self.click(CSS)
self.뒤로() = self.go_back()
```

<a id="translation_api"></a>
<h2><img src="https://seleniumbase.io/img/sb_icon.png" title="SeleniumBase" width="30" /> Translation API</h2>

You can use SeleniumBase to selectively translate the method names of any test from one language to another via the console scripts interface. Additionally, the ``import`` line at the top of the Python file will change to import the new ``BaseCase``. Example: ``BaseCase`` becomes ``CasoDeTeste`` when a test is translated into Portuguese.

```bash
seleniumbase translate
```

```
* Usage:
seleniumbase translate [SB_FILE].py [LANGUAGE] [ACTION]

* Languages:
``--en`` / ``--English``  |  ``--zh`` / ``--Chinese``
``--nl`` / ``--Dutch``    |  ``--fr`` / ``--French``
``--it`` / ``--Italian``  |  ``--ja`` / ``--Japanese``
``--ko`` / ``--Korean``   |  ``--pt`` / ``--Portuguese``
``--ru`` / ``--Russian``  |  ``--es`` / ``--Spanish``

* Actions:
``-p`` / ``--print``  (Print translation output to the screen)
``-o`` / ``--overwrite``  (Overwrite the file being translated)
``-c`` / ``--copy``  (Copy the translation to a new ``.py`` file)

* Options:
``-n``  (include line Numbers when using the Print action)

* Examples:
Translate test_1.py into Chinese and only print the output:
>>> seleniumbase translate test_1.py --zh  -p
Translate test_2.py into Portuguese and overwrite the file:
>>> seleniumbase translate test_2.py --pt  -o
Translate test_3.py into Dutch and make a copy of the file:
>>> seleniumbase translate test_3.py --nl  -c

* Output:
Translates a SeleniumBase Python file into the language
specified. Method calls and ``import`` lines get swapped.
Both a language and an action must be specified.
The ``-p`` action can be paired with one other action.
When running with ``-c`` (or ``--copy``) the new file name
will be the orginal name appended with an underscore
plus the 2-letter language code of the new language.
(Example: Translating ``test_1.py`` into Japanese with
``-c`` will create a new file called ``test_1_ja.py``.)
```
