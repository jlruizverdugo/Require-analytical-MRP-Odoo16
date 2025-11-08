from odoo import models, api, _
from odoo.exceptions import ValidationError

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    @api.constrains('analytic_account_id')
    def _check_analytic_account(self):
        # Si el campo no existe en el _fields de este modelo,
        # no hacemos nada (así evitamos errores si tu base no tiene el campo).
        if 'analytic_account_id' not in self._fields:
            return
        for rec in self:
            if not rec.analytic_account_id:
                # Mensaje claro para el usuario
                name = rec.name or rec.display_name or _("(sin referencia)")
                raise ValidationError(
                    _("La orden de fabricación %s necesita una cuenta analítica. "
                      "Introduce una cuenta analítica antes de guardar/confirmar.") % name
                )
