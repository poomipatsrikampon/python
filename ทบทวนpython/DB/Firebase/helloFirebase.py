import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Users/arm/Desktop/Poomipat/python/ทบทวนpython/DB/Firebase/hello-world-firebase-1-firebase-adminsdk-f3wyg-8126824613.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
  'databaseURL': 'https://hello-world-firebase-1-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('')
# data =ref.get()
# print(data['Sommai']['age'])
"""
posts_ref = ref.child('Users')

new_post_ref = posts_ref.push()
new_post_ref.set({
    'author': 'gracehop',
    'title': 'Announcing COBOL, a New Programming Language'
})

# We can also chain the two calls together
posts_ref.push().set({
    'author': 'alanisawesome',
    'title': 'The Turing Machine'
})

"""

"""
hopper_ref = ref.child('gracehop')
hopper_ref.update({
    'nickname': 'Amazing'
})
"""

hopper_ref = ref.child('text')
hopper_ref.delete()
print(ref.get())