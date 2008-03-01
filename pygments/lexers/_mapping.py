# -*- coding: utf-8 -*-
"""
    pygments.lexers._mapping
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer mapping defintions. This file is generated by itself. Everytime
    you change something on a builtin lexer defintion, run this script from
    the lexers folder to update it.

    Do not alter the LEXERS dictionary by hand.

    :copyright: 2006-2007 by Armin Ronacher, Georg Brandl.
    :license: BSD, see LICENSE for more details.
"""

LEXERS = {
    'ActionScriptLexer': ('pygments.lexers.web', 'ActionScript', ('as', 'actionscript'), ('*.as',), ('application/x-actionscript', 'text/x-actionscript', 'text/actionscript')),
    'ApacheConfLexer': ('pygments.lexers.text', 'ApacheConf', ('apacheconf', 'aconf', 'apache'), ('.htaccess', 'apache.conf', 'apache2.conf'), ('text/x-apacheconf',)),
    'BBCodeLexer': ('pygments.lexers.text', 'BBCode', ('bbcode',), (), ('text/x-bbcode',)),
    'BashLexer': ('pygments.lexers.other', 'Bash', ('bash', 'sh'), ('*.sh',), ('application/x-sh', 'application/x-shellscript')),
    'BatchLexer': ('pygments.lexers.other', 'Batchfile', ('bat',), ('*.bat', '*.cmd'), ('application/x-dos-batch',)),
    'BefungeLexer': ('pygments.lexers.other', 'Befunge', ('befunge',), ('*.befunge',), ('application/x-befunge',)),
    'BooLexer': ('pygments.lexers.dotnet', 'Boo', ('boo',), ('*.boo',), ('text/x-boo',)),
    'BrainfuckLexer': ('pygments.lexers.other', 'Brainfuck', ('brainfuck', 'bf'), ('*.bf', '*.b'), ('application/x-brainfuck',)),
    'CLexer': ('pygments.lexers.compiled', 'C', ('c',), ('*.c', '*.h'), ('text/x-chdr', 'text/x-csrc')),
    'CObjdumpLexer': ('pygments.lexers.asm', 'c-objdump', ('c-objdump',), ('*.c-objdump',), ('text/x-c-objdump',)),
    'CSharpLexer': ('pygments.lexers.dotnet', 'C#', ('csharp', 'c#'), ('*.cs',), ('text/x-csharp',)),
    'CommonLispLexer': ('pygments.lexers.functional', 'Common Lisp', ('common-lisp', 'cl'), ('*.cl', '*.lisp', '*.el'), ('text/x-common-lisp',)),
    'CppLexer': ('pygments.lexers.compiled', 'C++', ('cpp', 'c++'), ('*.cpp', '*.hpp', '*.c++', '*.h++'), ('text/x-c++hdr', 'text/x-c++src')),
    'CppObjdumpLexer': ('pygments.lexers.asm', 'cpp-objdump', ('cpp-objdump', 'c++-objdumb', 'cxx-objdump'), ('*.cpp-objdump', '*.c++-objdump', '*.cxx-objdump'), ('text/x-cpp-objdump',)),
    'CssDjangoLexer': ('pygments.lexers.templates', 'CSS+Django/Jinja', ('css+django', 'css+jinja'), (), ('text/css+django', 'text/css+jinja')),
    'CssErbLexer': ('pygments.lexers.templates', 'CSS+Ruby', ('css+erb', 'css+ruby'), (), ('text/css+ruby',)),
    'CssGenshiLexer': ('pygments.lexers.templates', 'CSS+Genshi Text', ('css+genshitext', 'css+genshi'), (), ('text/css+genshi',)),
    'CssLexer': ('pygments.lexers.web', 'CSS', ('css',), ('*.css',), ('text/css',)),
    'CssPhpLexer': ('pygments.lexers.templates', 'CSS+PHP', ('css+php',), (), ('text/css+php',)),
    'CssSmartyLexer': ('pygments.lexers.templates', 'CSS+Smarty', ('css+smarty',), (), ('text/css+smarty',)),
    'DLexer': ('pygments.lexers.compiled', 'D', ('d',), ('*.d', '*.di'), ('text/x-dsrc',)),
    'DObjdumpLexer': ('pygments.lexers.asm', 'd-objdump', ('d-objdump',), ('*.d-objdump',), ('text/x-d-objdump',)),
    'DebianControlLexer': ('pygments.lexers.text', 'Debian Control file', ('control',), ('control',), ()),
    'DelphiLexer': ('pygments.lexers.compiled', 'Delphi', ('delphi', 'pas', 'pascal', 'objectpascal'), ('*.pas',), ('text/x-pascal',)),
    'DiffLexer': ('pygments.lexers.text', 'Diff', ('diff',), ('*.diff', '*.patch'), ('text/x-diff', 'text/x-patch')),
    'DjangoLexer': ('pygments.lexers.templates', 'Django/Jinja', ('django', 'jinja'), (), ('application/x-django-templating', 'application/x-jinja')),
    'DylanLexer': ('pygments.lexers.compiled', 'DylanLexer', ('dylan',), ('*.dylan',), ('text/x-dylan',)),
    'ErbLexer': ('pygments.lexers.templates', 'ERB', ('erb',), (), ('application/x-ruby-templating',)),
    'ErlangLexer': ('pygments.lexers.functional', 'Erlang', ('erlang',), ('*.erl', '*.hrl'), ('text/x-erlang',)),
    'GasLexer': ('pygments.lexers.asm', 'GAS', ('gas',), ('*.s', '*.S'), ('text/x-gas',)),
    'GenshiLexer': ('pygments.lexers.templates', 'Genshi', ('genshi', 'kid', 'xml+genshi', 'xml+kid'), ('*.kid',), ('application/x-genshi', 'application/x-kid')),
    'GenshiTextLexer': ('pygments.lexers.templates', 'Genshi Text', ('genshitext',), (), ('application/x-genshi-text', 'text/x-genshi')),
    'GettextLexer': ('pygments.lexers.text', 'Gettext Catalog', ('pot', 'po'), ('*.pot', '*.po'), ('application/x-gettext', 'text/x-gettext', 'text/gettext')),
    'GroffLexer': ('pygments.lexers.text', 'Groff', ('groff', 'nroff', 'man'), ('*.[1234567]', '*.man'), ('application/x-troff', 'text/troff')),
    'HaskellLexer': ('pygments.lexers.functional', 'Haskell', ('haskell', 'hs'), ('*.hs',), ('text/x-haskell',)),
    'HtmlDjangoLexer': ('pygments.lexers.templates', 'HTML+Django/Jinja', ('html+django', 'html+jinja'), (), ('text/html+django', 'text/html+jinja')),
    'HtmlGenshiLexer': ('pygments.lexers.templates', 'HTML+Genshi', ('html+genshi', 'html+kid'), (), ('text/html+genshi',)),
    'HtmlLexer': ('pygments.lexers.web', 'HTML', ('html',), ('*.html', '*.htm', '*.xhtml', '*.xslt'), ('text/html', 'application/xhtml+xml')),
    'HtmlPhpLexer': ('pygments.lexers.templates', 'HTML+PHP', ('html+php',), ('*.phtml',), ('application/x-php', 'application/x-httpd-php', 'application/x-httpd-php3', 'application/x-httpd-php4', 'application/x-httpd-php5')),
    'HtmlSmartyLexer': ('pygments.lexers.templates', 'HTML+Smarty', ('html+smarty',), (), ('text/html+smarty',)),
    'IniLexer': ('pygments.lexers.text', 'INI', ('ini', 'cfg'), ('*.ini', '*.cfg'), ('text/x-ini',)),
    'IrcLogsLexer': ('pygments.lexers.text', 'IRC logs', ('irc',), ('*.weechatlog',), ('text/x-irclog',)),
    'JavaLexer': ('pygments.lexers.compiled', 'Java', ('java',), ('*.java',), ('text/x-java',)),
    'JavascriptDjangoLexer': ('pygments.lexers.templates', 'JavaScript+Django/Jinja', ('js+django', 'javascript+django', 'js+jinja', 'javascript+jinja'), (), ('application/x-javascript+django', 'application/x-javascript+jinja', 'text/x-javascript+django', 'text/x-javascript+jinja', 'text/javascript+django', 'text/javascript+jinja')),
    'JavascriptErbLexer': ('pygments.lexers.templates', 'JavaScript+Ruby', ('js+erb', 'javascript+erb', 'js+ruby', 'javascript+ruby'), (), ('application/x-javascript+ruby', 'text/x-javascript+ruby', 'text/javascript+ruby')),
    'JavascriptGenshiLexer': ('pygments.lexers.templates', 'JavaScript+Genshi Text', ('js+genshitext', 'js+genshi', 'javascript+genshitext', 'javascript+genshi'), (), ('application/x-javascript+genshi', 'text/x-javascript+genshi', 'text/javascript+genshi')),
    'JavascriptLexer': ('pygments.lexers.web', 'JavaScript', ('js', 'javascript'), ('*.js',), ('application/x-javascript', 'text/x-javascript', 'text/javascript')),
    'JavascriptPhpLexer': ('pygments.lexers.templates', 'JavaScript+PHP', ('js+php', 'javascript+php'), (), ('application/x-javascript+php', 'text/x-javascript+php', 'text/javascript+php')),
    'JavascriptSmartyLexer': ('pygments.lexers.templates', 'JavaScript+Smarty', ('js+smarty', 'javascript+smarty'), (), ('application/x-javascript+smarty', 'text/x-javascript+smarty', 'text/javascript+smarty')),
    'JspLexer': ('pygments.lexers.templates', 'Java Server Page', ('jsp',), ('*.jsp',), ('application/x-jsp',)),
    'LiterateHaskellLexer': ('pygments.lexers.functional', 'Literate Haskell', ('lhs', 'literate-haskell'), ('*.lhs',), ('text/x-literate-haskell',)),
    'LlvmLexer': ('pygments.lexers.asm', 'LLVM', ('llvm',), ('*.ll',), ('text/x-llvm',)),
    'LuaLexer': ('pygments.lexers.agile', 'Lua', ('lua',), ('*.lua',), ('text/x-lua', 'application/x-lua')),
    'MOOCodeLexer': ('pygments.lexers.other', 'MOOCode', ('moocode',), ('*.moo',), ('text/x-moocode',)),
    'MakefileLexer': ('pygments.lexers.text', 'Makefile', ('make', 'makefile', 'mf'), ('*.mak', 'Makefile', 'makefile'), ('text/x-makefile',)),
    'MakoCssLexer': ('pygments.lexers.templates', 'CSS+Mako', ('css+mako',), (), ('text/css+mako',)),
    'MakoHtmlLexer': ('pygments.lexers.templates', 'HTML+Mako', ('html+mako',), (), ('text/html+mako',)),
    'MakoJavascriptLexer': ('pygments.lexers.templates', 'JavaScript+Mako', ('js+mako', 'javascript+mako'), (), ('application/x-javascript+mako', 'text/x-javascript+mako', 'text/javascript+mako')),
    'MakoLexer': ('pygments.lexers.templates', 'Mako', ('mako',), ('*.mao',), ('application/x-mako',)),
    'MakoXmlLexer': ('pygments.lexers.templates', 'XML+Mako', ('xml+mako',), (), ('application/xml+mako',)),
    'MiniDLexer': ('pygments.lexers.agile', 'MiniD', ('minid',), ('*.md',), ('text/x-minidsrc',)),
    'MoinWikiLexer': ('pygments.lexers.text', 'MoinMoin/Trac Wiki markup', ('trac-wiki', 'moin'), (), ('text/x-trac-wiki',)),
    'MuPADLexer': ('pygments.lexers.math', 'MuPAD', ('mupad',), ('*.mu',), ()),
    'MySqlLexer': ('pygments.lexers.other', 'MySQL', ('mysql',), (), ('text/x-mysql',)),
    'MyghtyCssLexer': ('pygments.lexers.templates', 'CSS+Myghty', ('css+myghty',), (), ('text/css+myghty',)),
    'MyghtyHtmlLexer': ('pygments.lexers.templates', 'HTML+Myghty', ('html+myghty',), (), ('text/html+myghty',)),
    'MyghtyJavascriptLexer': ('pygments.lexers.templates', 'JavaScript+Myghty', ('js+myghty', 'javascript+myghty'), (), ('application/x-javascript+myghty', 'text/x-javascript+myghty', 'text/javascript+mygthy')),
    'MyghtyLexer': ('pygments.lexers.templates', 'Myghty', ('myghty',), ('*.myt', 'autodelegate'), ('application/x-myghty',)),
    'MyghtyXmlLexer': ('pygments.lexers.templates', 'XML+Myghty', ('xml+myghty',), (), ('application/xml+myghty',)),
    'ObjdumpLexer': ('pygments.lexers.asm', 'objdump', ('objdump',), ('*.objdump',), ('text/x-objdump',)),
    'ObjectiveCLexer': ('pygments.lexers.compiled', 'Objective-C', ('objective-c', 'objectivec', 'obj-c', 'objc'), ('*.m',), ('text/x-objective-c',)),
    'OcamlLexer': ('pygments.lexers.compiled', 'OCaml', ('ocaml',), ('*.ml', '*.mli', '*.mll', '*.mly'), ('text/x-ocaml',)),
    'OcamlLexer': ('pygments.lexers.functional', 'OCaml', ('ocaml',), ('*.ml', '*.mli', '*.mll', '*.mly'), ('text/x-ocaml',)),
    'PerlLexer': ('pygments.lexers.agile', 'Perl', ('perl', 'pl'), ('*.pl', '*.pm'), ('text/x-perl', 'application/x-perl')),
    'PhpLexer': ('pygments.lexers.web', 'PHP', ('php', 'php3', 'php4', 'php5'), ('*.php', '*.php[345]'), ('text/x-php',)),
    'PythonConsoleLexer': ('pygments.lexers.agile', 'Python console session', ('pycon',), (), ('text/x-python-doctest',)),
    'PythonLexer': ('pygments.lexers.agile', 'Python', ('python', 'py'), ('*.py', '*.pyw', '*.sc', 'SConstruct', 'SConscript'), ('text/x-python', 'application/x-python')),
    'PythonTracebackLexer': ('pygments.lexers.agile', 'Python Traceback', ('pytb',), ('*.pytb',), ('text/x-python-traceback',)),
    'RawTokenLexer': ('pygments.lexers.special', 'Raw token data', ('raw',), ('*.raw',), ('application/x-pygments-tokens',)),
    'RedcodeLexer': ('pygments.lexers.other', 'Redcode', ('redcode',), ('*.cw',), ()),
    'RhtmlLexer': ('pygments.lexers.templates', 'RHTML', ('rhtml', 'html+erb', 'html+ruby'), ('*.rhtml',), ('text/html+ruby',)),
    'RstLexer': ('pygments.lexers.text', 'reStructuredText', ('rst', 'rest', 'restructuredtext'), ('*.rst', '*.rest'), ('text/x-rst',)),
    'RubyConsoleLexer': ('pygments.lexers.agile', 'Ruby irb session', ('rbcon', 'irb'), (), ('text/x-ruby-shellsession',)),
    'RubyLexer': ('pygments.lexers.agile', 'Ruby', ('rb', 'ruby'), ('*.rb', '*.rbw', 'Rakefile', '*.rake', '*.gemspec', '*.rbx'), ('text/x-ruby', 'application/x-ruby')),
    'SchemeLexer': ('pygments.lexers.functional', 'Scheme', ('scheme', 'scm'), ('*.scm',), ('text/x-scheme', 'application/x-scheme')),
    'SmartyLexer': ('pygments.lexers.templates', 'Smarty', ('smarty',), ('*.tpl',), ('application/x-smarty',)),
    'SourcesListLexer': ('pygments.lexers.text', 'Debian Sourcelist', ('sourceslist', 'sources.list'), ('sources.list',), ()),
    'SqlLexer': ('pygments.lexers.other', 'SQL', ('sql',), ('*.sql',), ('text/x-sql',)),
    'SquidConfLexer': ('pygments.lexers.text', 'SquidConf', ('squidconf', 'squid.conf', 'squid'), ('squid.conf',), ('text/x-squidconf',)),
    'TclLexer': ('pygments.lexers.agile', 'Tcl', ('tcl',), ('*.tcl',), ('text/x-tcl', 'text/x-script.tcl', 'application/x-tcl')),
    'TexLexer': ('pygments.lexers.text', 'TeX', ('tex', 'latex'), ('*.tex', '*.aux', '*.toc'), ('text/x-tex', 'text/x-latex')),
    'TextLexer': ('pygments.lexers.special', 'Text only', ('text',), ('*.txt',), ('text/plain',)),
    'VbNetLexer': ('pygments.lexers.dotnet', 'VB.net', ('vb.net', 'vbnet'), ('*.vb', '*.bas'), ('text/x-vbnet', 'text/x-vba')),
    'VimLexer': ('pygments.lexers.text', 'VimL', ('vim',), ('*.vim', '.vimrc'), ('text/x-vim',)),
    'XmlDjangoLexer': ('pygments.lexers.templates', 'XML+Django/Jinja', ('xml+django', 'xml+jinja'), (), ('application/xml+django', 'application/xml+jinja')),
    'XmlErbLexer': ('pygments.lexers.templates', 'XML+Ruby', ('xml+erb', 'xml+ruby'), (), ('application/xml+ruby',)),
    'XmlLexer': ('pygments.lexers.web', 'XML', ('xml',), ('*.xml', '*.xsl', '*.rss', '*.xslt'), ('text/xml', 'application/xml', 'image/svg+xml', 'application/rss+xml', 'application/atom+xml', 'application/xsl+xml', 'application/xslt+xml')),
    'XmlPhpLexer': ('pygments.lexers.templates', 'XML+PHP', ('xml+php',), (), ('application/xml+php',)),
    'XmlSmartyLexer': ('pygments.lexers.templates', 'XML+Smarty', ('xml+smarty',), (), ('application/xml+smarty',))
}

if __name__ == '__main__':
    import sys
    import os

    # lookup lexers
    found_lexers = []
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    for filename in os.listdir('.'):
        if filename.endswith('.py') and not filename.startswith('_'):
            module_name = 'pygments.lexers.%s' % filename[:-3]
            print module_name
            module = __import__(module_name, None, None, [''])
            for lexer_name in module.__all__:
                lexer = getattr(module, lexer_name)
                found_lexers.append(
                    '%r: %r' % (lexer_name,
                                (module_name,
                                 lexer.name,
                                 tuple(lexer.aliases),
                                 tuple(lexer.filenames),
                                 tuple(lexer.mimetypes))))
    # sort them, that should make the diff files for svn smaller
    found_lexers.sort()

    # extract useful sourcecode from this file
    f = file(__file__)
    try:
        content = f.read()
    finally:
        f.close()
    header = content[:content.find('LEXERS = {')]
    footer = content[content.find("if __name__ == '__main__':"):]

    # write new file
    f = file(__file__, 'w')
    f.write(header)
    f.write('LEXERS = {\n    %s\n}\n\n' % ',\n    '.join(found_lexers))
    f.write(footer)
    f.close()
