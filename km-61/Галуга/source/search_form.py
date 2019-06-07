from flask_wtf import Form
from wtforms import StringField,   SubmitField
from dao.userhelper import UserHelper

class SearchForm(Form):

    document_path = StringField('path fail: ')
    submit = SubmitField('Search')


    def get_result(self):
        helper = UserHelper()
        return helper.getDocumentData(self.document_path.data)