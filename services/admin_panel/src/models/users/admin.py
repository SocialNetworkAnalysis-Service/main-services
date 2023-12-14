from flask_admin.contrib.sqla import ModelView


class UsersAdminView(ModelView):
    create_modal = True
    edit_modal = True
    
    column_list = ['phone']

    column_labels = dict(phone="номер телефона")