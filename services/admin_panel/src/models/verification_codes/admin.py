from flask_admin.contrib.sqla import ModelView


class VerifCodesAdminView(ModelView):
    create_modal = True
    edit_modal = True
    
    column_list = ['phone', 'verification_code']

    column_labels = dict(phone="номер телефона", verification_code="sms-код")