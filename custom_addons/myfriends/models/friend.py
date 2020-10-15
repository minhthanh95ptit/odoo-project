from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class MyFriend(models.Model):
    _name = "my.friend"
    _description = "My friend model"

    name = fields.Char('Friend Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('Friend Description')
    age = fields.Integer('Friend Age', default=1)
    weight = fields.Float('Weight (kg)')
    dob = fields.Date('DOB', required=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default='male')

