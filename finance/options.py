from django.db import connection

class FinacialStatemntHelper(object):
    pk = 0
    code = ""
    name = ""
    sales_order_count = 0
    service_count = 0
    employee_count = 0
    expense = 0.0
    invoice_count = 0
    invoice_sum = 0.0

def get_financial_statement():
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT
            crm_customer.id AS id,
            crm_customer.code AS code,
            crm_customer.name AS name,
            COUNT(DISTINCT crm_salesorder.number) AS sales_order_count,
            COUNT(DISTINCT crm_salesorderdetail.quantity) AS service_count,
            COUNT(DISTINCT hrm_employeecontract.id) AS employee_count,
            SUM(DISTINCT operational_payroll.total) AS expense,
            COUNT(DISTINCT finance_invoice.id) AS invoice_count,
            SUM(DISTINCT finance_invoicedetail.amount) AS invoice_sum
        FROM crm_customer
        JOIN crm_salesorder ON crm_salesorder.customer_id = crm_customer.id
        JOIN crm_salesorderdetail ON crm_salesorderdetail.sales_order_id = crm_salesorder.id
        JOIN hrm_employeecontract ON hrm_employeecontract.service_related_id = crm_salesorderdetail.id
        JOIN operational_payroll ON operational_payroll.contract_id = hrm_employeecontract.id
        JOIN finance_invoice ON finance_invoice.sales_order_id = crm_salesorder.id
        JOIN finance_invoicedetail ON finance_invoicedetail.invoice_id = finance_invoice.id
        """
    )
    result_list = []
    for row in cursor.fetchall():
        obj = FinacialStatemntHelper()
        obj.pk = row[0]
        obj.code = row[1]
        obj.name = row[2]
        obj.sales_order_count = row[3]
        obj.service_count = row[4]
        obj.employee_count = row[5]
        obj.expense = row[6]
        obj.invoice_count = row[7]
        obj.invoice_sum = row[8]
        result_list.append(obj)

    print(result_list)
    return result_list
