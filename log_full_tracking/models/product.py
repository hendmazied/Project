from odoo import models, api, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _setup_complete(self):
        
        res = super(ProductTemplate, self)._setup_complete()
        
        blacklist = ['write_date', '__last_update', 'message_ids', 'activity_ids']
        
        for field_name, field_obj in self._fields.items():
            if field_name not in blacklist:
                field_obj.tracking = True 
                
        return res
class Productcategory(models.Model):
    _inherit = 'product.category'

    @api.model
    def _setup_complete(self):
        
        res = super(Productcategory, self)._setup_complete()
        
        blacklist = ['write_date', '__last_update', 'message_ids', 'activity_ids']
        
        for field_name, field_obj in self._fields.items():
            if field_name not in blacklist:
                field_obj.tracking = True 
                
        return res
class Accountaccount(models.Model):
    _inherit = 'account.account'

    @api.model
    def _setup_complete(self):
        
        res = super(Accountaccount, self)._setup_complete()
        
        blacklist = ['write_date', '__last_update', 'message_ids', 'activity_ids']
        
        for field_name, field_obj in self._fields.items():
            if field_name not in blacklist:
                field_obj.tracking = True 
                
        return res
 
class Accountanalyticaccount(models.Model):
    _inherit = 'account.analytic.account'

    @api.model
    def _setup_complete(self):
        res = super(Accountanalyticaccount, self)._setup_complete()
        
        
        unsupported_types = ['html', 'binary', 'reference', 'many2many', 'one2many']
        
        blacklist = [
            'write_date', 'create_date', 'write_uid', 'create_uid',
            '__last_update', 'message_ids', 'activity_ids', 
            'message_follower_ids', 'access_token', 'default_values' 
        ]
        
        for field_name, field_obj in self._fields.items():
           
            if (field_name not in blacklist and 
                field_obj.type not in unsupported_types and 
                not getattr(field_obj, 'compute', None)):
                
                field_obj.tracking = True 
                
        return res
 
class Accountjournal(models.Model):
    _inherit = 'account.journal'

    @api.model
    def _setup_complete(self):
        res = super(Accountjournal, self)._setup_complete()
        
        
        unsupported_types = ['html', 'binary', 'reference', 'many2many', 'one2many']
        
        blacklist = [
            'write_date', 'create_date', 'write_uid', 'create_uid',
            '__last_update', 'message_ids', 'activity_ids', 
            'message_follower_ids', 'access_token', 'default_values' 
        ]
        
        for field_name, field_obj in self._fields.items():
           
            if (field_name not in blacklist and 
                field_obj.type not in unsupported_types and 
                not getattr(field_obj, 'compute', None)):
                
                field_obj.tracking = True 
                
        return res
class Mrpbom(models.Model):
    _inherit = 'mrp.bom'

    @api.model
    def _setup_complete(self):
        res = super(Mrpbom, self)._setup_complete()
        
        
        unsupported_types = ['html', 'binary', 'reference', 'many2many', 'one2many']
        
        blacklist = [
            'write_date', 'create_date', 'write_uid', 'create_uid',
            '__last_update', 'message_ids', 'activity_ids', 
            'message_follower_ids', 'access_token', 'default_values' 
        ]
        
        for field_name, field_obj in self._fields.items():
           
            if (field_name not in blacklist and 
                field_obj.type not in unsupported_types and 
                not getattr(field_obj, 'compute', None)):
                
                field_obj.tracking = True 
                
        return res
    

class AnalyticDistributionModel(models.Model):
    _inherit = ['account.analytic.distribution.model', 'mail.thread', 'mail.activity.mixin']
    _name = 'account.analytic.distribution.model'


    @api.model
    def _setup_complete(self):
        
        res = super(AnalyticDistributionModel, self)._setup_complete()
        
        blacklist = ['write_date', '__last_update', 'message_ids', 'activity_ids']
        
        for field_name, field_obj in self._fields.items():
            if field_name not in blacklist:
                field_obj.tracking = True 
                
        return res
class Accountanalyticplan(models.Model):
    _inherit = ['account.analytic.plan', 'mail.thread', 'mail.activity.mixin']
    _name = 'account.analytic.plan'


    @api.model
    def _setup_complete(self):
        
        res = super(Accountanalyticplan, self)._setup_complete()
        
        blacklist = ['write_date', '__last_update', 'message_ids', 'activity_ids']
        
        for field_name, field_obj in self._fields.items():
            if field_name not in blacklist:
                field_obj.tracking = True 
                
        return res
class Stockwarehouse(models.Model):
    _inherit = ['stock.warehouse', 'mail.thread', 'mail.activity.mixin']
    _name = 'stock.warehouse'


    @api.model
    def _setup_complete(self):
        res = super(Stockwarehouse, self)._setup_complete()
        
        
        unsupported_types = ['html', 'binary', 'reference', 'many2many', 'one2many']
        
        blacklist = [
            'write_date', 'create_date', 'write_uid', 'create_uid',
            '__last_update', 'message_ids', 'activity_ids', 
            'message_follower_ids', 'access_token', 'default_values' 
        ]
        
        for field_name, field_obj in self._fields.items():
           
            if (field_name not in blacklist and 
                field_obj.type not in unsupported_types and 
                not getattr(field_obj, 'compute', None)):
                
                field_obj.tracking = True 
                
        return res




class StockLocation(models.Model):
    _inherit = ['stock.location', 'mail.thread', 'mail.activity.mixin']
    _name = 'stock.location'

    @api.model
    def _setup_complete(self):
        res = super(StockLocation, self)._setup_complete()
        
        
        unsupported_types = ['html', 'binary', 'reference', 'many2many', 'one2many']
        
        blacklist = [
            'write_date', 'create_date', 'write_uid', 'create_uid',
            '__last_update', 'message_ids', 'activity_ids', 
            'message_follower_ids', 'access_token', 'default_values' 
        ]
        
        for field_name, field_obj in self._fields.items():
           
            if (field_name not in blacklist and 
                field_obj.type not in unsupported_types and 
                not getattr(field_obj, 'compute', None)):
                
                field_obj.tracking = True 
                
        return res
    


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    # تفعيل التتبع (اختياري مع الـ write اليدوي بس للأمان)
    product_id = fields.Many2one('product.product', string='Component', tracking=True)
    product_qty = fields.Float(string='Quantity', tracking=True)
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure', tracking=True)

    def write(self, vals):
        # 1. بنضيف الـ UoM في حفظ القيم القديمة قبل التعديل
        pre_values = {line.id: {
            'product_id': line.product_id.display_name,
            'product_qty': line.product_qty,
            'uom_id': line.product_uom_id.display_name, # ضفنا دي
        } for line in self}

        res = super(MrpBomLine, self).write(vals)

        for line in self:
            if line.bom_id:
                tracking_notes = []
                
                # تتبع المنتج
                if 'product_id' in vals:
                    old_name = pre_values[line.id]['product_id']
                    new_name = line.product_id.display_name
                    tracking_notes.append(f"product: {old_name} ➔ {new_name}")
                
                # تتبع الكمية
                if 'product_qty' in vals:
                    old_qty = pre_values[line.id]['product_qty']
                    new_qty = line.product_qty
                    tracking_notes.append(f"{line.product_id.name}: {old_qty:g} ➔ {new_qty:g}")

                # 2. تتبع وحدة القياس (الـ UoM) - الجزء اللي كان ناقص
                if 'product_uom_id' in vals:
                    old_uom = pre_values[line.id]['uom_id']
                    new_uom = line.product_uom_id.display_name
                    tracking_notes.append(f" {old_uom} ➔ {new_uom}  (Unit of Measure)")

                if tracking_notes:

                    # بنبعت الرسالة كـ Note عشان تظهر منقطة ونظيفة

                    body = f"{''.join(tracking_notes)} "

                    line.bom_id.message_post(body=body, subtype_xmlid='mail.mt_note')

        return res


class AccountPaymentMethodLine(models.Model):
    _inherit = 'account.payment.method.line'

    def write(self, vals):
        # 1. حفظ القيم القديمة قبل التعديل
        # ضفنا هنا 'payment_account_id' عشان نراقب حسابات الاستلام/الدفع
        pre_values = {line.id: {
            'name': line.name,
            'account_name': line.payment_account_id.display_name or "فارغ",
        } for line in self}

        res = super(AccountPaymentMethodLine, self).write(vals)

        # 2. إرسال التتبع لشاتر الأب (Journal)
        for line in self:
            target = line.journal_id
            if target:
                tracking_notes = []
                
                # تتبع تغيير الاسم
                if 'name' in vals:
                    old_n = pre_values[line.id]['name']
                    tracking_notes.append(f"Name: {old_n} ➔ {line.name}")
                
                # تتبع تغيير حساب الاستلام (Outstanding Receipts account)
                if 'payment_account_id' in vals:
                    old_acc = pre_values[line.id]['account_name']
                    new_acc = line.payment_account_id.display_name or "فارغ"
                    tracking_notes.append(
                        f"Account ({line.name}): {old_acc} ➔ {new_acc} (Outstanding Account)"
                    )

                if tracking_notes:
           
                    # بنبعت الرسالة كـ Note عشان تظهر منقطة ونظيفة

                    body = f"{''.join(tracking_notes)} "

                    target.message_post(body=body, subtype_xmlid='mail.mt_note')
        return res
