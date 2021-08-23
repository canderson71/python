#******************************
#
# NAME      : db_tables.py
# AUthOR    : Chris Anderson
# EMAIL     : chris.anderson@andersonleatherworks.com
# DATE      : 08/22/2021
# PURPOSE   : This file contains database tables construct
#
#******************************

class dbtables:
    def _make_tables():
        TABLES = {}
        TABLES['lwprojects'] = (
            'CREATE TABLE `lwprojects` ('
            '  `project_id` int(11) NOT NULL AUTO_INCREMENT,'
            '  `cost` decimal(10,2) NOT NULL,'
            '  `total_cost` decimal(10,2) NOT NULL,'
            '  `markup` decimal(10,2) NOT NULL,'
            '  `labor_hours` decimal(10,2) NOT NULL,'
            '  `sell_price` decimal(10,2) NOT NULL,'
            '  `adjusted` decimal(10,2) NOT NULL,'
            '  `profit` decimal(10,2) NOT NULL,'
            '  `hardware1_id` int(11) NOT NULL,'
            '  `hardware1_qty` decimal(10,2) NOT NULL,'
            '  `hardware2_id` int(11) NOT NULL,'
            '  `hardware2_qty` decimal(10,2) NOT NULL,'
            '  `hardware3_id` int(11) NOT NULL,'
            '  `hardware3_qty` decimal(10,2) NOT NULL,'
            '  `hardware4_id` int(11) NOT NULL,'
            '  `hardware4_qty` decimal(10,2) NOT NULL,'
            '  `hardware5_id` int(11) NOT NULL,'
            '  `hardware5_qty` decimal(10,2) NOT NULL,'
            '  `hardware6_id` int(11) NOT NULL,'
            '  `hardware6_qty` decimal(10,2) NOT NULL,'
            '  `hardware7_id` int(11) NOT NULL,'
            '  `hardware7_qty` decimal(10,2) NOT NULL,'
            '  `hardware8_id` int(11) NOT NULL,'
            '  `hardware8_qty` decimal(10,2) NOT NULL,'
            '  `hardware9_id` int(11) NOT NULL,'
            '  `hardware9_qty` decimal(10,2) NOT NULL,'
            '  `hardware10_id` int(11) NOT NULL,'
            '  `hardware10_qty` decimal(10,2) NOT NULL,'
            '  PRIMARY KEY (`project_id`)'
            ') ENGINE=InnoDB')

        TABLES['lwlabor'] = (
            'CREATE TABLE `lwlabor` ('
            '  `labor_id` int(11) NOT NULL AUTO_INCREMENT,'
            '  `annual_expnesies` decimal(10,2) NOT NULL,'
            '  `annual_sallary` decimal(10,2) NOT NULL,'
            '  `total_expenses` decimal(10,2) NOT NULL,'
            '  `work_weeks` decimal(2) NOT NULL,'
            '  `daily_hours` decimal(2) NOT NULL,'
            '  `days_per_week` decimal(1) NOT NULL,'
            '  `expenses_per_day` decimal(10,2) NOT NULL,'
            '  `shop_rate` decimal(10,2) NOT NULL,'
            '  PRIMARY KEY (`labor_id`)'
            ') ENGINE=InnoDB')

        TABLES['lwcosts'] = (
            'CREATE TABLE `lwcosts` ('
            '  `cost_id` int(11) NOT NULL AUTO_INCREMENT,'
            '  `cost` decimal(10,2) NOT NULL,'
            '  `total_cost` decimal(10,2) NOT NULL,'
            '  `markup` decimal(10,2) NOT NULL,'
            '  `labor_hours` decimal(10,2) NOT NULL,'
            '  `sell_price` decimal(10,2) NOT NULL,'
            '  `adjusted` decimal(10,2) NOT NULL,'
            '  `profit` decimal(10,2) NOT NULL,'
            '  PRIMARY KEY (`cost_id`)'
            ') ENGINE=InnoDB')

        TABLES['lwhardware'] = (
            'CREATE TABLE `lwhardware` ('
            '  `hardware_id` int(11) NOT NULL AUTO_INCREMENT,'
            '  `hardware_name` varchar(50) NOT NULL,'
            '  `hardware_cost_per_each` decimal(10,2) NOT NULL,'
            '  PRIMARY KEY (`hardware_id`)'
            ') ENGINE=InnoDB')
        return TABLES