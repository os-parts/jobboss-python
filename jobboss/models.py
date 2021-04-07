# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = IS_TEST` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from jobboss.settings import IS_TEST
from django.db import models
from jobboss.autonumber import AutoNumberMixin, AutoIncrementColumn, \
    AutoNumberColumn


class Account(models.Model):
    account = models.CharField(db_column='Account', primary_key=True, max_length=10)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rollup_account = models.CharField(db_column='Rollup_Account', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    section_name = models.CharField(db_column='Section_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    qb_id = models.CharField(db_column='QB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Account'


class AdditionalCharge(models.Model):
    additional_chargekey = models.AutoField(db_column='Additional_ChargeKey', primary_key=True)  # Field name made lowercase.
    additional_charge = models.IntegerField(db_column='Additional_Charge', unique=True, blank=True, null=True)  # Field name made lowercase.
    job = models.ForeignKey('Job', models.DO_NOTHING, db_column='Job', blank=True, null=True)  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    invoice = models.CharField(db_column='Invoice', max_length=8, blank=True, null=True)  # Field name made lowercase.
    so_detail = models.IntegerField(db_column='SO_Detail', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=25, blank=True, null=True)  # Field name made lowercase.
    est_price = models.DecimalField(db_column='Est_Price', max_digits=19, decimal_places=4)  # Field name made lowercase.
    act_price = models.DecimalField(db_column='Act_Price', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    job_revenue = models.BooleanField(db_column='Job_Revenue')  # Field name made lowercase.
    commissionable = models.BooleanField(db_column='Commssionable')  # Field name made lowercase.
    processed = models.BooleanField(db_column='Processed')  # Field name made lowercase.
    taxable = models.BooleanField(db_column='Taxable')  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    charge_type = models.SmallIntegerField(db_column='Charge_Type', blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    approved = models.NullBooleanField(db_column='Approved')  # Field name made lowercase.
    recurring = models.NullBooleanField(db_column='Recurring')  # Field name made lowercase.
    delivery = models.IntegerField(db_column='Delivery', blank=True, null=True)  # Field name made lowercase.
    qb_id = models.CharField(db_column='QB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    commissionincluded = models.BooleanField(db_column='CommissionIncluded')  # New v12

    class Meta:
        managed = IS_TEST
        db_table = 'Additional_Charge'


class Address(AutoNumberMixin, models.Model):
    auto_number_attrs = [AutoIncrementColumn('address')]

    addresskey = models.AutoField(db_column='AddressKey', primary_key=True)  # Field name made lowercase.
    address = models.IntegerField(db_column='Address', unique=True, blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey('Customer', models.DO_NOTHING, db_column='Customer', blank=True, null=True)  # Field name made lowercase.
    vendor = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=5)  # Field name made lowercase.
    ship_via = models.CharField(db_column='Ship_Via', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ship_to_id = models.CharField(db_column='Ship_To_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    line1 = models.CharField(db_column='Line1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    line2 = models.CharField(db_column='Line2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    billable = models.BooleanField(db_column='Billable')  # Field name made lowercase.
    shippable = models.BooleanField(db_column='Shippable')  # Field name made lowercase.
    cell_phone = models.CharField(db_column='Cell_Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Address'


class Addresscountry(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'AddressCountry'


class Addressstate(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    statecode = models.CharField(db_column='StateCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'AddressState'


class Attachment(AutoNumberMixin, models.Model):
    auto_number_attrs = [AutoIncrementColumn('attachment')]

    attachmentkey = models.AutoField(db_column='AttachmentKey', primary_key=True)  # Field name made lowercase.
    attachment = models.IntegerField(db_column='Attachment', unique=True, blank=True, null=True)  # Field name made lowercase.
    owner_type = models.CharField(db_column='Owner_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    owner_id = models.CharField(db_column='Owner_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    attach_path = models.TextField(db_column='Attach_Path', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    description = models.CharField(db_column='Description', max_length=254, blank=True, null=True)  # Field name made lowercase.
    print_attachment = models.BooleanField(db_column='Print_Attachment')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    attach_type = models.CharField(db_column='Attach_Type', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Attachment'


class AutoNumber(models.Model):
    type = models.CharField(db_column='Type', primary_key=True, max_length=15)  # Field name made lowercase.
    system_generated = models.BooleanField(db_column='System_Generated')  # Field name made lowercase.
    last_nbr = models.CharField(db_column='Last_Nbr', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Auto_Number'


class BarStockCutoff(models.Model):
    bar_stock_cutoffkey = models.AutoField(db_column='Bar_Stock_CutoffKey', primary_key=True)  # Field name made lowercase.
    bar_stock_cutoff = models.IntegerField(db_column='Bar_Stock_Cutoff', unique=True, blank=True, null=True)  # Field name made lowercase.
    to_diameter = models.FloatField(db_column='To_Diameter')  # Field name made lowercase.
    cut_off = models.FloatField(db_column='Cut_Off')  # Field name made lowercase.
    std_bar_end = models.FloatField(db_column='Std_Bar_End', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Bar_Stock_Cutoff'


class BillOfJobs(models.Model):
    parent_job = models.ForeignKey('Job', models.DO_NOTHING, db_column='Parent_Job', related_name='bill_child')  # Field name made lowercase.
    component_job = models.ForeignKey('Job', models.DO_NOTHING, db_column='Component_Job', related_name='bill_parent')  # Field name made lowercase.
    job_operation = models.IntegerField(db_column='Job_Operation', blank=True, null=True)  # Field name made lowercase.
    relationship_type = models.CharField(db_column='Relationship_Type', max_length=9)  # Field name made lowercase.
    relationship_qty = models.IntegerField(db_column='Relationship_Qty', blank=True, null=True)  # Field name made lowercase.
    manual_link = models.BooleanField(db_column='Manual_Link')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    root_job = models.CharField(db_column='Root_Job', max_length=10, blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    job_operation_oid = models.CharField(db_column='Job_Operation_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    root_job_oid = models.CharField(db_column='Root_Job_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    parent_job_oid = models.CharField(db_column='Parent_Job_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    component_job_oid = models.CharField(db_column='Component_Job_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Bill_Of_Jobs'
        unique_together = (('parent_job', 'component_job'),)


class BillOfQuotes(models.Model):
    parent_quote = models.ForeignKey('Quote', models.DO_NOTHING, db_column='Parent_Quote', related_name='bill_child')  # Field name made lowercase.
    component_quote = models.ForeignKey('Quote', models.DO_NOTHING, db_column='Component_Quote', related_name='bill_parent')  # Field name made lowercase.
    quote_operation = models.IntegerField(db_column='Quote_Operation', blank=True, null=True)  # Field name made lowercase.
    relationship_type = models.CharField(db_column='Relationship_Type', max_length=9)  # Field name made lowercase.
    relationship_qty = models.IntegerField(db_column='Relationship_Qty', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Bill_Of_Quotes'
        unique_together = (('parent_quote', 'component_quote'),)


class Contact(AutoNumberMixin, models.Model):
    auto_number_attrs = [AutoIncrementColumn('contact')]

    contactkey = models.AutoField(db_column='ContactKey', primary_key=True)  # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact', unique=True, blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address = models.IntegerField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    contact_name = models.CharField(db_column='Contact_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone_ext = models.CharField(db_column='Phone_Ext', max_length=8, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    cell_phone = models.CharField(db_column='Cell_Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Contact'


class Cost(models.Model):
    costkey = models.AutoField(db_column='CostKey', primary_key=True)  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', unique=True, blank=True, null=True)  # Field name made lowercase.
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='Account')  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=50, blank=True, null=True)  # Field name made lowercase.
    budget_amt = models.DecimalField(db_column='Budget_Amt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mtd_amt = models.DecimalField(db_column='MTD_Amt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    per_ending_amt_5x = models.DecimalField(db_column='Per_Ending_Amt_5x', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Cost'


class CurrencyDef(models.Model):
    currency_defkey = models.AutoField(db_column='Currency_DefKey', primary_key=True)  # Field name made lowercase.
    currency_def = models.IntegerField(db_column='Currency_Def', unique=True, blank=True, null=True)  # Field name made lowercase.
    currency_name = models.CharField(db_column='Currency_Name', unique=True, max_length=10)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    base_currency = models.IntegerField(db_column='Base_Currency', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.
    emu_member = models.BooleanField(db_column='EMU_Member')  # Field name made lowercase.
    sig_digits = models.SmallIntegerField(db_column='Sig_Digits')  # Field name made lowercase.
    dec_symbol = models.CharField(db_column='Dec_Symbol', max_length=1, blank=True, null=True)  # Field name made lowercase.
    thousand_separator = models.CharField(db_column='Thousand_Separator', max_length=1, blank=True, null=True)  # Field name made lowercase.
    neg_format = models.SmallIntegerField(db_column='Neg_Format', blank=True, null=True)  # Field name made lowercase.
    pos_format = models.SmallIntegerField(db_column='Pos_Format', blank=True, null=True)  # Field name made lowercase.
    locale = models.IntegerField(db_column='Locale', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Currency_Def'


class CurrencyRate(models.Model):
    currency_ratekey = models.AutoField(db_column='Currency_RateKey', primary_key=True)  # Field name made lowercase.
    currency_rate = models.IntegerField(db_column='Currency_Rate', unique=True, blank=True, null=True)  # Field name made lowercase.
    source_currency = models.IntegerField(db_column='Source_Currency')  # Field name made lowercase.
    target_currency = models.IntegerField(db_column='Target_Currency')  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.
    effective_date = models.DateTimeField(db_column='Effective_Date', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Currency_Rate'


class Customer(models.Model):
    customer = models.CharField(db_column='Customer', primary_key=True, max_length=10)  # Field name made lowercase.
    sales_rep = models.CharField(db_column='Sales_Rep', max_length=6, blank=True, null=True)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='Terms', max_length=15, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ship_via = models.CharField(db_column='Ship_Via', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ship_lead_days = models.SmallIntegerField(db_column='Ship_Lead_Days', blank=True, null=True)  # Field name made lowercase.
    print_statement = models.BooleanField(db_column='Print_Statement')  # Field name made lowercase.
    credit_limit = models.DecimalField(db_column='Credit_Limit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    curr_balance = models.DecimalField(db_column='Curr_Balance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    customer_since = models.DateTimeField(db_column='Customer_Since', blank=True, null=True)  # Field name made lowercase.
    accept_bo = models.BooleanField(db_column='Accept_BO')  # Field name made lowercase.
    pricing_level = models.CharField(db_column='Pricing_Level', max_length=15, blank=True, null=True)  # Field name made lowercase.
    partner = models.CharField(db_column='Partner', max_length=16, blank=True, null=True)  # Field name made lowercase.
    currency_def = models.IntegerField(db_column='Currency_Def', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    tax_id = models.CharField(db_column='Tax_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    acct_mgr = models.CharField(db_column='Acct_Mgr', max_length=6, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    qb_id = models.CharField(db_column='QB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pst_id = models.CharField(db_column='PST_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    send_report_by_email = models.BooleanField(db_column='Send_Report_By_Email')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Customer'


class CustomerPart(models.Model):
    customer_partkey = models.AutoField(db_column='Customer_PartKey', primary_key=True)  # Field name made lowercase.
    customer_part = models.IntegerField(db_column='Customer_Part', unique=True, blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    material = models.ForeignKey('Material', models.DO_NOTHING, db_column='Material')  # Field name made lowercase.
    part_number = models.CharField(db_column='Part_Number', max_length=30)  # Field name made lowercase.
    rev = models.CharField(db_column='Rev', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ext_description = models.TextField(db_column='Ext_Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sell_price = models.FloatField(db_column='Sell_Price')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    customer_type = models.CharField(db_column='Customer_Type', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Customer_Part'


class Delivery(AutoNumberMixin, models.Model):
    auto_number_attrs = [AutoIncrementColumn('delivery')]

    deliverykey = models.AutoField(db_column='DeliveryKey', primary_key=True)  # Field name made lowercase.
    delivery = models.IntegerField(db_column='Delivery', unique=True, blank=True, null=True)  # Field name made lowercase.
    packlist = models.CharField(db_column='Packlist', max_length=8, blank=True, null=True)  # Field name made lowercase.
    job = models.ForeignKey('Job', models.DO_NOTHING, db_column='Job', blank=True, null=True)  # Field name made lowercase.
    invoice = models.CharField(db_column='Invoice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crmemo = models.CharField(db_column='CrMemo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invoice_line = models.CharField(db_column='Invoice_Line', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crmemo_line = models.CharField(db_column='CrMemo_Line', max_length=50, blank=True, null=True)  # Field name made lowercase.
    so_detail = models.IntegerField(db_column='SO_Detail', blank=True, null=True)  # Field name made lowercase.
    requested_date = models.DateTimeField(db_column='Requested_Date', blank=True, null=True)  # Field name made lowercase.
    promised_date = models.DateTimeField(db_column='Promised_Date')  # Field name made lowercase.
    shipped_date = models.DateTimeField(db_column='Shipped_Date', blank=True, null=True)  # Field name made lowercase.
    invoice_date = models.DateTimeField(db_column='Invoice_Date', blank=True, null=True)  # Field name made lowercase.
    returned_date = models.DateTimeField(db_column='Returned_Date', blank=True, null=True)  # Field name made lowercase.
    crmemo_date = models.DateTimeField(db_column='CrMemo_Date', blank=True, null=True)  # Field name made lowercase.
    promised_quantity = models.IntegerField(db_column='Promised_Quantity')  # Field name made lowercase.
    shipped_quantity = models.IntegerField(db_column='Shipped_Quantity', blank=True, null=True)  # Field name made lowercase.
    remaining_quantity = models.IntegerField(db_column='Remaining_Quantity', blank=True, null=True)  # Field name made lowercase.
    returned_quantity = models.IntegerField(db_column='Returned_Quantity', blank=True, null=True)  # Field name made lowercase.
    ncp_quantity = models.IntegerField(db_column='NCP_Quantity', blank=True, null=True)  # Field name made lowercase.
    return_document = models.CharField(db_column='Return_Document', max_length=15, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    job_oid = models.CharField(db_column='Job_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_Updated_By', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Delivery'


class Employee(models.Model):
    employee = models.CharField(db_column='Employee', primary_key=True, max_length=6)  # Field name made lowercase.
    work_center = models.ForeignKey('WorkCenter', models.DO_NOTHING, db_column='Work_Center', blank=True, null=True)  # Field name made lowercase.
    address = models.IntegerField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    middle_initial = models.CharField(db_column='Middle_Initial', max_length=1, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', max_length=11, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=6)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=1)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    hourly_rate = models.DecimalField(db_column='Hourly_Rate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    commission_pct = models.FloatField(db_column='Commission_Pct', blank=True, null=True)  # Field name made lowercase.
    shift_start = models.DateTimeField(db_column='Shift_Start', blank=True, null=True)  # Field name made lowercase.
    shift_end = models.DateTimeField(db_column='Shift_End', blank=True, null=True)  # Field name made lowercase.
    hire_date = models.DateTimeField(db_column='Hire_Date', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    shift = models.CharField(db_column='Shift', max_length=36, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=15, blank=True, null=True)  # Field name made lowercase.
    supervisor = models.CharField(db_column='Supervisor', max_length=6, blank=True, null=True)  # Field name made lowercase.
    default_tran_limit = models.SmallIntegerField(db_column='Default_Tran_Limit', blank=True, null=True)  # Field name made lowercase.
    begin_tran_prompt = models.CharField(db_column='Begin_Tran_Prompt', max_length=15, blank=True, null=True)  # Field name made lowercase.
    repeat_tran_prompt = models.CharField(db_column='Repeat_Tran_Prompt', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tran_repeater = models.NullBooleanField(db_column='Tran_Repeater')  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Employee'


class FiscalPeriod(models.Model):
    fiscal_period = models.CharField(db_column='Fiscal_Period', primary_key=True, max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    per_nbr = models.SmallIntegerField(db_column='Per_Nbr')  # Field name made lowercase.
    fiscal_year = models.CharField(db_column='Fiscal_Year', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Fiscal_Period'


class FiscalYear(models.Model):
    fiscal_year = models.CharField(db_column='Fiscal_Year', primary_key=True, max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nbr_periods = models.SmallIntegerField(db_column='Nbr_Periods')  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Fiscal_Year'


class GlEntry(models.Model):
    gl_entry = models.CharField(db_column='GL_Entry', primary_key=True, max_length=50)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=15, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    entry_type = models.SmallIntegerField(db_column='Entry_Type')  # Field name made lowercase.
    transaction_date = models.DateTimeField(db_column='Transaction_Date', blank=True, null=True)  # Field name made lowercase.
    posted = models.BooleanField(db_column='Posted')  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=15, blank=True, null=True)  # Field name made lowercase.
    statement_date = models.DateTimeField(db_column='Statement_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'GL_Entry'


class GlobalPref(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    pref_type = models.CharField(db_column='Pref_Type', max_length=20)  # Field name made lowercase.
    data_type = models.CharField(db_column='Data_Type', max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=20)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Global_Pref'


class Holiday(models.Model):
    holiday = models.CharField(db_column='Holiday', primary_key=True, max_length=50)  # Field name made lowercase.
    holidayname = models.CharField(db_column='HolidayName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shift = models.CharField(db_column='Shift', max_length=36, blank=True, null=True)  # Field name made lowercase.
    holidaystart = models.DateTimeField(db_column='HolidayStart', blank=True, null=True)  # Field name made lowercase.
    holidayend = models.DateTimeField(db_column='HolidayEnd', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Holiday'


class Identitylog(models.Model):
    spid = models.IntegerField(db_column='Spid', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    keyvalue = models.IntegerField(db_column='KeyValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'IdentityLog'


class InvoiceDetail(models.Model):
    invoice_detailkey = models.AutoField(db_column='Invoice_DetailKey', primary_key=True)  # Field name made lowercase.
    invoice_detail = models.IntegerField(db_column='Invoice_Detail', unique=True, blank=True, null=True)  # Field name made lowercase.
    document = models.ForeignKey('InvoiceHeader', models.DO_NOTHING, db_column='Document')  # Field name made lowercase.
    document_line = models.SmallIntegerField(db_column='Document_Line', blank=True, null=True)  # Field name made lowercase.
    packlist = models.CharField(db_column='Packlist', max_length=8, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=10, blank=True, null=True)  # Field name made lowercase.
    so_detail = models.IntegerField(db_column='SO_Detail', blank=True, null=True)  # Field name made lowercase.
    material_trans = models.IntegerField(db_column='Material_Trans', blank=True, null=True)  # Field name made lowercase.
    ar_code = models.CharField(db_column='AR_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ship_date = models.DateTimeField(db_column='Ship_Date', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unit_price = models.FloatField(db_column='Unit_Price', blank=True, null=True)  # Field name made lowercase.
    price_uofm = models.CharField(db_column='Price_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sales_rep = models.CharField(db_column='Sales_Rep', max_length=8, blank=True, null=True)  # Field name made lowercase.
    commission_pct = models.FloatField(db_column='Commission_Pct', blank=True, null=True)  # Field name made lowercase.
    taxable = models.BooleanField(db_column='Taxable')  # Field name made lowercase.
    commissionable = models.BooleanField(db_column='Commissionable')  # Field name made lowercase.
    discountable = models.BooleanField(db_column='Discountable')  # Field name made lowercase.
    backorder_qty = models.FloatField(db_column='Backorder_Qty')  # Field name made lowercase.
    order_qty = models.FloatField(db_column='Order_Qty')  # Field name made lowercase.
    job_revenue = models.BooleanField(db_column='Job_Revenue')  # Field name made lowercase.
    prepay = models.BooleanField(db_column='Prepay')  # Field name made lowercase.
    prepaid_amt = models.DecimalField(db_column='Prepaid_Amt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prepaid_code = models.CharField(db_column='Prepaid_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=10, blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    part_number = models.CharField(db_column='Part_Number', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ext_description = models.TextField(db_column='Ext_Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    part_description = models.CharField(db_column='Part_Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    revision = models.CharField(db_column='Revision', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customer_po = models.CharField(db_column='Customer_PO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    poline = models.CharField(db_column='POLine', max_length=10, blank=True, null=True)  # Field name made lowercase.
    source_type = models.SmallIntegerField(db_column='Source_Type', blank=True, null=True)  # Field name made lowercase.
    additional_charge = models.IntegerField(db_column='Additional_Charge', blank=True, null=True)  # Field name made lowercase.
    price_coefficient = models.FloatField(db_column='Price_Coefficient')  # Field name made lowercase.
    order_unit = models.CharField(db_column='Order_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    price_unit_conv = models.FloatField(db_column='Price_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    prog_payment = models.NullBooleanField(db_column='Prog_Payment')  # Field name made lowercase.
    prepaid_tax_amount = models.DecimalField(db_column='Prepaid_Tax_Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    commissionincluded = models.BooleanField(db_column='CommissionIncluded')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Invoice_Detail'


class InvoiceHeader(AutoNumberMixin, models.Model):
    auto_number_attrs = [AutoNumberColumn('document', 'Invoice')]

    document = models.CharField(db_column='Document', primary_key=True, max_length=8)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer')  # Field name made lowercase.
    ship_to = models.IntegerField(db_column='Ship_To', blank=True, null=True)  # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    ship_via = models.CharField(db_column='Ship_Via', max_length=15, blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='Terms', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    document_date = models.DateTimeField(db_column='Document_Date', blank=True, null=True)  # Field name made lowercase.
    ar_description = models.CharField(db_column='AR_Description', max_length=25, blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    orig_invoice_amt = models.DecimalField(db_column='Orig_Invoice_Amt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    open_invoice_amt = models.DecimalField(db_column='Open_Invoice_Amt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    open_invoice_amt_curr_per = models.DecimalField(db_column='Open_Invoice_Amt_Curr_Per', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=1)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=3)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taxable_amt = models.DecimalField(db_column='Taxable_Amt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sales_tax_rate1 = models.FloatField(db_column='Sales_Tax_Rate1', blank=True, null=True)  # Field name made lowercase.
    sales_tax_rate2 = models.FloatField(db_column='Sales_Tax_Rate2', blank=True, null=True)  # Field name made lowercase.
    sales_tax_rate3 = models.FloatField(db_column='Sales_Tax_Rate3', blank=True, null=True)  # Field name made lowercase.
    sales_tax_rate4 = models.FloatField(db_column='Sales_Tax_Rate4', blank=True, null=True)  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate')  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.BooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    print_date = models.DateTimeField(db_column='Print_Date', blank=True, null=True)  # Field name made lowercase.
    edi = models.BooleanField(db_column='EDI')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    bill_to = models.IntegerField(db_column='Bill_To', blank=True, null=True)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    invoiced_by = models.CharField(db_column='Invoiced_By', max_length=30, blank=True, null=True)  # Field name made lowercase.
    journal_entry = models.CharField(db_column='Journal_Entry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paid_date = models.DateTimeField(db_column='Paid_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Invoice_Header'


class InvoiceReceipt(models.Model):
    invoice = models.ForeignKey(InvoiceHeader, models.DO_NOTHING, db_column='Invoice')  # Field name made lowercase.
    receipt = models.ForeignKey('Receipt', models.DO_NOTHING, db_column='Receipt')  # Field name made lowercase.
    amount_applied = models.DecimalField(db_column='Amount_Applied', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    invoice_receipt = models.CharField(db_column='Invoice_Receipt', primary_key=True, max_length=50)  # Field name made lowercase.
    application_type = models.SmallIntegerField(db_column='Application_Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Invoice_Receipt'


class Job(AutoNumberMixin, models.Model):
    auto_number_attrs = [AutoNumberColumn('job', 'Job')]

    job = models.CharField(db_column='Job', primary_key=True, max_length=10)  # Field name made lowercase.
    sales_rep = models.ForeignKey(Employee, models.DO_NOTHING, db_column='Sales_Rep', blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer', blank=True, null=True)  # Field name made lowercase.
    ship_to = models.IntegerField(db_column='Ship_To', blank=True, null=True)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    quote = models.CharField(db_column='Quote', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    ship_via = models.CharField(db_column='Ship_Via', max_length=15, blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='Terms', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    top_lvl_job = models.CharField(db_column='Top_Lvl_Job', max_length=10, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=8)  # Field name made lowercase.
    order_date = models.DateTimeField(db_column='Order_Date')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    status_date = models.DateTimeField(db_column='Status_Date')  # Field name made lowercase.
    part_number = models.CharField(db_column='Part_Number', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rev = models.CharField(db_column='Rev', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ext_description = models.TextField(db_column='Ext_Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drawing = models.CharField(db_column='Drawing', max_length=30, blank=True, null=True)  # Field name made lowercase.
    build_to_stock = models.BooleanField(db_column='Build_To_Stock')  # Field name made lowercase.
    order_quantity = models.IntegerField(db_column='Order_Quantity')  # Field name made lowercase.
    extra_quantity = models.IntegerField(db_column='Extra_Quantity', blank=True, null=True)  # Field name made lowercase.
    pick_quantity = models.IntegerField(db_column='Pick_Quantity', blank=True, null=True)  # Field name made lowercase.
    make_quantity = models.IntegerField(db_column='Make_Quantity')  # Field name made lowercase.
    split_quantity = models.IntegerField(db_column='Split_Quantity', blank=True, null=True)  # Field name made lowercase.
    completed_quantity = models.IntegerField(db_column='Completed_Quantity', blank=True, null=True)  # Field name made lowercase.
    shipped_quantity = models.IntegerField(db_column='Shipped_Quantity', blank=True, null=True)  # Field name made lowercase.
    fg_transfer_qty = models.IntegerField(db_column='FG_Transfer_Qty', blank=True, null=True)  # Field name made lowercase.
    returned_quantity = models.IntegerField(db_column='Returned_Quantity', blank=True, null=True)  # Field name made lowercase.
    in_production_quantity = models.IntegerField(db_column='In_Production_Quantity')  # Field name made lowercase.
    assembly_level = models.SmallIntegerField(db_column='Assembly_Level', blank=True, null=True)  # Field name made lowercase.
    certs_required = models.BooleanField(db_column='Certs_Required')  # Field name made lowercase.
    time_and_materials = models.BooleanField(db_column='Time_And_Materials')  # Field name made lowercase.
    open_operations = models.SmallIntegerField(db_column='Open_Operations', blank=True, null=True)  # Field name made lowercase.
    scrap_pct = models.FloatField(db_column='Scrap_Pct')  # Field name made lowercase.
    est_scrap_qty = models.IntegerField(db_column='Est_Scrap_Qty', blank=True, null=True)  # Field name made lowercase.
    est_rem_hrs = models.FloatField(db_column='Est_Rem_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_total_hrs = models.FloatField(db_column='Est_Total_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_labor = models.DecimalField(db_column='Est_Labor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_material = models.DecimalField(db_column='Est_Material', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_service = models.DecimalField(db_column='Est_Service', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_labor_burden = models.DecimalField(db_column='Est_Labor_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_machine_burden = models.DecimalField(db_column='Est_Machine_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_ga_burden = models.DecimalField(db_column='Est_GA_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_revenue = models.DecimalField(db_column='Act_Revenue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_scrap_quantity = models.IntegerField(db_column='Act_Scrap_Quantity', blank=True, null=True)  # Field name made lowercase.
    act_total_hrs = models.FloatField(db_column='Act_Total_Hrs', blank=True, null=True)  # Field name made lowercase.
    act_labor = models.DecimalField(db_column='Act_Labor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_material = models.DecimalField(db_column='Act_Material', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_service = models.DecimalField(db_column='Act_Service', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_labor_burden = models.DecimalField(db_column='Act_Labor_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_machine_burden = models.DecimalField(db_column='Act_Machine_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_ga_burden = models.DecimalField(db_column='Act_GA_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    unit_price = models.FloatField(db_column='Unit_Price', blank=True, null=True)  # Field name made lowercase.
    total_price = models.DecimalField(db_column='Total_Price', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    price_uofm = models.CharField(db_column='Price_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate')  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.BooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    commission_pct = models.FloatField(db_column='Commission_Pct', blank=True, null=True)  # Field name made lowercase.
    customer_po = models.CharField(db_column='Customer_PO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customer_po_ln = models.CharField(db_column='Customer_PO_LN', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sched_end = models.DateTimeField(db_column='Sched_End', blank=True, null=True)  # Field name made lowercase.
    sched_start = models.DateTimeField(db_column='Sched_Start', blank=True, null=True)  # Field name made lowercase.
    quantity_per = models.FloatField(db_column='Quantity_Per', blank=True, null=True)  # Field name made lowercase.
    profit_pct = models.FloatField(db_column='Profit_Pct', blank=True, null=True)  # Field name made lowercase.
    labor_markup_pct = models.FloatField(db_column='Labor_Markup_Pct')  # Field name made lowercase.
    mat_markup_pct = models.FloatField(db_column='Mat_Markup_Pct')  # Field name made lowercase.
    serv_markup_pct = models.FloatField(db_column='Serv_Markup_Pct')  # Field name made lowercase.
    labor_burden_markup_pct = models.FloatField(db_column='Labor_Burden_Markup_Pct')  # Field name made lowercase.
    machine_burden_markup_pct = models.FloatField(db_column='Machine_Burden_Markup_Pct')  # Field name made lowercase.
    ga_burden_markup_pct = models.FloatField(db_column='GA_Burden_Markup_Pct')  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    profit_markup = models.CharField(db_column='Profit_Markup', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prepaid_amt = models.DecimalField(db_column='Prepaid_Amt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    split_to_job = models.BooleanField(db_column='Split_To_Job')  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    order_unit = models.CharField(db_column='Order_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    price_unit_conv = models.FloatField(db_column='Price_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    holder_id = models.CharField(db_column='Holder_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=20, blank=True, null=True)  # Field name made lowercase.
    order_taken_by = models.CharField(db_column='Order_Taken_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    plan_modified = models.NullBooleanField(db_column='Plan_Modified')  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    released_date = models.DateTimeField(db_column='Released_Date', blank=True, null=True)  # Field name made lowercase.
    prepaid_tax_amount = models.DecimalField(db_column='Prepaid_Tax_Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prepaid_trade_amt = models.DecimalField(db_column='Prepaid_Trade_Amt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_Updated_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    commissionincluded = models.BooleanField(db_column='CommissionIncluded')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Job'


class JobException(models.Model):
    job_exception = models.AutoField(db_column='Job_Exception', primary_key=True)  # Field name made lowercase.
    requirement = models.CharField(db_column='Requirement', max_length=30, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', max_length=36)  # Field name made lowercase.
    job_operation_oid = models.CharField(db_column='Job_Operation_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='Created_Time', blank=True, null=True)  # Field name made lowercase.
    material_req_oid = models.CharField(db_column='Material_Req_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    exception_type = models.IntegerField(db_column='Exception_Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Job_Exception'


class JobOperation(models.Model):
    job_operationkey = models.AutoField(db_column='Job_OperationKey', primary_key=True)  # Field name made lowercase.
    job_operation = models.IntegerField(db_column='Job_Operation', unique=True, blank=True, null=True)  # Field name made lowercase.
    vendor = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    work_center = models.ForeignKey('WorkCenter', models.DO_NOTHING, db_column='Work_Center', blank=True, null=True)  # Field name made lowercase.
    job = models.ForeignKey(Job, models.DO_NOTHING, db_column='Job')  # Field name made lowercase.
    operation_service = models.CharField(db_column='Operation_Service', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wc_vendor = models.CharField(db_column='WC_Vendor', max_length=10)  # Field name made lowercase.
    inside_oper = models.BooleanField(db_column='Inside_Oper')  # Field name made lowercase.
    sequence = models.SmallIntegerField(db_column='Sequence')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=25, blank=True, null=True)  # Field name made lowercase.
    priority = models.FloatField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    run_method = models.CharField(db_column='Run_Method', max_length=8, blank=True, null=True)  # Field name made lowercase.
    run = models.FloatField(db_column='Run', blank=True, null=True)  # Field name made lowercase.
    est_run_per_part = models.FloatField(db_column='Est_Run_Per_Part', blank=True, null=True)  # Field name made lowercase.
    efficiency_pct = models.FloatField(db_column='Efficiency_Pct', blank=True, null=True)  # Field name made lowercase.
    attended_pct = models.FloatField(db_column='Attended_Pct', blank=True, null=True)  # Field name made lowercase.
    queue_hrs = models.FloatField(db_column='Queue_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_total_hrs = models.FloatField(db_column='Est_Total_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_setup_hrs = models.FloatField(db_column='Est_Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_run_hrs = models.FloatField(db_column='Est_Run_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_setup_labor = models.DecimalField(db_column='Est_Setup_Labor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_run_labor = models.DecimalField(db_column='Est_Run_Labor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_labor_burden = models.DecimalField(db_column='Est_Labor_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_machine_burden = models.DecimalField(db_column='Est_Machine_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_ga_burden = models.DecimalField(db_column='Est_GA_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_required_qty = models.IntegerField(db_column='Est_Required_Qty', blank=True, null=True)  # Field name made lowercase.
    est_unit_cost = models.FloatField(db_column='Est_Unit_Cost')  # Field name made lowercase.
    est_addl_cost = models.DecimalField(db_column='Est_Addl_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_total_cost = models.DecimalField(db_column='Est_Total_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    deferred_qty = models.FloatField(db_column='Deferred_Qty')  # Field name made lowercase.
    act_setup_hrs = models.FloatField(db_column='Act_Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    act_run_hrs = models.FloatField(db_column='Act_Run_Hrs', blank=True, null=True)  # Field name made lowercase.
    act_run_qty = models.IntegerField(db_column='Act_Run_Qty', blank=True, null=True)  # Field name made lowercase.
    act_scrap_qty = models.IntegerField(db_column='Act_Scrap_Qty', blank=True, null=True)  # Field name made lowercase.
    act_setup_labor = models.DecimalField(db_column='Act_Setup_Labor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_run_labor = models.DecimalField(db_column='Act_Run_Labor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_labor_burden = models.DecimalField(db_column='Act_Labor_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_machine_burden = models.DecimalField(db_column='Act_Machine_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_ga_burden = models.DecimalField(db_column='Act_GA_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_unit_cost = models.FloatField(db_column='Act_Unit_Cost')  # Field name made lowercase.
    act_addl_cost = models.DecimalField(db_column='Act_Addl_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    addl_cost_desc = models.CharField(db_column='Addl_Cost_Desc', max_length=15, blank=True, null=True)  # Field name made lowercase.
    act_total_cost = models.DecimalField(db_column='Act_Total_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    setup_pct_complete = models.FloatField(db_column='Setup_Pct_Complete', blank=True, null=True)  # Field name made lowercase.
    run_pct_complete = models.FloatField(db_column='Run_Pct_Complete', blank=True, null=True)  # Field name made lowercase.
    rem_run_hrs = models.FloatField(db_column='Rem_Run_Hrs', blank=True, null=True)  # Field name made lowercase.
    rem_setup_hrs = models.FloatField(db_column='Rem_Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    rem_total_hrs = models.FloatField(db_column='Rem_Total_Hrs', blank=True, null=True)  # Field name made lowercase.
    overlap_method = models.CharField(db_column='Overlap_Method', max_length=3, blank=True, null=True)  # Field name made lowercase.
    overlap = models.FloatField(db_column='Overlap', blank=True, null=True)  # Field name made lowercase.
    overlap_qty = models.FloatField(db_column='Overlap_Qty', blank=True, null=True)  # Field name made lowercase.
    est_ovl_hrs = models.FloatField(db_column='Est_Ovl_Hrs', blank=True, null=True)  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    sched_ovl_start_old = models.DateTimeField(db_column='Sched_Ovl_Start_OLD', blank=True, null=True)  # Field name made lowercase.
    sched_ovl_start_hr_old = models.FloatField(db_column='Sched_Ovl_Start_Hr_OLD', blank=True, null=True)  # Field name made lowercase.
    sched_start = models.DateTimeField(db_column='Sched_Start', blank=True, null=True)  # Field name made lowercase.
    sched_start_hr_old = models.FloatField(db_column='Sched_Start_Hr_OLD', blank=True, null=True)  # Field name made lowercase.
    sched_end = models.DateTimeField(db_column='Sched_End', blank=True, null=True)  # Field name made lowercase.
    sched_end_hr_old = models.FloatField(db_column='Sched_End_Hr_OLD', blank=True, null=True)  # Field name made lowercase.
    schedule_exception_old = models.BooleanField(db_column='Schedule_Exception_OLD')  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    minimum_chg_amt = models.DecimalField(db_column='Minimum_Chg_Amt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cost_unit = models.CharField(db_column='Cost_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cost_unit_conv = models.FloatField(db_column='Cost_Unit_Conv')  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate')  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.BooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    rwk_quantity = models.IntegerField(db_column='Rwk_Quantity', blank=True, null=True)  # Field name made lowercase.
    rwk_setup_hrs = models.FloatField(db_column='Rwk_Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    rwk_run_hrs = models.FloatField(db_column='Rwk_Run_Hrs', blank=True, null=True)  # Field name made lowercase.
    rwk_setup_labor = models.DecimalField(db_column='Rwk_Setup_Labor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rwk_run_labor = models.DecimalField(db_column='Rwk_Run_Labor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rwk_labor_burden = models.DecimalField(db_column='Rwk_Labor_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rwk_machine_burden = models.DecimalField(db_column='Rwk_Machine_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rwk_ga_burden = models.DecimalField(db_column='Rwk_GA_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rwk_scrap_qty = models.FloatField(db_column='Rwk_Scrap_Qty', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    holder_id = models.CharField(db_column='Holder_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    op_group = models.CharField(db_column='Op_Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    act_run_labor_hrs = models.FloatField(db_column='Act_Run_Labor_Hrs', blank=True, null=True)  # Field name made lowercase.
    setup_qty = models.IntegerField(db_column='Setup_Qty', blank=True, null=True)  # Field name made lowercase.
    run_qty = models.IntegerField(db_column='Run_Qty', blank=True, null=True)  # Field name made lowercase.
    rwk_run_labor_hrs = models.FloatField(db_column='Rwk_Run_Labor_Hrs', blank=True, null=True)  # Field name made lowercase.
    rwk_setup_qty = models.IntegerField(db_column='Rwk_Setup_Qty', blank=True, null=True)  # Field name made lowercase.
    rwk_run_qty = models.IntegerField(db_column='Rwk_Run_Qty', blank=True, null=True)  # Field name made lowercase.
    act_setup_labor_hrs = models.FloatField(db_column='Act_Setup_Labor_Hrs', blank=True, null=True)  # Field name made lowercase.
    rwk_setup_labor_hrs = models.FloatField(db_column='Rwk_Setup_Labor_Hrs', blank=True, null=True)  # Field name made lowercase.
    floor_notes = models.TextField(db_column='Floor_Notes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    job_oid = models.CharField(db_column='Job_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sched_resources = models.FloatField(db_column='Sched_Resources', blank=True, null=True)  # Field name made lowercase.
    lag_hours = models.FloatField(db_column='Lag_Hours', blank=True, null=True)  # Field name made lowercase.
    workcenter_oid = models.CharField(db_column='WorkCenter_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    manual_start_lock = models.NullBooleanField(db_column='Manual_Start_Lock')  # Field name made lowercase.
    manual_stop_lock = models.NullBooleanField(db_column='Manual_Stop_Lock')  # Field name made lowercase.
    priority_zero_lock = models.NullBooleanField(db_column='Priority_Zero_Lock')  # Field name made lowercase.
    firm_zone_lock = models.NullBooleanField(db_column='Firm_Zone_Lock')  # Field name made lowercase.
    sb_orig_oid = models.CharField(db_column='SB_Orig_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sb_setup_hrs = models.FloatField(db_column='SB_Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    sb_run_hrs = models.FloatField(db_column='SB_Run_Hrs', blank=True, null=True)  # Field name made lowercase.
    sb_run = models.FloatField(db_column='SB_Run', blank=True, null=True)  # Field name made lowercase.
    sb_runmethod = models.CharField(db_column='SB_RunMethod', max_length=8, blank=True, null=True)  # Field name made lowercase.
    sb_efficiency = models.FloatField(db_column='SB_Efficiency', blank=True, null=True)  # Field name made lowercase.
    actual_start = models.DateTimeField(db_column='Actual_Start', blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_Updated_By', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Job_Operation'


class JobOperationTime(models.Model):
    job_operation = models.IntegerField(db_column='Job_Operation')  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=6)  # Field name made lowercase.
    work_date = models.DateTimeField(db_column='Work_Date')  # Field name made lowercase.
    act_setup_hrs = models.FloatField(db_column='Act_Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    act_run_hrs = models.FloatField(db_column='Act_Run_Hrs', blank=True, null=True)  # Field name made lowercase.
    act_run_qty = models.IntegerField(db_column='Act_Run_Qty', blank=True, null=True)  # Field name made lowercase.
    act_scrap_qty = models.IntegerField(db_column='Act_Scrap_Qty', blank=True, null=True)  # Field name made lowercase.
    overtime_hrs = models.FloatField(db_column='Overtime_Hrs', blank=True, null=True)  # Field name made lowercase.
    setup_overtime_hrs = models.FloatField(db_column='Setup_Overtime_Hrs')  # Field name made lowercase.
    overtime_factor = models.FloatField(db_column='Overtime_Factor', blank=True, null=True)  # Field name made lowercase.
    operation_complete = models.BooleanField(db_column='Operation_Complete')  # Field name made lowercase.
    attended_pct = models.FloatField(db_column='Attended_Pct', blank=True, null=True)  # Field name made lowercase.
    rework_time = models.BooleanField(db_column='Rework_Time')  # Field name made lowercase.
    setup_pct_complete = models.FloatField(db_column='Setup_Pct_Complete', blank=True, null=True)  # Field name made lowercase.
    run_pct_complete = models.FloatField(db_column='Run_Pct_Complete', blank=True, null=True)  # Field name made lowercase.
    setup_labor_rate = models.FloatField(db_column='Setup_Labor_Rate', blank=True, null=True)  # Field name made lowercase.
    run_labor_rate = models.FloatField(db_column='Run_Labor_Rate', blank=True, null=True)  # Field name made lowercase.
    labor_burden = models.FloatField(db_column='Labor_Burden', blank=True, null=True)  # Field name made lowercase.
    setup_labor_burden = models.FloatField(db_column='Setup_Labor_Burden')  # Field name made lowercase.
    machine_burden = models.DecimalField(db_column='Machine_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ga_burden = models.DecimalField(db_column='GA_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    entry_type = models.SmallIntegerField(db_column='Entry_Type')  # Field name made lowercase.
    job_operation_time = models.CharField(db_column='Job_Operation_Time', primary_key=True, max_length=50)  # Field name made lowercase.
    scrap_code = models.CharField(db_column='Scrap_Code', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rwk_code = models.CharField(db_column='Rwk_Code', max_length=25, blank=True, null=True)  # Field name made lowercase.
    wc = models.CharField(db_column='WC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    op_group = models.CharField(db_column='Op_Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    act_setup_qty = models.IntegerField(db_column='Act_Setup_Qty', blank=True, null=True)  # Field name made lowercase.
    act_run_labor_hrs = models.FloatField(db_column='Act_Run_Labor_Hrs', blank=True, null=True)  # Field name made lowercase.
    act_setup_labor_hrs = models.FloatField(db_column='Act_Setup_Labor_Hrs', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    overtime_hrs_7x = models.FloatField(db_column='Overtime_Hrs_7x', blank=True, null=True)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    job_operation_oid = models.CharField(db_column='Job_Operation_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    employee_oid = models.CharField(db_column='Employee_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Job_Operation_Time'


class JournalEntry(models.Model):
    journal_entrykey = models.AutoField(db_column='Journal_EntryKey', primary_key=True)  # Field name made lowercase.
    journal_entry = models.IntegerField(db_column='Journal_Entry', unique=True, blank=True, null=True)  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=15, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=30, blank=True, null=True)  # Field name made lowercase.
    transaction_date = models.DateTimeField(db_column='Transaction_Date', blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=13)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    posted = models.BooleanField(db_column='Posted')  # Field name made lowercase.
    creation_date = models.DateTimeField(db_column='Creation_Date', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    originating_transaction = models.CharField(db_column='Originating_Transaction', max_length=50, blank=True, null=True)  # Field name made lowercase.
    statement_date = models.DateTimeField(db_column='Statement_Date', blank=True, null=True)  # Field name made lowercase.
    line_description = models.CharField(db_column='Line_Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    order_number = models.CharField(db_column='Order_Number', max_length=30, blank=True, null=True)  # Field name made lowercase.
    partner_type = models.IntegerField(db_column='Partner_Type', blank=True, null=True)  # Field name made lowercase.
    cust_trans_type = models.IntegerField(db_column='Cust_Trans_Type', blank=True, null=True)  # Field name made lowercase.
    partner = models.CharField(db_column='Partner', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=8, blank=True, null=True)  # Field name made lowercase.
    item_id = models.CharField(db_column='Item_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    item_description = models.CharField(db_column='Item_Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cust_trans = models.CharField(db_column='Cust_Trans', max_length=50, blank=True, null=True)  # Field name made lowercase.
    currency_def = models.IntegerField(db_column='Currency_Def', blank=True, null=True)  # Field name made lowercase.
    holder_type = models.CharField(db_column='Holder_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfg_holder_type = models.CharField(db_column='MFG_Holder_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mfg_holder_id = models.CharField(db_column='MFG_Holder_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Journal_Entry'


class Location(models.Model):
    locationkey = models.AutoField(db_column='LocationKey', primary_key=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='Location', unique=True, blank=True, null=True)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    warehouse = models.CharField(db_column='Warehouse', max_length=4, blank=True, null=True)  # Field name made lowercase.
    location_id = models.CharField(db_column='Location_ID', unique=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=25, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=8, blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Location'


class LookupType(models.Model):
    lookup_type = models.IntegerField(db_column='Lookup_Type', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    param_sequence = models.IntegerField(db_column='Param_Sequence', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Lookup_Type'


class Material(models.Model):
    material = models.CharField(db_column='Material', primary_key=True, max_length=30)  # Field name made lowercase.
    primary_vendor = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='Primary_Vendor', blank=True, null=True)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    shape = models.ForeignKey('Shapes', models.DO_NOTHING, db_column='Shape', blank=True, null=True)  # Field name made lowercase.
    location_id = models.CharField(db_column='Location_ID', max_length=10)  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    pick_buy_indicator = models.CharField(db_column='Pick_Buy_Indicator', max_length=1)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    rev = models.CharField(db_column='Rev', max_length=8, blank=True, null=True)  # Field name made lowercase.
    stocked_uofm = models.CharField(db_column='Stocked_UofM', max_length=4)  # Field name made lowercase.
    purchase_uofm = models.CharField(db_column='Purchase_UofM', max_length=4)  # Field name made lowercase.
    cost_uofm = models.CharField(db_column='Cost_UofM', max_length=4)  # Field name made lowercase.
    price_uofm = models.CharField(db_column='Price_UofM', max_length=4)  # Field name made lowercase.
    selling_price = models.FloatField(db_column='Selling_Price', blank=True, null=True)  # Field name made lowercase.
    standard_cost = models.FloatField(db_column='Standard_Cost')  # Field name made lowercase.
    average_cost = models.FloatField(db_column='Average_Cost', blank=True, null=True)  # Field name made lowercase.
    last_cost = models.FloatField(db_column='Last_Cost', blank=True, null=True)  # Field name made lowercase.
    on_order_qty = models.FloatField(db_column='On_Order_Qty', blank=True, null=True)  # Field name made lowercase.
    order_point = models.FloatField(db_column='Order_Point', blank=True, null=True)  # Field name made lowercase.
    reorder_qty = models.FloatField(db_column='Reorder_Qty')  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days')  # Field name made lowercase.
    uofm_conv_factor = models.FloatField(db_column='UofM_Conv_Factor')  # Field name made lowercase.
    lot_trace = models.BooleanField(db_column='Lot_Trace')  # Field name made lowercase.
    rd_whole_unit = models.BooleanField(db_column='Rd_Whole_Unit')  # Field name made lowercase.
    ext_description = models.TextField(db_column='Ext_Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    make_buy = models.CharField(db_column='Make_Buy', max_length=1)  # Field name made lowercase.
    vendor_reference = models.CharField(db_column='Vendor_Reference', max_length=30, blank=True, null=True)  # Field name made lowercase.
    drawing = models.CharField(db_column='Drawing', max_length=30, blank=True, null=True)  # Field name made lowercase.
    use_price_breaks = models.BooleanField(db_column='Use_Price_Breaks')  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price_unit_conv = models.FloatField(db_column='Price_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    holder_id = models.CharField(db_column='Holder_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    taxable = models.NullBooleanField(db_column='Taxable')  # Field name made lowercase.
    is_length = models.FloatField(db_column='IS_Length', blank=True, null=True)  # Field name made lowercase.
    is_width = models.FloatField(db_column='IS_Width', blank=True, null=True)  # Field name made lowercase.
    is_weight_factor = models.FloatField(db_column='IS_Weight_Factor', blank=True, null=True)  # Field name made lowercase.
    is_thickness = models.FloatField(db_column='IS_Thickness', blank=True, null=True)  # Field name made lowercase.
    stock_item = models.CharField(db_column='Stock_Item', max_length=50, blank=True, null=True)  # Field name made lowercase.
    affects_schedule = models.NullBooleanField(db_column='Affects_Schedule')  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    shape_oid = models.CharField(db_column='Shape_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tooling = models.NullBooleanField(db_column='Tooling')  # Field name made lowercase.
    isserialized = models.BooleanField(db_column='IsSerialized')  # Field name made lowercase.
    maxusage = models.IntegerField(db_column='MaxUsage', blank=True, null=True)  # Field name made lowercase.
    shelflife = models.FloatField(db_column='ShelfLife', blank=True, null=True)  # Field name made lowercase.
    shelflifeuofm = models.CharField(db_column='ShelfLifeUofM', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Material'


class MaterialLocation(models.Model):
    material_locationkey = models.AutoField(db_column='Material_LocationKey', primary_key=True)  # Field name made lowercase.
    material_location = models.IntegerField(db_column='Material_Location', unique=True, blank=True, null=True)  # Field name made lowercase.
    location_id = models.CharField(db_column='Location_ID', max_length=10)  # Field name made lowercase.
    material = models.ForeignKey(Material, models.DO_NOTHING, db_column='Material')  # Field name made lowercase.
    lot = models.CharField(db_column='Lot', max_length=20, blank=True, null=True)  # Field name made lowercase.
    on_hand_qty = models.FloatField(db_column='On_Hand_Qty')  # Field name made lowercase.
    unit_cost = models.FloatField(db_column='Unit_Cost', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Material_Location'


class MaterialReq(AutoNumberMixin, models.Model):
    auto_number_attrs = [AutoIncrementColumn('material_req')]

    material_reqkey = models.AutoField(db_column='Material_ReqKey', primary_key=True)  # Field name made lowercase.
    material_req = models.IntegerField(db_column='Material_Req', unique=True, blank=True, null=True)  # Field name made lowercase.
    job_operation = models.IntegerField(db_column='Job_Operation', blank=True, null=True)  # Field name made lowercase.
    job = models.ForeignKey(Job, models.DO_NOTHING, db_column='Job')  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=30, blank=True, null=True)  # Field name made lowercase.
    vendor = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pick_buy_indicator = models.CharField(db_column='Pick_Buy_Indicator', max_length=1)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    quantity_per_basis = models.CharField(db_column='Quantity_Per_Basis', max_length=1, blank=True, null=True)  # Field name made lowercase.
    quantity_per = models.FloatField(db_column='Quantity_Per', blank=True, null=True)  # Field name made lowercase.
    uofm = models.CharField(db_column='UofM', max_length=4)  # Field name made lowercase.
    deferred_qty = models.FloatField(db_column='Deferred_Qty')  # Field name made lowercase.
    est_qty = models.FloatField(db_column='Est_Qty', blank=True, null=True)  # Field name made lowercase.
    est_unit_cost = models.FloatField(db_column='Est_Unit_Cost', blank=True, null=True)  # Field name made lowercase.
    est_addl_cost = models.DecimalField(db_column='Est_Addl_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_total_cost = models.DecimalField(db_column='Est_Total_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    addl_cost_desc = models.CharField(db_column='Addl_Cost_Desc', max_length=25, blank=True, null=True)  # Field name made lowercase.
    act_qty = models.FloatField(db_column='Act_Qty', blank=True, null=True)  # Field name made lowercase.
    act_unit_cost = models.FloatField(db_column='Act_Unit_Cost', blank=True, null=True)  # Field name made lowercase.
    act_addl_cost = models.DecimalField(db_column='Act_Addl_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_total_cost = models.DecimalField(db_column='Act_Total_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    part_length = models.FloatField(db_column='Part_Length', blank=True, null=True)  # Field name made lowercase.
    part_width = models.FloatField(db_column='Part_Width', blank=True, null=True)  # Field name made lowercase.
    bar_end = models.FloatField(db_column='Bar_End', blank=True, null=True)  # Field name made lowercase.
    cutoff = models.FloatField(db_column='Cutoff', blank=True, null=True)  # Field name made lowercase.
    facing = models.FloatField(db_column='Facing', blank=True, null=True)  # Field name made lowercase.
    bar_length = models.FloatField(db_column='Bar_Length', blank=True, null=True)  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate')  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.BooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    certs_required = models.BooleanField(db_column='Certs_Required')  # Field name made lowercase.
    manual_link = models.BooleanField(db_column='Manual_Link')  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    sched_start_date = models.DateTimeField(db_column='Sched_Start_Date', blank=True, null=True)  # Field name made lowercase.
    sched_end_date = models.DateTimeField(db_column='Sched_End_Date', blank=True, null=True)  # Field name made lowercase.
    vendor_reference = models.CharField(db_column='Vendor_Reference', max_length=30, blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    holder_id = models.CharField(db_column='Holder_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cost_uofm = models.CharField(db_column='Cost_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cost_unit_conv = models.FloatField(db_column='Cost_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    quantity_multiplier = models.FloatField(db_column='Quantity_Multiplier', blank=True, null=True)  # Field name made lowercase.
    drawing_id = models.CharField(db_column='Drawing_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    res_type = models.SmallIntegerField(db_column='Res_Type', blank=True, null=True)  # Field name made lowercase.
    res_id = models.CharField(db_column='Res_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    res_qty = models.FloatField(db_column='Res_Qty', blank=True, null=True)  # Field name made lowercase.
    partial_res = models.NullBooleanField(db_column='Partial_Res')  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    job_operation_oid = models.CharField(db_column='Job_Operation_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    job_oid = models.CharField(db_column='Job_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    affects_schedule = models.NullBooleanField(db_column='Affects_Schedule')  # Field name made lowercase.
    material_oid = models.CharField(db_column='Material_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    rounded = models.BooleanField(db_column='Rounded')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Material_Req'


class MaterialTrans(models.Model):
    material_transkey = models.AutoField(db_column='Material_TransKey', primary_key=True)  # Field name made lowercase.
    material_trans = models.IntegerField(db_column='Material_Trans', unique=True, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=30, blank=True, null=True)  # Field name made lowercase.
    po_number = models.CharField(db_column='PO_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    po_line = models.CharField(db_column='PO_Line', max_length=10, blank=True, null=True)  # Field name made lowercase.
    document = models.CharField(db_column='Document', max_length=15, blank=True, null=True)  # Field name made lowercase.
    so_detail = models.IntegerField(db_column='SO_Detail', blank=True, null=True)  # Field name made lowercase.
    source = models.IntegerField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    material_req = models.IntegerField(db_column='Material_Req', blank=True, null=True)  # Field name made lowercase.
    job_operation = models.IntegerField(db_column='Job_Operation', blank=True, null=True)  # Field name made lowercase.
    location_id = models.CharField(db_column='Location_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    service = models.CharField(db_column='Service', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lot = models.CharField(db_column='Lot', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tran_type = models.CharField(db_column='Tran_Type', max_length=10)  # Field name made lowercase.
    material_trans_date = models.DateTimeField(db_column='Material_Trans_Date', blank=True, null=True)  # Field name made lowercase.
    unit_cost = models.FloatField(db_column='Unit_Cost', blank=True, null=True)  # Field name made lowercase.
    addl_cost = models.FloatField(db_column='Addl_Cost', blank=True, null=True)  # Field name made lowercase.
    purch_unit_weight = models.FloatField(db_column='Purch_Unit_Weight', blank=True, null=True)  # Field name made lowercase.
    stock_uofm = models.CharField(db_column='Stock_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cost_uofm = models.CharField(db_column='Cost_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=15, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    selling_price = models.FloatField(db_column='Selling_Price')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=100, blank=True, null=True)  # Field name made lowercase.
    holder_id = models.CharField(db_column='Holder_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tax_assigned = models.FloatField(db_column='Tax_Assigned', blank=True, null=True)  # Field name made lowercase.
    no_quote = models.NullBooleanField(db_column='No_Quote')  # Field name made lowercase.
    lead_days = models.IntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    vendor_trans = models.IntegerField(db_column='Vendor_Trans', blank=True, null=True)  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    processed = models.BooleanField(db_column='Processed')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Material_Trans'


class OpGroup(models.Model):
    op_group = models.CharField(db_column='Op_Group', primary_key=True, max_length=50)  # Field name made lowercase.
    work_center = models.CharField(db_column='Work_Center', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    schedule_end = models.DateTimeField(db_column='Schedule_End', blank=True, null=True)  # Field name made lowercase.
    schedule_start = models.DateTimeField(db_column='Schedule_Start', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Op_Group'


class Operation(models.Model):
    operation = models.CharField(db_column='Operation', primary_key=True, max_length=10)  # Field name made lowercase.
    work_center = models.ForeignKey('WorkCenter', models.DO_NOTHING, db_column='Work_Center')  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=25, blank=True, null=True)  # Field name made lowercase.
    est_setup_hrs = models.FloatField(db_column='Est_Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    run = models.FloatField(db_column='Run', blank=True, null=True)  # Field name made lowercase.
    run_method = models.CharField(db_column='Run_Method', max_length=8, blank=True, null=True)  # Field name made lowercase.
    attended_pct = models.FloatField(db_column='Attended_Pct', blank=True, null=True)  # Field name made lowercase.
    overlap_method = models.CharField(db_column='Overlap_Method', max_length=3, blank=True, null=True)  # Field name made lowercase.
    overlap = models.FloatField(db_column='Overlap', blank=True, null=True)  # Field name made lowercase.
    efficiency_pct = models.FloatField(db_column='Efficiency_Pct', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    workcenter_oid = models.CharField(db_column='WorkCenter_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sched_resources = models.FloatField(db_column='Sched_Resources', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Operation'


class PoDetail(models.Model):
    po_detailkey = models.AutoField(db_column='PO_DetailKey', primary_key=True)  # Field name made lowercase.
    po_detail = models.IntegerField(db_column='PO_Detail', unique=True, blank=True, null=True)  # Field name made lowercase.
    po = models.CharField(db_column='PO', max_length=8)  # Field name made lowercase.
    line = models.CharField(db_column='Line', max_length=6)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8, blank=True, null=True)  # Field name made lowercase.
    order_quantity = models.FloatField(db_column='Order_Quantity')  # Field name made lowercase.
    purchase_unit = models.CharField(db_column='Purchase_Unit', max_length=4)  # Field name made lowercase.
    unit_cost = models.FloatField(db_column='Unit_Cost', blank=True, null=True)  # Field name made lowercase.
    certs_required = models.BooleanField(db_column='Certs_Required')  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    vendor_reference = models.CharField(db_column='Vendor_Reference', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cost_unit = models.CharField(db_column='Cost_Unit', max_length=4)  # Field name made lowercase.
    purchase_unit_weight = models.FloatField(db_column='Purchase_Unit_Weight')  # Field name made lowercase.
    addl_cost_desc1 = models.CharField(db_column='Addl_Cost_Desc1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    addl_cost_desc2 = models.CharField(db_column='Addl_Cost_Desc2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    addl_cost_est_amt1 = models.DecimalField(db_column='Addl_Cost_Est_Amt1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    addl_cost_est_amt2 = models.DecimalField(db_column='Addl_Cost_Est_Amt2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    addl_cost_act_amt1 = models.DecimalField(db_column='Addl_Cost_Act_Amt1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    addl_cost_act_amt2 = models.DecimalField(db_column='Addl_Cost_Act_Amt2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    act_cost = models.DecimalField(db_column='Act_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_ext_amount = models.DecimalField(db_column='Est_Ext_Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ext_description = models.TextField(db_column='Ext_Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=100, blank=True, null=True)  # Field name made lowercase.
    line_revision = models.CharField(db_column='Line_Revision', max_length=4, blank=True, null=True)  # Field name made lowercase.
    holder_id = models.CharField(db_column='Holder_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    addl_cost_taxable1 = models.NullBooleanField(db_column='Addl_Cost_Taxable1')  # Field name made lowercase.
    addl_cost_taxable2 = models.NullBooleanField(db_column='Addl_Cost_Taxable2')  # Field name made lowercase.
    po_line5x = models.IntegerField(db_column='PO_Line5x', blank=True, null=True)  # Field name made lowercase.
    awarded_vendor = models.CharField(db_column='Awarded_Vendor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lowest_quote = models.IntegerField(db_column='Lowest_Quote', blank=True, null=True)  # Field name made lowercase.
    plan_modified = models.NullBooleanField(db_column='Plan_Modified')  # Field name made lowercase.
    price_locked = models.NullBooleanField(db_column='Price_Locked')  # Field name made lowercase.
    po_type = models.IntegerField(db_column='PO_Type', blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    po_header_oid = models.CharField(db_column='PO_Header_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'PO_Detail'


class PoHeader(models.Model):
    po = models.CharField(db_column='PO', primary_key=True, max_length=8)  # Field name made lowercase.
    vendor = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    ship_to = models.IntegerField(db_column='Ship_To', blank=True, null=True)  # Field name made lowercase.
    ship_via = models.CharField(db_column='Ship_Via', max_length=15, blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='Terms', max_length=15, blank=True, null=True)  # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    drop_ship_ship_to = models.IntegerField(db_column='Drop_Ship_Ship_To', blank=True, null=True)  # Field name made lowercase.
    drop_ship_contact = models.IntegerField(db_column='Drop_Ship_Contact', blank=True, null=True)  # Field name made lowercase.
    drop_ship = models.CharField(db_column='Drop_Ship', max_length=10, blank=True, null=True)  # Field name made lowercase.
    drop_ship_customer = models.CharField(db_column='Drop_Ship_Customer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateTimeField(db_column='Order_Date')  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    print_date = models.DateTimeField(db_column='Print_Date', blank=True, null=True)  # Field name made lowercase.
    fob = models.CharField(db_column='FOB', max_length=11, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    issued_by = models.CharField(db_column='Issued_By', max_length=30, blank=True, null=True)  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate')  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.BooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    po_type = models.IntegerField(db_column='PO_Type')  # Field name made lowercase.
    track_changes = models.NullBooleanField(db_column='Track_Changes')  # Field name made lowercase.
    print_details = models.NullBooleanField(db_column='Print_Details')  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'PO_Header'
        unique_together = (('po', 'po_type'),)


class PacklistDetail(models.Model):
    packlist_detailkey = models.AutoField(db_column='Packlist_DetailKey', primary_key=True)  # Field name made lowercase.
    packlist_detail = models.IntegerField(db_column='Packlist_Detail', unique=True, blank=True, null=True)  # Field name made lowercase.
    packlist = models.ForeignKey('PacklistHeader', models.DO_NOTHING, db_column='Packlist')  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job_operation = models.IntegerField(db_column='Job_Operation', blank=True, null=True)  # Field name made lowercase.
    material_trans = models.IntegerField(db_column='Material_Trans', blank=True, null=True)  # Field name made lowercase.
    so_detail = models.IntegerField(db_column='SO_Detail', blank=True, null=True)  # Field name made lowercase.
    invoice_line = models.CharField(db_column='Invoice_Line', max_length=50, blank=True, null=True)  # Field name made lowercase.
    po_number = models.CharField(db_column='PO_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    original_packlist = models.IntegerField(db_column='Original_Packlist', blank=True, null=True)  # Field name made lowercase.
    reopen_delivery = models.BooleanField(db_column='Reopen_Delivery')  # Field name made lowercase.
    tracking_nbr = models.CharField(db_column='Tracking_Nbr', max_length=20, blank=True, null=True)  # Field name made lowercase.
    unit_price = models.FloatField(db_column='Unit_Price', blank=True, null=True)  # Field name made lowercase.
    price_uofm = models.CharField(db_column='Price_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    promised_qty = models.FloatField(db_column='Promised_Qty')  # Field name made lowercase.
    backorder_qty = models.FloatField(db_column='Backorder_Qty')  # Field name made lowercase.
    instructions = models.TextField(db_column='Instructions', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    order_unit = models.CharField(db_column='Order_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    price_unit_conv = models.FloatField(db_column='Price_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    freight_amt = models.FloatField(db_column='Freight_Amt', blank=True, null=True)  # Field name made lowercase.
    bol_comments = models.TextField(db_column='BOL_Comments', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cartons = models.IntegerField(db_column='Cartons', blank=True, null=True)  # Field name made lowercase.
    hazardous_material = models.NullBooleanField(db_column='Hazardous_Material')  # Field name made lowercase.
    nmfc_code = models.CharField(db_column='NMFC_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pallets = models.IntegerField(db_column='Pallets', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    freight_class = models.CharField(db_column='Freight_Class', max_length=15, blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    job_operation_oid = models.CharField(db_column='Job_Operation_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    po_header_oid = models.CharField(db_column='PO_Header_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    packlist_oid = models.CharField(db_column='Packlist_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lot = models.CharField(db_column='Lot', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Packlist_Detail'


class PacklistHeader(models.Model):
    packlist = models.CharField(db_column='Packlist', primary_key=True, max_length=8)  # Field name made lowercase.
    customer_vendor = models.CharField(db_column='Customer_Vendor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    invoice = models.CharField(db_column='Invoice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ship_to = models.IntegerField(db_column='Ship_To', blank=True, null=True)  # Field name made lowercase.
    ship_via = models.CharField(db_column='Ship_Via', max_length=15, blank=True, null=True)  # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    packlist_date = models.DateTimeField(db_column='Packlist_Date', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=8)  # Field name made lowercase.
    invoiced = models.BooleanField(db_column='Invoiced')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    freight_amt = models.FloatField(db_column='Freight_Amt', blank=True, null=True)  # Field name made lowercase.
    bol_number = models.CharField(db_column='BOL_Number', max_length=10, blank=True, null=True)  # Field name made lowercase.
    carrier_bill_to = models.IntegerField(db_column='Carrier_Bill_To', blank=True, null=True)  # Field name made lowercase.
    bol_terms = models.SmallIntegerField(db_column='BOL_Terms', blank=True, null=True)  # Field name made lowercase.
    third_party_acct = models.CharField(db_column='Third_Party_Acct', max_length=20, blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    qb_ready = models.NullBooleanField(db_column='QB_Ready')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Packlist_Header'


class Preferences(models.Model):
    preferenceskey = models.AutoField(db_column='PreferencesKey', primary_key=True)  # Field name made lowercase.
    preferences = models.IntegerField(db_column='Preferences', unique=True, blank=True, null=True)  # Field name made lowercase.
    system_base_currency = models.IntegerField(db_column='System_Base_Currency', blank=True, null=True)  # Field name made lowercase.
    imperial_metric = models.CharField(db_column='Imperial_Metric', max_length=1)  # Field name made lowercase.
    mat_cost_method = models.CharField(db_column='Mat_Cost_Method', max_length=8)  # Field name made lowercase.
    labor_rate = models.CharField(db_column='Labor_Rate', max_length=1)  # Field name made lowercase.
    labor_burden = models.CharField(db_column='Labor_Burden', max_length=1)  # Field name made lowercase.
    wc_rate = models.DecimalField(db_column='WC_Rate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    profit_markup = models.CharField(db_column='Profit_Markup', max_length=1)  # Field name made lowercase.
    profit_pct = models.FloatField(db_column='Profit_Pct')  # Field name made lowercase.
    labor_markup_pct = models.FloatField(db_column='Labor_Markup_Pct')  # Field name made lowercase.
    mat_markup_pct = models.FloatField(db_column='Mat_Markup_Pct')  # Field name made lowercase.
    serv_markup_pct = models.FloatField(db_column='Serv_Markup_Pct')  # Field name made lowercase.
    labor_burden_markup_pct = models.FloatField(db_column='Labor_Burden_Markup_Pct')  # Field name made lowercase.
    machine_burden_markup_pct = models.FloatField(db_column='Machine_Burden_Markup_Pct')  # Field name made lowercase.
    ga_burden_markup_pct = models.FloatField(db_column='GA_Burden_Markup_Pct')  # Field name made lowercase.
    run_method = models.CharField(db_column='Run_Method', max_length=8)  # Field name made lowercase.
    transfer_cost_method = models.CharField(db_column='Transfer_Cost_Method', max_length=10)  # Field name made lowercase.
    inv_cost_method = models.CharField(db_column='Inv_Cost_Method', max_length=8)  # Field name made lowercase.
    calc_rem_hours = models.CharField(db_column='Calc_Rem_Hours', max_length=1)  # Field name made lowercase.
    copy_job_hours = models.CharField(db_column='Copy_Job_Hours', max_length=1)  # Field name made lowercase.
    close_rule = models.CharField(db_column='Close_Rule', max_length=15)  # Field name made lowercase.
    ship_lead_days = models.SmallIntegerField(db_column='Ship_Lead_Days', blank=True, null=True)  # Field name made lowercase.
    link_material = models.BooleanField(db_column='Link_Material')  # Field name made lowercase.
    so_ship_override = models.BooleanField(db_column='SO_Ship_Override')  # Field name made lowercase.
    partner = models.CharField(db_column='Partner', max_length=16, blank=True, null=True)  # Field name made lowercase.
    link_component = models.BooleanField(db_column='Link_Component')  # Field name made lowercase.
    update_job_from_po = models.BooleanField(db_column='Update_Job_From_PO')  # Field name made lowercase.
    interface_ar = models.BooleanField(db_column='Interface_AR')  # Field name made lowercase.
    time_entry_pct = models.SmallIntegerField(db_column='Time_Entry_Pct')  # Field name made lowercase.
    auto_complete_oper = models.BooleanField(db_column='Auto_Complete_Oper')  # Field name made lowercase.
    overlap_method = models.CharField(db_column='Overlap_Method', max_length=3, blank=True, null=True)  # Field name made lowercase.
    burden_incl_comm = models.BooleanField(db_column='Burden_Incl_Comm')  # Field name made lowercase.
    incl_scrap_qty = models.BooleanField(db_column='Incl_Scrap_Qty')  # Field name made lowercase.
    default_status = models.IntegerField(db_column='Default_Status')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    sell_misc_items = models.BooleanField(db_column='Sell_Misc_Items')  # Field name made lowercase.
    use_discounts = models.BooleanField(db_column='Use_Discounts')  # Field name made lowercase.
    quote_default_status = models.SmallIntegerField(db_column='Quote_Default_Status')  # Field name made lowercase.
    order_unit = models.CharField(db_column='Order_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    price_unit_conv = models.FloatField(db_column='Price_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    price_unit = models.CharField(db_column='Price_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    post_transactions = models.NullBooleanField(db_column='Post_Transactions')  # Field name made lowercase.
    quote_decimal_places = models.IntegerField(db_column='Quote_Decimal_Places', blank=True, null=True)  # Field name made lowercase.
    freight_class = models.CharField(db_column='Freight_Class', max_length=15, blank=True, null=True)  # Field name made lowercase.
    default_tran_limit = models.SmallIntegerField(db_column='Default_Tran_Limit', blank=True, null=True)  # Field name made lowercase.
    home_prompt = models.CharField(db_column='Home_Prompt', max_length=15, blank=True, null=True)  # Field name made lowercase.
    track_po_changes = models.NullBooleanField(db_column='Track_PO_Changes')  # Field name made lowercase.
    track_job_changes = models.NullBooleanField(db_column='Track_Job_Changes')  # Field name made lowercase.
    synergyurl = models.CharField(db_column='SynergyURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    synergysqlserver = models.CharField(db_column='SynergySQLServer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    synergysqldb = models.CharField(db_column='SynergySQLDB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    synergydbprefix = models.CharField(db_column='SynergyDBPrefix', max_length=255, blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    material_affects_schedule = models.NullBooleanField(db_column='Material_Affects_Schedule')  # Field name made lowercase.
    allow_prior_schedule = models.NullBooleanField(db_column='Allow_Prior_Schedule')  # Field name made lowercase.
    qualitysystemurl = models.CharField(db_column='QualitySystemURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    win_probability = models.IntegerField(db_column='Win_Probability', blank=True, null=True)  # Field name made lowercase.
    expiration_days = models.IntegerField(db_column='Expiration_Days', blank=True, null=True)  # Field name made lowercase.
    syn_items_fg = models.NullBooleanField(db_column='Syn_Items_FG')  # Field name made lowercase.
    syn_items_supply = models.NullBooleanField(db_column='Syn_Items_Supply')  # Field name made lowercase.
    syn_items_hw = models.NullBooleanField(db_column='Syn_Items_HW')  # Field name made lowercase.
    syn_items_raw = models.NullBooleanField(db_column='Syn_Items_Raw')  # Field name made lowercase.
    syn_items_includerev = models.NullBooleanField(db_column='Syn_Items_IncludeRev')  # Field name made lowercase.
    autologoutoption = models.IntegerField(db_column='AutoLogoutOption', blank=True, null=True)  # Field name made lowercase.
    autologoutidletime = models.FloatField(db_column='AutoLogoutIdleTime', blank=True, null=True)  # Field name made lowercase.
    unique_jobpart_serialnum = models.BooleanField(db_column='Unique_JobPart_SerialNum')  # Field name made lowercase.
    track_routing_changes = models.BooleanField(db_column='Track_Routing_Changes')  # Field name made lowercase.
    unipoint_tokenkey = models.CharField(db_column='uniPoint_TokenKey', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quality_solution_key = models.IntegerField(db_column='Quality_Solution_Key')  # Field name made lowercase.
    mobilelogoutidletime = models.FloatField(db_column='MobileLogoutIdleTime')  # Field name made lowercase.
    quelaghourssource = models.IntegerField(db_column='QueLagHoursSource')  # Field name made lowercase.
    unipoint_server_path = models.CharField(db_column='uniPoint_Server_Path', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Preferences'


class PriceBreak(models.Model):
    price_breakkey = models.AutoField(db_column='Price_BreakKey', primary_key=True)  # Field name made lowercase.
    price_break = models.IntegerField(db_column='Price_Break', unique=True, blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=30, blank=True, null=True)  # Field name made lowercase.
    minimum_qty = models.FloatField(db_column='Minimum_Qty')  # Field name made lowercase.
    sell_price = models.FloatField(db_column='Sell_Price')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    vendor_material = models.CharField(db_column='Vendor_Material', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Price_Break'


class Quote(models.Model):
    quote = models.CharField(db_column='Quote', primary_key=True, max_length=50)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=15, blank=True, null=True)  # Field name made lowercase.
    top_lvl_quote = models.CharField(db_column='Top_Lvl_Quote', max_length=50)  # Field name made lowercase.
    quoted_by = models.CharField(db_column='Quoted_By', max_length=30, blank=True, null=True)  # Field name made lowercase.
    part_number = models.CharField(db_column='Part_Number', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rev = models.CharField(db_column='Rev', max_length=8, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ext_description = models.TextField(db_column='Ext_Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drawing = models.CharField(db_column='Drawing', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=16, blank=True, null=True)  # Field name made lowercase.
    commission_pct = models.FloatField(db_column='Commission_Pct', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=8, blank=True, null=True)  # Field name made lowercase.
    certs_required = models.BooleanField(db_column='Certs_Required')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    status_date = models.DateTimeField(db_column='Status_Date', blank=True, null=True)  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    assembly_level = models.SmallIntegerField(db_column='Assembly_Level', blank=True, null=True)  # Field name made lowercase.
    quantity_per = models.FloatField(db_column='Quantity_Per', blank=True, null=True)  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    profit_markup = models.CharField(db_column='Profit_Markup', max_length=1, blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sched_end = models.DateTimeField(db_column='Sched_End', blank=True, null=True)  # Field name made lowercase.
    sched_start = models.DateTimeField(db_column='Sched_Start', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    rfq = models.CharField(db_column='RFQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    line = models.CharField(db_column='Line', max_length=6, blank=True, null=True)  # Field name made lowercase.
    assembly_id = models.CharField(db_column='Assembly_ID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    win_probability = models.IntegerField(db_column='Win_Probability', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Quote'


class QuoteAddlCharge(models.Model):
    quote_addl_chargekey = models.AutoField(db_column='Quote_Addl_ChargeKey', primary_key=True)  # Field name made lowercase.
    addl_charge = models.IntegerField(db_column='Addl_Charge', unique=True, blank=True, null=True)  # Field name made lowercase.
    quote = models.ForeignKey(Quote, models.DO_NOTHING, db_column='Quote')  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=25, blank=True, null=True)  # Field name made lowercase.
    est_price = models.DecimalField(db_column='Est_Price', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    job_revenue = models.BooleanField(db_column='Job_Revenue')  # Field name made lowercase.
    commissionable = models.BooleanField(db_column='Commissionable')  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    recurring = models.NullBooleanField(db_column='Recurring')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Quote_Addl_Charge'


class QuoteOperation(models.Model):
    quote_operationkey = models.AutoField(db_column='Quote_OperationKey', primary_key=True)  # Field name made lowercase.
    quote_operation = models.IntegerField(db_column='Quote_Operation', unique=True, blank=True, null=True)  # Field name made lowercase.
    vendor = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    work_center = models.ForeignKey('WorkCenter', models.DO_NOTHING, db_column='Work_Center', blank=True, null=True)  # Field name made lowercase.
    quote = models.ForeignKey(Quote, models.DO_NOTHING, db_column='Quote')  # Field name made lowercase.
    wc_vendor = models.CharField(db_column='WC_Vendor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=25, blank=True, null=True)  # Field name made lowercase.
    run = models.FloatField(db_column='Run', blank=True, null=True)  # Field name made lowercase.
    run_method = models.CharField(db_column='Run_Method', max_length=8, blank=True, null=True)  # Field name made lowercase.
    efficiency_pct = models.FloatField(db_column='Efficiency_Pct', blank=True, null=True)  # Field name made lowercase.
    est_run_per_part = models.FloatField(db_column='Est_Run_Per_Part', blank=True, null=True)  # Field name made lowercase.
    attended_pct = models.FloatField(db_column='Attended_Pct', blank=True, null=True)  # Field name made lowercase.
    queue_hrs = models.FloatField(db_column='Queue_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_setup_hrs = models.FloatField(db_column='Est_Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    operation_service = models.CharField(db_column='Operation_Service', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sequence = models.SmallIntegerField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.
    inside_oper = models.BooleanField(db_column='Inside_Oper')  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    est_unit_cost = models.FloatField(db_column='Est_Unit_Cost', blank=True, null=True)  # Field name made lowercase.
    est_addl_cost = models.DecimalField(db_column='Est_Addl_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    addl_cost_desc = models.CharField(db_column='Addl_Cost_Desc', max_length=15, blank=True, null=True)  # Field name made lowercase.
    minimum_chg_amt = models.DecimalField(db_column='Minimum_Chg_Amt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cost_unit = models.CharField(db_column='Cost_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cost_unit_conv = models.FloatField(db_column='Cost_Unit_Conv')  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate')  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.BooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    run_labor_rate = models.DecimalField(db_column='Run_Labor_Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    setup_labor_rate = models.DecimalField(db_column='Setup_Labor_Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    run_labor_burden_rate = models.DecimalField(db_column='Run_Labor_Burden_Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    setup_labor_burden_rate = models.DecimalField(db_column='Setup_Labor_Burden_Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    machine_burden_rate = models.DecimalField(db_column='Machine_Burden_Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ga_burden_rate = models.DecimalField(db_column='GA_Burden_Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    sched_resources = models.FloatField(db_column='Sched_Resources', blank=True, null=True)  # Field name made lowercase.
    lag_hours = models.FloatField(db_column='Lag_Hours', blank=True, null=True)  # Field name made lowercase.
    overlap = models.FloatField(db_column='Overlap', blank=True, null=True)  # Field name made lowercase.
    overlap_method = models.CharField(db_column='Overlap_Method', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Quote_Operation'


class QuoteOperationQty(models.Model):
    quote_operation_qtykey = models.AutoField(db_column='Quote_Operation_QtyKey', primary_key=True)  # Field name made lowercase.
    quote_operation_qty = models.IntegerField(db_column='Quote_Operation_Qty', unique=True, blank=True, null=True)  # Field name made lowercase.
    quote_operation = models.IntegerField(db_column='Quote_Operation', blank=True, null=True)  # Field name made lowercase.
    quote_qty_key = models.IntegerField(db_column='Quote_Qty_Key', blank=True, null=True)  # Field name made lowercase.
    est_setup_hrs = models.FloatField(db_column='Est_Setup_Hrs')  # Field name made lowercase.
    est_run_hrs = models.FloatField(db_column='Est_Run_Hrs')  # Field name made lowercase.
    est_total_hrs = models.FloatField(db_column='Est_Total_Hrs')  # Field name made lowercase.
    est_setup_labor = models.DecimalField(db_column='Est_Setup_Labor', max_digits=19, decimal_places=4)  # Field name made lowercase.
    est_run_labor = models.DecimalField(db_column='Est_Run_Labor', max_digits=19, decimal_places=4)  # Field name made lowercase.
    est_labor_burden = models.DecimalField(db_column='Est_Labor_Burden', max_digits=19, decimal_places=4)  # Field name made lowercase.
    est_machine_burden = models.DecimalField(db_column='Est_Machine_Burden', max_digits=19, decimal_places=4)  # Field name made lowercase.
    est_ga_burden = models.DecimalField(db_column='Est_GA_Burden', max_digits=19, decimal_places=4)  # Field name made lowercase.
    sequence = models.SmallIntegerField(db_column='Sequence')  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority')  # Field name made lowercase.
    inside_oper = models.BooleanField(db_column='Inside_Oper')  # Field name made lowercase.
    est_unit_cost = models.FloatField(db_column='Est_Unit_Cost')  # Field name made lowercase.
    est_addl_cost = models.DecimalField(db_column='Est_Addl_Cost', max_digits=19, decimal_places=4)  # Field name made lowercase.
    addl_cost_desc = models.CharField(db_column='Addl_Cost_Desc', max_length=15, blank=True, null=True)  # Field name made lowercase.
    offset_rate = models.DecimalField(db_column='Offset_Rate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    est_total_cost = models.DecimalField(db_column='Est_Total_Cost', max_digits=19, decimal_places=4)  # Field name made lowercase.
    nbr_setups = models.FloatField(db_column='Nbr_Setups', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    run = models.FloatField(db_column='Run', blank=True, null=True)  # Field name made lowercase.
    run_method = models.CharField(db_column='Run_Method', max_length=8, blank=True, null=True)  # Field name made lowercase.
    efficiency_pct = models.FloatField(db_column='Efficiency_Pct', blank=True, null=True)  # Field name made lowercase.
    est_run_per_part = models.FloatField(db_column='Est_Run_Per_Part', blank=True, null=True)  # Field name made lowercase.
    setup_hrs = models.FloatField(db_column='Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    locked = models.NullBooleanField(db_column='Locked')  # Field name made lowercase.
    overlap_qty = models.FloatField(db_column='Overlap_Qty', blank=True, null=True)  # Field name made lowercase.
    est_ovl_hrs = models.FloatField(db_column='Est_Ovl_Hrs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Quote_Operation_Qty'


class QuoteQty(models.Model):
    quote_qtykey = models.AutoField(db_column='Quote_QtyKey', primary_key=True)  # Field name made lowercase.
    quote_qty_key = models.IntegerField(db_column='Quote_Qty_Key', unique=True, blank=True, null=True)  # Field name made lowercase.
    quote = models.ForeignKey(Quote, models.DO_NOTHING, db_column='Quote')  # Field name made lowercase.
    parent_quote_qty_key = models.IntegerField(db_column='Parent_Quote_Qty_Key', blank=True, null=True)  # Field name made lowercase.
    quote_qty = models.IntegerField(db_column='Quote_Qty', blank=True, null=True)  # Field name made lowercase.
    yield_pct = models.FloatField(db_column='Yield_Pct', blank=True, null=True)  # Field name made lowercase.
    make_quantity = models.IntegerField(db_column='Make_Quantity', blank=True, null=True)  # Field name made lowercase.
    est_setup_hrs = models.FloatField(db_column='Est_Setup_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_run_hrs = models.FloatField(db_column='Est_Run_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_total_hrs = models.FloatField(db_column='Est_Total_Hrs', blank=True, null=True)  # Field name made lowercase.
    est_labor = models.DecimalField(db_column='Est_Labor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_material = models.DecimalField(db_column='Est_Material', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_service = models.DecimalField(db_column='Est_Service', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_labor_burden = models.DecimalField(db_column='Est_Labor_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_machine_burden = models.DecimalField(db_column='Est_Machine_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    est_ga_burden = models.DecimalField(db_column='Est_GA_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unit_price = models.FloatField(db_column='Unit_Price', blank=True, null=True)  # Field name made lowercase.
    quoted_unit_price = models.FloatField(db_column='Quoted_Unit_Price', blank=True, null=True)  # Field name made lowercase.
    total_price = models.DecimalField(db_column='Total_Price', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    price_uofm = models.CharField(db_column='Price_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    profit_pct = models.FloatField(db_column='Profit_Pct', blank=True, null=True)  # Field name made lowercase.
    labor_markup_pct = models.FloatField(db_column='Labor_Markup_Pct', blank=True, null=True)  # Field name made lowercase.
    mat_markup_pct = models.FloatField(db_column='Mat_Markup_Pct', blank=True, null=True)  # Field name made lowercase.
    serv_markup_pct = models.FloatField(db_column='Serv_Markup_Pct', blank=True, null=True)  # Field name made lowercase.
    labor_burden_markup_pct = models.FloatField(db_column='Labor_Burden_Markup_Pct')  # Field name made lowercase.
    machine_burden_markup_pct = models.FloatField(db_column='Machine_Burden_Markup_Pct')  # Field name made lowercase.
    ga_burden_markup_pct = models.FloatField(db_column='GA_Burden_Markup_Pct')  # Field name made lowercase.
    open_operations = models.SmallIntegerField(db_column='Open_Operations', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    order_unit = models.CharField(db_column='Order_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    price_unit_conv = models.FloatField(db_column='Price_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    decimal_places = models.IntegerField(db_column='Decimal_Places', blank=True, null=True)  # Field name made lowercase.
    price_source = models.IntegerField(db_column='Price_Source', blank=True, null=True)  # Field name made lowercase.
    locked_source = models.NullBooleanField(db_column='Locked_Source')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Quote_Qty'


class QuoteReq(models.Model):
    quote_reqkey = models.AutoField(db_column='Quote_ReqKey', primary_key=True)  # Field name made lowercase.
    quote_req = models.IntegerField(db_column='Quote_Req', unique=True, blank=True, null=True)  # Field name made lowercase.
    quote = models.ForeignKey(Quote, models.DO_NOTHING, db_column='Quote')  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quote_operation = models.IntegerField(db_column='Quote_Operation', blank=True, null=True)  # Field name made lowercase.
    vendor = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pick_buy_indicator = models.CharField(db_column='Pick_Buy_Indicator', max_length=1)  # Field name made lowercase.
    quantity_per_basis = models.CharField(db_column='Quantity_Per_Basis', max_length=1, blank=True, null=True)  # Field name made lowercase.
    quantity_per = models.FloatField(db_column='Quantity_Per', blank=True, null=True)  # Field name made lowercase.
    uofm = models.CharField(db_column='UofM', max_length=4)  # Field name made lowercase.
    cost_uofm = models.CharField(db_column='Cost_UofM', max_length=4)  # Field name made lowercase.
    est_unit_cost = models.FloatField(db_column='Est_Unit_Cost', blank=True, null=True)  # Field name made lowercase.
    vendor_reference = models.CharField(db_column='Vendor_Reference', max_length=30, blank=True, null=True)  # Field name made lowercase.
    part_length = models.FloatField(db_column='Part_Length', blank=True, null=True)  # Field name made lowercase.
    part_width = models.FloatField(db_column='Part_Width', blank=True, null=True)  # Field name made lowercase.
    bar_end = models.FloatField(db_column='Bar_End', blank=True, null=True)  # Field name made lowercase.
    cutoff = models.FloatField(db_column='Cutoff', blank=True, null=True)  # Field name made lowercase.
    facing = models.FloatField(db_column='Facing', blank=True, null=True)  # Field name made lowercase.
    bar_length = models.FloatField(db_column='Bar_Length', blank=True, null=True)  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate')  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.BooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    certs_required = models.BooleanField(db_column='Certs_Required')  # Field name made lowercase.
    sched_start_date = models.DateTimeField(db_column='Sched_Start_Date', blank=True, null=True)  # Field name made lowercase.
    sched_end_date = models.DateTimeField(db_column='Sched_End_Date', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    cost_unit_conv = models.FloatField(db_column='Cost_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    quantity_multiplier = models.FloatField(db_column='Quantity_Multiplier', blank=True, null=True)  # Field name made lowercase.
    drawing_id = models.CharField(db_column='Drawing_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    affects_schedule = models.NullBooleanField(db_column='Affects_Schedule')  # Field name made lowercase.
    rounded = models.BooleanField(db_column='Rounded')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Quote_Req'


class QuoteReqQty(models.Model):
    quote_req_qtykey = models.AutoField(db_column='Quote_Req_QtyKey', primary_key=True)  # Field name made lowercase.
    quote_req_qty = models.IntegerField(db_column='Quote_Req_Qty', unique=True, blank=True, null=True)  # Field name made lowercase.
    quote_req = models.IntegerField(db_column='Quote_Req', blank=True, null=True)  # Field name made lowercase.
    quote = models.CharField(db_column='Quote', max_length=50)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quote_qty_key = models.IntegerField(db_column='Quote_Qty_Key', blank=True, null=True)  # Field name made lowercase.
    make_quantity = models.IntegerField(db_column='Make_Quantity', blank=True, null=True)  # Field name made lowercase.
    est_qty = models.FloatField(db_column='Est_Qty', blank=True, null=True)  # Field name made lowercase.
    est_unit_cost = models.FloatField(db_column='Est_Unit_Cost', blank=True, null=True)  # Field name made lowercase.
    est_addl_cost = models.DecimalField(db_column='Est_Addl_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    addl_cost_desc = models.CharField(db_column='Addl_Cost_Desc', max_length=25, blank=True, null=True)  # Field name made lowercase.
    est_total_cost = models.DecimalField(db_column='Est_Total_Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Quote_Req_Qty'


class Rfq(AutoNumberMixin, models.Model):
    auto_number_attrs = [AutoNumberColumn('rfq', 'Rfq')]

    rfq = models.CharField(db_column='RFQ', primary_key=True, max_length=10)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sales_rep = models.CharField(db_column='Sales_Rep', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ship_to = models.IntegerField(db_column='Ship_To', blank=True, null=True)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='Terms', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    quote_date = models.DateTimeField(db_column='Quote_Date', blank=True, null=True)  # Field name made lowercase.
    commission_pct = models.FloatField(db_column='Commission_Pct', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reference = models.CharField(db_column='Reference', max_length=30, blank=True, null=True)  # Field name made lowercase.
    status_date = models.DateTimeField(db_column='Status_Date', blank=True, null=True)  # Field name made lowercase.
    rfq_date = models.DateTimeField(db_column='RFQ_Date', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.NullBooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate', blank=True, null=True)  # Field name made lowercase.
    ship_via = models.CharField(db_column='Ship_Via', max_length=15, blank=True, null=True)  # Field name made lowercase.
    certs_required = models.NullBooleanField(db_column='Certs_Required')  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    quoted_by = models.CharField(db_column='Quoted_By', max_length=30, blank=True, null=True)  # Field name made lowercase.
    submitted_date = models.DateTimeField(db_column='Submitted_Date', blank=True, null=True)  # Field name made lowercase.
    submittal_due_date = models.DateTimeField(db_column='Submittal_Due_Date', blank=True, null=True)  # Field name made lowercase.
    expiration_date = models.DateTimeField(db_column='Expiration_Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8, blank=True, null=True)  # Field name made lowercase.
    followup_date = models.DateTimeField(db_column='Followup_Date', blank=True, null=True)  # Field name made lowercase.
    act_followup_date = models.DateTimeField(db_column='Act_Followup_Date', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=20, blank=True, null=True)  # Field name made lowercase.
    win_probability = models.IntegerField(db_column='Win_Probability', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'RFQ'


class RfqVendor(models.Model):
    rfq_vendor = models.CharField(db_column='RFQ_Vendor', primary_key=True, max_length=50)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    po_header = models.CharField(db_column='PO_Header', max_length=8, blank=True, null=True)  # Field name made lowercase.
    date_added = models.DateTimeField(db_column='Date_Added', blank=True, null=True)  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    send_to_address = models.IntegerField(db_column='Send_To_Address', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'RFQ_Vendor'


class RawStockOld(models.Model):
    raw_stock = models.CharField(db_column='Raw_Stock', max_length=30)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
    shape = models.CharField(db_column='Shape', max_length=10)  # Field name made lowercase.
    length = models.FloatField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    length2 = models.FloatField(db_column='Length2', blank=True, null=True)  # Field name made lowercase.
    thickness = models.FloatField(db_column='Thickness', blank=True, null=True)  # Field name made lowercase.
    gauge = models.FloatField(db_column='Gauge', blank=True, null=True)  # Field name made lowercase.
    distance_across = models.FloatField(db_column='Distance_Across', blank=True, null=True)  # Field name made lowercase.
    purchase_unit_weight = models.FloatField(db_column='Purchase_Unit_Weight', blank=True, null=True)  # Field name made lowercase.
    weight_factor = models.FloatField(db_column='Weight_Factor')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Raw_Stock_Old'


class RawStockWeight(models.Model):
    type = models.CharField(db_column='Type', primary_key=True, max_length=10)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    lbs_per_cu_in = models.FloatField(db_column='Lbs_Per_Cu_In', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    tfm_alloy = models.CharField(db_column='TFM_Alloy', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Raw_Stock_Weight'


class Receipt(models.Model):
    receipt = models.CharField(db_column='Receipt', primary_key=True, max_length=50)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='Customer', blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ar_code = models.CharField(db_column='AR_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=8, blank=True, null=True)  # Field name made lowercase.
    reverse_entry = models.BooleanField(db_column='Reverse_Entry')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    deposit_date = models.DateTimeField(db_column='Deposit_Date', blank=True, null=True)  # Field name made lowercase.
    receipt_date = models.DateTimeField(db_column='Receipt_Date', blank=True, null=True)  # Field name made lowercase.
    payer = models.CharField(db_column='Payer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    period = models.CharField(db_column='Period', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deposit = models.CharField(db_column='Deposit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_receipt = models.CharField(db_column='Customer_Receipt', max_length=50, blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = IS_TEST
        db_table = 'Receipt'


class ReceiptDistribution(models.Model):
    receipt_distribution = models.CharField(db_column='Receipt_Distribution', primary_key=True, max_length=50)  # Field name made lowercase.
    receipt = models.CharField(db_column='Receipt', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ar_code = models.CharField(db_column='AR_Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Receipt_Distribution'


class Report(models.Model):
    reportidkey = models.AutoField(db_column='ReportIDKey', primary_key=True)  # Field name made lowercase.
    reportid = models.IntegerField(db_column='ReportID', unique=True, blank=True, null=True)  # Field name made lowercase.
    module = models.CharField(db_column='Module', max_length=21)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    filter = models.BooleanField(db_column='Filter')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    title2 = models.CharField(db_column='Title2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=254, blank=True, null=True)  # Field name made lowercase.
    description2 = models.CharField(db_column='Description2', max_length=254, blank=True, null=True)  # Field name made lowercase.
    databasename = models.CharField(db_column='DatabaseName', max_length=25)  # Field name made lowercase.
    databasecaption = models.CharField(db_column='DatabaseCaption', max_length=254)  # Field name made lowercase.
    databasecaption2 = models.CharField(db_column='DatabaseCaption2', max_length=254, blank=True, null=True)  # Field name made lowercase.
    accessddemacro = models.CharField(db_column='AccessDDEMacro', max_length=254, blank=True, null=True)  # Field name made lowercase.
    accessddeservice = models.CharField(db_column='AccessDDEService', max_length=254, blank=True, null=True)  # Field name made lowercase.
    accessddetopic = models.CharField(db_column='AccessDDETopic', max_length=254, blank=True, null=True)  # Field name made lowercase.
    parms = models.CharField(db_column='Parms', max_length=254, blank=True, null=True)  # Field name made lowercase.
    usejobboss = models.BooleanField(db_column='UseJobBOSS')  # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=254, blank=True, null=True)  # Field name made lowercase.
    commandlineargs = models.CharField(db_column='CommandLineArgs', max_length=254, blank=True, null=True)  # Field name made lowercase.
    usedde = models.BooleanField(db_column='UseDDE')  # Field name made lowercase.
    ddemacro = models.CharField(db_column='DDEMacro', max_length=254, blank=True, null=True)  # Field name made lowercase.
    ddeservice = models.CharField(db_column='DDEService', max_length=254, blank=True, null=True)  # Field name made lowercase.
    ddetopic = models.CharField(db_column='DDETopic', max_length=50, blank=True, null=True)  # Field name made lowercase.
    secname = models.CharField(db_column='SecName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Report'


class SoDetail(models.Model):
    so_detailkey = models.AutoField(db_column='SO_DetailKey', primary_key=True)  # Field name made lowercase.
    so_detail = models.IntegerField(db_column='SO_Detail', unique=True, blank=True, null=True)  # Field name made lowercase.
    sales_order = models.ForeignKey('SoHeader', models.DO_NOTHING, db_column='Sales_Order')  # Field name made lowercase.
    so_line = models.CharField(db_column='SO_Line', max_length=6)  # Field name made lowercase.
    po = models.CharField(db_column='PO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    line = models.CharField(db_column='Line', max_length=6, blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ship_to = models.IntegerField(db_column='Ship_To', blank=True, null=True)  # Field name made lowercase.
    drop_ship = models.BooleanField(db_column='Drop_Ship')  # Field name made lowercase.
    quote = models.CharField(db_column='Quote', max_length=50, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=9)  # Field name made lowercase.
    make_buy = models.CharField(db_column='Make_Buy', max_length=1)  # Field name made lowercase.
    unit_price = models.FloatField(db_column='Unit_Price')  # Field name made lowercase.
    discount_pct = models.FloatField(db_column='Discount_Pct')  # Field name made lowercase.
    price_uofm = models.CharField(db_column='Price_UofM', max_length=4)  # Field name made lowercase.
    total_price = models.DecimalField(db_column='Total_Price', max_digits=19, decimal_places=4)  # Field name made lowercase.
    deferred_qty = models.FloatField(db_column='Deferred_Qty')  # Field name made lowercase.
    prepaid_amt = models.DecimalField(db_column='Prepaid_Amt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    unit_cost = models.FloatField(db_column='Unit_Cost')  # Field name made lowercase.
    order_qty = models.FloatField(db_column='Order_Qty')  # Field name made lowercase.
    stock_uofm = models.CharField(db_column='Stock_UofM', max_length=4)  # Field name made lowercase.
    backorder_qty = models.FloatField(db_column='Backorder_Qty')  # Field name made lowercase.
    picked_qty = models.FloatField(db_column='Picked_Qty')  # Field name made lowercase.
    shipped_qty = models.FloatField(db_column='Shipped_Qty')  # Field name made lowercase.
    returned_qty = models.FloatField(db_column='Returned_Qty')  # Field name made lowercase.
    certs_required = models.BooleanField(db_column='Certs_Required')  # Field name made lowercase.
    taxable = models.BooleanField(db_column='Taxable')  # Field name made lowercase.
    commissionable = models.BooleanField(db_column='Commissionable')  # Field name made lowercase.
    commission_pct = models.FloatField(db_column='Commission_Pct')  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    promised_date = models.DateTimeField(db_column='Promised_Date', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    price_unit_conv = models.FloatField(db_column='Price_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    rev = models.CharField(db_column='Rev', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ext_description = models.TextField(db_column='Ext_Description', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cost_uofm = models.CharField(db_column='Cost_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cost_unit_conv = models.FloatField(db_column='Cost_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    res_type = models.SmallIntegerField(db_column='Res_Type', blank=True, null=True)  # Field name made lowercase.
    res_id = models.CharField(db_column='Res_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    res_qty = models.FloatField(db_column='Res_Qty', blank=True, null=True)  # Field name made lowercase.
    partial_res = models.NullBooleanField(db_column='Partial_Res')  # Field name made lowercase.
    prepaid_trade_amt = models.DecimalField(db_column='Prepaid_Trade_Amt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    commissionincluded = models.BooleanField(db_column='CommissionIncluded')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'SO_Detail'


class SoHeader(AutoNumberMixin, models.Model):
    auto_number_attrs = [AutoNumberColumn('sales_order', 'SalesOrder')]

    sales_order = models.CharField(db_column='Sales_Order', primary_key=True, max_length=10)  # Field name made lowercase.
    customer = models.CharField(db_column='Customer', max_length=10)  # Field name made lowercase.
    ship_to = models.IntegerField(db_column='Ship_To', blank=True, null=True)  # Field name made lowercase.
    contact = models.IntegerField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    sales_rep = models.CharField(db_column='Sales_Rep', max_length=6, blank=True, null=True)  # Field name made lowercase.
    order_taken_by = models.CharField(db_column='Order_Taken_By', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ship_via = models.CharField(db_column='Ship_Via', max_length=15, blank=True, null=True)  # Shipment Method
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='Terms', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sales_tax_amt = models.DecimalField(db_column='Sales_Tax_Amt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    sales_tax_rate = models.FloatField(db_column='Sales_Tax_Rate')  # Field name made lowercase.
    order_date = models.DateTimeField(db_column='Order_Date')  # Field name made lowercase.
    promised_date = models.DateTimeField(db_column='Promised_Date', blank=True, null=True)  # Field name made lowercase.
    customer_po = models.CharField(db_column='Customer_PO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8)  # Field name made lowercase.
    total_price = models.DecimalField(db_column='Total_Price', max_digits=19, decimal_places=4)  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate')  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.BooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # internal notes
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # external notes
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prepaid_tax_amount = models.DecimalField(db_column='Prepaid_Tax_Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'SO_Header'


class SchedBillDist(models.Model):
    sched_bill_dist = models.CharField(db_column='Sched_Bill_Dist', primary_key=True, max_length=50)  # Field name made lowercase.
    scheduled_bill = models.CharField(db_column='Scheduled_Bill', max_length=50, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    discountable = models.NullBooleanField(db_column='Discountable')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Sched_Bill_Dist'


class ScheduledBill(models.Model):
    scheduled_bill = models.CharField(db_column='Scheduled_Bill', primary_key=True, max_length=50)  # Field name made lowercase.
    started_date = models.DateTimeField(db_column='Started_Date', blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    invoice_day = models.SmallIntegerField(db_column='Invoice_Day')  # Field name made lowercase.
    base_number = models.CharField(db_column='Base_Number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    occurrence = models.SmallIntegerField(db_column='Occurrence')  # Field name made lowercase.
    remit_to = models.IntegerField(db_column='Remit_To', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Scheduled_Bill'


class Serialnumber(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    currentusage = models.FloatField(db_column='CurrentUsage', blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'SerialNumber'
        unique_together = (('serialnumber', 'partnumber'),)


class Serialnumberdetail(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    serialnumber_oid = models.CharField(db_column='SerialNumber_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    reference_oid = models.CharField(db_column='Reference_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ownerreference_oid = models.CharField(db_column='OwnerReference_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    objecttype = models.IntegerField(db_column='ObjectType', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'SerialNumberDetail'


class Service(models.Model):
    service = models.CharField(db_column='Service', primary_key=True, max_length=10)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=25, blank=True, null=True)  # Field name made lowercase.
    minimum_chg = models.DecimalField(db_column='Minimum_Chg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days')  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Service'


class ShapeDimension(models.Model):
    shape_dimension = models.CharField(db_column='Shape_Dimension', primary_key=True, max_length=50)  # Field name made lowercase.
    shape = models.CharField(db_column='Shape', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dimension = models.CharField(db_column='Dimension', max_length=50, blank=True, null=True)  # Field name made lowercase.
    db_field_name = models.CharField(db_column='DB_Field_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    display_name = models.CharField(db_column='Display_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    unique_dimension = models.NullBooleanField(db_column='Unique_Dimension')  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Shape_Dimension'


class Shapes(models.Model):
    shape = models.CharField(db_column='Shape', primary_key=True, max_length=10)  # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=254, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    index = models.IntegerField(db_column='Index', blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Shapes'


class Source(models.Model):
    sourcekey = models.AutoField(db_column='SourceKey', primary_key=True)  # Field name made lowercase.
    source = models.IntegerField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    po_detail = models.IntegerField(db_column='PO_Detail', blank=True, null=True)  # Field name made lowercase.
    job_operation = models.IntegerField(db_column='Job_Operation', blank=True, null=True)  # Field name made lowercase.
    material_req = models.IntegerField(db_column='Material_Req', blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=30, blank=True, null=True)  # Field name made lowercase.
    isso = models.BooleanField(db_column='IsSO')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    misc_material = models.BooleanField(db_column='Misc_Material')  # Field name made lowercase.
    act_qty = models.FloatField(db_column='Act_Qty')  # Field name made lowercase.
    act_unit_cost = models.FloatField(db_column='Act_Unit_Cost')  # Field name made lowercase.
    stocked_uofm = models.CharField(db_column='Stocked_UofM', max_length=4)  # Field name made lowercase.
    inv_qty = models.FloatField(db_column='Inv_Qty')  # Field name made lowercase.
    last_recv_date = models.DateTimeField(db_column='Last_Recv_Date', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    holder_id = models.CharField(db_column='Holder_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    total_tax_assigned = models.FloatField(db_column='Total_Tax_Assigned', blank=True, null=True)  # Field name made lowercase.
    source_type = models.IntegerField(db_column='Source_Type', blank=True, null=True)  # Field name made lowercase.
    po_type = models.IntegerField(db_column='PO_Type', blank=True, null=True)  # Field name made lowercase.
    quote_operation_qty = models.IntegerField(db_column='Quote_Operation_Qty', blank=True, null=True)  # Field name made lowercase.
    quote_req_qty = models.IntegerField(db_column='Quote_Req_Qty', blank=True, null=True)  # Field name made lowercase.
    cost_unit = models.CharField(db_column='Cost_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ordered_qty = models.FloatField(db_column='Ordered_Qty', blank=True, null=True)  # Field name made lowercase.
    poordered_qty = models.FloatField(db_column='POOrdered_Qty', blank=True, null=True)  # Field name made lowercase.
    order_unit = models.CharField(db_column='Order_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cost_unit_conv = models.FloatField(db_column='Cost_Unit_Conv', blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateTimeField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    po_detail_oid = models.CharField(db_column='PO_Detail_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    material_req_oid = models.CharField(db_column='Material_Req_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    job_operation_oid = models.CharField(db_column='Job_Operation_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Source'


class StatusChange(models.Model):
    status_changekey = models.AutoField(db_column='Status_ChangeKey', primary_key=True)  # Field name made lowercase.
    status_change = models.IntegerField(db_column='Status_Change', blank=True, null=True)  # Field name made lowercase.
    from_status = models.IntegerField(db_column='From_Status')  # Field name made lowercase.
    to_status = models.IntegerField(db_column='To_Status')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Status_Change'


class StatusDefinitions(models.Model):
    status_definitionskey = models.AutoField(db_column='Status_DefinitionsKey', primary_key=True)  # Field name made lowercase.
    status_definitions = models.IntegerField(db_column='Status_Definitions', blank=True, null=True)  # Field name made lowercase.
    status_class = models.CharField(db_column='Status_Class', max_length=30, blank=True, null=True)  # Field name made lowercase.
    display_name = models.CharField(db_column='Display_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Status_Definitions'


class StockItem(models.Model):
    stock_item = models.CharField(db_column='Stock_Item', primary_key=True, max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    primary_vendor = models.CharField(db_column='Primary_Vendor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shape = models.CharField(db_column='Shape', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location_id = models.CharField(db_column='Location_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sales_code = models.CharField(db_column='Sales_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pick_buy_indicator = models.CharField(db_column='Pick_Buy_Indicator', max_length=1, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    stocked_uofm = models.CharField(db_column='Stocked_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    purchase_uofm = models.CharField(db_column='Purchase_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cost_uofm = models.CharField(db_column='Cost_UofM', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rd_whole_unit = models.NullBooleanField(db_column='Rd_Whole_Unit')  # Field name made lowercase.
    lot_trace = models.NullBooleanField(db_column='Lot_Trace')  # Field name made lowercase.
    lead_days = models.IntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alloy = models.CharField(db_column='Alloy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pounds_per_base_unit = models.FloatField(db_column='Pounds_Per_Base_Unit', blank=True, null=True)  # Field name made lowercase.
    dimension_1 = models.FloatField(db_column='Dimension_1', blank=True, null=True)  # Field name made lowercase.
    dimension_2 = models.FloatField(db_column='Dimension_2', blank=True, null=True)  # Field name made lowercase.
    dimension_3 = models.FloatField(db_column='Dimension_3', blank=True, null=True)  # Field name made lowercase.
    dimension_4 = models.FloatField(db_column='Dimension_4', blank=True, null=True)  # Field name made lowercase.
    dimension_5 = models.FloatField(db_column='Dimension_5', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Stock_Item'


class TfmAlloy(models.Model):
    tfm_alloy = models.CharField(db_column='TFM_Alloy', primary_key=True, max_length=50)  # Field name made lowercase.
    alloy = models.CharField(db_column='Alloy', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'TFM_Alloy'


class TaxCodeDetail(models.Model):
    tax_code_detail = models.CharField(db_column='Tax_Code_Detail', primary_key=True, max_length=50)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    taxer = models.CharField(db_column='Taxer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    post_to_gl = models.NullBooleanField(db_column='Post_To_GL')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Tax_Code_Detail'


class TaxDetail(models.Model):
    tax_detail = models.CharField(db_column='Tax_Detail', primary_key=True, max_length=50)  # Field name made lowercase.
    owner_id = models.CharField(db_column='Owner_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    owner_type = models.IntegerField(db_column='Owner_Type', blank=True, null=True)  # Field name made lowercase.
    taxer = models.CharField(db_column='Taxer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    tax_amt = models.FloatField(db_column='Tax_Amt', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    post_gl = models.NullBooleanField(db_column='Post_GL')  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Tax_Detail'


class Taxer(models.Model):
    taxer = models.CharField(db_column='Taxer', primary_key=True, max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collection_account = models.CharField(db_column='Collection_Account', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paid_account = models.CharField(db_column='Paid_Account', max_length=100, blank=True, null=True)  # Field name made lowercase.
    default_rate = models.FloatField(db_column='Default_Rate', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Taxer'


class TempId(models.Model):
    session_id = models.CharField(db_column='Session_ID', primary_key=True, max_length=50)  # Field name made lowercase.
    item = models.CharField(db_column='Item', max_length=50)  # Field name made lowercase.
    item2 = models.CharField(db_column='Item2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item3 = models.CharField(db_column='Item3', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Temp_ID'
        unique_together = (('session_id', 'item'),)


class ThirdPartyIntegration(models.Model):
    integration_key = models.AutoField(db_column='Integration_Key', primary_key=True)  # Field name made lowercase.
    integration_type = models.CharField(db_column='Integration_Type', max_length=20)  # Field name made lowercase.
    integration_name = models.CharField(db_column='Integration_Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Third_Party_Integration'


class TransactionData(models.Model):
    transaction_data = models.CharField(db_column='Transaction_Data', primary_key=True, max_length=50)  # Field name made lowercase.
    transaction_type = models.IntegerField(db_column='Transaction_Type', blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=6, blank=True, null=True)  # Field name made lowercase.
    work_date = models.DateTimeField(db_column='Work_Date', blank=True, null=True)  # Field name made lowercase.
    terminal_id = models.CharField(db_column='Terminal_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    transaction_start = models.DateTimeField(db_column='Transaction_Start', blank=True, null=True)  # Field name made lowercase.
    transaction_end = models.DateTimeField(db_column='Transaction_End', blank=True, null=True)  # Field name made lowercase.
    error_id = models.CharField(db_column='Error_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    error_text = models.CharField(db_column='Error_Text', max_length=255, blank=True, null=True)  # Field name made lowercase.
    linked_tran_int = models.IntegerField(db_column='Linked_Tran_Int', blank=True, null=True)  # Field name made lowercase.
    linked_tran_string = models.CharField(db_column='Linked_Tran_String', max_length=50, blank=True, null=True)  # Field name made lowercase.
    target_int = models.IntegerField(db_column='Target_Int', blank=True, null=True)  # Field name made lowercase.
    target_string = models.CharField(db_column='Target_String', max_length=50, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=10, blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    document = models.CharField(db_column='Document', max_length=15, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location_1 = models.CharField(db_column='Location_1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lot = models.CharField(db_column='Lot', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lot_1 = models.CharField(db_column='Lot_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    po = models.CharField(db_column='PO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    po_line = models.CharField(db_column='PO_Line', max_length=6, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    close = models.NullBooleanField(db_column='Close')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Transaction_Data'


class TransactionDefinition(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    prompt_display = models.CharField(db_column='Prompt_Display', max_length=30, blank=True, null=True)  # Field name made lowercase.
    deferred = models.NullBooleanField(db_column='Deferred')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    enabled = models.NullBooleanField(db_column='Enabled')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    ischildtrans = models.BooleanField(db_column='IsChildTrans')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Transaction_Definition'


class TransactionDetail(models.Model):
    transaction_detail = models.AutoField(db_column='Transaction_Detail', primary_key=True)  # Field name made lowercase.
    transaction_data = models.CharField(db_column='Transaction_Data', max_length=50, blank=True, null=True)  # Field name made lowercase.
    target_integer = models.IntegerField(db_column='Target_Integer', blank=True, null=True)  # Field name made lowercase.
    labor_hrs = models.FloatField(db_column='Labor_Hrs', blank=True, null=True)  # Field name made lowercase.
    machine_hrs = models.FloatField(db_column='Machine_Hrs', blank=True, null=True)  # Field name made lowercase.
    percent_complete = models.FloatField(db_column='Percent_Complete', blank=True, null=True)  # Field name made lowercase.
    entry_type = models.IntegerField(db_column='Entry_Type', blank=True, null=True)  # Field name made lowercase.
    rework = models.NullBooleanField(db_column='Rework')  # Field name made lowercase.
    rework_rsn = models.CharField(db_column='Rework_Rsn', max_length=15, blank=True, null=True)  # Field name made lowercase.
    scrap_rsn = models.CharField(db_column='Scrap_Rsn', max_length=15, blank=True, null=True)  # Field name made lowercase.
    scrap_qty = models.IntegerField(db_column='Scrap_Qty', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    complete_operation = models.NullBooleanField(db_column='Complete_Operation')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    work_center = models.CharField(db_column='Work_Center', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operation = models.CharField(db_column='Operation', max_length=10, blank=True, null=True)  # Field name made lowercase.
    linked_tran_string = models.CharField(db_column='Linked_Tran_String', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sn_oid = models.CharField(db_column='SN_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    currentusage = models.FloatField(db_column='CurrentUsage', blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    sn_isscrapped = models.BooleanField(db_column='SN_IsScrapped')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Transaction_Detail'


class TransactionSetting(models.Model):
    transaction_setting = models.CharField(db_column='Transaction_Setting', primary_key=True, max_length=50)  # Field name made lowercase.
    transaction_value = models.CharField(db_column='Transaction_Value', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=6, blank=True, null=True)  # Field name made lowercase.
    permission = models.CharField(db_column='Permission', max_length=50, blank=True, null=True)  # Field name made lowercase.
    default_value = models.CharField(db_column='Default_Value', max_length=50, blank=True, null=True)  # Field name made lowercase.
    display_text = models.CharField(db_column='Display_Text', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hidden = models.NullBooleanField(db_column='Hidden')  # Field name made lowercase.
    required = models.NullBooleanField(db_column='Required')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Transaction_Setting'


class TransactionValue(models.Model):
    transaction_value = models.CharField(db_column='Transaction_Value', primary_key=True, max_length=50)  # Field name made lowercase.
    data_type = models.IntegerField(db_column='Data_Type', blank=True, null=True)  # Field name made lowercase.
    default_value = models.CharField(db_column='Default_Value', max_length=50, blank=True, null=True)  # Field name made lowercase.
    display_text = models.CharField(db_column='Display_Text', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hidden = models.NullBooleanField(db_column='Hidden')  # Field name made lowercase.
    max_value = models.IntegerField(db_column='Max_Value', blank=True, null=True)  # Field name made lowercase.
    min_value = models.IntegerField(db_column='Min_Value', blank=True, null=True)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence', blank=True, null=True)  # Field name made lowercase.
    string_length = models.IntegerField(db_column='String_Length', blank=True, null=True)  # Field name made lowercase.
    system_required = models.NullBooleanField(db_column='System_Required')  # Field name made lowercase.
    user_required = models.NullBooleanField(db_column='User_Required')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    transaction_definition = models.IntegerField(db_column='Transaction_Definition', blank=True, null=True)  # Field name made lowercase.
    db_validation = models.NullBooleanField(db_column='DB_Validation')  # Field name made lowercase.
    confirmation_prompt = models.NullBooleanField(db_column='Confirmation_Prompt')  # Field name made lowercase.
    transaction_field = models.CharField(db_column='Transaction_Field', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Transaction_Value'


class UserCode(models.Model):
    type = models.CharField(db_column='Type', primary_key=True, max_length=8)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=25)  # Field name made lowercase.
    date1 = models.DateTimeField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    numeric1 = models.FloatField(db_column='Numeric1', blank=True, null=True)  # Field name made lowercase.
    numeric2 = models.FloatField(db_column='Numeric2', blank=True, null=True)  # Field name made lowercase.
    numeric3 = models.FloatField(db_column='Numeric3', blank=True, null=True)  # Field name made lowercase.
    numeric4 = models.FloatField(db_column='Numeric4', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    text3 = models.TextField(db_column='Text3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'User_Code'
        unique_together = (('type', 'code'),)


class UserLabels(models.Model):
    table_name = models.CharField(db_column='Table_Name', primary_key=True, max_length=50)  # Field name made lowercase.
    date1_label = models.CharField(db_column='Date1_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    date2_label = models.CharField(db_column='Date2_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    text1_label = models.CharField(db_column='Text1_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    text2_label = models.CharField(db_column='Text2_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    text3_label = models.CharField(db_column='Text3_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    text4_label = models.CharField(db_column='Text4_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    text5_label = models.CharField(db_column='Text5_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    amount1_label = models.CharField(db_column='Amount1_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    amount2_label = models.CharField(db_column='Amount2_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    numeric1_label = models.CharField(db_column='Numeric1_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    numeric2_label = models.CharField(db_column='Numeric2_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    decimal1_label = models.CharField(db_column='Decimal1_Label', max_length=12, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'User_Labels'


class UserValues(models.Model):
    user_valueskey = models.AutoField(db_column='User_ValuesKey', primary_key=True)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', unique=True, blank=True, null=True)  # Field name made lowercase.
    date1 = models.DateTimeField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date2 = models.DateTimeField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=25, blank=True, null=True)  # Field name made lowercase.
    text5 = models.CharField(db_column='Text5', max_length=25, blank=True, null=True)  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    numeric1 = models.FloatField(db_column='Numeric1', blank=True, null=True)  # Field name made lowercase.
    numeric2 = models.FloatField(db_column='Numeric2', blank=True, null=True)  # Field name made lowercase.
    decimal1 = models.FloatField(db_column='Decimal1', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'User_Values'


class Vendor(models.Model):
    vendor = models.CharField(db_column='Vendor', primary_key=True, max_length=10)  # Field name made lowercase.
    user_values = models.IntegerField(db_column='User_Values', blank=True, null=True)  # Field name made lowercase.
    ship_via = models.CharField(db_column='Ship_Via', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tax_id = models.CharField(db_column='Tax_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tax_code = models.CharField(db_column='Tax_Code', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_account = models.CharField(db_column='GL_Account', max_length=100, blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='Terms', max_length=15, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.
    vendor_since = models.DateTimeField(db_column='Vendor_Since', blank=True, null=True)  # Field name made lowercase.
    our_account_id = models.CharField(db_column='Our_Account_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    send_1099 = models.BooleanField(db_column='Send_1099')  # Field name made lowercase.
    currency_def = models.IntegerField(db_column='Currency_Def', blank=True, null=True)  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    acct_mgr = models.CharField(db_column='Acct_Mgr', max_length=6, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    qb_id = models.CharField(db_column='QB_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    send_report_by_email = models.BooleanField(db_column='Send_Report_By_Email')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Vendor'


class VendorMaterial(models.Model):
    vendor_material = models.CharField(db_column='Vendor_Material', primary_key=True, max_length=50)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    material_owner = models.CharField(db_column='Material_Owner', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_reference = models.CharField(db_column='Vendor_Reference', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sell_price = models.FloatField(db_column='Sell_Price', blank=True, null=True)  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    lead_days = models.IntegerField(db_column='Lead_Days', blank=True, null=True)  # Field name made lowercase.
    price_unit = models.CharField(db_column='Price_Unit', max_length=4, blank=True, null=True)  # Field name made lowercase.
    owner_type = models.IntegerField(db_column='Owner_Type', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Vendor_Material'


class VendorService(models.Model):
    vendor_servicekey = models.AutoField(db_column='Vendor_ServiceKey', primary_key=True)  # Field name made lowercase.
    vendor_service = models.IntegerField(db_column='Vendor_Service', blank=True, null=True)  # Field name made lowercase.
    vendor = models.ForeignKey(Vendor, models.DO_NOTHING, db_column='Vendor')  # Field name made lowercase.
    service = models.ForeignKey(Service, models.DO_NOTHING, db_column='Service')  # Field name made lowercase.
    minimum_chg = models.DecimalField(db_column='Minimum_Chg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    currency_conv_rate = models.FloatField(db_column='Currency_Conv_Rate')  # Field name made lowercase.
    trade_currency = models.IntegerField(db_column='Trade_Currency', blank=True, null=True)  # Field name made lowercase.
    fixed_rate = models.BooleanField(db_column='Fixed_Rate')  # Field name made lowercase.
    trade_date = models.DateTimeField(db_column='Trade_Date', blank=True, null=True)  # Field name made lowercase.
    lead_days = models.SmallIntegerField(db_column='Lead_Days')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Vendor_Service'


class WcdisplaySequence(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    workcenter_oid = models.CharField(db_column='WorkCenter_OID', max_length=36)  # Field name made lowercase.
    sequence = models.IntegerField(db_column='Sequence')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='Created_Date')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'WCDisplay_Sequence'


class Wcemployee(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    workcenter_oid = models.CharField(db_column='WorkCenter_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    employee_oid = models.CharField(db_column='Employee_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'WCEmployee'


class Wcmaterialclass(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    workcenter_oid = models.CharField(db_column='WorkCenter_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    class_oid = models.CharField(db_column='Class_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'WCMaterialClass'


class Wcmaterialshape(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    workcenter_oid = models.CharField(db_column='WorkCenter_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    shape_oid = models.CharField(db_column='Shape_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'WCMaterialShape'


class WcshiftOverride(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    shift_id = models.CharField(db_column='Shift_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    machines = models.IntegerField(db_column='Machines', blank=True, null=True)  # Field name made lowercase.
    operators = models.IntegerField(db_column='Operators', blank=True, null=True)  # Field name made lowercase.
    operators_per_machine = models.FloatField(db_column='Operators_Per_Machine', blank=True, null=True)  # Field name made lowercase.
    shift_type = models.IntegerField(db_column='Shift_Type', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    hours = models.FloatField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    workcenter_oid = models.CharField(db_column='WorkCenter_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    is_work_day = models.NullBooleanField(db_column='Is_Work_Day')  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'WCShift_Override'


class WcshiftStandard(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    shift_id = models.CharField(db_column='Shift_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    machines = models.IntegerField(db_column='Machines', blank=True, null=True)  # Field name made lowercase.
    operators = models.IntegerField(db_column='Operators', blank=True, null=True)  # Field name made lowercase.
    operators_per_machine = models.FloatField(db_column='Operators_Per_Machine', blank=True, null=True)  # Field name made lowercase.
    shift_type = models.IntegerField(db_column='Shift_Type', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    hours = models.FloatField(db_column='Hours', blank=True, null=True)  # Field name made lowercase.
    workcenter_oid = models.CharField(db_column='WorkCenter_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'WCShift_Standard'


class WorkcenterLoad(models.Model):
    objectid = models.CharField(db_column='ObjectID', primary_key=True, max_length=36)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    workcenter_oid = models.CharField(db_column='WorkCenter_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    resource_id = models.SmallIntegerField(db_column='Resource_ID', blank=True, null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='Created_Time', blank=True, null=True)  # Field name made lowercase.
    last_updated = models.DateTimeField(db_column='Last_Updated', blank=True, null=True)  # Field name made lowercase.
    job_operation_oid = models.CharField(db_column='Job_Operation_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    fixed = models.NullBooleanField(db_column='Fixed')  # Field name made lowercase.
    load_multiplier = models.FloatField(db_column='Load_Multiplier')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'WorkCenter_Load'


class WorkCenter(models.Model):
    work_center = models.CharField(db_column='Work_Center', primary_key=True, max_length=10)  # Field name made lowercase.
    user_values_old = models.IntegerField(db_column='User_Values_OLD', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=15, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=8)  # Field name made lowercase.
    setup_labor_rate = models.DecimalField(db_column='Setup_Labor_Rate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    run_labor_rate = models.DecimalField(db_column='Run_Labor_Rate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    labor_burden = models.FloatField(db_column='Labor_Burden', blank=True, null=True)  # Field name made lowercase.
    machine_burden = models.DecimalField(db_column='Machine_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ga_burden = models.DecimalField(db_column='GA_Burden', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sched_hrs_old = models.FloatField(db_column='Sched_Hrs_OLD', blank=True, null=True)  # Field name made lowercase.
    queue_hrs = models.FloatField(db_column='Queue_Hrs', blank=True, null=True)  # Field name made lowercase.
    nbr_limiting_rsrc_old = models.SmallIntegerField(db_column='Nbr_Limiting_Rsrc_OLD', blank=True, null=True)  # Field name made lowercase.
    capacity_old = models.FloatField(db_column='Capacity_OLD', blank=True, null=True)  # Field name made lowercase.
    link_material = models.BooleanField(db_column='Link_Material')  # Field name made lowercase.
    link_component = models.BooleanField(db_column='Link_Component')  # Field name made lowercase.
    note_text = models.TextField(db_column='Note_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_updated = models.DateTimeField(db_column='Last_Updated')  # Field name made lowercase.
    is_parent = models.NullBooleanField(db_column='Is_Parent')  # Field name made lowercase.
    has_parent = models.NullBooleanField(db_column='Has_Parent')  # Field name made lowercase.
    parent_id = models.CharField(db_column='Parent_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectID', unique=True, max_length=36)  # Field name made lowercase.
    machines = models.IntegerField(db_column='Machines', blank=True, null=True)  # Field name made lowercase.
    operators = models.IntegerField(db_column='Operators', blank=True, null=True)  # Field name made lowercase.
    operators_per_machine = models.FloatField(db_column='Operators_Per_Machine', blank=True, null=True)  # Field name made lowercase.
    parent_oid = models.CharField(db_column='Parent_OID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    link_finishedgoods = models.NullBooleanField(db_column='Link_FinishedGoods')  # Field name made lowercase.
    link_hardware = models.NullBooleanField(db_column='Link_Hardware')  # Field name made lowercase.
    link_supplies = models.NullBooleanField(db_column='Link_Supplies')  # Field name made lowercase.
    link_misc = models.NullBooleanField(db_column='Link_Misc')  # Field name made lowercase.
    link_rawstock = models.NullBooleanField(db_column='Link_RawStock')  # Field name made lowercase.
    finite_schedule = models.NullBooleanField(db_column='Finite_Schedule')  # Field name made lowercase.
    lag_hrs = models.FloatField(db_column='Lag_Hrs', blank=True, null=True)  # Field name made lowercase.
    uvdate1 = models.DateTimeField(db_column='UVDate1', blank=True, null=True)  # Field name made lowercase.
    uvdate2 = models.DateTimeField(db_column='UVDate2', blank=True, null=True)  # Field name made lowercase.
    uvtext1 = models.CharField(db_column='UVText1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uvtext2 = models.CharField(db_column='UVText2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uvtext3 = models.CharField(db_column='UVText3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uvtext4 = models.CharField(db_column='UVText4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uvtext5 = models.CharField(db_column='UVText5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uvamount1 = models.DecimalField(db_column='UVAmount1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    uvamount2 = models.DecimalField(db_column='UVAmount2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    uvnumeric1 = models.FloatField(db_column='UVNumeric1', blank=True, null=True)  # Field name made lowercase.
    uvnumeric2 = models.FloatField(db_column='UVNumeric2', blank=True, null=True)  # Field name made lowercase.
    uvdecimal1 = models.FloatField(db_column='UVDecimal1', blank=True, null=True)  # Field name made lowercase.
    uvnote_text = models.TextField(db_column='UVNote_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    equipment = models.NullBooleanField(db_column='Equipment')  # Field name made lowercase.

    class Meta:
        managed = IS_TEST
        db_table = 'Work_Center'
