# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person


class family_scheme__qualifies_for_minimum_family_tax_credit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = u'Is a person is qualified as eligible for the minimum family tax credit'
    reference = "http://www.legislation.govt.nz/act/public/2007/0097/latest/DLM1518484.html"

    def formula(persons, period, parameters):
        base_qualifies = persons("family_scheme__base_qualifies", period)
        received_tested_benefit = persons('social_security__received_income_tested_benefit', period.this_year)
        received_parents_allowance = persons('veterans_support__received_parents_allowance', period)
        received_childrens_pension = persons('veterans_support__received_childrens_pension', period)

        return base_qualifies * not_(received_tested_benefit) * not_(received_parents_allowance) * not_(received_childrens_pension)
