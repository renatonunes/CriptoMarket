import sqlite3

def inserir_usuario(banco, first_name, last_name, id_telegram):
    conn = sqlite3.connect(banco)
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO usuarios (first_name, last_name, id_telegram) VALUES (?, ?, ?)
    ''', (first_name, last_name, id_telegram))
    
    conn.commit()
    conn.close()

    print("deu boa")

def usuario_existe(banco, id_telegram):
    conn = sqlite3.connect(banco)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id_telegram = ?', (id_telegram,))
    usuario = cursor.fetchone()

    return usuario is not None