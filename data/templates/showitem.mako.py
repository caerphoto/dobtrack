from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1283110120.7049019
_template_filename='/home/andy/dobtrack/dobtrack/templates/showitem.mako'
_template_uri='/showitem.mako'
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
        # SOURCE LINE 5
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 7
        __M_writer(escape(c.pagetitle))
        __M_writer(u'</h1>\n\n<p>Item added by: ')
        # SOURCE LINE 9
        __M_writer(escape(c.item.initials))
        __M_writer(u'</p>\n\n<table class="itemdetail">\n  <tr>\n    <th>Customer</th>\n    <th>Value</th>\n    <th>Cost Centre</th>\n    <th>Order Number</th>\n  </tr>\n  <tr>\n    <td>')
        # SOURCE LINE 19
        __M_writer(escape(c.item.customer))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 20
        __M_writer(escape(c.item.value))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 21
        __M_writer(escape(c.item.costcentre))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 22
        __M_writer(escape(c.item.order))
        __M_writer(u'</td>\n  </tr>\n</table>\n\n<table class="itemdetail">\n  <tr>\n    <th>Make</th>\n    <th>Model</th>\n    <th>Part Number</th>\n    <th>Serial Number</th>\n    <th>Asset Tag</th>\n    <th>Warranty</th>\n  </tr>\n  <tr>\n    <td>')
        # SOURCE LINE 36
        __M_writer(escape(c.item.make))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 37
        __M_writer(escape(c.item.model))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 38
        __M_writer(escape(c.item.part))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 39
        __M_writer(escape(c.item.serial))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 40
        __M_writer(escape(c.item.asset))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 41
        __M_writer(escape(c.item.warranty))
        __M_writer(u'</td>\n  </tr>\n</table>\n\n<table class="itemdetail">\n  <tr>\n    <th>Location</th>\n    <th>Issue</th>\n    <th>Current State</th>\n    <th>Solution</th>\n  </tr>\n  <tr id="itemstatus">\n    <td>')
        # SOURCE LINE 53
        __M_writer(escape(c.item.location))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 54
        __M_writer(escape(c.item.issue))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 55
        __M_writer(escape(c.item.state))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 56
        __M_writer(escape(c.item.solution))
        __M_writer(u'</td>\n  </tr>\n</table>\n\n<table class="itemdetail">\n  <tr>\n    <th>GRN</th>\n    <th>SAP/GDN</th>\n    <th>Folio Number</th>\n    <th>RTS Date</th>\n  </tr>\n  <tr>\n    <td>')
        # SOURCE LINE 68
        __M_writer(escape(c.item.grn))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 69
        __M_writer(escape(c.item.sap))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 70
        __M_writer(escape(c.item.folio))
        __M_writer(u'</td>\n    <td>')
        # SOURCE LINE 71
        __M_writer(escape(c.item.rtsdate))
        __M_writer(u'</td>\n  </tr>\n</table>\n\n<p>\n<a href="')
        # SOURCE LINE 76
        __M_writer(escape(url(controller='dobitem', action='edititem', id=c.item.rep)))
        __M_writer(u'">Edit item details...</a>\n</p>\n\n<form name="delete" method="post" action=\n      "')
        # SOURCE LINE 80
        __M_writer(escape(url(controller='dobitem', action='deletefromdb', id=c.item.rep)))
        __M_writer(u'">\n  <input type="submit" name="delitem" value="Delete Item" />\n</form>\n<p>\n<br />\nor <a href="')
        # SOURCE LINE 85
        __M_writer(escape(url(controller='dobitem', action='index')))
        __M_writer(u'">return to index</a>.\n</p>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


