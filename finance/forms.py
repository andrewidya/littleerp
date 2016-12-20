from django import forms
from django.utils.translation import ugettext_lazy as _

from crm.models import SalesOrder


class FinanceStatementPeriodForm(forms.Form):
    MONTHS = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'Desember'),
    )

    month = forms.ChoiceField(
        label=_('Month'),
        choices=MONTHS,
    )
    year = forms.ChoiceField(
        label=_('Year'),
        choices=()
    )

    def __init__(self, *args, **kwargs):
        super(FinanceStatementPeriodForm, self).__init__(*args, **kwargs)
        self.fields['year'].choices = self._generate_year()
        month = self.fields['month'].choices
        if len(month) > 1:
            month.insert(0, ('', '---'))
            self.fields['month'].choices = month

    def _generate_year(self):
        sales_order = SalesOrder.objects.all()
        early_year = sales_order.dates('date_start', 'year', order='ASC')[0].year
        last_year = sales_order.dates('date_end', 'year', order='DESC')[0].year
        container = []
        counter = early_year
        while counter <= last_year:
            container.append((counter, counter))
            counter += 1
        if len(container) > 1:
            container.insert(0, ('', '---'))
        return container
