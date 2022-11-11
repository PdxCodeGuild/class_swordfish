import dlib
import face_recognition
import csv

"""Do I Know You?"""

# """Compare an unknown person's picture against a known"""
# known_image = face_recognition.load_image_file("/Users/rcleav/Desktop/PDX_projects/class_swordfish/code/rachel/Python/people_I_know/sandy_harris.jpeg")
# known_image_encoding = face_recognition.face_encodings(known_image)[0] #index 0 indicates first encoding / image of face
# unknown_image = known_image = face_recognition.load_image_file("/Users/rcleav/Desktop/PDX_projects/class_swordfish/code/rachel/Python/Unknown/Unknown3.jpeg")
# unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]
# compare_images = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)
# if compare_images[0] == True:
#     print("You know them!")
# else:
#     print("This isn't the person you're looking for.")

"""This also works for images with multiple people"""

sandy_harris = face_recognition.load_image_file("/Users/rcleav/Desktop/PDX_projects/class_swordfish/code/rachel/Python/people_I_know/sandy_harris.jpeg")
unknown_image = face_recognition.load_image_file("/Users/rcleav/Desktop/PDX_projects/class_swordfish/code/rachel/Python//Unknown/Unknown5.jpeg")
known_image_encoding = face_recognition.face_encodings(sandy_harris)[0]
unknown_image_encoding = face_recognition.face_encodings(unknown_image)
compare_images = face_recognition.compare_faces(known_image_encoding, unknown_image_encoding)

unknown_image_file = "/Users/rcleav/Desktop/PDX_projects/class_swordfish/code/rachel/Python/people_I_know/sandy_harris.jpeg"
if compare_images[0] == True:
    print("You know them!")
else:
    add_to_file = input("This person is not in your address book; do you want to add them? Y/N ")
    if add_to_file == "Y":
        name = input("Name: ")
        contact_info = input("Contact info: ")
        friends = input("Friends: ")
        notes = input("Notes: ")
        with open('address_book.csv', mode='w') as f:
            fieldnames = ['name', 'contact_info', 'friends', 'notes', 'photos']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name': name, 'contact_info': contact_info, 'friends': friends, 'notes': notes, 'photos': unknown_image_file})
    else:
        print("Maybe next time")


