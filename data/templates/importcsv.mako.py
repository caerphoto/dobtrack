from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1283120990.1571929
_template_filename='/home/andy/dobtrack/dobtrack/templates/importcsv.mako'
_template_uri='/importcsv.mako'
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
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 6
        __M_writer(escape(c.pagetitle))
        __M_writer(u'</h1>\n\n<p>Choose a file to import:</p>\n\n<form name="uploadform" enctype="multipart/form-data" method="POST" action=\n  "')
        # SOURCE LINE 11
        __M_writer(escape(url(controller='dobitem', action='upload')))
        __M_writer(u'">\nFilename: <input type="file" name="csvfile" /><br />\n<input type="submit" value="Upload" />\n</form>\n<p><a href="')
        # SOURCE LINE 15
        __M_writer(escape(url(controller='dobitem', action='index')))
        __M_writer(u'">Return to index</a>.</p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


