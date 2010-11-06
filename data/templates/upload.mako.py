from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1285797741.574662
_template_filename='/home/andy/dobtrack/dobtrack/templates/upload.mako'
_template_uri='/upload.mako'
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
        int = context.get('int', UNDEFINED)
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 6
        __M_writer(escape(c.pagetitle))
        __M_writer(u'</h1>\n<p>\n  ')
        # SOURCE LINE 8
        __M_writer(escape(c.rowsadded))
        __M_writer(u' items were added to the database.\n</p>\n<p>\n  The following REP numbers appeared more than once:<br />\n')
        # SOURCE LINE 12
        for rep in c.duplicatereps:
            # SOURCE LINE 13
            __M_writer(u'    ')
            __M_writer(escape(int(rep)))
            __M_writer(u'<br />\n')
        # SOURCE LINE 15
        __M_writer(u'</p>\n<p>\n  The following REP numbers had unrecognisable customer information:<br />\n')
        # SOURCE LINE 18
        for cust in c.unknowncustomers:
            # SOURCE LINE 19
            __M_writer(u'    REP: ')
            __M_writer(escape(cust['rep']))
            __M_writer(u', Customer: ')
            __M_writer(escape(cust['customer']))
            __M_writer(u'<br />\n')
        # SOURCE LINE 21
        __M_writer(u'</p>\n\n<p><a href="')
        # SOURCE LINE 23
        __M_writer(escape(url(controller='dobitem', action='index')))
        __M_writer(u'">Return to index</a>.</p>\n')
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


