from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1283362433.3968129
_template_filename='/home/andy/dobtrack/dobtrack/templates/edititem.mako'
_template_uri='/edititem.mako'
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
        __M_writer(u'</h1>\n\n<p>Item added by <strong>')
        # SOURCE LINE 9
        __M_writer(escape(c.item.initials))
        __M_writer(u'</strong></p>\n<form id="delitem" name="delete" method="post" action=\n      "')
        # SOURCE LINE 11
        __M_writer(escape(url(controller='dobitem', action='deletefromdb', id=c.item.rep)))
        __M_writer(u'">\n    <input type="submit" name="delitem" value="Delete Item" /> (WARNING: cannot be undone)\n</form>\n\n<form name="add" method="POST" action=\n      "')
        # SOURCE LINE 16
        __M_writer(escape(url(controller='dobitem', action='applyitemedit', id=c.item.rep)))
        __M_writer(u'">\n  <div id="singlelines">\n  <table>\n    <tr>\n      <th class="itemdetails_leftcol"><label for="customer">Customer:</label></th>\n      <td>\n        <select name="customer">\n          <option value="TESCO">Tesco</option>\n          <option value="HSBC">HSBC</option>\n          <option value="SPECSAVERS">Specsavers</option>\n        </select>\n')
        # SOURCE LINE 27
        if c.item.fujitsuowned:
            # SOURCE LINE 28
            __M_writer(u'        <input type="checkbox" name="fujitsuowned" id="fujitsuowned" checked="checked" />\n')
            # SOURCE LINE 29
        else:
            # SOURCE LINE 30
            __M_writer(u'        <input type="checkbox" name="fujitsuowned" id="fujitsuowned" />\n')
        # SOURCE LINE 32
        __M_writer(u'        <label for="fujitsuowned">Fujitsu owned</label>\n      </td>\n    </tr>\n    <tr>\n      <th><label for="value">Value:</label></th>\n      <td><input type="text" name="value" value=\'')
        # SOURCE LINE 37
        __M_writer(escape("{0:.2f}".format(c.item.value / 100.0)))
        __M_writer(u'\' /></td>\n    </tr>\n    <tr>\n      <th><label for="costcentre">Cost centre:</label></th>\n      <td><input type="text" name="costcentre" value="')
        # SOURCE LINE 41
        __M_writer(escape(c.item.costcentre))
        __M_writer(u'" /></td>\n    </tr>\n    <tr>\n      <th><label for="order">Order number:</label></th>\n      <td><input type="text" name="order" value="')
        # SOURCE LINE 45
        __M_writer(escape(c.item.order))
        __M_writer(u'" /></td>\n    </tr>\n  </table>\n\n  <table>\n    <tr>\n      <th class="itemdetails_leftcol"><label for="make">Make:</label></th>\n      <td><input type="text" name="make" value="')
        # SOURCE LINE 52
        __M_writer(escape(c.item.make))
        __M_writer(u'" /></td>\n    </tr>\n    <tr>\n      <th><label for="model">Model:</label></th>\n      <td><input type="text" name="model" value="')
        # SOURCE LINE 56
        __M_writer(escape(c.item.model))
        __M_writer(u'" /></td>\n    </tr>\n    <tr>\n      <th><label for="part">Part number:</label></th>\n      <td><input type="text" name="part" value="')
        # SOURCE LINE 60
        __M_writer(escape(c.item.part))
        __M_writer(u'" /></td>\n    </tr>\n    <tr>\n      <th><label for="serial">Serial number:</label></th>\n      <td><input type="text" name="serial" value="')
        # SOURCE LINE 64
        __M_writer(escape(c.item.serial))
        __M_writer(u'" /></td>\n    </tr>\n    <tr>\n      <th><label for="asset">Asset tag:</label></th>\n      <td><input type="text" name="asset" value="')
        # SOURCE LINE 68
        __M_writer(escape(c.item.asset))
        __M_writer(u'" /></td>\n    </tr>\n    <tr>\n      <th><label for="warranty">Warranty:</label></th>\n      <td><input type="text" name="warranty" value="')
        # SOURCE LINE 72
        __M_writer(escape(c.item.warranty))
        __M_writer(u'" /></td>\n    </tr>\n  </table>\n\n  <table>\n    <tr>\n      <th class="itemdetails_leftcol"><label for="location">Location:</label></th>\n      <td><input type="text" name="location" value="')
        # SOURCE LINE 79
        __M_writer(escape(c.item.location))
        __M_writer(u'" /></td>\n    </tr>\n  </table>\n  <table>\n    <tr>\n      <th class="itemdetails_leftcol"><label for="grn">GRN - SAP:</label></th>\n      <td>\n            <input type="text" name="grn" id="grn" value="')
        # SOURCE LINE 86
        __M_writer(escape(c.item.grn))
        __M_writer(u'" maxlength="8"/>\n            <input type="text" name="sap" id="sap" value="')
        # SOURCE LINE 87
        __M_writer(escape(c.item.sap))
        __M_writer(u'" maxlength="8"/>\n      </td>\n    </tr>\n  </table>\n\n  <table>\n    <tr>\n      <th class="itemdetails_leftcol"><label for="folio">Folio:</label></th>\n      <td><input type="text" name="folio" value="')
        # SOURCE LINE 95
        __M_writer(escape(c.item.folio))
        __M_writer(u'" /></td>\n    </tr>\n    <tr>\n      <th><label for="rtsdate">RTS Date:</label></th>\n      <td><input type="text" name="rtsdate" value="')
        # SOURCE LINE 99
        __M_writer(escape(c.item.rtsdate))
        __M_writer(u'" /></td>\n    </tr>\n  </table>\n\n\n  </div>\n  <div id="textareas">\n    <p>Issue:</p>\n    <div class="textarea"><textarea name="issue">')
        # SOURCE LINE 107
        __M_writer(escape(c.item.issue))
        __M_writer(u'</textarea></div>\n\n    <p>Current State:</p>\n    <div class="textarea"><textarea name="state">')
        # SOURCE LINE 110
        __M_writer(escape(c.item.state))
        __M_writer(u'</textarea></div>\n\n    <p>Solution:</p>\n    <div class="textarea"><textarea name="solution">')
        # SOURCE LINE 113
        __M_writer(escape(c.item.solution))
        __M_writer(u'</textarea></div>\n\n    <input type="submit" name="submit" value="Apply Changes" />\n  </div>\n</form>\n<div id="formender">\n<div id="debug1">&nbsp;</div>\n<div id="debug2">&nbsp;</div>\n<a href="')
        # SOURCE LINE 121
        __M_writer(escape(url(controller='dobitem', action='index')))
        __M_writer(u'">Return to index</a>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <script type="text/javascript" src="/edititem.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


