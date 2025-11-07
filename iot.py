
import time
import random
import firebase_admin
from firebase_admin import credentials, db
cred = credentials.Certificate("/content/sol-iot-firebase-adminsdk-fbsvc-230d04dd93.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sol-iot-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')

def simulate_pc():
    pc_id = random.randint(1, 100)
    temp = random.uniform(45, 80)
    efficiency = 100 - (temp - 40) * 1.2
    internet_speed = random.uniform(50, 120)
    usage_time = random.uniform(10, 120)
    cost = round(usage_time * 0.1, 2)
    pollution = round(temp * 0.03 + random.uniform(0.1, 0.5), 2)
    activities = ["anime", "film", "web", "gaming"]
    activity = random.choice(activities)
    return {
        "pc_id": f"PC_{pc_id}",
        "temp": round(temp, 2),
        "efficiency": round(efficiency, 2),
        "internet": round(internet_speed, 2),
        "usage": round(usage_time, 2),
        "cost": cost,
        "pollution": pollution,
        "activity": activity,
        "timestamp": time.time()
    }


while True:
        
        data = simulate_pc()
        ref.push(data)
        print(f"✅ Envoyé vers Firebase : {data}")
        time.sleep(10)
