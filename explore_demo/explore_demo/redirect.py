import frappe
import requests

@frappe.whitelist()
def generate_redirect_url():
    # try:
    doc = frappe.get_doc("Explore Demo Settings")
    
    if not doc.site_name:
        frappe.throw("Site Name is not set in explore demo settings")
    
    # Prepare API credentials
    api_key = doc.api_key
    api_secret = doc.get_password('api_secret')
    
    # Construct the API URL
    url = f"{doc.site_name}/api/method/explore_demo.explore_demo.login_api.login"
    
    headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    payload = {
        "usr" : doc.user_id,
        "pwd" : doc.get_password("password")
    }
    
    # Make the request
    response = requests.post(url, json=payload, headers=headers)

    return response
    # Check for successful response
    if response:
        return {
            "site_url": doc.site_name,
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