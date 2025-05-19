import os
import subprocess
import frappe

def auto_restore():
    # Define paths
    doc=frappe.get_doc("Auto Restore")
    if not doc.enable:
        return
    backup_file = doc.path_to_database
    site_name = frappe.local.site

    # Command to restore DB
    cmd = f"bench --site {site_name} --force restore {backup_file}"

    try:
        subprocess.run(cmd, shell=True, check=True)
        frappe.logger().info("Database restored successfully.")
    except subprocess.CalledProcessError as e:
        frappe.logger().error(f"Restore failed: {e}")


# from explore_demo.explore_demo.auto_restore import auto_restore