import firebase_admin, time
from firebase_admin import credentials, auth, db
from firebase_admin.exceptions import FirebaseError

# Initialize Firebase
cred = credentials.Certificate("ec-463-mini-project-611d6-firebase-adminsdk-v5cy4-2be1bc3cd3.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ec-463-mini-project-611d6-default-rtdb.firebaseio.com/'
})


def create_user(email: str):
    user = auth.create_user(
        email=email,
        email_verified=False,
        disabled=False
    )
    print('Successfully created new user:', user.uid)

    # Store user data in the Realtime Database
    ref = db.reference(f'users/{user.uid}')
    ref.set({
        'email': email
        # 'created_at': time.time()
    })

    return user.uid

def authenticate_user(email: str) -> str:
    try:
        user = auth.get_user_by_email(email)
        return user.uid
    except FirebaseError as e:
        print(f"Error authenticating user: {e}")
        return None

def get_user_data(user_id: str):
    try:
        ref = db.reference(f'users/{user_id}')
        user_data = ref.get()
        if user_data:
            print(f"User Data for {user_id}:")
            for score_id, score_data in user_data.get('scores', {}).items():
                print(f"  Score ID: {score_id}")
                print(f"    Average Response Time: {score_data.get('average_response_time_ms', 'N/A')} ms")
                print(f"    Minimum Response Time: {score_data.get('minimum_response_time_ms', 'N/A')} ms")
                print(f"    Maximum Response Time: {score_data.get('maximum_response_time_ms', 'N/A')} ms")
                print(f"    Score: {score_data.get('score', 'N/A')}")
        else:
            print(f"No data found for user {user_id}")
    except FirebaseError as e:
        print(f"Error retrieving user data: {e}")

if __name__ == "__main__":
    action = input("Do you want to (r)egister, (l)ogin, or (v)iew data? ")

    email = input("Enter your email: ")

    if action == 'r':
        user_id = create_user(email)
    elif action == 'l':
        user_id = authenticate_user(email)
    elif action == 'v':
        user_id = authenticate_user(email)
        if user_id:
            get_user_data(user_id)

    if user_id and action in ['r', 'l']:
        print(f"User ID: {user_id}")
        with open("user_credentials.txt", "w") as f:
            f.write(user_id)
    elif action in ['r', 'l']:
        print("Authentication failed")
