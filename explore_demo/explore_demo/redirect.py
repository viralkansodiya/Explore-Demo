# In fossdemo.com site
import frappe
import secrets
import requests


# Api where the website page is developed
@frappe.whitelist()
def generate_redirect_url():
    token = secrets.token_urlsafe(32)
    # Store token and user in kingstech.com Redis
    doc = frappe.get_doc("Explore Demo Settings")
    if not doc.site_name:
        frappe.throw("Site Name is not set in explore demo settings")

    requests.post(f"{doc.site_name}/api/method/explore_demo.explore_demo.redirect.store_token", json={
        "token": token,
        "user": doc.user_id
    })

    return f"{doc.site_name}/api/method/explore_demo.explore_demo.login_api.token_login?token={token}"




# API redirect site
# explore_demo.explore_demo.redirect.store_token
@frappe.whitelist(allow_guest=True)
def store_token(token, user):
    frappe.cache().set_value(f"login_token:{token}", user, expires_in_sec=60)
