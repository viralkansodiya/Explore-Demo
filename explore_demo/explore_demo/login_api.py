import frappe
from frappe import auth

@frappe.whitelist(allow_guest=True)
def login_with_redirect(usr, pwd):
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()

        frappe.local.response["type"] = "redirect"
        frappe.local.response["location"] = "/app"

    except frappe.exceptions.AuthenticationError:
        frappe.throw("Authentication Failed")
