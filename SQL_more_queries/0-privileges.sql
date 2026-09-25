-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN, SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN ON *.* FROM 'user_0d_1'@'localhost', 'user_0d_2'@'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
