import logging
import re

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from dobtrack.lib.base import BaseController, render, Session
from dobtrack.model import Item

from webhelpers.html import escape, HTML, literal, url_escape
from webhelpers.html.tags import *


log = logging.getLogger(__name__)

def paddate(s):
    if len(s) < 6:
        return s
    parts = ['', '', '']
    parts[0] = s[:4]
    if s[4] == 1:
        parts[1] = s[4:6]
        parts[2] = s[6:8]
    else:
        parts[1] = s[4:5]
        parts[2] = s[5:7]

    if len(parts[1]) == 1:
        parts[1] = "0" + parts[1]
    if len(parts[2]) == 1:
        parts[2] = "0" + parts[2]

    return "".join(parts)

def parsedate(s):
    # Converts the given string to "yyyymmdd". Assumes the string is in
    # "dd/mm/yy" or "dd/mm/yyyy" format - if it's not, a blank string is
    # returned.
    import re
    reg = re.compile(r"\d+")
    parts = reg.findall(s)
    if len(parts) == 3:
        for i in range(3):
            parts[i] = int(parts[i])

        if parts[2] < 2000:
            parts[2] += 2000

        # Swap year and day
        tmp = parts[0]+0
        parts[0] = parts[2]+0
        parts[2] = tmp+0

        for i in range(3):
            parts[i] = "{0:02d}".format(parts[i])
        return "".join(parts)
    else:
        # Can't parse so return empty string
        return ""

def unformatdate(s):
    datestr = s.strip()
    if len(datestr) < 8 or len(datestr) > 8:
        return datestr
    else:
        return "/".join([datestr[-2:], datestr[-4:-2], datestr[0:4]])

class DobitemController(BaseController):

    def runquery(self, params):
        """
        Returns a list of items based on the given parameters (which will
        usually come from the calling function's request.params[]).
        """
        print "[dobtrack log] runquery() called with these parameters:"
        print ", ".join((s + ': "' + params[s] + '"') for s in params)

        from sqlalchemy import or_
        sfields = ("datein", "kind", "initials", "customer", "costcentre",
                   "ordernum", "make", "model", "part", "serial", "asset",
                   "warranty", "location", "issue", "state", "solution",
                   "grn", "sap", "rtsdate", "comment")
        nfields = ("rep", "folio", "value")
        bfields = ("fujitsuowned",)
        allfields = sfields + nfields + bfields

        sortby = params["sortby"]
        sortasc = params["sortdir"] == "asc"
        filter = params["filter"]
        filterby = params["filterby"]
        page = int(params["page"])
        perpage = int(params["perpage"])
        sheet = params["sheet"]


        firstitem = perpage * page
        lastitem = firstitem + perpage

        itemlist = []

        print "[dobtrack log] Creating sublist query object"

        # Sort by chosen column first, then by REP
        # Resulting filter will look something like this:
        # "ORDER BY location DESC, rep DESC"
        if not sortasc:
            sortby += " DESC"

        if not sortby == "rep":
            sortby += ", rep"
        if not sortasc:
            sortby += " DESC"

        # Create sub-list based on selected sheet
        if sheet == "B":
            sublist = self.item_q.order_by(sortby)
        elif sheet == "L":
            sublist = self.item_q.filter(Item.folio == 0).order_by(sortby)
        else:
            sublist = self.item_q.filter(Item.folio != 0).order_by(sortby)

        if session['user'] != "admin":
            sublist = sublist.filter(Item.customer ==
                    (session['user']).upper())

        print "[dobtrack log] sublist created"

        filterstr = ""
        if filter:
            filters = filter.split(" ")
            if filterby:
                print "[dobtrack log] Filtering with '%s' in '%s' column" %\
                (filter, filterby)
                # Some columns need special handling
                if filterby == "rep" or filterby == "value":
                    # Search the string representation of each REP
                    for row in sublist:
                        for i, f in enumerate(filters):
                            if f in str(getattr(row, filterby)):
                                itemlist.append(row)
                                break
                elif filterby == "folio":
                    # Search for an exact numerical match
                    itemlist = sublist.filter(Item.folio == int(filters[0])).all()
                else:
                    # Otherwise just do a string search
                    terms = []
                    for term in filters:
                        terms.append(filterby + " LIKE '%" + term + "%'")
                    print "[dobtrack log] filterstr: %s" % filterstr
                    itemlist = sublist.filter(or_(*terms)).all()

            else:
                # Search all columns with an AND search
                for row in sublist:
                    matchcount = 0
                    for i, f in enumerate(filters):
                        for field in allfields:
                            if f in str(getattr(row, field)):
                                matchcount += 1
                                break
                    if matchcount == len(filters):
                        itemlist.append(row)
        else:
            print "[dobtrack log] No filter specified"
            # this one is the easiest - no filter so return all items
            itemlist = sublist.all()

        items = []

        if perpage == 0:
            # return all items
            for item in itemlist:
                items.append(
                    dict((field, getattr(item, field)) for field in allfields))
        else:
            # return a subset of the items based on page and perpage
            for item in itemlist[firstitem:lastitem]:
                items.append(
                    dict((field, getattr(item, field)) for field in allfields))
        print "\n[dobtrack log] Final filtered list created:",\
            len(items), "items[%d..%d] of" % (firstitem, lastitem-1)
        return {"items": items, "numfiltered": len(itemlist)}

    def __before__(self):
        print "[dobtrack log] __before__() of DobitemController() called"
        self.item_q = Session.query(Item)
        session.requestcount = 0
        if "user" not in session:
            print "'user' not in session"
            session["path_before_login"] = request.url
            session.save()
            return redirect("/login")

    def fixdate(self):
        items = self.item_q.all()
        for i, item in enumerate(items):
            items[i].rtsdate = parsedate(item.rtsdate)
        Session.commit()
        return redirect("/")

    def index(self):
        """
        Simply returns the more-or-less static index.mako template.
        The actual data loading etc. is done in Javascript once the page has
        loaded (see getitems() further down).
        """
        print "index() called"
        c.pagetitle = "DOB/DOA Tracker"
        c.itemcount = self.item_q.count()
        return render('/index.mako')

    def rtsform(self, id):
        import datetime
        c.item = self.item_q.filter_by(rep=id).first()
        repstring = "REP{0:0=7}".format(c.item.rep)
        c.printrep = repstring[0:6] + " " + repstring[6:10]
        c.pagetitle = "RTS form for # %s" % c.item.rep
        now = datetime.datetime.now()
        if not c.item.rtsdate:
            c.item.rtsdate = "%s/%s/%s" % (now.day, now.month, now.year)
        Session.commit()
        return render("/rtsform.mako")

    def tableprint(self):
        c.pagetitle = "DOB/DOA Tracker"
        return render("/tableprint.mako")

    def doesrepexist(self, id):
        # Return "yes" if id exists
        if Session.query(Item.rep).filter_by(rep=id).first():
            return "yes"
        else:
            return ""

    @jsonify
    def addtodb(self):
        if session["user"] != "admin":
            return

        import datetime

        if request.params['value']:
            f = float(request.params['value'])
        else:
            f = 0.0

        r = round(f, 2)
        newvalue = int(r*100)

        newitem = Item(rep=int(request.params['rep']),
                       customer=request.params['customer'].upper()[:30],
                       value=newvalue,
                       costcentre=request.params['costcentre'].upper()[:20],
                       ordernum=request.params['ordernum'].upper()[:20],
                       make=request.params['make'].upper()[:30],
                       model=request.params['model'].upper()[:50],
                       part=request.params['part'].upper()[:30],
                       serial=request.params['serial'].upper()[:30],
                       asset=request.params['asset'].upper()[:30],
                       warranty=request.params['warranty'].upper()[:30],
                       issue=request.params['issue'].upper()[:300],
                       state=request.params['state'].upper()[:300],
                       location=request.params['location'].upper()[:300],
                       comment=request.params['comment'].upper()[:300])
        if request.params.get('fujitsuowned') == 'yes':
            newitem.fujitsuowned = True
        else:
            newitem.fujitsuowned = False

        newitem.initials = "AF";
        now = datetime.datetime.now()
        newitem.datein = "%s%s%s" % (now.year, now.month, now.day)
        Session.add(newitem)
        Session.commit()

        fields = ("rep", "datein", "kind", "initials", "customer", "value",
                  "costcentre", "ordernum", "make", "model", "part", "serial",
                  "asset", "warranty", "location", "issue", "state", "solution",
                  "grn", "sap", "rtsdate", "folio", "comment")

        return dict((field, getattr(newitem, field)) for field in fields)

    def importcsv(self):
        c.pagetitle = "Import data from CSV file"
        return render('/importcsv.mako')

    def upload(self):
        """
        Really nasty CSV importer that does minimal error checking and
        expects everything to be laid out in a particular manner.
        """
        import csv
        csvfile = request.POST['csvfile']
        csvreader = csv.reader(csvfile.file, delimiter="\t", quotechar='"')

        rowsadded = 0
        repsadded = []
        c.duplicatereps = []
        c.unknowncustomers = []

        for row in csvreader:
            rep = row[3][3:][:7]
            if rep == '':
                rep = rowsadded

            # Skip over duplicate REP numbers
            if rep not in repsadded:
                newitem = Item(rep=int(rep),
                               kind=row[0].decode('utf-8', 'ignore')[:3],
                               initials=row[1].decode('utf-8', 'ignore')[:3],
                               customer=row[4].decode('utf-8', 'ignore')[:30],
                               costcentre=row[6].decode('utf-8', 'ignore')[:20],
                               ordernum=row[7].decode('utf-8', 'ignore')[:20],
                               make=row[8].decode('utf-8', 'ignore')[:30],
                               model=row[9].decode('utf-8', 'ignore')[:50],
                               part=row[10].decode('utf-8', 'ignore')[:30],
                               serial=row[11].decode('utf-8', 'ignore')[:30],
                               asset=row[12].decode('utf-8', 'ignore')[:30],
                               issue=row[14].decode('utf-8', 'ignore')[:300],
                               state=row[15].decode('utf-8', 'ignore')[:300],
                               location=row[16].decode('utf-8', 'ignore')[:300],
                               solution=row[17].decode('utf-8', 'ignore')[:300],
                               sap=row[18].decode('utf-8', 'ignore')[:8],
                               grn=row[19].decode('utf-8', 'ignore')[:8])

                # Sometimes Excel doesn't include the last column (or the CSV
                # reader doesn't read it properly).
                if len(row) >= 21:
                    # Sometimes the Folio column has non-numbers in it
                    try:
                        newitem.folio = int(row[21])
                    except ValueError:
                        newitem.folio = 0

                # Ditto for Value column, particularly items added long ago
                # by a certain "JH".
                try:
                    f = float(row[5])
                except ValueError:
                    f = 0.0

                # Store values as integers
                r = round(f, 2)
                newitem.value = int(r*100)

                newitem.datein = parsedate(row[2].decode('utf-8', 'ignore')[:20])
                newitem.warranty = parsedate(row[13].decode('utf-8', 'ignore')[:20])
                newitem.rtsdate = parsedate(row[20].decode('utf-8', 'ignore')[:20])

                # Return
                custs = ["TESCO", "HSBC", "SPECSAVERS", "HBOS", "RBSG"]
                def detectcust(cust):
                    for acust in custs:
                        if cust[:len(acust)] == acust:
                            return acust
                    if cust != "UNKNOWN":
                        c.unknowncustomers.append({"rep": newitem.rep,
                                                   "customer": cust})
                    return "UNKNOWN"

                newcust = detectcust(newitem.customer)

                # If there's a "/" in the customer name, assume it's owned
                # by Fujitsu if the character after the "/" is an "F"
                slash = newitem.customer.find("/")
                if slash != -1:
                    if newitem.customer[slash + 1] == "F":
                        newitem.fujitsuowned = True
                    else:
                        newitem.fujitsuowned = False

                newitem.customer = newcust

                Session.add(newitem)
                rowsadded = rowsadded + 1
                repsadded += [rep]
            else:
                c.duplicatereps += [rep]
                print "[dobtrack] Ignoring duplicate rep of %s" % rep

        Session.commit()
        print "[dobtrack] Unrecognised 'customer' entries:"
        print c.unknowncustomers

        c.rowsadded = rowsadded
        c.pagetitle = "CSV file uploaded successfully"
        return render('/upload.mako')

    def exportcsv(self):
        '''
        Exports the currently filtered items as a comma-separated .csv file.
        It's pretty basic but it does the job.
        '''
        response.headers['Content-type'] = 'text/csv'
        params = dict(request.params)
        params["perpage"] = "0"
        items = self.runquery(params)["items"]

        # Need this otherwise the columns are in whatever order the database
        # query returned them (usually wrong). Plus, not all fields are
        # relevant to the spreadsheet.
        fields = ("kind", "initials", "datein", "rep", "customer", "value",
            "costcentre", "ordernum", "make", "model", "part", "serial",
            "asset", "warranty", "issue", "state", "location", "solution",
            "grn", "sap", "rtsdate", "folio")

        result = ["DOA/DOB,Initials,Date To Us,REP,Customer,Value,Cost Centre"+
            ",Order #,Make,Model,Part #,Serial #,Asset #,Warranty,Issue,"+
            "Current State,Location,Solution,GRN,SAP,RTS Date,Folio\n"]
        for row in items:
            item = []
            for field in fields:
                if field == "rep":
                    item.append("REP{0:07d}".format(row["rep"]))
                elif field == "datein" or field == "warranty" or field ==\
                "rtsdate":
                    item.append(unformatdate(row[field]))
                elif field == "value":
                    item.append("{0:.2f}".format(row["value"]))
                else:
                    # turn single quotes into pairs
                    f = '""'.join(str(row[field]).split('"'))
                    item.append('"%s"' % f)
            result.append(",".join(item) + "\n")
        return result


    @jsonify
    def getitem(self, id):
        dbitem = self.item_q.filter_by(rep=id).first()

        fields = ("rep", "datein", "kind", "initials", "customer",
                  "fujitsuowned", "value", "costcentre", "ordernum", "make",
                  "model", "part", "serial", "asset", "warranty", "location",
                  "issue", "state", "solution", "grn", "sap", "rtsdate",
                  "folio", "comment")

        return dict((field, getattr(dbitem, field)) for field in fields)

    def deleteitem(self, id):
        if session["user"] != "admin":
            return id

        item = self.item_q.filter_by(rep=id).first()
        Session.delete(item)
        Session.commit()
        return id

    def deleteallitems(self):
        if session["user"] != "admin":
            return

        for item in self.item_q.all():
            Session.delete(item)
        Session.commit()
        c.pagetitle = "DOB/DOA Tracker"
        c.itemcount = 0
        return redirect("/")

    def testaction(self, id):
        raise RuntimeError();

    @jsonify
    def applyitemedit(self, id):
        if session["user"] != "admin":
            return

        item = self.item_q.filter_by(rep=id).first()

        f = float(request.params['value'])
        r = round(f, 2)
        item.value = int(r*100)

        fields30 = ("customer", "make", "part", "serial", "asset", "warranty")
        fields20 = ("costcentre", "ordernum", "rtsdate")
        fields300 = ("issue", "state", "solution", "location", "comment")

        allfields = fields30 + fields20 + fields300 +\
            ("rep", "initials", "value", "model", "grn", "sap", "folio",
             "fujitsuowned", "kind")

        for field in fields30:
            setattr(item, field, request.params[field].upper()[:30])

        for field in fields20:
            setattr(item, field, request.params[field].upper()[:20])

        for field in fields300:
            setattr(item, field, request.params[field].upper()[:300])

        item.model = request.params['model'].upper()[:50]
        item.grn = request.params['grn'].upper()[:8]
        item.sap = request.params['sap'].upper()[:8]
        item.folio = int(request.params['folio'])
        item.kind = request.params['kind'].upper()[:3]

        if request.params.get('fujitsuowned') == 'yes':
            item.fujitsuowned = True
        else:
            item.fujitsuowned = False

        Session.commit()

        result = dict((field, getattr(item, field)) for field in allfields)

        # Return info to JS handler, so it can update the index table
        return result

    @jsonify
    def getitems(self):
        itemresult = self.runquery(request.params)

        allcusts = [
            {"value": "TESCO", "text": "Tesco"},
            {"value": "HSBC", "text": "HSBC"},
            {"value": "SPECSAVERS", "text": "Specsavers"},
            {"value": "HBOS", "text": "HBOS"},
            {"value": "RBSG", "text": "RBSG"},
            {"value": "LLOYDS", "text": "Lloyds Pharmacy"},
            {"value": "BOOTS", "text": "Boots"},
            {"value": "UNKNOWN", "text": "(UNKNOWN)"}]

        customers = allcusts

        if session['user'] != "admin":
            for customer in allcusts:
                if customer["value"].lower() == session["user"]:
                    customers = [customer]
                    break

        result = {"total": self.item_q.count(),
                  "filtered": itemresult["numfiltered"],
                  "page": int(request.params["page"]),
                  "perpage": int(request.params["perpage"]),
                  "filterstr": request.params["filter"],
                  "username": session['user'],
                  "customers": customers,
                  "items": itemresult["items"]}

        return result
