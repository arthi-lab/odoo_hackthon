{
    'name': 'Inventory Management System (IMS)',
    'version': '1.0',
    'summary': 'Modular IMS for digitizing stock operations',
    'description': """
        A centralized, real-time inventory management system.
        - Incoming Stocks (Receipts)
        - Outgoing Stocks (Delivery Orders)
        - Internal Transfers
        - Stock Adjustments
        - Reordering Rules
        - Inventory Dashboard
    """,
    'category': 'Inventory/Inventory',
    'author': 'Antigravity',
    'depends': ['stock', 'product', 'mail', 'auth_signup'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/operation_views.xml',
        'views/dashboard_views.xml',
        'views/setting_views.xml',
        'views/auth_templates.xml',
        'data/cron_data.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'stock_ims/static/src/css/ims_dashboard.css',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
