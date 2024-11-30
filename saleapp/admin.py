from saleapp.models import Category, Product
from saleapp import db, app
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

class ProductView(ModelView):
    column_searchable_list = ['name', 'description']
    column_filters = ['name', 'price']
    can_view_details = True
    can_export = True
    column_export_list = ['image']
    column_labels = {
        'name': 'tên',
        'description':'mô tả'
    }

    def is_accessible(self):
        return current_user.is_authenticated


class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')
admin.add_view(ModelView(Category, db.session, name='Danh mục'))
admin.add_view(ProductView(Product, db.session, name='Sản phẩm'))
admin.add_view(StatsView(name='Thống kê'))