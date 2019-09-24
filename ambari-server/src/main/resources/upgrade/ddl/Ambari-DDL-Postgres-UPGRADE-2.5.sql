DO $$
    BEGIN
        IF EXISTS
            ( SELECT 1
              FROM   information_schema.tables
              WHERE  table_schema = 'ambari'
              AND    table_name = 'cluster_version'
            )
        THEN
                UPDATE ambari.cluster_version SET state='CURRENT'
                where repo_version_id=(SELECT repo_version_id FROM ambari.repo_version);
        END IF ;
        IF EXISTS
            ( SELECT 1
              FROM   information_schema.tables
              WHERE  table_schema = 'ambari'
              AND    table_name = 'host_version'
            )
        THEN
                UPDATE ambari.host_version SET state='INSTALLED';
                UPDATE ambari.host_version SET state='CURRENT' WHERE repo_version_id = (select max(repo_version_id) from ambari.repo_version) and state='INSTALLED';
        END IF ;
    END
   $$ ;
