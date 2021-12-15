import psycopg2
from psycopg2 import sql

def ensure_connections(func):
    def inner(*args, **kwargs):
        with psycopg2.connect('postgres://yspcmtqjeuhrqn:ab397b5f3639ed6a483aac2d3f2ecddc4f7397f92eb7c424475e0de26cbc794f@ec2-3-228-75-39.compute-1.amazonaws.com:5432/deol41la4md6ih') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res

    return inner

@ensure_connections
def init_db(conn, force: bool = False): 
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS users')
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id          SERIAL PRIMARY KEY,
            user_id                 TEXT,
            nomorsuratpengantar     TEXT,
            nomorsuratkematian      TEXT,
            tanggalsuratpengantar   TEXT,
            tanggalsuratkematian    TEXT,
            namapemohon             TEXT,
            namakematian            TEXT,
            namapelapor             TEXT,
            jeniskelaminpemohon     TEXT,
            jeniskelaminkematian    TEXT,
            jeniskelaminpelapor     TEXT,
            ttlpemohon              TEXT,
            ttlkematian             TEXT,
            ttlpelapor              TEXT,
            statuspemohon           TEXT,
            agamapemohon            TEXT,
            pekerjaanpemohon        TEXT,
            nikpemohon              TEXT,
            nikkematian             TEXT,
            nikpelapor              TEXT,
            nokkkematian            TEXT,
            pbbpemohon              TEXT,
            alamatpemohon           TEXT,
            alamatkematian          TEXT,
            alamatpelapor           TEXT,
            keperluanpemohon        TEXT,
            waktukematian           TEXT,
            hubungankematian        TEXT
            )
    ''')
    conn.commit()

@ensure_connections
def reg_db_pengantar(conn, nomorsuratpengantar: str, tanggalsuratpengantar: str, namapemohon: str, 
                            ttlpemohon: str, jeniskelaminpemohon: str, statuspemohon: str, agamapemohon: str, 
                            pekerjaanpemohon: str, nikpemohon: str, pbbpemohon: str, alamatpemohon: str, 
                            keperluanpemohon: str):
    c = conn.cursor()
    c.execute("""INSERT INTO users (nomorsuratpengantar, tanggalsuratpengantar, namapemohon, ttlpemohon, 
                                    jeniskelaminpemohon, statuspemohon, agamapemohon, pekerjaanpemohon, nikpemohon, 
                                    pbbpemohon, alamatpemohon, keperluanpemohon) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
              (nomorsuratpengantar, tanggalsuratpengantar, namapemohon, ttlpemohon, 
                                    jeniskelaminpemohon, statuspemohon, agamapemohon, pekerjaanpemohon, nikpemohon, 
                                    pbbpemohon, alamatpemohon, keperluanpemohon))
    conn.commit()

@ensure_connections
def reg_db_kematian(conn, nomorsuratkematian: str, tanggalsuratkematian: str, namakematian: str, namapelapor: str, hubungankematian: str, 
                            ttlkematian: str, ttlpelapor: str, jeniskelaminkematian: str, jeniskelaminpelapor: str, nikpelapor: str, 
                            nokkkematian: str, nikkematian: str, alamatpelapor: str, alamatkematian: str, 
                            waktukematian: str):
    c = conn.cursor()
    c.execute("""INSERT INTO users (nomorsuratkematian, tanggalsuratkematian, namakematian, namapelapor, 
                                    hubungankematian, ttlkematian, ttlpelapor, jeniskelaminkematian, jeniskelaminpelapor, 
                                    nikpelapor, nokkkematian, nikkematian, alamatpelapor, alamatkematian, waktukematian) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
              (nomorsuratkematian, tanggalsuratkematian, namakematian, namapelapor, 
                                    hubungankematian, ttlkematian, ttlpelapor, jeniskelaminkematian, jeniskelaminpelapor, 
                                    nikpelapor, nokkkematian, nikkematian, alamatpelapor, alamatkematian, waktukematian))
    conn.commit()

@ensure_connections
def get_infopengantar(conn, nomorsuratpengantar: str):
    c = conn.cursor()
    c.execute("""SELECT * FROM users WHERE nomorsuratpengantar::text=%s""", (nomorsuratpengantar,))
    return c.fetchone()

@ensure_connections
def get_infokematian(conn, nomorsuratkematian: str):
    c = conn.cursor()
    c.execute("""SELECT * FROM users WHERE nomorsuratkematian::text=%s""", (nomorsuratkematian,))
    return c.fetchone()

@ensure_connections
def check_nomorsuratpengantar(conn, nomorsuratpengantar: str):  # mengecek ketersediaan user di database
    c = conn.cursor()
    c.execute("""SELECT EXISTS(SELECT * FROM users WHERE nomorsuratpengantar::text=%s);""", (nomorsuratpengantar,))
    return c.fetchone()

@ensure_connections
def check_nomorsuratkematian(conn, nomorsuratkematian: str):  # mengecek ketersediaan user di database
    c = conn.cursor()
    c.execute("""SELECT EXISTS(SELECT * FROM users WHERE nomorsuratkematian::text=%s);""", (nomorsuratkematian,))
    return c.fetchone()
    
if __name__ == '__main__':
    init_db()