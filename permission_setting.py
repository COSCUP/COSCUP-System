#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys

self_permission = { 
    'role': 'self',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin'], 'write':['self'] },
                'language': { 'read': ['self', 'admin'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin'], 'write':['self'] },
                'others': { 'read': ['self', 'admin'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}

admin_permission = { 
    'role': 'admin',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin'], 'write':['self'] },
                'language': { 'read': ['self', 'admin'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin'], 'write':['self'] },
                'others': { 'read': ['self', 'admin'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}

team_admin_permission = { 
    'role': 'team-admin',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin', 'team-admin'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin', 'team-admin'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin', 'team-admin'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin', 'team-admin'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin', 'team-admin'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin', 'team-admin'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin', 'team-admin'], 'write':['self'] },
                'language': { 'read': ['self', 'admin', 'team-admin'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin', 'team-admin'], 'write':['self'] },
                'others': { 'read': ['self', 'admin', 'team-admin'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}

team_committee_permission = { 
    'role': 'team-committee',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin', 'team-committee'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin', 'team-committee'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin', 'team-committee'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin', 'team-committee'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin', 'team-committee'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin', 'team-committee'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin', 'team-committee'], 'write':['self'] },
                'language': { 'read': ['self', 'admin', 'team-committee'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin', 'team-committee'], 'write':['self'] },
                'others': { 'read': ['self', 'admin', 'team-committee'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}


team_field_permission = { 
    'role': 'team-field',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin', 'team-field'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin', 'team-field'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin', 'team-field'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin', 'team-field'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin', 'team-field'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin', 'team-field'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin', 'team-field'], 'write':['self'] },
                'language': { 'read': ['self', 'admin', 'team-field'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin', 'team-field'], 'write':['self'] },
                'others': { 'read': ['self', 'admin', 'team-field'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}

team_sales_permission = { 
    'role': 'team-sales',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin', 'team-sales'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin', 'team-sales'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin', 'team-sales'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin', 'team-sales'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin', 'team-sales'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin', 'team-sales'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin', 'team-sales'], 'write':['self'] },
                'language': { 'read': ['self', 'admin', 'team-sales'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin', 'team-sales'], 'write':['self'] },
                'others': { 'read': ['self', 'admin', 'team-sales'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}

team_cpr_permission = { 
    'role': 'team-cpr',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin', 'team-cpr'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin', 'team-cpr'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin', 'team-cpr'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin', 'team-cpr'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin', 'team-cpr'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin', 'team-cpr'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin', 'team-cpr'], 'write':['self'] },
                'language': { 'read': ['self', 'admin', 'team-cpr'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin', 'team-cpr'], 'write':['self'] },
                'others': { 'read': ['self', 'admin', 'team-cpr'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}

team_marketing_permission = { 
    'role': 'team-marketing',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin', 'team-marketing'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin', 'team-marketing'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin', 'team-marketing'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin', 'team-marketing'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin', 'team-marketing'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin', 'team-marketing'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin', 'team-marketing'], 'write':['self'] },
                'language': { 'read': ['self', 'admin', 'team-marketing'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin', 'team-marketing'], 'write':['self'] },
                'others': { 'read': ['self', 'admin', 'team-marketing'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}

team_accountant_permission = { 
    'role': 'team-accountant',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin', 'team-accountant'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin', 'team-accountant'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin', 'team-accountant'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin', 'team-accountant'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin', 'team-accountant'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin', 'team-accountant'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin', 'team-accountant'], 'write':['self'] },
                'language': { 'read': ['self', 'admin', 'team-accountant'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin', 'team-accountant'], 'write':['self'] },
                'others': { 'read': ['self', 'admin', 'team-accountant'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}

cashier_permission = { 
    'role': 'cashier',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin', 'cashier'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin', 'cashier'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin', 'cashier'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin', 'cashier'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin', 'cashier'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin', 'cashier'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin', 'cashier'], 'write':['self'] },
                'language': { 'read': ['self', 'admin', 'cashier'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin', 'cashier'], 'write':['self'] },
                'others': { 'read': ['self', 'admin', 'cashier'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}

team_archiving_permission = { 
    'role': 'team-archiving',
    'fields': { 'id': { 'read': [], 'write': ['self'] },
                'team': { 'read': [], 'write': ['self'] },
                'last_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'first_name': { 'read': ['self', 'admin'], 'write': ['self'] },
                'nickname': { 'read': [], 'write': ['self'] },
                'gender': { 'read': ['self', 'admin', 'team-archiving'], 'write': ['self'] },
                'email': { 'read': ['self', 'admin', 'team-archiving'], 'write': ['self'] },
                'phone': { 'read': ['self', 'admin'], 'write': ['self'] },
                't-shirt': { 'read': ['self', 'admin'], 'write': ['self'] },
                'food': { 'read': ['self', 'admin'], 'write': ['self'] },
                'certificate': { 'read': ['self', 'admin', 'team-archiving'], 'write': ['self'] },
                'accommodation': { 'read': ['self', 'admin', 'team-archiving'], 'write': ['self'] },
                'traffic': { 'read': ['self', 'admin', 'team-archiving'], 'write': ['self'] },
                'origin': { 'read': ['self', 'admin', 'team-archiving'], 'write':['self'] },
                'birthday': { 'read': ['self', 'admin'], 'write':['self'] },
                'new': { 'read': ['self', 'admin', 'team-archiving'], 'write':['self'] },
                'language': { 'read': ['self', 'admin', 'team-archiving'], 'write':['self'] },
                'skill': { 'read': ['self', 'admin', 'team-archiving'], 'write':['self'] },
                'others': { 'read': ['self', 'admin', 'team-archiving'], 'write':['self'] },
                'redmine': { 'read': [], 'write':['self'] },
                'project': { 'read': [], 'write':['self', 'admin'] },
                'role': { 'read': [], 'write':['admin'] },
                'comment': { 'read': ['admin'], 'write':['admin'] },
    }
}
