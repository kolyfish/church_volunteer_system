import random


def auto_schedule_volunteers(service_date_id, db):
    # 擷取當前的服務類型
    service_types = db.query("SELECT * FROM ServiceType")

    # 每個服務類型進行排班
    for service_type in service_types:
        service_type_id = service_type['id']

        # 資格檢查：找到符合條件的志工
        qualified_volunteers = db.query("""
            SELECT v.id, v.name FROM Volunteer v
            JOIN VolunteerSkill vs ON v.id = vs.volunteer_id
            WHERE vs.service_type_id = ? AND v.is_active = TRUE
        """, [service_type_id])

        # 確認志工是否在特定日期可用
        day_of_week = db.query("""
            SELECT strftime('%w', service_date) as dow 
            FROM ServiceDate 
            WHERE id = ?
        """, [service_date_id])[0]['dow']

        available_volunteers = [
            volunteer for volunteer in qualified_volunteers
            if db.query("""
                SELECT is_available
                FROM VolunteerAvailability
                WHERE volunteer_id = ? AND day_of_week = ?
            """, [volunteer['id'], day_of_week])
        ]

        # 根據最近10次排班次數排序
        for volunteer in available_volunteers:
            volunteer['schedule_count'] = db.query("""
                SELECT COUNT(*) as count
                FROM VolunteerSchedule
                WHERE volunteer_id = ?
                AND service_date_id > (SELECT MAX(id) - 10 FROM ServiceDate)
            """, [volunteer['id']])[0]['count']

        # 優先選擇服侍次數較少的志工，並隨機打散
        available_volunteers.sort(key=lambda v: v['schedule_count'])
        random.shuffle(available_volunteers)

        # 確認所需人數，並進行排班
        for _ in range(service_type['required_volunteers']):
            if available_volunteers:
                selected_volunteer = available_volunteers.pop(0)
                db.execute("""
                    INSERT INTO VolunteerSchedule (volunteer_id, service_type_id, service_date_id)
                    VALUES (?, ?, ?)
                """, [selected_volunteer['id'], service_type_id, service_date_id])

    print("排班已完成！")
