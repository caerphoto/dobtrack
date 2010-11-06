from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1283282674.049083
_template_filename='/home/andy/dobtrack/dobtrack/templates/additem.mako'
_template_uri='/additem.mako'
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
        # SOURCE LINE 6
        __M_writer(u'\n\n<h1>')
        # SOURCE LINE 8
        __M_writer(escape(c.pagetitle))
        __M_writer(u'</h1>\n\n<form name="add" method="POST" action=\n      "')
        # SOURCE LINE 11
        __M_writer(escape(url(controller='dobitem', action='addtodb')))
        __M_writer(u'">\n  <div id="singlelines">\n  <table>\n    <tr>\n      <th class="itemdetails_leftcol"><label for="rep">REP number:</label></th>\n      <td><input type="text" name="rep" value="')
        # SOURCE LINE 16
        __M_writer(escape(c.newrep))
        __M_writer(u'" /></td>\n    </tr>\n    <tr>\n      <th><label for="initials">Initials:</label></th>\n      <td><input type="text" name="initials" value="AF" /></td>\n    </tr>\n    <tr>\n      <th><label for="customer">Customer:</label></th>\n      <td>\n        <select name="customer">\n          <option value="TESCO">Tesco</option>\n          <option value="HSBC">HSBC</option>\n          <option value="SPECSAVERS">Specsavers</option>\n        </select>\n        <input type="checkbox" name="fujitsuowned" id="fujitsuowned" /><label\n          for="fujitsuowned">Fujitsu owned</label>\n      </td>\n    </tr>\n    <tr>\n      <th><label for="value">Value:</label></th>\n      <td><input type="text" name="value" value="0.00"/></td>\n    </tr>\n    <tr>\n      <th><label for="costcentre">Cost centre:</label></th>\n      <td><input type="text" name="costcentre" /></td>\n    </tr>\n    <tr>\n      <th><label for="order">Order number:</label></th>\n      <td><input type="text" name="order" /></td>\n    </tr>\n  </table>\n\n  <table>\n    <tr>\n      <th class="itemdetails_leftcol"><label for="make">Make:</label></th>\n      <td><input type="text" name="make" /></td>\n    </tr>\n    <tr>\n      <th><label for="model">Model:</label></th>\n      <td><input type="text" name="model" /></td>\n    </tr>\n    <tr>\n      <th><label for="part">Part number:</label></th>\n      <td><input type="text" name="part" /></td>\n    </tr>\n    <tr>\n      <th><label for="serial">Serial number:</label></th>\n      <td><input type="text" name="serial" /></td>\n    </tr>\n    <tr>\n      <th><label for="asset">Asset tag:</label></th>\n      <td><input type="text" name="asset" /></td>\n    </tr>\n    <tr>\n      <th><label for="warranty">Warranty:</label></th>\n      <td><input type="text" name="warranty" /></td>\n    </tr>\n  </table>\n\n  <table>\n    <tr>\n      <th class="itemdetails_leftcol"><label for="location">Location:</label></th>\n      <td><input type="text" name="location" /></td>\n    </tr>\n  </table>\n  </div>\n  <div id="textareas">\n    <p>Issue:</p>\n    <div class="textarea"><textarea name="issue"></textarea></div>\n    <p>Current State:</p>\n    <div class="textarea"><textarea name="state">Awaiting parts/test</textarea></div>\n    <input type="submit" name="submit" value="Submit" />\n  </div>\n\n</form>\n<div id="formender">\n<a href="')
        # SOURCE LINE 92
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
        __M_writer(u'\n    <script type="text/javascript" src="/edititem.js"></script>\n    <script type="text/javascript" src="/additem.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


