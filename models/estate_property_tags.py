from odoo import fields,models

class Tags(models.Model):
	_name = "estate.property.tags"
	_description = "Property Tags"
	_rec_name = "property_tag"
	property_tag = fields.Char(required="True")
