import dropbox
import convertapi
import cloudinary
import cloudinary.uploader
import cloudinary.api
import pathlib
import pandas as pd
import dropbox
from dropbox.exceptions import AuthError

# convertapi.api_secret = 'test_grayscale.txt'
# convertapi.convert('jpg', {
#     'File': '/Users/alden/Desktop/code-guild/class_swordfish/code/alden/python/test_grayscale.txt'
# }, from_format = 'txt').save_files('/Users/alden/Desktop/code-guild/class_swordfish/code/alden/python')
# CLOUDINARY_URL=cloudinary://994283729819321:gSSPK785un0cpN87wLaJGXAIZD8@dtsls0p4e

# cloudinary.uploader.upload('image_pos.txt')
dbx = dropbox.Dropbox('sl.BQRVHjEJP5EyJvR6P6JMfVO_PUis7zQAQGGubVagmqOUV6KzSvV8S9J16_s_-jpiWxoI9gEDrnx5SN-rDGLLAvpCQuYnGkiEUOjZYqHQXAZY42JL_IzFjDH0_nJTqNOhgWHtERk')
# dbx.users_get_current_account()
dbx.files_upload("test_grayscale.txt", '/Users/alden/Desktop/code-guild/class_swordfish/code/alden/python/test_grayscale.txt')