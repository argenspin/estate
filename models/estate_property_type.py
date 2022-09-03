from odoo import fields, models

class PType(models.Model):
	_name='estate.property.type'
	_description='Property Type'
	_rec_name='property_type'
	#property_id = fields.Char()
	property_type = fields.Char()

