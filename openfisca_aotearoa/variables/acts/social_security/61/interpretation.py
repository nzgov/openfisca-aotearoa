from openfisca_aotearoa.entities import Person
from openfisca_core.model_api import *

"""
http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM5468373
"""


class social_security__has_accomodation_costs(Variable):
    value_type = bool
    entity = Person
    label = u"Person has accommodation costs"
    definition_period = MONTH

    reference = """http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM362802
        accommodation costs, in relation to any person for any given period, means, -
        (a) in relation to premises rented by the person, the amount payable by the person for
            rent of the premises, excluding any service costs included in that rent and any arrears:
        (b) in relation to premises that are owned by the person, the total amount of all
            payments (including essential repairs and maintenance, local authority rates, and
            house insurance premiums, but excluding any service costs and any arrears) that -
        (i) subject to section 68A, are required to be made under any mortgage security for
            money advanced under that security to acquire the premises, or to repay advances
            similarly secured; or
        (ii) the chief executive is satisfied are reasonably required to be made:
        (c)in relation to a person who is a boarder or lodger in any premises, 62% of the amount
            paid for board or lodging (excluding any arrears):
        provided that, where a person is a joint tenant or owner in common of any premises with
            another person or other persons living in the premises, that applicant's accommodation
            costs shall be the share of the total accommodation costs of the premises that the
            chief executive is satisfied the person is paying
        """


class social_security__is_a_beneficiary(Variable):
    value_type = bool
    entity = Person
    label = "Person is a beneficiary"
    definition_period = MONTH
    reference = """beneficiary means any person who is being paid -
        (a) jobseeker support, sole parent support, a supported living payment, a youth payment, a young parent payment, or an emergency benefit; or
        (b) New Zealand superannuation or a veteran's pension
        """


class social_security__is_being_paid_jobseeker_benefit(Variable):
    value_type = bool
    entity = Person
    label = "Is being paid Jobseeker"
    definition_period = MONTH


class social_security__cash_assets(Variable):
    value_type = int
    entity = Person
    label = "cash assets"
    definition_period = MONTH
    reference = """cash assets-
        (a)means
        (i) money saved with a bank or other institution, money invested with a bank
            or other institution, or money banked with a bank or other institution:
        (ii) money invested in securities, bonds, or debentures, or advanced on mortgage:
        (iia) money withdrawn from a KiwiSaver scheme registered under subpart 2 of
            Part 4 of the Financial Markets Conduct Act 2013:
        (iii) money invested in shares in a partnership or limited liability company or
            other incorporated or unincorporated body; but
        (ab) does not include any contributions to, or any member's interest in, any
            KiwiSaver scheme that is registered under subpart 2 of Part 4 of the Financial
            Markets Conduct Act 2013; and
        (b) does not include any specified item or amount of cash assets, or cash assets
            of a specified kind, that is declared not to be cash assets for the purposes
            of this Act by regulations made under section 132
        """
