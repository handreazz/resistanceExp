import psycopg2
from Genome.context.config import config

params = config()
#params['database'] = 'hermuba'

conn = psycopg2.connect(**params)
cur = conn.cursor()

table_name = 'blastp_out_max_evalue'


cur.execute("""
ALTER TABLE {0}
ADD COLUMN trans_evalue decimal

""".format(table_name))
cur.execute("""
UPDATE {0}
SET trans_evalue =  log_evalue(evalue)


""".format(table_name))


conn.commit()
cur.close()
conn.close()
