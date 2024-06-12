def savings(gross_pay, tax_rate, expenses):
    after_tax_pay=(gross_pay-(gross_pay*tax_rate))//1
    return int(after_tax_pay-expenses)

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_material_consumed=num_jobs*job_consumption
    material_remaining=total_material-total_material_consumed
    return str(material_remaining)+material_units

def interest(principal, rate, periods):
    simple_interest=principal*rate*periods
    final_value=(principal+simple_interest)//1
    return int(final_value)