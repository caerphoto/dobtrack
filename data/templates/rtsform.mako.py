from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1288012440.099329
_template_filename='/home/andy/dobtrack/dobtrack/templates/rtsform.mako'
_template_uri='/rtsform.mako'
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
        # SOURCE LINE 12
        __M_writer(u'\n\n<p id="rtsform_controls">\n<input type="button" value="Print" onclick="window.print()" /> &nbsp;\n<input type="button" value="Close" onclick="window.close()" />\n</p>\n\n<div id="foliocontainer">Folio: <span id="folio">&nbsp;</span></div>\n\n<h1>Fujitsu Services - WAR08</h1>\n<h2>DOB/DOA Return To Good Stock Form</h2>\n\n<div id="rep" class="detailsection">\n    <div class="propertylabel">DOB/DOA stock control barcode:</div>\n    <div class="itemproperty">')
        # SOURCE LINE 26
        __M_writer(escape(c.printrep))
        __M_writer(u'</div>\n</div>\n\n<div class="detailsection">\n    <div class="propertylabel">Part #:</div>\n    <div class="itemproperty">')
        # SOURCE LINE 31
        __M_writer(escape(c.item.part))
        __M_writer(u'</div>\n</div>\n\n<div id="itemdesc" class="detailsection">\n    <div class="propertylabel">Item description:</div>\n    <div class="itemproperty">')
        # SOURCE LINE 36
        __M_writer(escape(c.item.make))
        __M_writer(u' ')
        __M_writer(escape(c.item.model))
        __M_writer(u'</div>\n</div>\n\n<div class="detailsection">\n    <div class="propertylabel">Serial #:</div>\n    <div class="itemproperty">')
        # SOURCE LINE 41
        __M_writer(escape(c.item.serial))
        __M_writer(u'</div>\n</div>\n\n<div class="detailsection">\n    <div class="propertylabel">RTS date:</div>\n    <div class="itemproperty">')
        # SOURCE LINE 46
        __M_writer(escape(c.item.rtsdate))
        __M_writer(u'</div>\n</div>\n\n<div class="detailsection">\n    <div class="propertylabel">SAP # (604&hellip;):</div>\n    <div class="itemproperty">')
        # SOURCE LINE 51
        __M_writer(escape(c.item.sap))
        __M_writer(u'</div>\n</div>\n\n<div class="detailsection">\n    <div class="propertylabel">GRN # (840&hellip;):</div>\n    <div class="itemproperty">')
        # SOURCE LINE 56
        __M_writer(escape(c.item.grn))
        __M_writer(u'</div>\n</div>\n\n<h3 id="sigsection">Accepted to WAR08 warehouse by:</h3>\n<div>Name:\n<div id="namebox">&nbsp;</div></div>\n\n<div>Signature:\n<div id="signaturebox">&nbsp;</div></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <link rel="stylesheet" type="text/css" href="/rtsform.css" />\n    <style>\n      @page {\n        @top-right {\n            content: "')
        # SOURCE LINE 8
        __M_writer(escape(c.item.folio))
        __M_writer(u'";\n        }\n      }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


