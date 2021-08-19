# Copyright (c) 2020 Sarthak Mittal
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FIELD_TYPES = {
    "general": 0,
    "optional": 1,
    "amount": 2,
    "date": 3
}

FIELDS = dict()

FIELDS["invoice_no"] = FIELD_TYPES["general"]
FIELDS["vendor_name"] = FIELD_TYPES["general"]
FIELDS["date"] = FIELD_TYPES["date"]
FIELDS["amount"] = FIELD_TYPES["general"]
FIELDS["tax_amount"] = FIELD_TYPES["amount"]
FIELDS["1st_sign_id"] = FIELD_TYPES["date"]
FIELDS["2st_sign_id"] = FIELD_TYPES["date"]
FIELDS["vendor_no"] = FIELD_TYPES["general"]
FIELDS["beneficiary_name"] = FIELD_TYPES["general"]
FIELDS["bl_no"] = FIELD_TYPES["general"]
FIELDS["port_of_loading"] = FIELD_TYPES["general"]
FIELDS["customs_declaration_no"] = FIELD_TYPES["general"]
FIELDS["po_no"] = FIELD_TYPES["general"]
FIELDS["clearance_date"] = FIELD_TYPES["date"]
FIELDS["vat_mount"] = FIELD_TYPES["amount"]
FIELDS["import_tax_amount"] = FIELD_TYPES["amount"]
FIELDS["vendor_code"] = FIELD_TYPES["optional"]
