from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1286913544.154778
_template_filename='/home/andy/dobtrack/dobtrack/templates/tableprint.mako'
_template_uri='/tableprint.mako'
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
        __M_writer(u'\n\n<input type="button" value="Close" onclick="window.close()" />\n\n<h1>')
        # SOURCE LINE 9
        __M_writer(escape(c.pagetitle))
        __M_writer(u'</h1>\n\n<table>\n  <thead class="colhead">\n    <tr id="columnheaders">\n    </tr>\n    <tr id="loadingmessage" class="i loadingmessage">\n      <td colspan="8" style="padding: 1em">\n        <img src="/ajax-loader_grey.gif" width="16" height="16"\n             style="vertical-align: -30%" /> Loading item data...\n      </td>\n    </tr>\n  </thead>\n  <tbody id="indextable">\n  </tbody>\n</table>\n\n<script type="text/javascript" src="/jquery.js"></script>\n<script type="text/javascript" src="/common.js"></script>\n<script type="text/javascript" src="/tableprint.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <link rel="stylesheet" type="text/css" href="/tableprint.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


