from odoo import models, fields

class Courrier(models.Model):
    _name = 'courrier.management'
    _description = 'Gestion des Courriers'
    reference = fields.Char(string="Référence", required=True)
    type = fields.Selection([('entrant', 'Courrier Entrant'), ('sortant', 'Courrier Sortant')],string="Type",)
    sender = fields.Char(string="Expéditeur")
    receiver = fields.Char(string="Destinataire")
    subject = fields.Char(string="Objet")
    date = fields.Date(string="Date", default=fields.Date.today)
    status = fields.Selection([('draft', 'Brouillon'),('sent', 'Envoyé'),('received', 'Reçu'),
                               ('archived', 'Archivé')],default='draft')
    description = fields.Text(string="Description")
