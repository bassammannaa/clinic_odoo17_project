# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, tools
import logging
from odoo.exceptions import ValidationError
import datetime

logger = logging.getLogger(__name__)


class Physician(models.Model):
    _name = 'clinic.physician'
    _description = 'Physician'

    name = fields.Char(string="Name",
                       required=True,
                       store=True,
                       readonly=False,
                       copy=False,
                       help="Physician Name", )
    medical_license = fields.Char(string="Medical License",
                       required=False,
                       store=True,
                       readonly=False,
                       copy=False,
                       help="Medical License", )

    @api.model_create_multi
    def create(self, vals):
        try:
            obj = super(Physician, self).create(vals)
        except Exception as e:
            logger.exception("create Method")
            raise ValidationError(e)
        return obj

    def write(self, vals):
        try:
            obj = super(Physician, self).write(vals)
        except Exception as e:
            logger.exception("Write Method")
            raise ValidationError(e)
        return obj

    def unlink(self):
        try:
            return super(Physician, self).unlink()
        except Exception as e:
            logger.exception("unlink Method")
            raise ValidationError(e)
