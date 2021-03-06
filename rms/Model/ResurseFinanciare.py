from camelot.admin.action import Action, ActionStep
from camelot.admin.not_editable_admin import not_editable_admin
from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToOne, Session
from sqlalchemy import Unicode, Date, Integer, Boolean, String

#todo dropdown pt categorii
class ResurseFinanciare(Entity):
    __tablename__ = 'resurse_financiare'

    tip = Column('type', String(10))
    valoare = Column(Integer, nullable=False, default=0)
    categorie = Column(Unicode(50))
    activitate = ManyToOne("Activitate")
    __mapper_args__ = {
        'polymorphic_on': tip,
    }

    def __unicode__(self):
        return self.categorie or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'ResurseFinanciare'
        verbose_name_plural = 'ResurseFinanciare'
        list_display = ['tip', 'valoare', 'categorie']
        form_display = ['tip', 'valoare', 'categorie']
        field_attributes = {'valoare': {'minimum': 0, 'maximum': 50000}
        }

    class Admin2(EntityAdmin):
        verbose_name = 'Resursa Financiara'
        verbose_name_plural = 'Resurse Financiare'
        list_display = ['valoare', 'tip', 'categorie']

    Admin2 = not_editable_admin(Admin2)


class Venituri(ResurseFinanciare):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'venituri'
    }

    class Admin(EntityAdmin):
        verbose_name = 'Venituri'
        verbose_name_plural = 'Venituri'
        list_display = ['tip', 'valoare', 'categorie']
        form_display = ['tip', 'valoare', 'categorie']


class Cheltuieli(ResurseFinanciare):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'Cheltuieli'
    }

    class Admin(EntityAdmin):
        verbose_name = 'Cheltuieli'
        verbose_name_plural = 'Cheltuieli'
        list_display = ['tip', 'valoare', 'categorie']
        form_display = ['tip', 'valoare', 'categorie']


