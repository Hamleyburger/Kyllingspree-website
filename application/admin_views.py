from application import app

@app.route("/admin/dashboard")
def admin_dashboard():
    return "admin dashboard. Do admin stuff here."

@app.route("/admin/profile")
def admin_profile():
    return "admin profile: You're an admin and I know your name"