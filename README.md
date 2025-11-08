# Require-analytical-MRP-Odoo16
It forces the user to enter an analytic account in Odoo’s manufacturing module
# Requiere Analítica MRP

## Overview
This Odoo 16 module makes the **analytic account mandatory** on manufacturing orders (MRP).  
It ensures that every manufacturing order is linked to an analytic account, helping maintain consistent cost tracking and financial control within production operations.

## Features
- Enforces analytic account requirement in Manufacturing Orders.
- Integrates seamlessly with the Odoo Manufacturing (`mrp`) module.
- Simple and lightweight implementation.
- Helps improve analytic and cost accounting accuracy.

## Installation
1. Download or clone this repository into your Odoo addons folder:
Restart your Odoo server.

Activate the Developer Mode in Odoo.

Go to Apps → Update Apps List.

Search for Requiere Analítica MRP and click Install.

Usage
Navigate to Manufacturing → Manufacturing Orders.

When creating or editing an order, you will be required to select an Analytic Account.

The form cannot be saved without selecting an analytic account.

Compatibility
Odoo 16.0

Depends on the core MRP module

Author
José Luis Ruiz Verdugo

License
This module is licensed under the LGPL-3 License.
See the LICENSE file for details.

