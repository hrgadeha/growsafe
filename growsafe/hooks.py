# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "growsafe"
app_title = "Growsafe"
app_publisher = "Hardik Gadesha"
app_description = "For Development of Custom Report for Growsafe Chemicals"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hardikgadesha@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/growsafe/css/growsafe.css"
# app_include_js = "/assets/growsafe/js/growsafe.js"

# include js, css files in header of web template
# web_include_css = "/assets/growsafe/css/growsafe.css"
# web_include_js = "/assets/growsafe/js/growsafe.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "growsafe.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "growsafe.install.before_install"
# after_install = "growsafe.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "growsafe.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

fixtures = [
	{
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
			"Sales Order-branch",
			"Sales Invoice-branch",
			"Branch-warehouse",
			"Sales Order-allow_submit",
			"Sales Order-has_overdue_invoice",
			"Sales Invoice-column_break_2",
			"Sales Invoice-ware_house",
			"Sales Invoice-section_break_4",
			"Sales Invoice-shipping",
			"Sales Invoice-grno",
			"Sales Invoice-freightterms",
			"Sales Invoice-column_break_131"
		]
	   ]
	]
    }
]

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"growsafe.tasks.all"
# 	],
# 	"daily": [
# 		"growsafe.tasks.daily"
# 	],
# 	"hourly": [
# 		"growsafe.tasks.hourly"
# 	],
# 	"weekly": [
# 		"growsafe.tasks.weekly"
# 	]
# 	"monthly": [
# 		"growsafe.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "growsafe.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "growsafe.event.get_events"
# }

