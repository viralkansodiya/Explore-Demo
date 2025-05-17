# In kingstech.com app (e.g., in `api.py`)
import frappe
from frappe.auth import LoginManager


# explore_demo.explore_demo.login_api.token_login
@frappe.whitelist(allow_guest=True)
def token_login(token):
    user = frappe.cache().get_value(f"login_token:{token}")
    if not user:
        frappe.throw("Invalid or expired token")

    login_manager = LoginManager()
    login_manager.authenticate(user=user, pwd=None)
    login_manager.post_login()
    return frappe.response
