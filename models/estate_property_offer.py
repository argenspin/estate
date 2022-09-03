from odoo import fields,models

class Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"
    price = fields.Float()
    status = fields.Selection(copy=False, selection=[('accepted','Accepted'),('refused','Refused')])
    partner_id = fields.Many2one('res.partner', required=True, string = "Partner ID")
    property_id = fields.Many2one('estate.property', required=True, string = "Property ID")