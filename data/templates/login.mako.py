from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1285257710.9205849
_template_filename='/home/andy/dobtrack/dobtrack/templates/login.mako'
_template_uri='login.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 7
        __M_writer(escape(c.pagetitle))
        __M_writer(u'</h1>\n\n<form name="login" action="submitlogin">\n    <label for="username">\n        User:\n        <input type="text" name="username" />\n    </label>\n\n    <label for="password">\n        Password:\n        <input type="password" name="password" />\n    </label>\n\n    <input type="submit" value="OK" />\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <link rel="stylesheet" type="text/css" href="/base.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


