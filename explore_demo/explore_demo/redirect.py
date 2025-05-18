import frappe
import requests

@frappe.whitelist()
def generate_redirect_url():
    doc = frappe.get_doc("Explore Demo Settings")
    
    if not doc.site_name:
        frappe.throw("Site Name is not set in explore demo settings")
    
    url = f"{doc.site_name}/api/method/explore_demo.explore_demo.login_api.login_with_redirect"
    
    headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    payload = {
        "usr" : doc.user_id,
        "pwd" : doc.get_password("password")
    }

    response = requests.post(url, json=payload, headers=headers)


    if response:
        return {
            "site_url": f"{doc.site_name}/api/method/explore_demo.explore_demo.login_api.login_with_redirect?usr={doc.user_id}&pwd={doc.get_password('password')}",
            "success": 1
        }
    else:
        return {
            "success": 0,
            "message": f"API request failed with status {response.status_code}",
            "error": response.text
        }
            
    # except Exception as e:
    #     return {
    #         "success": 0,
    #         "message": str(e)
    #     }