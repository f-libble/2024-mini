import urequests as requests
import json
import time
import random
from machine import Pin
import network

# Replace with your hotspot's SSID and password
ssid = "BU Guest (unencrypted)"
password = ""

# Initialize the network interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection
max_attempts = 10
attempts = 0
while not wlan.isconnected() and attempts < max_attempts:
    print('Connecting to network...')
    time.sleep(1)
    attempts += 1

if wlan.isconnected():
    print('Network connected:', wlan.ifconfig())
else:
    print('Failed to connect to network')

# Continue with the rest of your code if connected
if wlan.isconnected():
    # Firebase configuration
    firebase_url = "https://ec-463-mini-project-611d6-default-rtdb.firebaseio.com/users/{user_id}/scores.json"
    user_id = "PpRkstZSPIQgh4W1aPYUbN4zZzg1"  # Replace with the authenticated user's ID

    N = 10  # Number of flashes
    sample_ms = 10.0
    on_ms = 500
    debounce_ms = 50  # Debounce time in milliseconds

    def random_time_interval(tmin: float, tmax: float) -> float:
        """Return a random time interval between min and max."""
        return random.uniform(tmin, tmax)

    def blinker(N: int, led: Pin) -> None:
        """Blink the LED N times."""
        for _ in range(N):
            led.high()
            time.sleep(0.1)
            led.low()
            time.sleep(0.1)

    def write_json(json_filename: str, data: dict) -> None:
        """Writes data to a JSON file."""
        with open(json_filename, "w") as f:
            json.dump(data, f)

    def scorer(t: list[int | None]) -> None:
        """Calculate and print response times."""
        misses = t.count(None)
        print(f"You missed the light {misses} / {len(t)} times")

        t_good = [x for x in t if x is not None]

        if t_good:
            avg_response = sum(t_good) / len(t_good)
            min_response = min(t_good)
            max_response = max(t_good)
        else:
            avg_response = min_response = max_response = None

        print(f"Response Times: {t_good}")
        print(f"Average Response Time: {avg_response} ms")
        print(f"Minimum Response Time: {min_response} ms")
        print(f"Maximum Response Time: {max_response} ms")

        data = {
            "average_response_time_ms": avg_response,
            "minimum_response_time_ms": min_response,
            "maximum_response_time_ms": max_response,
            "score": (len(t) - misses) / len(t)
        }

        now = time.localtime()
        now_str = "-".join(map(str, now[:3])) + "T" + "_".join(map(str, now[3:6]))
        filename = f"score-{now_str}.json"

        print("write", filename)
        write_json(filename, data)

        # Send data to Firebase
        url = firebase_url.format(user_id=user_id)
        response = requests.post(url, data=json.dumps(data))
        print(f"Data sent to Firebase: {response.status_code}")

    def debounce(pin: Pin) -> bool:
        """Debounce the button press."""
        if pin.value() == 0:
            print("Button press detected")
            time.sleep(debounce_ms / 1000)  # Wait for debounce time
            if pin.value() == 0:  # Check if still pressed
                return True
        return False

    if __name__ == "__main__":
        led = Pin("LED", Pin.OUT)
        button = Pin(12, Pin.IN, Pin.PULL_UP)

        t: list[int | None] = []

        blinker(3, led)

        for i in range(N):
            time.sleep(random_time_interval(0.5, 5.0))

            led.high()

            tic = time.ticks_ms()
            t0 = None
            while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
                if debounce(button):
                    t0 = time.ticks_diff(time.ticks_ms(), tic)
                    print(f"Button press time: {t0} ms")
                    led.low()
                    break
            t.append(t0)

            led.low()

        blinker(5, led)

        scorer(t)

