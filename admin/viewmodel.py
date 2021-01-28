from admin import admin_blue


@admin_blue.route('/viewmodel')
def viewmodel():
    return "viewmodel"
