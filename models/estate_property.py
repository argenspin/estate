from odoo import fields, models

class TestModel(models.Model):
	_name = "estate.property"
	_description = "Test Model"
	name = fields.Char(required=True)
	description = fields.Text()
	postcode = fields.Char()
	date_availability = fields.Date()
	expected_price = fields.Float()
	selling_price = fields.Float()
	bedrooms = fields.Integer()
	living_area = fields.Integer()
	facades = fields.Integer()
	garage = fields.Boolean()
	garden = fields.Boolean()
	garder_area = fields.Integer()
	garden_orientation = fields.Selection(selection=[('north','North'),('south','South'),('west','West'),('east','East')])
	property_type = fields.Many2one('estate.property.type',string='Property Type')
	salesman = fields.Many2one('res.users',string='Salesman',default=lambda self: self.env.user)
	buyer = fields.Many2one('res.partner',string="Buyer")
	property_tag = fields.Many2many("estate.property.tags",string="Tags")
	offer_ids = fields.One2many('estate.property.offer','property_id',string='Offer Id')

