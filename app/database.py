import sqlite3

def initialize_database():
    conn = sqlite3.connect('database/church.db')
    cursor = conn.cursor()

    # 志工表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Volunteer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 服侍類型表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ServiceType (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 服侍日期表
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ServiceDate (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_date DATE NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 志工能力表 (多對多關聯)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS VolunteerSkill (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        volunteer_id INTEGER NOT NULL,
        service_type_id INTEGER NOT NULL,
        FOREIGN KEY (volunteer_id) REFERENCES Volunteer(id),
        FOREIGN KEY (service_type_id) REFERENCES ServiceType(id),
        UNIQUE(volunteer_id, service_type_id)
    )
    """)

    # 志工排班表 (多對多關聯)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS VolunteerSchedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        volunteer_id INTEGER NOT NULL,
        service_type_id INTEGER NOT NULL,
        service_date_id INTEGER NOT NULL,
        status TEXT DEFAULT 'scheduled',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (volunteer_id) REFERENCES Volunteer(id),
        FOREIGN KEY (service_type_id) REFERENCES ServiceType(id),
        FOREIGN KEY (service_date_id) REFERENCES ServiceDate(id)
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()