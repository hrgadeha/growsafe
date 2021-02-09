from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.document import Document
from frappe.utils import money_in_words


@frappe.whitelist(allow_guest=True)
def getOverdue(customer):
        si = frappe.db.sql("""select IF(status='Overdue', "1", "0") from `tabSales Invoice` where 
                        customer = %s and status = 'overdue' order by creation desc limit 1;;""",(customer))
        return si[0][0] if si else 0.0
