from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1286217279.339057
_template_filename='/home/andy/dobtrack/dobtrack/templates/base.mako'
_template_uri='/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\n  "http://www.w3.org/TR/html4/strict.dtd">\n<html>\n  <head>\n    <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">\n    ')
        # SOURCE LINE 6
        __M_writer(escape(self.head_tags()))
        __M_writer(u'\n\n    <title>')
        # SOURCE LINE 8
        __M_writer(escape(c.pagetitle))
        __M_writer(u'</title>\n  </head>\n  <body>\n    ')
        # SOURCE LINE 11
        __M_writer(escape(self.body()))
        __M_writer(u'\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


